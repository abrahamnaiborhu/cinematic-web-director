"""Offline tests for read-only preflight. Run: python3 -m unittest discover -s tests -v"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from preflight import BASE_REQUIRED_GSAP, run


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'project'
        self.project.mkdir()
        self.home = self.base / 'home'
        self.home.mkdir()

    def create_package(self, include_gsap=False, installed=False):
        deps = {'react': '^19.0.0'}
        if include_gsap:
            deps['gsap'] = '^3.15.0'
        (self.project / 'package.json').write_text(json.dumps({'dependencies': deps}))
        if installed:
            target = self.project / 'node_modules' / 'gsap'
            target.mkdir(parents=True)
            (target / 'package.json').write_text('{"name":"gsap","version":"3.15.0"}')

    def add_skills(self, names):
        for name in names:
            p = self.project / '.claude' / 'skills' / name
            p.mkdir(parents=True, exist_ok=True)
            (p / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: test\n---\n')

    def result(self, phase='discovery', docs_fallback=False):
        return run(self.project, 'claude-code', phase, docs_fallback, self.home)

    def test_discovery_checks_everything_but_does_not_block_missing_script_or_gsap(self):
        r = self.result()
        self.assertEqual(r['checks_reviewed'], 8)
        self.assertEqual([c['id'] for c in r['results']], list(range(1, 9)))
        self.assertEqual(r['overall_gate'], 'DEGRADED')
        self.assertFalse(r['blockers'])
        self.assertEqual(r['results'][4]['status'], 'MISSING')
        self.assertEqual(r['results'][5]['status'], 'DEFERRED')

    def test_implementation_blocks_missing_skills_and_script_and_runtime(self):
        self.create_package(include_gsap=True)
        r = self.result('implementation')
        self.assertEqual(r['overall_gate'], 'BLOCKED')
        self.assertIn('GreenSock official GSAP Skills', r['blockers'])
        self.assertIn('Project script', r['blockers'])
        self.assertIn('GSAP runtime package', r['blockers'])

    def test_implementation_can_pass_with_relevant_suites_and_runtime(self):
        self.create_package(include_gsap=True, installed=True)
        self.add_skills(list(BASE_REQUIRED_GSAP) + ['gsap-react'])
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Approved story\n')
        r = self.result('implementation')
        self.assertNotEqual(r['overall_gate'], 'BLOCKED')
        self.assertEqual(r['results'][2]['status'], 'VERIFIED')
        self.assertEqual(r['results'][5]['status'], 'VERIFIED')
        self.assertEqual(r['results'][4]['status'], 'VERIFIED')

    def test_docs_fallback_waives_only_official_skill_blocker(self):
        self.create_package(include_gsap=True, installed=True)
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Approved story\n')
        r = self.result('implementation', docs_fallback=True)
        self.assertNotIn('GreenSock official GSAP Skills', r['blockers'])
        self.assertEqual(r['results'][2]['status'], 'MISSING')
        self.assertNotEqual(r['overall_gate'], 'BLOCKED')

    def test_release_requires_visual_testing_evidence(self):
        self.create_package(include_gsap=True, installed=True)
        self.add_skills(list(BASE_REQUIRED_GSAP) + ['gsap-react'])
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Approved story\n')
        r = self.result('release')
        # This test is host-dependent: local browsers may be present. Only assert honest status.
        if not r['results'][6]['evidence']:
            self.assertIn('Browser and visual testing', r['blockers'])
        else:
            self.assertEqual(r['results'][6]['status'], 'UNVERIFIED')

    def test_claude_marketplace_inventory_is_inspected_in_known_location(self):
        self.create_package(include_gsap=True, installed=True)
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Approved\n')
        plugin_base = self.home / '.claude' / 'plugins' / 'cache' / 'greensock' / 'gsap-skills' / '1.0'
        for name in list(BASE_REQUIRED_GSAP) + ['gsap-react']:
            skill_dir = plugin_base / 'skills' / name
            skill_dir.mkdir(parents=True, exist_ok=True)
            (skill_dir / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: test\n---\n')
        inv = self.home / '.claude' / 'plugins' / 'installed_plugins.json'
        inv.parent.mkdir(parents=True, exist_ok=True)
        inv.write_text(json.dumps({'plugins': {'gsap-skills@greensock': [{'installPath': str(plugin_base)}]}}))
        r = self.result('implementation')
        self.assertEqual(r['results'][2]['status'], 'VERIFIED')
        self.assertNotIn('GreenSock official GSAP Skills', r['blockers'])

    def test_release_accepts_image_artifacts_with_attested_interactions(self):
        self.create_package(include_gsap=True, installed=True)
        self.add_skills(list(BASE_REQUIRED_GSAP) + ['gsap-react'])
        (self.project / 'PROJECT_SCRIPT.md').write_text('# Approved\n')
        desktop = self.base / 'desktop.png'
        mobile = self.base / 'mobile.png'
        for screenshot in (desktop, mobile):
            screenshot.write_bytes(b'\x89PNG\r\n\x1a\n' + b'0' * 120)
        r = run(self.project, 'claude-code', 'release', False, self.home,
                desktop_screenshot=desktop, mobile_screenshot=mobile, interactions_verified=True)
        self.assertEqual(r['results'][6]['status'], 'VERIFIED')
        self.assertNotIn('Browser and visual testing', r['blockers'])


if __name__ == '__main__':
    unittest.main()
