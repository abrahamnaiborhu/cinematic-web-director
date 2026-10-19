"""Offline behavior tests. Run: python3 -B -m unittest discover -s tests -v."""
import json
import os
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import preflight
from preflight import BASE_REQUIRED_GSAP, run


def write_png(path, width, height=2):
    """Generate a complete RGB PNG, not a signature-only image fixture."""
    def chunk(kind, payload):
        return struct.pack('>I', len(payload)) + kind + payload + struct.pack('>I', zlib.crc32(kind + payload))
    rows = (b'\0' + b'\x20\x40\x60' * width) * height
    path.write_bytes(b'\x89PNG\r\n\x1a\n' +
                     chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) +
                     chunk(b'IDAT', zlib.compress(rows)) + chunk(b'IEND', b''))


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'project'
        self.project.mkdir()
        self.home = self.base / 'home'
        self.home.mkdir()
        self.addCleanup(patch.stopall)
        patch('preflight.shutil.which', return_value=None).start()
        patch.dict(os.environ, {}, clear=True).start()

    def create_package(self, include_gsap=False, installed=False, root=None, deps=None):
        root = root or self.project
        root.mkdir(parents=True, exist_ok=True)
        dependencies = {'react': '^19.0.0'} if deps is None else dict(deps)
        if include_gsap:
            dependencies['gsap'] = '^3.15.0'
        (root / 'package.json').write_text(json.dumps({'dependencies': dependencies}))
        if installed:
            target = root / 'node_modules' / 'gsap'
            target.mkdir(parents=True)
            (target / 'package.json').write_text('{"name":"gsap","version":"3.15.0"}')

    def add_skills(self, names=None, root=None):
        root = root or self.project / '.claude' / 'skills'
        for name in names or list(BASE_REQUIRED_GSAP) + ['gsap-react']:
            p = root / name
            p.mkdir(parents=True, exist_ok=True)
            (p / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: fixture\n---\n')

    def provision(self):
        self.create_package(include_gsap=True, installed=True)
        self.add_skills()
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story\nStatus: DRAFT\n')

    def result(self, phase='discovery', docs_fallback=False, **kwargs):
        return run(self.project, 'claude-code', phase, docs_fallback, self.home, **kwargs)

    def test_discovery_reviews_eight_checks_without_implementation_blockers(self):
        r = self.result()
        self.assertEqual([c['id'] for c in r['results']], list(range(1, 9)))
        self.assertEqual(r['checks_reviewed'], 8)
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][5]['status'], 'DEFERRED')

    def test_implementation_blocks_missing_skills_script_and_runtime(self):
        self.create_package(include_gsap=True)
        r = self.result('implementation')
        for name in ('GreenSock official GSAP Skills', 'Project script', 'GSAP runtime package'):
            self.assertIn(name, r['blockers'])

    def test_local_evidence_does_not_imply_creative_approval(self):
        self.provision()
        r = self.result('implementation')
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][4]['evidence_scope'], 'filesystem')
        self.assertFalse(r['creative_approval_verified'])

    def test_explicit_and_inferred_agent_identities_remain_declarations(self):
        explicit = self.result()['results'][0]
        self.assertEqual(explicit['status'], 'UNVERIFIED')
        self.assertEqual(explicit['evidence_scope'], 'declaration')
        with patch.dict(os.environ, {'CODEX_HOME': str(self.home / 'custom')}):
            inferred = run(self.project, 'auto', 'discovery', False, self.home)['results'][0]
        self.assertEqual(inferred['status'], 'UNVERIFIED')
        self.assertEqual(inferred['evidence_scope'], 'inference')
        self.assertTrue(inferred['next_steps'])

    def test_complete_package_integrity_includes_all_four_templates(self):
        skill = self.base / 'skill'
        for source in preflight.SKILL_DIR.rglob('*.md'):
            if source.name == 'README.md':
                continue
            target = skill / source.relative_to(preflight.SKILL_DIR)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        (skill / 'templates/CONTINUITY_BIBLE.md').unlink()
        with patch('preflight.SKILL_DIR', skill):
            r = self.result()
        self.assertIn('Cinematic Web Director Skill', r['blockers'])

    def test_missing_or_blank_direction_guidance_blocks_discovery(self):
        skill = self.base / 'skill'
        for source in preflight.SKILL_DIR.rglob('*.md'):
            target = skill / source.relative_to(preflight.SKILL_DIR)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        for name in ('DESIGN_DIRECTION.md', 'MOTION_DIRECTION.md', 'DEVICE_EXPERIENCE.md',
                     'CREATIVE_REVIEW.md', 'PONYTAIL_ENGINEERING.md'):
            guidance = skill / 'references' / name
            original = guidance.read_bytes()
            for state in ('missing', 'blank'):
                with self.subTest(resource=name, state=state):
                    if state == 'missing':
                        guidance.unlink()
                    else:
                        guidance.write_text(' \n')
                    with patch('preflight.SKILL_DIR', skill):
                        report = self.result()
                    self.assertIn('Cinematic Web Director Skill', report['blockers'])
                    self.assertEqual(report['results'][1]['status'], 'MISSING')
                    self.assertIn(f'Missing: references/{name}', report['results'][1]['evidence'])
            guidance.write_bytes(original)

    def test_missing_review_template_blocks_discovery(self):
        skill = self.base / 'skill'
        for source in preflight.SKILL_DIR.rglob('*.md'):
            target = skill / source.relative_to(preflight.SKILL_DIR)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        template = skill / 'templates' / 'REVIEW_PACKAGE.md'
        template.unlink(missing_ok=True)
        with patch('preflight.SKILL_DIR', skill):
            report = self.result()
        self.assertIn('Cinematic Web Director Skill', report['blockers'])

    def test_optional_tools_are_not_readiness_caveats(self):
        self.provision()
        r = self.result('implementation')
        self.assertEqual(r['results'][7]['status'], 'DEFERRED')
        self.assertNotIn('Optional creative tools', r['caveats'])

    def test_custom_codex_home_is_searched(self):
        custom = self.home / 'custom-codex'
        self.add_skills(root=custom / 'skills')
        with patch.dict(os.environ, {'CODEX_HOME': str(custom)}):
            r = run(self.project, 'codex', 'discovery', False, self.home)
        self.assertEqual(r['results'][2]['status'], 'VERIFIED')

    def test_cursor_and_explicit_other_agent_skill_roots(self):
        for agent, root in [('cursor', self.project / '.cursor/skills'), ('other', self.base / 'custom-skills')]:
            self.add_skills(root=root)
            r = run(self.project, agent, 'discovery', False, self.home, extra_skill_roots=[root])
            self.assertEqual(r['results'][2]['status'], 'VERIFIED')

    def test_claude_marketplace_inventory(self):
        self.provision()
        local = self.project / '.claude/skills'
        for p in local.glob('*/SKILL.md'):
            p.unlink()
        plugin = self.home / '.claude/plugins/cache/greensock/gsap-skills/1.0'
        self.add_skills(root=plugin / 'skills')
        inv = self.home / '.claude/plugins/installed_plugins.json'
        inv.parent.mkdir(parents=True, exist_ok=True)
        inv.write_text(json.dumps({'plugins': {'gsap-skills@greensock': [{'installPath': str(plugin)}]}}))
        self.assertEqual(self.result('implementation')['results'][2]['status'], 'VERIFIED')

    def test_only_selected_gsap_topics_are_required(self):
        self.provision()
        r = self.result('implementation', required_gsap_skills=['gsap-scrolltrigger'])
        self.assertIn('GreenSock official GSAP Skills', r['blockers'])
        self.add_skills(names=['gsap-scrolltrigger'])
        self.assertFalse(self.result('implementation', required_gsap_skills=['gsap-scrolltrigger'])['blockers'])

    def test_docs_fallback_waives_only_skill_blocker(self):
        self.create_package(include_gsap=True)
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', docs_fallback=True)
        self.assertNotIn('GreenSock official GSAP Skills', r['blockers'])
        self.assertIn('GSAP runtime package', r['blockers'])
        self.assertEqual(r['results'][2]['status'], 'MISSING')

    def test_non_gsap_batch_does_not_require_gsap(self):
        (self.project / 'index.html').write_text('<h1>Portfolio</h1>')
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Static composition batch')
        r = self.result('implementation', gsap_required=False)
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][2]['status'], 'DEFERRED')
        self.assertEqual(r['results'][5]['status'], 'DEFERRED')
        self.assertEqual(r['results'][2]['next_steps'], [])
        self.assertEqual(r['results'][5]['next_steps'], [])

    def test_static_cdn_runtime_needs_explicit_observation(self):
        (self.project / 'index.html').write_text('<script src="https://cdn.example.test/gsap.js"></script>')
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        self.add_skills(names=list(BASE_REQUIRED_GSAP))
        r = self.result('implementation')
        self.assertNotIn('Project environment', r['blockers'])
        self.assertIn('GSAP runtime package', r['blockers'])
        r = self.result('implementation', observations={6: 'Agent loaded the CDN and exercised gsap.to in the running browser.'})
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][5]['status'], 'UNVERIFIED')
        self.assertEqual(r['results'][5]['evidence_scope'], 'agent-attestation')

    def test_remote_skill_evidence_does_not_pretend_files_are_installed(self):
        self.create_package(include_gsap=True, installed=True)
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', observations={3: 'Session exposed and read the required official GreenSock resources.'})
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][2]['status'], 'UNVERIFIED')
        self.assertEqual(r['results'][2]['local_status'], 'MISSING')

    def test_observations_cannot_override_integrity_or_missing_brief(self):
        self.create_package(include_gsap=True, installed=True)
        with self.assertRaises(ValueError):
            self.result('implementation', observations={5: 'Approve any story'})

    def test_explicit_source_and_script_paths(self):
        app = self.project / 'unusual/presentation'
        self.create_package(include_gsap=True, installed=True, root=app)
        self.add_skills()
        brief = self.project / 'materials/client-approved.md'
        brief.parent.mkdir()
        brief.write_text('# Brief')
        r = self.result('implementation', source_root=app, script_path=brief)
        self.assertFalse(r['blockers'])
        self.assertEqual(r['source_root'], str(app.resolve()))

    def test_sibling_dependencies_do_not_satisfy_selected_application(self):
        self.create_package(include_gsap=True, installed=True, root=self.project / 'frontend')
        self.create_package(root=self.project / 'web', deps={'next': '^16.0.0'})
        self.add_skills()
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', source_root=self.project / 'web')
        self.assertIn('GSAP runtime package', r['blockers'])
        self.assertEqual(r['applications'][1]['framework'], 'Next.js')

    def test_ambiguous_application_selection_requires_source_root(self):
        self.create_package(root=self.project / 'frontend')
        self.create_package(root=self.project / 'web')
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', gsap_required=False)
        self.assertIn('Project environment', r['blockers'])

    def test_hoisted_runtime_is_resolved_only_for_declaring_application(self):
        self.create_package(include_gsap=True, installed=True, deps={})
        self.create_package(include_gsap=True, root=self.project / 'frontend')
        self.add_skills()
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', source_root=self.project / 'frontend')
        self.assertNotIn('GSAP runtime package', r['blockers'])

    def test_malformed_runtime_manifest_is_not_verified(self):
        self.provision()
        (self.project / 'node_modules/gsap/package.json').write_text('not JSON')
        self.assertIn('GSAP runtime package', self.result('implementation')['blockers'])

    def test_prototype_needs_brief_and_technical_requirements(self):
        self.create_package(include_gsap=True, installed=True)
        self.add_skills()
        self.assertIn('Project script', self.result('prototype')['blockers'])
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Explicitly approved experiment')
        self.assertFalse(self.result('prototype')['blockers'])

    def test_release_blocks_without_visual_evidence_regardless_of_tool_inventory(self):
        self.provision()
        self.assertIn('Browser and visual testing', self.result('release')['blockers'])

    def test_signature_only_images_do_not_clear_release(self):
        self.provision()
        desktop, mobile = self.base / 'desktop.png', self.base / 'mobile.png'
        for path in (desktop, mobile):
            path.write_bytes(b'\x89PNG\r\n\x1a\n' + b'0' * 120)
        r = self.result('release', desktop_screenshot=desktop, mobile_screenshot=mobile, interactions_verified=True)
        self.assertIn('Browser and visual testing', r['blockers'])

    def test_png_integrity_and_dimensions_with_attestation_can_clear_release(self):
        self.provision()
        desktop, mobile = self.base / 'desktop.png', self.base / 'mobile.png'
        write_png(desktop, 1280)
        write_png(mobile, 390)
        r = self.result('release', desktop_screenshot=desktop, mobile_screenshot=mobile, interactions_verified=True)
        self.assertNotIn('Browser and visual testing', r['blockers'])
        self.assertEqual(r['results'][6]['status'], 'UNVERIFIED')
        self.assertEqual(r['results'][6]['evidence_scope'], 'filesystem+attestation')

    def test_duplicate_capture_cannot_stand_for_two_viewports(self):
        self.provision()
        path = self.base / 'one.png'
        write_png(path, 1280)
        r = self.result('release', desktop_screenshot=path, mobile_screenshot=path, interactions_verified=True)
        self.assertIn('Browser and visual testing', r['blockers'])

    def test_corrupt_png_payload_is_rejected(self):
        path = self.base / 'corrupt.png'
        write_png(path, 390)
        body = bytearray(path.read_bytes())
        body[-20] ^= 1
        path.write_bytes(body)
        self.assertFalse(preflight.valid_screenshot(path))

    def test_observation_file_is_project_and_phase_bound(self):
        path = self.base / 'observations.json'
        path.write_text(json.dumps({'project_root': str(self.project), 'phase': 'implementation',
                                    'checks': {'6': 'Observed GSAP import in browser'}}))
        self.assertEqual(preflight.load_observations(path, self.project, 'implementation'), {6: 'Observed GSAP import in browser'})
        with self.assertRaises(ValueError):
            preflight.load_observations(path, self.project, 'release')

    def test_cli_exit_codes_and_default_read_only_behavior(self):
        script = Path(preflight.__file__)
        before = sorted(str(p.relative_to(self.project)) for p in self.project.rglob('*'))
        cmd = [sys.executable, '-B', str(script), '--project', str(self.project), '--agent', 'other', '--format', 'json']
        env = {'PATH': os.defpath, 'HOME': str(self.home)}
        discovery = subprocess.run(cmd, capture_output=True, text=True, env=env)
        implementation = subprocess.run(cmd + ['--phase', 'implementation'], capture_output=True, text=True, env=env)
        self.assertEqual(discovery.returncode, 0)
        self.assertEqual(implementation.returncode, 2)
        self.assertEqual(json.loads(discovery.stdout)['checks_reviewed'], 8)
        self.assertEqual(before, sorted(str(p.relative_to(self.project)) for p in self.project.rglob('*')))

    def test_cli_exposes_scoped_options_and_prototype_phase(self):
        (self.project / 'index.html').write_text('<h1>Composition experiment</h1>')
        brief = self.project / 'experiment.md'
        brief.write_text('# Approved bounded experiment')
        completed = subprocess.run([
            sys.executable, '-B', str(Path(preflight.__file__)), '--project', str(self.project),
            '--agent', 'other', '--phase', 'prototype', '--gsap', 'not-required',
            '--source-root', '.', '--script', 'experiment.md', '--skill-root', str(self.base / 'skills'),
            '--format', 'json'], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        report = json.loads(completed.stdout)
        self.assertEqual(report['source_root'], str(self.project.resolve()))
        self.assertFalse(report['gsap_required'])

    def test_cli_rejects_unrelated_observations(self):
        observations = self.base / 'evidence.json'
        observations.write_text(json.dumps({'project_root': str(self.home), 'phase': 'implementation',
                                            'checks': {'6': 'Observed runtime'}}))
        completed = subprocess.run([
            sys.executable, '-B', str(Path(preflight.__file__)), '--project', str(self.project),
            '--phase', 'implementation', '--observations', str(observations)],
            capture_output=True, text=True)
        self.assertEqual(completed.returncode, 2)
        self.assertIn('does not match', completed.stderr)

    def test_observations_are_bound_to_selected_source(self):
        nested = self.project / 'frontend'
        nested.mkdir()
        path = self.base / 'evidence.json'
        path.write_text(json.dumps({'project_root': str(self.project), 'phase': 'implementation',
                                    'checks': {'6': 'Root app was checked'}}))
        with self.assertRaises(ValueError):
            preflight.load_observations(path, self.project, 'implementation', nested)

    def test_skill_name_prefix_is_not_an_exact_metadata_match(self):
        self.add_skills(names=list(BASE_REQUIRED_GSAP))
        path = self.project / '.claude/skills/gsap-core/SKILL.md'
        path.write_text('---\nname: gsap-core-unrelated\ndescription: fixture\n---\n')
        self.assertEqual(self.result()['results'][2]['status'], 'MISSING')

    def test_quoted_skill_metadata_is_readable(self):
        self.add_skills(names=list(BASE_REQUIRED_GSAP))
        path = self.project / '.claude/skills/gsap-core/SKILL.md'
        path.write_text('---\nname: "gsap-core"\ndescription: fixture\n---\n')
        self.assertEqual(self.result()['results'][2]['status'], 'VERIFIED')

    def test_malformed_project_manifest_does_not_clear_source_gate(self):
        (self.project / 'package.json').write_text('not JSON')
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Story')
        r = self.result('implementation', gsap_required=False)
        self.assertIn('Project environment', r['blockers'])

    def test_blank_default_brief_does_not_hide_readable_equivalent(self):
        self.provision()
        (self.project / 'PROJECT_SCRIPT.md').write_text('   ')
        (self.project / 'PROJECT_BRIEF.md').write_text('# Readable equivalent brief')
        self.assertNotIn('Project script', self.result('implementation')['blockers'])

    def test_optional_manifest_declaration_is_not_verified_installation(self):
        self.create_package(deps={'three': '^0.180.0'})
        result = self.result()
        self.assertEqual(result['results'][7]['status'], 'UNVERIFIED')
        self.assertEqual(result['results'][7]['evidence_scope'], 'declaration')
        self.assertNotIn('Optional creative tools', result['caveats'])


if __name__ == '__main__':
    unittest.main()
