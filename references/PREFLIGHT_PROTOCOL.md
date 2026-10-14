# Phase 0 — Preflight Protocol

## Why this exists

Beginners must not be expected to know their coding-agent setup. The director first inspects available tools and documents the gaps. Run at the start of a project or when the agent, workspace, or dependencies change. Re-run before implementation and release.

**Never conflate inspection with success.** Each check must be reviewed, but some will be MISSING / DEFERRED / UNVERIFIED. A file on disk is not proof that an AI has loaded it, and an installed browser package is not proof that the agent can take screenshots.

## Eight checks

| # | Check | Auto-observable evidence | Agent-side follow-up | Stage consequence |
|---|---|---|---|---|
| 1 | AI agent identification | Explicit agent ID, or tentative environment variable | Agent declares its own identity and tool permissions | Unverified ID is a caveat, not an invented detection |
| 2 | Cinematic Web Director Skill | SKILL.md and reference files readable with expected metadata | Confirm this session actually loaded instructions | Missing skill package blocks all phases |
| 3 | Official GreenSock Skills | Readable GSAP skill files in relevant agent folders | Verify active-agent discovery, especially plugin marketplace installs; read core/timeline/scrolltrigger and relevant plugin instructions | Missing skills warn during discovery; block implementation unless owner explicitly approves docs fallback |
| 4 | Project environment | package.json, lockfiles, conventional source paths | Identify unusual monorepo/non-JS layout; inspect real source | No identified source blocks existing-code implementation, not discovery |
| 5 | Project script | PROJECT_SCRIPT.md or equivalent at common locations | Read content, assess factual completeness, seek story approval | Absence expected in discovery; must be approved before implementation |
| 6 | GSAP runtime package | declared `gsap` dependency and accessible node_modules package | Verify bundler import/CDN in a running browser, verify plugin imports | Deferred during story stages; missing runtime blocks GSAP coding |
| 7 | Browser and visual testing | Playwright/Puppeteer/Cypress manifest or local executables | Confirm agent-side browser/MCP tools and perform real screenshots/interaction tests | Release blocks until desktop/mobile screenshots and actual interaction tests are supplied |
| 8 | Optional creative tools | matter-js, three.js, SVG tools, ffmpeg, etc. | Choose only when scene treatment warrants it | No block by default |

## Status meanings

- **VERIFIED:** specific inspectable evidence exists. The script's verification is filesystem-level; it is not a blanket endorsement of runtime behavior or agent visibility.
- **UNVERIFIED:** plausible evidence or declared intent exists but decisive verification is outside the script's scope.
- **MISSING:** the tool or document is not found in inspected locations; do not equate this with absent everywhere.
- **DEFERRED:** a dependency is not necessary for the present stage.
- **BLOCKED overall gate:** one or more phase-critical checks cannot proceed. Fix them before attempting that phase.
- **DEGRADED overall gate:** no current blockers but at least one caveat exists. Proceed with limitations made clear.
- **READY overall gate:** all eight checks are verified for the current scope. This does not certify web-design quality.

## How to run

From the skill root:

```bash
python3 scripts/preflight.py --project /path/to/site --agent claude-code --phase discovery
python3 scripts/preflight.py --project /path/to/site --agent cursor --phase implementation
python3 scripts/preflight.py --project /path/to/site --agent codex --phase release --format json
```

Supported agent values: `claude-code`, `cursor`, `codex`, `other`, `auto`. `auto` can only infer from limited environment hints and often results in `UNVERIFIED`. This is more accurate than claiming to detect an active agent from unrelated folders.

Optional: `--out ./preflight-report.json --format json`. This *explicitly* saves a report; default operation is read-only. Re-execute after installing dependencies. CLI exit code `2` denotes a BLOCKED gate; `0` means the current stage is not blocked.

If the official GSAP agent skills cannot be installed, an implementation phase may use the `--allow-gsap-docs-fallback` exception **only after explicit approval** and must consult current official GSAP documentation. The exception does not pretend agent skills are present.

## Corrective steps

- GSAP agent skills: official https://github.com/greensock/gsap-skills — `npx skills add https://github.com/greensock/gsap-skills --agent claude-code` (replace agent as appropriate). Ask permission before executing.
- Verify existing installation from `npx skills list` and, where applicable, `npx skills ls -a claude-code`. CLI inventory is a cross-check, not proof the current agent loaded the skill.
- Plugin marketplace installs for Claude Code or remote rules for Cursor may not appear in the locations scanned. If tool metadata confirms those skills are loaded, document that evidence rather than overriding it with a false negative from the script.
- A missing PROJECT_SCRIPT.md should trigger creative discovery, not a premature blank document declaration as "approved".
- For a non-Node or nested monorepo, supply the actual source root as `--project` or manually augment the report; automated detection is necessarily conservative.
- Browser tests must include actual screenshots and UI interaction at representative viewports. Presence of Playwright in package.json is insufficient.

## Truth and safety constraints

This script never installs dependencies, accesses the network, modifies the website or asks for credentials. It does not scan private data outside narrowly expected skill roots and project manifests. Treat this report as **preflight evidence**, not an authoritative inventory of all installed programs on a computer.
