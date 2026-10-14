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
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SKILL_NAME = 'cinematic-web-director'
GSAP_SKILLS = (
    'gsap-core', 'gsap-timeline', 'gsap-scrolltrigger', 'gsap-plugins',
    'gsap-utils', 'gsap-react', 'gsap-performance', 'gsap-frameworks'
)
BASE_REQUIRED_GSAP = ('gsap-core', 'gsap-timeline', 'gsap-scrolltrigger', 'gsap-plugins', 'gsap-performance')
SKILL_DIR = Path(__file__).resolve().parents[1]


def check(id_: int, name: str, status: str, summary: str, *, evidence=None,
          next_steps=None, blocking: bool = False) -> dict[str, Any]:
    return {
        'id': id_, 'name': name, 'status': status, 'blocking': blocking,
        'summary': summary, 'evidence': evidence or [], 'next_steps': next_steps or []
    }


def read_package(p: Path) -> dict:
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, UnicodeError):
        return {}


def package_roots(project: Path) -> list[Path]:
    candidates = [project, project / 'frontend', project / 'web', project / 'client',
                  project / 'site', project / 'apps' / 'web', project / 'apps' / 'frontend',
                  project / 'packages' / 'web']
    return [p for p in candidates if (p / 'package.json').is_file()]


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
        paths = [project / '.agents' / 'skills', home / '.agents' / 'skills', home / '.codex' / 'skills']
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
                        prefix = file.read(250)
                    if prefix.startswith('---') and f'name: {name}' in prefix:
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
            if path.is_file() and path.stat().st_size > 0:
                return path
    return None


def detect_framework(dependencies: dict) -> str:
    for dep, label in (
        ('next', 'Next.js'), ('nuxt', 'Nuxt'), ('@sveltejs/kit', 'SvelteKit'),
        ('astro', 'Astro'), ('@angular/core', 'Angular'), ('svelte', 'Svelte'),
        ('vue', 'Vue'), ('react', 'React'), ('vite', 'Vite'),
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


def valid_screenshot(path: Path | None) -> bool:
    if path is None or not path.expanduser().is_file():
        return False
    try:
        p = path.expanduser()
        if p.stat().st_size < 100:
            return False
        with p.open('rb') as file:
            h = file.read(12)
        return h.startswith(b'\x89PNG\r\n\x1a\n') or h.startswith(b'\xff\xd8\xff') or (h.startswith(b'RIFF') and h[8:12] == b'WEBP')
    except OSError:
        return False


def run(project: Path, agent_arg: str, phase: str, allow_docs_fallback: bool,
        home: Path | None = None, desktop_screenshot: Path | None = None,
        mobile_screenshot: Path | None = None, interactions_verified: bool = False) -> dict[str, Any]:
    project = project.expanduser().resolve()
    home = home or Path.home()
    implementation = phase in ('implementation', 'release')
    release = phase == 'release'
    agent, agent_evidence = identify_agent(agent_arg)
    roots = package_roots(project)
    deps = get_dependencies(roots)
    framework = detect_framework(deps)
    results = []

    # 1 — Agent identification
    agent_known = agent in ('claude-code', 'cursor', 'codex', 'other')
    results.append(check(1, 'AI agent identification', 'VERIFIED' if agent_known else 'UNVERIFIED',
        f'Active agent: {agent}.', evidence=[agent_evidence],
        next_steps=[] if agent_known else ['Pass --agent claude-code|cursor|codex|other from the active agent.']))

    # 2 — Skill self integrity (filesystem, not runtime activation)
    skill_main = SKILL_DIR / 'SKILL.md'
    resources = [SKILL_DIR / 'references' / 'PREFLIGHT_PROTOCOL.md',
                 SKILL_DIR / 'references' / 'CREATIVE_WORKFLOW.md',
                 SKILL_DIR / 'templates' / 'PROJECT_SCRIPT.md']
    missing = [str(p.relative_to(SKILL_DIR)) for p in [skill_main] + resources if not p.is_file()]
    body = skill_main.read_text(encoding='utf-8') if skill_main.is_file() else ''
    valid_header = body.startswith('---\n') and ('name: ' + SKILL_NAME) in body.split('---', 2)[1] if body.startswith('---\n') else False
    self_pass = not missing and valid_header
    results.append(check(2, 'Cinematic Web Director Skill', 'VERIFIED' if self_pass else 'MISSING',
        'Skill entry point and required references are readable on disk.' if self_pass else 'Skill package is incomplete or SKILL.md metadata is invalid.',
        evidence=[str(skill_main)] + ([f'Missing: {item}' for item in missing] if missing else []),
        next_steps=['Agent must also confirm that it has loaded SKILL.md instructions; disk access alone does not prove activation.'] if self_pass else ['Reinstall the complete cinematic-web-director skill package.'],
        blocking=not self_pass))

    # 3 — Official GSAP agent skills
    search_roots = skill_roots(project, agent, home)
    if agent == 'claude-code':
        search_roots += claude_plugin_skill_roots(home)
    found = available_gsap_skills(search_roots)
    required = list(BASE_REQUIRED_GSAP)
    if framework in ('React', 'Next.js'):
        required.append('gsap-react')
    if framework in ('Vue', 'Nuxt', 'Svelte', 'SvelteKit'):
        required.append('gsap-frameworks')
    missing_required = [name for name in required if name not in found]
    missing_optional = [name for name in GSAP_SKILLS if name not in found and name not in required]
    if not missing_required:
        skill_status = 'VERIFIED' if agent_known else 'UNVERIFIED'
        skill_message = f'All {len(required)} required official GSAP skill files are readable in the inspected skill directories.'
    else:
        skill_status = 'MISSING'
        skill_message = f'{len(found)}/8 official GSAP skill files found; missing required: {", ".join(missing_required)}.'
    skill_block = bool(missing_required and implementation and not allow_docs_fallback)
    steps = ['Active agent: explicitly read the relevant GSAP SKILL.md files and confirm they are discoverable in this session.']
    if missing_required:
        steps.extend(['Install the official suite with consent: npx skills add https://github.com/greensock/gsap-skills --agent ' + (agent if agent_known and agent != 'other' else '<your-agent>'),
                      'Then rerun the preflight and test actual agent access.'])
    if allow_docs_fallback and missing_required:
        steps.append('Explicit fallback accepted: follow and verify current official GSAP documentation instead; record this exception in the project.')
    results.append(check(3, 'GreenSock official GSAP Skills', skill_status, skill_message,
        evidence=[f'{name}: {path}' for name, path in sorted(found.items())] +
                 [f'Optional suite skills absent: {", ".join(missing_optional)}'] +
                 (['Claude plugin marketplace installation may not be visible to this filesystem scan.'] if agent == 'claude-code' else []),
        next_steps=steps, blocking=skill_block))

    # 4 — Project structure and package manager
    if roots:
        proj_status = 'VERIFIED'
        proj_message = f'Found {len(roots)} JS package manifest(s); detected {framework}; package manager: {package_manager(project, roots)}.'
        proj_ev = [str(root / 'package.json') for root in roots]
    else:
        proj_status = 'UNVERIFIED'
        proj_message = 'No package.json in the standard root/frontend/web/app locations. May be a blank project or a non-Node project.'
        proj_ev = [f'Project directory exists: {project.is_dir()}']
    results.append(check(4, 'Project environment', proj_status, proj_message,
        evidence=proj_ev,
        next_steps=[] if roots else ['Identify the source root and framework; for an empty project, create the scaffold only after creative approval.'],
        blocking=implementation and not roots))

    # 5 — Project script
    script = get_project_script(project)
    results.append(check(5, 'Project script', 'VERIFIED' if script else 'MISSING',
        f'Found nonempty script/brief: {script.name}.' if script else 'No project-specific script or creative brief found in standard locations.',
        evidence=[str(script)] if script else [],
        next_steps=['Read and assess the script: file presence does not guarantee narrative completeness.'] if script else
                   ['Discovery phase: collaboratively create PROJECT_SCRIPT.md using the bundled template.',
                    'Implementation phase: approve the script and continuity decisions first.'],
        blocking=implementation and not bool(script)))

    # 6 — GSAP package (runtime) in target project
    installed = [(root / 'node_modules' / 'gsap' / 'package.json') for root in roots]
    installed = [p for p in installed if p.is_file()]
    manifest_gsap = 'gsap' in deps
    if installed:
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
        next_steps=[] if installed else ['Before implementation, check package root and run a user-approved package install if required.',
                                         'For a CDN-based site, manually verify actual script loading and plugin availability.'],
        blocking=implementation and not bool(installed)))

    # 7 — Browser and visual test capabilities
    browser_binaries = [f'{exe}: {shutil.which(exe)}' for exe in
                        ('chromium', 'chromium-browser', 'google-chrome', 'firefox', 'playwright') if shutil.which(exe)]
    automation = [name for name in ('@playwright/test', 'playwright', 'puppeteer', 'cypress') if name in deps]
    visuals_passed = bool(valid_screenshot(desktop_screenshot) and valid_screenshot(mobile_screenshot) and interactions_verified)
    if visuals_passed:
        bstatus = 'VERIFIED'
        bmsg = 'Actual desktop/mobile image artifacts exist and the running agent attests interaction checks were performed.'
    elif automation or browser_binaries:
        bstatus = 'UNVERIFIED'
        bmsg = 'Potential browser/test tooling detected; functional desktop/mobile screenshot and interaction tests remain unverified.'
    else:
        bstatus = 'MISSING'
        bmsg = 'No local browser/test tools detected; remote agent browser tools cannot be inspected here.'
    screenshot_ev = []
    for label, path in [('Desktop screenshot', desktop_screenshot), ('Mobile screenshot', mobile_screenshot)]:
        if path is not None:
            screenshot_ev.append(f'{label}: {path} (valid image: {valid_screenshot(path)})')
    if interactions_verified:
        screenshot_ev.append('Interactions: explicitly attested by invoking agent/user; cannot be independently tested by this script')
    results.append(check(7, 'Browser and visual testing', bstatus, bmsg,
        evidence=automation + browser_binaries + screenshot_ev,
        next_steps=[] if visuals_passed else [
            'Agent: use browser/MCP tooling or manual QA to test a rendered website, capture desktop and mobile screenshots, and verify navigation/interaction.',
            'On release preflight pass --desktop-screenshot PATH --mobile-screenshot PATH --interactions-verified only after those real tests pass.'],
        blocking=release and not visuals_passed))

    # 8 — Optional creative tooling
    candidates = ('matter-js', 'three', '@react-three/fiber', 'pixi.js', 'ogl',
                  'lottie-web', 'lenis', 'motion', 'framer-motion', '@rive-app/react-canvas')
    optional = [name for name in candidates if name in deps]
    optional += [f'{exe}: {shutil.which(exe)}' for exe in ('inkscape', 'magick', 'convert', 'ffmpeg') if shutil.which(exe)]
    results.append(check(8, 'Optional creative tools', 'VERIFIED' if optional else 'DEFERRED',
        'Some creative tooling exists.' if optional else 'No optional creative tools detected; choose tools only when the motion treatment requires them.',
        evidence=optional,
        next_steps=['Do not install physics/graphics libraries without an approved scene-level need.']))

    blockers = [r['name'] for r in results if r['blocking']]
    caveats = [r['name'] for r in results if r['status'] not in ('VERIFIED',) and not r['blocking']]
    gate = 'BLOCKED' if blockers else ('DEGRADED' if caveats else 'READY')
    return {
        'schema_version': '1.0', 'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'skill': SKILL_NAME, 'project_root': str(project), 'phase': phase,
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
        lines.append(f'[{r["status"]}] {r["id"]}. {r["name"]}' + (' [BLOCKER]' if r['blocking'] else ''))
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
        lines.append('Current phase may proceed, subject to agent-side confirmation and documented caveats.')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path.cwd(), help='Website project root (default: cwd)')
    parser.add_argument('--agent', choices=('auto', 'claude-code', 'codex', 'cursor', 'other'), default='auto')
    parser.add_argument('--phase', choices=('discovery', 'implementation', 'release'), default='discovery')
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
    report = run(args.project, args.agent, args.phase, args.allow_gsap_docs_fallback,
                 desktop_screenshot=args.desktop_screenshot, mobile_screenshot=args.mobile_screenshot,
                 interactions_verified=args.interactions_verified)
    output = json.dumps(report, indent=2, ensure_ascii=False) if args.format == 'json' else render_human(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output + '\n', encoding='utf-8')
    print(output)
    return 2 if report['overall_gate'] == 'BLOCKED' else 0


if __name__ == '__main__':
    sys.exit(main())
