#!/usr/bin/env python3
"""Read-only, offline Phase 0 preflight for Cinematic Web Director.

Checks presence on the local filesystem; it cannot prove that an AI agent has
activated a skill or that browser automation is available through an MCP tool.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import struct
import sys
import zlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SKILL_NAME = 'cinematic-web-director'
GSAP_SKILLS = (
    'gsap-core', 'gsap-timeline', 'gsap-scrolltrigger', 'gsap-plugins',
    'gsap-utils', 'gsap-react', 'gsap-performance', 'gsap-frameworks'
)
BASE_REQUIRED_GSAP = ('gsap-core', 'gsap-performance')
SKILL_DIR = Path(__file__).resolve().parents[1]


def check(id_: int, name: str, status: str, summary: str, *, evidence=None,
          next_steps=None, blocking: bool = False, evidence_scope='filesystem') -> dict[str, Any]:
    return {
        'id': id_, 'name': name, 'status': status, 'blocking': blocking,
        'summary': summary, 'evidence': evidence or [], 'next_steps': next_steps or [],
        'evidence_scope': evidence_scope
    }


def read_package(p: Path) -> dict:
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, UnicodeError):
        return {}


def read_document(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except (OSError, UnicodeError):
        return ''


def has_skill_header(text: str, expected_name: str) -> bool:
    """Check the basic name/description scalars, without claiming full YAML validation."""
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        return False
    try:
        end = lines.index('---', 1)
    except ValueError:
        return False
    fields = {}
    for line in lines[1:end]:
        if line.startswith(('name:', 'description:')):
            key, value = line.split(':', 1)
            value = value.split(' #', 1)[0].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            fields[key] = value
    return fields.get('name') == expected_name and bool(fields.get('description'))


def package_roots(project: Path) -> list[Path]:
    candidates = [project, project / 'frontend', project / 'web', project / 'client',
                  project / 'site', project / 'apps' / 'web', project / 'apps' / 'frontend',
                  project / 'packages' / 'web']
    return [p for p in candidates if (p / 'package.json').is_file()]


def project_path(project: Path, path: Path) -> Path:
    path = path.expanduser()
    return (path if path.is_absolute() else project / path).resolve()


def select_source(project: Path, roots: list[Path], explicit: Path | None) -> Path | None:
    if explicit is not None:
        selected = project_path(project, explicit)
        if not selected.is_dir() or not selected.is_relative_to(project):
            raise ValueError('Source root must be an existing directory inside the project.')
        return selected
    # A workspace manifest is not necessarily the website application.
    frontends = [p for p in roots if detect_framework(get_dependencies([p])) not in
                 ('JavaScript / unspecified', 'NestJS')]
    candidates = frontends or roots
    if len(candidates) == 1:
        return candidates[0]
    if not candidates and (project / 'index.html').is_file():
        return project
    return None


def runtime_packages(project: Path, source: Path | None, deps: dict) -> list[Path]:
    if source is None or 'gsap' not in deps:
        return []
    paths = []
    for root in (source, *source.parents):
        if not root.is_relative_to(project):
            break
        path = root / 'node_modules' / 'gsap' / 'package.json'
        pkg = read_package(path)
        if pkg.get('name') == 'gsap' and isinstance(pkg.get('version'), str) and pkg['version'].strip():
            paths.append(path)
            break
    return paths


def validate_observations(observations: dict) -> dict[int, str]:
    if not isinstance(observations, dict):
        raise ValueError('Observations must be a check-ID to evidence-text object.')
    result = {}
    for key, value in observations.items():
        if str(key) not in ('3', '4', '6') or not isinstance(value, str) or not value.strip():
            raise ValueError('Only checks 3, 4 and 6 accept nonempty agent observation text.')
        result[int(key)] = value.strip()
    return result


def load_observations(path: Path, project: Path, phase: str,
                      source_root: Path | None = None) -> dict[int, str]:
    try:
        data = json.loads(path.expanduser().read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValueError(f'Cannot read observation file: {exc}') from exc
    if not isinstance(data, dict) or not isinstance(data.get('project_root'), str):
        raise ValueError('Observation file must identify project_root, phase and checks.')
    project = project.expanduser().resolve()
    if Path(data['project_root']).expanduser().resolve() != project or data.get('phase') != phase:
        raise ValueError('Observation file does not match this project and phase.')
    expected_source = project_path(project, source_root) if source_root else project
    recorded_source = data.get('source_root', data['project_root'])
    if not isinstance(recorded_source, str) or project_path(project, Path(recorded_source)) != expected_source:
        raise ValueError('Observation file does not match the selected source root.')
    if 'checks' not in data:
        raise ValueError('Observation file is missing checks.')
    return validate_observations(data['checks'])


def identify_agent(explicit: str) -> tuple[str, str]:
    if explicit != 'auto':
        return explicit, 'Provided explicitly by the invoking agent/user; not independently attested.'
    candidates = []
    env = os.environ
    if env.get('CLAUDECODE') or env.get('CLAUDE_CODE_ENTRYPOINT'):
        candidates.append('claude-code')
    if env.get('CODEX_HOME') or env.get('CODEX_THREAD_ID'):
        candidates.append('codex')
    if env.get('CURSOR_TRACE_ID') or env.get('CURSOR_SESSION_ID'):
        candidates.append('cursor')
    if len(set(candidates)) == 1:
        return candidates[0], 'Inferred from an environment variable; agent must confirm.'
    return 'unknown', 'Cannot determine the active agent from this Python process.'


def skill_roots(project: Path, agent: str, home: Path) -> list[Path]:
    common = [project / '.agents' / 'skills', home / '.agents' / 'skills',
              home / '.config' / 'agents' / 'skills']
    if agent == 'claude-code':
        paths = [project / '.claude' / 'skills', home / '.claude' / 'skills']
    elif agent == 'cursor':
        paths = [project / '.cursor' / 'skills', home / '.cursor' / 'skills']
    elif agent == 'codex':
        codex_home = Path(os.environ.get('CODEX_HOME') or home / '.codex').expanduser()
        paths = [project / '.agents' / 'skills', home / '.agents' / 'skills', codex_home / 'skills']
    else:
        paths = [project / '.claude' / 'skills', home / '.claude' / 'skills',
                 project / '.cursor' / 'skills', home / '.cursor' / 'skills',
                 home / '.codex' / 'skills']
    seen = set()
    out = []
    for path in paths + common:
        if str(path) not in seen:
            seen.add(str(path))
            out.append(path)
    return out


def available_gsap_skills(roots: list[Path]) -> dict[str, str]:
    result = {}
    for root in roots:
        for name in GSAP_SKILLS:
            p = root / name / 'SKILL.md'
            if name not in result and p.is_file():
                try:
                    with p.open('r', encoding='utf-8') as file:
                        prefix = file.read(8192)
                    if has_skill_header(prefix, name):
                        result[name] = str(p)
                except (OSError, UnicodeError):
                    pass
    return result


def claude_plugin_skill_roots(home: Path) -> list[Path]:
    """Find explicitly declared GSAP plugin paths (no broad home-directory scan)."""
    inventory = home / '.claude' / 'plugins' / 'installed_plugins.json'
    if not inventory.is_file():
        return []
    try:
        data = json.loads(inventory.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError):
        return []
    result = []

    def inspect(node: Any, hint: str = '') -> None:
        if isinstance(node, dict):
            tag = ' '.join(str(node.get(k, '')) for k in ('name', 'id', 'source', 'marketplace'))
            tag = (hint + ' ' + tag).lower()
            path = node.get('installPath') or node.get('install_path')
            if isinstance(path, str) and ('greensock' in tag or 'gsap-skills' in tag):
                base = Path(path).expanduser()
                if base.is_dir():
                    result.append(base / 'skills')
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    inspect(value, hint + ' ' + str(key).lower())
        elif isinstance(node, list):
            for value in node[:200]:
                inspect(value, hint)

    inspect(data)
    return list(dict.fromkeys(result))


def get_project_script(project: Path) -> Path | None:
    names = ('PROJECT_SCRIPT.md', 'PROJECT_BRIEF.md', 'CREATIVE_BRIEF.md', 'STORY_SCRIPT.md')
    locations = (project, project / 'docs', project / 'creative',
                 project / 'docs' / 'creative', project / '.director')
    for place in locations:
        for name in names:
            path = place / name
            if path.is_file() and read_document(path).strip():
                return path
    return None


def detect_framework(dependencies: dict) -> str:
    for dep, label in (
        ('next', 'Next.js'), ('nuxt', 'Nuxt'), ('@sveltejs/kit', 'SvelteKit'),
        ('astro', 'Astro'), ('@angular/core', 'Angular'), ('svelte', 'Svelte'),
        ('vue', 'Vue'), ('react', 'React'), ('vite', 'Vite'), ('@nestjs/core', 'NestJS'),
    ):
        if dep in dependencies:
            return label
    return 'JavaScript / unspecified'


def package_manager(project: Path, roots: list[Path]) -> str:
    checks = [('pnpm-lock.yaml', 'pnpm'), ('yarn.lock', 'yarn'),
              ('bun.lock', 'bun'), ('bun.lockb', 'bun'),
              ('package-lock.json', 'npm'), ('npm-shrinkwrap.json', 'npm')]
    for root in [project] + roots:
        for filename, name in checks:
            if (root / filename).exists():
                return name
    return 'unverified'


def get_dependencies(roots: list[Path]) -> dict[str, str]:
    deps = {}
    for root in roots:
        pkg = read_package(root / 'package.json')
        for field in ('dependencies', 'devDependencies', 'optionalDependencies'):
            value = pkg.get(field)
            if isinstance(value, dict):
                deps.update({k: str(v) for k, v in value.items()})
    return deps


def png_dimensions(path: Path | None) -> tuple[int, int] | None:
    """Validate bounded, non-interlaced 8-bit PNG structure and scanline data.

    This verifies an image file, not its origin, page content or visual quality.
    Other formats/encodings stay unverified rather than accepting their signatures.
    """
    if path is None:
        return None
    try:
        path = path.expanduser()
        if not path.is_file() or path.stat().st_size > 32 * 1024 * 1024:
            return None
        data = path.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n':
            return None
        offset, dimensions, row_size = 8, None, 0
        compressed = bytearray()
        ended_data = False
        while offset + 12 <= len(data):
            length = struct.unpack('>I', data[offset:offset + 4])[0]
            kind = data[offset + 4:offset + 8]
            end = offset + 12 + length
            if end > len(data):
                return None
            payload = data[offset + 8:end - 4]
            crc = struct.unpack('>I', data[end - 4:end])[0]
            if zlib.crc32(kind + payload) != crc:
                return None
            if dimensions is None and kind != b'IHDR':
                return None
            if kind == b'IHDR':
                if dimensions is not None or length != 13:
                    return None
                width, height, bits, color, compression, filtering, interlace = struct.unpack('>IIBBBBB', payload)
                channels = {0: 1, 2: 3, 4: 2, 6: 4}.get(color)
                if not channels or bits != 8 or compression or filtering or interlace or not width or not height:
                    return None
                row_size = width * channels + 1
                if row_size * height > 128 * 1024 * 1024:
                    return None
                dimensions = width, height
            elif kind == b'IDAT':
                if ended_data:
                    return None
                compressed.extend(payload)
            elif kind == b'IEND':
                if length or end != len(data) or not compressed:
                    return None
                expected = row_size * dimensions[1]
                decoder = zlib.decompressobj()
                rows = decoder.decompress(bytes(compressed), expected + 1)
                if len(rows) != expected or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
                    return None
                if any(rows[pos] > 4 for pos in range(0, expected, row_size)):
                    return None
                return dimensions
            elif kind == b'PLTE':
                if compressed or color in (0, 4) or not length or length % 3 or length > 768:
                    return None
            elif not kind.isalpha() or not kind[0] & 32:
                return None
            if compressed and kind != b'IDAT':
                ended_data = True
            offset = end
    except (OSError, ValueError, struct.error, zlib.error):
        return None
    return None


def valid_screenshot(path: Path | None) -> bool:
    return png_dimensions(path) is not None


def run(project: Path, agent_arg: str, phase: str, allow_docs_fallback: bool,
        home: Path | None = None, desktop_screenshot: Path | None = None,
        mobile_screenshot: Path | None = None, interactions_verified: bool = False,
        *, extra_skill_roots: list[Path] | None = None, source_root: Path | None = None,
        script_path: Path | None = None, gsap_required: bool = True,
        required_gsap_skills: list[str] | None = None, observations: dict | None = None) -> dict[str, Any]:
    project = project.expanduser().resolve()
    if not project.is_dir() or phase not in ('discovery', 'prototype', 'implementation', 'release'):
        raise ValueError('Use an existing project directory and a supported phase.')
    home = home or Path.home()
    implementation = phase in ('prototype', 'implementation', 'release')
    release = phase == 'release'
    agent, agent_evidence = identify_agent(agent_arg)
    roots = package_roots(project)
    selected = select_source(project, roots, source_root)
    if selected and (selected / 'package.json').is_file() and selected not in roots:
        roots.append(selected)
    deps = get_dependencies([selected]) if selected else {}
    framework = detect_framework(deps)
    observations = validate_observations({} if observations is None else observations)
    if required_gsap_skills and (not gsap_required or any(n not in GSAP_SKILLS for n in required_gsap_skills)):
        raise ValueError('Select known GSAP topics only for a batch that requires GSAP.')
    results = []

    # 1 — Agent identification
    agent_known = agent in ('claude-code', 'cursor', 'codex', 'other')
    results.append(check(1, 'AI agent identification', 'UNVERIFIED',
        f'Active agent: {agent}.', evidence=[agent_evidence],
        next_steps=['Confirm active-agent identity and permissions in the session; this process cannot attest them.'],
        evidence_scope='declaration' if agent_arg != 'auto' else 'inference'))

    # 2 — Skill self integrity (filesystem, not runtime activation)
    skill_main = SKILL_DIR / 'SKILL.md'
    resources = [SKILL_DIR / 'references' / name for name in
                 ('PREFLIGHT_PROTOCOL.md', 'CREATIVE_WORKFLOW.md', 'DESIGN_DIRECTION.md',
                  'MOTION_DIRECTION.md', 'DEVICE_EXPERIENCE.md', 'CREATIVE_REVIEW.md',
                  'PONYTAIL_ENGINEERING.md', 'JCODEMUNCH_WORKFLOW.md', 'EXPERIENCE_SYSTEM.md',
                  'TASTE_DISCOVERY.md', 'MOTION_COMPANION.md')]
    resources += [SKILL_DIR / 'templates' / name for name in
                  ('PROJECT_SCRIPT.md', 'CONTINUITY_BIBLE.md', 'SCENE_TREATMENT.md',
                   'ITERATION_LOG.md', 'REVIEW_PACKAGE.md')]
    resources += [SKILL_DIR / 'assets' / name for name in ('taste-guide.html', 'motion-companion.html')]
    missing = [str(p.relative_to(SKILL_DIR)) for p in [skill_main] + resources if not p.is_file()]
    body = read_document(skill_main)
    missing += [str(p.relative_to(SKILL_DIR)) for p in resources
                if p.is_file() and not read_document(p).strip()]
    valid_header = has_skill_header(body, SKILL_NAME)
    self_pass = not missing and valid_header
    results.append(check(2, 'Cinematic Web Director Skill', 'VERIFIED' if self_pass else 'MISSING',
        'Skill entry point and required references are readable on disk.' if self_pass else 'Skill package is incomplete or SKILL.md metadata is invalid.',
        evidence=[str(skill_main)] + ([f'Missing: {item}' for item in missing] if missing else []),
        next_steps=['Agent must also confirm that it has loaded SKILL.md instructions; disk access alone does not prove activation.'] if self_pass else ['Reinstall the complete cinematic-web-director skill package.'],
        blocking=not self_pass))

    # 3 — Official GSAP agent skills
    search_roots = skill_roots(project, agent, home)
    search_roots += [project_path(project, p) for p in extra_skill_roots or []]
    if agent == 'claude-code':
        search_roots += claude_plugin_skill_roots(home)
    found = available_gsap_skills(search_roots)
    required = list(dict.fromkeys((*BASE_REQUIRED_GSAP, *(required_gsap_skills or []))))
    if framework in ('React', 'Next.js'):
        required.append('gsap-react')
    if framework in ('Vue', 'Nuxt', 'Svelte', 'SvelteKit'):
        required.append('gsap-frameworks')
    required = list(dict.fromkeys(required))
    missing_required = [name for name in required if name not in found]
    missing_optional = [name for name in GSAP_SKILLS if name not in found and name not in required]
    if not gsap_required:
        skill_status = 'DEFERRED'
        skill_message = 'This approved batch declares no GSAP work; skill requirements are deferred.'
    elif not missing_required:
        skill_status = 'VERIFIED' if agent_known else 'UNVERIFIED'
        skill_message = f'All {len(required)} required official GSAP skill files are readable in the inspected skill directories.'
    else:
        skill_status = 'MISSING'
        skill_message = f'{len(found)}/8 official GSAP skill files found; missing required: {", ".join(missing_required)}.'
    skill_block = bool(gsap_required and missing_required and implementation and not allow_docs_fallback)
    steps = ['Active agent: explicitly read the relevant GSAP SKILL.md files and confirm they are discoverable in this session.'] if gsap_required else []
    if gsap_required and missing_required:
        steps.extend(['Install the official suite with consent: npx skills add https://github.com/greensock/gsap-skills --agent ' + (agent if agent_known and agent != 'other' else '<your-agent>'),
                      'Then rerun the preflight and test actual agent access.'])
    if gsap_required and allow_docs_fallback and missing_required:
        steps.append('Explicit fallback accepted: follow and verify current official GSAP documentation instead; record this exception in the project.')
    results.append(check(3, 'GreenSock official GSAP Skills', skill_status, skill_message,
        evidence=[f'{name}: {path}' for name, path in sorted(found.items())] +
                 [f'Optional suite skills absent: {", ".join(missing_optional)}'] +
                 (['Claude plugin marketplace installation may not be visible to this filesystem scan.'] if agent == 'claude-code' else []),
        next_steps=steps, blocking=skill_block))

    # 4 — Project structure and package manager
    manifest = read_package(selected / 'package.json') if selected else {}
    source_identified = bool(selected and (manifest or (selected / 'index.html').is_file()))
    if source_identified:
        proj_status = 'VERIFIED'
        source_type = framework if manifest else 'Static HTML'
        proj_message = (f'Selected source: {selected}; source type from local evidence: {source_type}; '
                        f'package manager: {package_manager(project, [selected])}.')
        proj_ev = [str(selected / ('package.json' if manifest else 'index.html'))]
    else:
        proj_status = 'UNVERIFIED'
        proj_message = 'Source is not identified or multiple applications are ambiguous. Supply --source-root.'
        proj_ev = [f'Project directory exists: {project.is_dir()}']
    results.append(check(4, 'Project environment', proj_status, proj_message,
        evidence=proj_ev,
        next_steps=[] if source_identified else ['Select the actual application with --source-root; confirm unusual layouts using scoped observations.'],
        blocking=implementation and not source_identified))

    # 5 — Project script
    script = project_path(project, script_path) if script_path else get_project_script(project)
    if script and (not script.is_file() or not read_document(script).strip()):
        script = None
    results.append(check(5, 'Project script', 'VERIFIED' if script else 'MISSING',
        f'Found readable nonempty script/brief: {script.name}.' if script else 'No readable nonempty project brief found in inspected locations.',
        evidence=[str(script)] if script else [],
        next_steps=['Read and assess the script: file presence does not guarantee narrative completeness.'] if script else
                   ['Discovery phase: collaboratively create PROJECT_SCRIPT.md using the bundled template.',
                    'Implementation phase: approve the script and continuity decisions first.'],
        blocking=implementation and not bool(script)))

    # 6 — GSAP package (runtime) in target project
    installed = runtime_packages(project, selected, deps)
    manifest_gsap = 'gsap' in deps
    if not gsap_required:
        runtime_status = 'DEFERRED'
        runtime_message = 'This approved batch declares no GSAP work; runtime requirements are deferred.'
    elif installed:
        runtime_status = 'VERIFIED'
        runtime_message = f'Local gsap package present; declared version: {deps.get("gsap", "not specified in manifest")}.'
    elif manifest_gsap:
        runtime_status = 'UNVERIFIED'
        runtime_message = f'gsap is declared ({deps["gsap"]}) but local runtime installation is not verified.'
    elif not implementation:
        runtime_status = 'DEFERRED'
        runtime_message = 'No GSAP dependency detected; runtime setup can wait until implementation.'
    else:
        runtime_status = 'MISSING'
        runtime_message = 'No local GSAP runtime detected in the inspected JavaScript projects.'
    results.append(check(6, 'GSAP runtime package', runtime_status, runtime_message,
        evidence=[str(p) for p in installed],
        next_steps=[] if installed or not gsap_required else ['Before implementation, check package root and run a user-approved package install if required.',
                                         'For a CDN-based site, manually verify actual script loading and plugin availability.'],
        blocking=gsap_required and implementation and not bool(installed)))

    # 7 — Browser and visual test capabilities
    browser_binaries = [f'{exe}: {shutil.which(exe)}' for exe in
                        ('chromium', 'chromium-browser', 'google-chrome', 'firefox', 'playwright') if shutil.which(exe)]
    automation = [name for name in ('@playwright/test', 'playwright', 'puppeteer', 'cypress') if name in deps]
    desktop_size = png_dimensions(desktop_screenshot)
    mobile_size = png_dimensions(mobile_screenshot)
    visuals_passed = bool(desktop_size and mobile_size and
                          desktop_size[0] > mobile_size[0] and interactions_verified)
    if visuals_passed:
        bstatus = 'UNVERIFIED'
        bmsg = ('PNG integrity and distinct viewport widths checked; capture provenance, '
                'page rendering and interaction results are agent-attested, not independently verified.')
    elif automation or browser_binaries:
        bstatus = 'UNVERIFIED'
        bmsg = 'Potential browser/test tooling detected; functional desktop/mobile screenshot and interaction tests remain unverified.'
    else:
        bstatus = 'MISSING'
        bmsg = 'No local browser/test tools detected; remote agent browser tools cannot be inspected here.'
    screenshot_ev = []
    for label, path, size in [('Desktop screenshot', desktop_screenshot, desktop_size),
                             ('Mobile screenshot', mobile_screenshot, mobile_size)]:
        if path is not None:
            screenshot_ev.append(f'{label}: {path} (validated PNG dimensions: {size})')
    if interactions_verified:
        screenshot_ev.append('Interactions: explicitly attested by invoking agent/user; cannot be independently tested by this script')
    results.append(check(7, 'Browser and visual testing', bstatus, bmsg,
        evidence=automation + browser_binaries + screenshot_ev,
        next_steps=[] if visuals_passed else [
            'Agent: use browser/MCP tooling or manual QA to test a rendered website, capture desktop and mobile screenshots, and verify navigation/interaction.',
            'For release supply non-interlaced 8-bit PNG captures at distinct desktop/mobile widths and attest interactions only after real QA.'],
        blocking=release and not visuals_passed,
        evidence_scope='filesystem+attestation' if visuals_passed else 'filesystem'))

    # 8 — Optional creative tooling
    candidates = ('matter-js', 'three', '@react-three/fiber', 'pixi.js', 'ogl',
                  'lottie-web', 'lenis', 'motion', 'framer-motion', '@rive-app/react-canvas')
    declared_optional = [name for name in candidates if name in deps]
    optional_binaries = [f'{exe}: {shutil.which(exe)}' for exe in
                         ('inkscape', 'magick', 'convert', 'ffmpeg') if shutil.which(exe)]
    optional = declared_optional + optional_binaries
    results.append(check(8, 'Optional creative tools',
        'UNVERIFIED' if declared_optional else ('VERIFIED' if optional_binaries else 'DEFERRED'),
        'Optional declarations/locations found; verify functionality only when required.' if optional else
        'No optional tools detected; choose them only when the treatment requires them.',
        evidence=optional,
        evidence_scope='filesystem+declaration' if declared_optional and optional_binaries else
                       ('declaration' if declared_optional else 'filesystem'),
        next_steps=['Use tools required by approved scope; their declarations do not prove installation.']))

    for id_, evidence in observations.items():
        item = results[id_ - 1]
        if item['status'] == 'DEFERRED':
            continue
        if id_ == 4 and selected is None:
            raise ValueError('Agent observations cannot disambiguate applications; supply --source-root.')
        item['local_status'] = item['status']
        item['status'] = 'UNVERIFIED'
        item['evidence_scope'] = 'agent-attestation'
        item['evidence'].append('Agent reports: ' + evidence)
        item['summary'] += ' Scoped agent evidence accepted; not independently verified by this checker.'
        item['blocking'] = False

    blockers = [r['name'] for r in results if r['blocking']]
    caveats = [r['name'] for r in results if r['id'] != 8 and
               r['status'] not in ('VERIFIED', 'DEFERRED') and not r['blocking']]
    gate = 'BLOCKED' if blockers else ('DEGRADED' if caveats else 'READY')
    return {
        'schema_version': '1.1', 'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'skill': SKILL_NAME, 'project_root': str(project), 'phase': phase,
        'source_root': str(selected) if selected else None,
        'gsap_required': gsap_required, 'creative_approval_verified': False,
        'applications': [{'root': str(p), 'framework': detect_framework(get_dependencies([p])),
                          'declared_packages': sorted(get_dependencies([p]))} for p in roots],
        'active_agent': agent, 'overall_gate': gate, 'checks_reviewed': len(results),
        'checks_total': 8, 'blockers': blockers, 'caveats': caveats,
        'limitations': [
            'Read-only and offline. No packages or skills are installed by this checker.',
            'Filesystem discovery cannot prove a skill is activated in the agent session.',
            'Tool and browser availability exposed only to the AI agent must be confirmed by that agent.',
            'Files found do not imply story approval, valid imports, animation correctness or visual quality.'
        ],
        'results': results
    }


def render_human(report: dict[str, Any]) -> str:
    lines = [f'CINEMATIC WEB DIRECTOR — PHASE 0 PREFLIGHT',
             f'Project: {report["project_root"]}', f'Phase: {report["phase"]} | Agent: {report["active_agent"]}',
             f'Gate: {report["overall_gate"]} | {report["checks_reviewed"]}/{report["checks_total"]} reviewed (NOT 8/8 passed)', '']
    for r in report['results']:
        lines.append(f'[{r["status"]}; {r["evidence_scope"]}] {r["id"]}. {r["name"]}' +
                     (' [BLOCKER]' if r['blocking'] else ''))
        lines.append('  ' + r['summary'])
        for ev in r['evidence'][:6]:
            lines.append('  evidence: ' + ev)
        if len(r['evidence']) > 6:
            lines.append(f'  ...and {len(r["evidence"])-6} more evidence item(s)')
        for step in r['next_steps']:
            lines.append('  next: ' + step)
        lines.append('')
    if report['blockers']:
        lines.append('Resolve blockers before proceeding to this phase: ' + '; '.join(report['blockers']))
    else:
        lines.append('Technical scope is not blocked. Creative/prototype/sprint approvals and live QA remain agent-side gates.')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path.cwd(), help='Website project root (default: cwd)')
    parser.add_argument('--agent', choices=('auto', 'claude-code', 'codex', 'cursor', 'other'), default='auto')
    parser.add_argument('--phase', choices=('discovery', 'prototype', 'implementation', 'release'), default='discovery')
    parser.add_argument('--source-root', type=Path, help='Actual application directory, absolute or relative to project')
    parser.add_argument('--script', type=Path, help='Existing brief/script, absolute or relative to project')
    parser.add_argument('--skill-root', type=Path, action='append', default=[],
                        help='Additional parent directory of official GSAP skill folders; repeatable')
    parser.add_argument('--gsap', choices=('required', 'not-required'), default='required',
                        help='Requirements of the approved batch; default: required')
    parser.add_argument('--gsap-skill', choices=GSAP_SKILLS, action='append', default=[],
                        help='Additional GSAP topic required by the approved treatment; repeatable')
    parser.add_argument('--observations', type=Path,
                        help='Project/source/phase-bound JSON attestations for checks 3, 4 and 6')
    parser.add_argument('--allow-gsap-docs-fallback', action='store_true',
                        help='Use only with explicit project owner approval, when official agent skills are unavailable')
    parser.add_argument('--desktop-screenshot', type=Path, help='Existing desktop screenshot from real visual QA')
    parser.add_argument('--mobile-screenshot', type=Path, help='Existing mobile screenshot from real visual QA')
    parser.add_argument('--interactions-verified', action='store_true',
                        help='Attest that the page interactions were actually smoke-tested')
    parser.add_argument('--format', choices=('human', 'json'), default='human')
    parser.add_argument('--out', type=Path, help='Optional report file path; by default prints only')
    args = parser.parse_args()
    if not args.project.expanduser().is_dir():
        parser.error(f'Project directory not found: {args.project}')
    try:
        project = args.project.expanduser().resolve()
        selected = select_source(project, package_roots(project), args.source_root)
        observations = load_observations(args.observations, project, args.phase, selected) if args.observations else {}
        report = run(project, args.agent, args.phase, args.allow_gsap_docs_fallback,
                     desktop_screenshot=args.desktop_screenshot, mobile_screenshot=args.mobile_screenshot,
                     interactions_verified=args.interactions_verified, source_root=args.source_root,
                     script_path=args.script, extra_skill_roots=args.skill_root,
                     gsap_required=args.gsap == 'required', required_gsap_skills=args.gsap_skill,
                     observations=observations)
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    output = json.dumps(report, indent=2, ensure_ascii=False) if args.format == 'json' else render_human(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output + '\n', encoding='utf-8')
    print(output)
    return 2 if report['overall_gate'] == 'BLOCKED' else 0


if __name__ == '__main__':
    sys.exit(main())
