# Cinematic Web Director (v0.2.0)

An Agent Skills-format creative production partner for creating or redesigning landing pages, portfolios and product websites. It guides discovery, content and copy, site structure, art direction, purposeful motion, approved experiments, production sprints and critique. It accommodates experienced developers who are new to motion design.

The package contains agent instructions and adaptable templates, plus an executable offline eight-check preflight. Creative effectiveness requires real use and rendered website evaluation; the checker does not generate a website or certify its design quality.

Download the [v0.2.0 release and ZIP](https://github.com/abrahamnaiborhu/cinematic-web-director/releases/tag/v0.2.0), follow the [beginner tutorial](TUTORIAL.md), or read the [changelog](CHANGELOG.md). This is a development pre-release.

## Start a project or redesign

Invoke the installed skill and describe what you want to build or improve. For example:

> Help redesign my portfolio. Inspect the existing site and materials in this project, help me improve its story and presentation, and develop the direction with me before production.

The director asks one focused question at a time where possible, inspects available materials, proposes and explains alternatives, and helps establish an approved brief. References may remain anywhere relevant in the project. If more material is useful, the director can suggest `creative/references/`; links can go in a Markdown file.

Pre-production approves the overall site structure, important visitor journeys, content and creative direction. Small motion prototypes require explicit, bounded approval. Detailed treatments and acceptance criteria are approved for upcoming sprint batches. The agent then builds, verifies, critiques and refines continuously through the approved plan, reporting results without mandatory reapproval at every sprint boundary. Changes to scope, creative intent or model authorization return for the relevant decision.

Architecture is evaluated with the creative requirements. Existing tools may be retained, extended or migrated; no particular framework, state library, backend or effect is mandatory. Model configurations and responsibilities are agreed per scope, with visible handoff notices and honest limits on runtime identity/detection.

## Install the skill

Run from your website project for a project-scoped installation (choose your agent):

```bash
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent codex
# Other examples:
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent claude-code
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent cursor
```

Add `--global` to reuse the skill across projects. For an exact version, install the extracted release directory as a local source; see the tutorial.

For manual installation, copy the complete directory to the target agent's configured skills location and confirm that the session can read it. This repository revision does not install the skill or external tools into your agent.

## Package guide

- [SKILL.md](SKILL.md): role, entry points, principles and routing.
- [Creative workflow](references/CREATIVE_WORKFLOW.md): discovery, redesign, storyboarding, approvals, prototypes, architecture, model handoff, sprints and critique.
- [Preflight protocol](references/PREFLIGHT_PROTOCOL.md): evidence meanings, phases, paths, observations and release requirements.
- [Project script](templates/PROJECT_SCRIPT.md): evolving brief, sources, copy/content, journeys, architecture, approvals, model agreement and sprint plan.
- [Continuity bible](templates/CONTINUITY_BIBLE.md): shared identity and connections across pages, scenes and states.
- [Treatment](templates/SCENE_TREATMENT.md): storyboard, interaction/motion detail, optional prototype agreement and acceptance criteria.
- [Iteration log](templates/ITERATION_LOG.md): evidence, corrections, decisions, handoffs and sprint outcomes.

Templates are maintained by the director with the client. Adapt them and reuse equivalent existing project documents. A blank template or nonempty brief is not an approval.

## Run preflight

The examples below run from this skill directory, against a separate website project:

```bash
python3 -B scripts/preflight.py --project /path/to/site --agent codex --phase discovery
python3 -B scripts/preflight.py --project /path/to/site --agent codex --phase prototype
python3 -B scripts/preflight.py --project /path/to/site --agent codex --phase implementation --gsap-skill gsap-timeline --gsap-skill gsap-scrolltrigger
```

For an unusual layout, use `--source-root`, `--script` and repeatable `--skill-root`. For an approved batch without GSAP work, use `--gsap not-required`. Each application keeps its own dependency findings. Codex custom skill locations honor `CODEX_HOME`.

The checker has no third-party Python dependencies. Use Python 3.10 or newer. It makes no network calls, installs or browser launches, and writes only when `--out` is explicitly supplied:

```bash
python3 -B scripts/preflight.py --project /path/to/site --agent codex --phase discovery --format json --out ./preflight.json
```

Exit `0` means the technical scope is not blocked, possibly DEGRADED. Exit `2` means blocked or invalid input. **8/8 reviewed measures inspection coverage.** Agent declarations, inference and observations are distinguished from local evidence; creative approval is always a separate agent-side gate.

Project/source/phase-bound observations can supply actual session evidence for skill access, unusual source layouts or runtime imports through `--observations`. They remain explicitly unverified attestations. See the protocol for the JSON contract and limitations.

For release:

```bash
python3 -B scripts/preflight.py --project /path/to/site --agent codex --phase release --desktop-screenshot ./qa/desktop.png --mobile-screenshot ./qa/mobile.png --interactions-verified
```

Use supported non-interlaced 8-bit PNG captures at distinct desktop/mobile widths. The checker validates image structure and dimensions; capture provenance, visual quality and interactions remain agent-attested. The protocol documents supported encodings and size limits.

## Official GSAP resources

Prefer the relevant installed [official GreenSock skills](https://github.com/greensock/gsap-skills). Install them separately within authorized scope:

```bash
npx skills add https://github.com/greensock/gsap-skills --agent codex
```

This skill owns creative direction and production coordination; the official suite supplies GSAP implementation guidance. An explicitly approved official-documentation fallback is available when skill access is unavailable. No installation is implied by a URL or file inventory.

## Package a release

Update the README version and changelog entry, run the tests, then build the archive:

```bash
python3 -B scripts/package_release.py --version 0.2.0 --out dist
```

This produces `dist/cinematic-web-director-v0.2.0.zip` and `dist/SHA256SUMS.txt`. The ZIP contains one `cinematic-web-director/` directory with the skill, tutorial, references, templates, scripts and tests. Packaging uses an explicit file list and reproducible archive metadata; Git metadata, secrets, caches and previous build output are excluded.

## Validation scope

Run the offline checker regressions:

```bash
python3 -B -m unittest discover -s tests -v
```

They cover release packaging and phase gates, custom/agent skill locations, static and multi-application projects, scoped observations, selected GSAP requirements, runtime metadata, release evidence and CLI behavior. Fixtures and generated PNGs validate checker behavior, not a real website's creative quality.

The revised instructions were also reviewed against the scenarios below. This was a manual instruction walkthrough, not an independent agent execution or rendered-site trial:

| Scenario | Workflow response reviewed |
|---|---|
| Empty landing-page project | Intent clarification and guided discovery; defer missing implementation tools |
| Existing portfolio with scattered references | Inventory sources, inspect available baseline, clarify reference roles, develop browsing/case-study structure |
| Multi-page product site with existing data tools | Evaluate visitor journeys and application boundaries; justify reuse/additions/migration |
| New material during production | Review affected decisions/versions and preserve independent authorized work |
| Model unavailable or fallback requested | Disclose configuration/evidence, apply scoped authorization or pause dependent work |
| Interactive physics experiment | Explicit prototype scope and appropriate reset/replay/return choice |

Live portability tests in Claude Code, Cursor and Codex, independent behavioral evaluations, and rendered website trials remain necessary to establish real-world creative effectiveness. The bundled external skill validator requires PyYAML; when it is unavailable, do not claim that validator passed. Frontmatter, local links and package consistency can still be inspected without installing dependencies.

References:

- https://agentskills.io/specification
- https://github.com/vercel-labs/skills
- https://github.com/greensock/gsap-skills
