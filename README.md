# Cinematic Web Director — Preflight-enabled Skill (v0.1)

A portable Agent Skills-format starter for beginner-friendly, narrative-led web art direction. This package implements **Phase 0** as an executable, read-only eight-check preflight and provides the workflow and artifact templates for subsequent creative stages.

It is **not** an auto-installed GSAP package, an automatic website generator, or a completed Simpul project. The original Simpul Markdown is not modified.

## Install the skill

Extract the folder and install it into the target agent (from the folder **above** `cinematic-web-director/`):

```bash
npx skills add ./cinematic-web-director --agent claude-code
# or
npx skills add ./cinematic-web-director --agent cursor
# or
npx skills add ./cinematic-web-director --agent codex
```

The Skills CLI supports local paths; for an offline/manual installation, copy the full skill directory into the agent's configured skills location. Reopen the agent session if needed for skill discovery.

## Run the Phase 0 checker directly

```bash
python3 cinematic-web-director/scripts/preflight.py --project /path/to/website --agent claude-code --phase discovery
```

Rerun just before GSAP coding:

```bash
python3 cinematic-web-director/scripts/preflight.py --project /path/to/website --agent claude-code --phase implementation
```

Obtain a machine-readable report if desired:

```bash
python3 cinematic-web-director/scripts/preflight.py --project /path/to/website --agent claude-code --phase discovery --format json --out ./preflight.json
```

The checker performs **no network calls, no installs and no writes unless `--out` is used**. It can tell you what it sees in conventional local paths, but it cannot access Claude/Cursor/Codex capabilities that are exposed only inside the agent's session. The agent must combine its own live tool inventory with the filesystem report.

Release preflight requires real desktop/mobile screenshot files and an explicit interaction test attestation: `--desktop-screenshot ./qa/desktop.png --mobile-screenshot ./qa/mobile.png --interactions-verified`.

Exit code `0`: phase not blocked (may be DEGRADED). Exit code `2`: BLOCKED. `8/8 reviewed` measures the number inspected—not eight passed.

## Official GSAP skills

Install separately with permission:

```bash
npx skills add https://github.com/greensock/gsap-skills --agent claude-code
```

Check details in `references/PREFLIGHT_PROTOCOL.md` and the external source: https://github.com/greensock/gsap-skills.

## Project documents

The project-specific script and continuity files are **templates**, not hardcoded Simpul content. Develop them during the guided workflow. The checker intentionally treats a missing script as normal during discovery.

## Validation scope

Tests verify the local checker using isolated fixture projects. They do **not** prove a real user's agent sees GreenSock skills or that a browser can render their website. Those require tests on the user's computer or connected execution environment.

References:
- https://agentskills.io/specification
- https://github.com/vercel-labs/skills
- https://github.com/greensock/gsap-skills
