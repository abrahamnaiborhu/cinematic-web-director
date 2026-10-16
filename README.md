# Cinematic Web Director (v0.4.1)

An Agent Skills-format creative production partner for creating or redesigning landing pages, portfolios and product websites. It guides discovery, content and copy, site structure, art direction, purposeful motion, approved experiments, production sprints and critique. It accommodates experienced developers who are new to motion design.

The package contains agent instructions and adaptable templates, plus an executable offline eight-check preflight. Creative effectiveness requires real use and rendered website evaluation; the checker does not generate a website or certify its design quality.

This revision prepares the v0.4.1 development candidate; it is not a published release. Previously published packages are available through [GitHub releases](https://github.com/abrahamnaiborhu/cinematic-web-director/releases), including [v0.2.0](https://github.com/abrahamnaiborhu/cinematic-web-director/releases/tag/v0.2.0). Follow the [beginner tutorial](TUTORIAL.md) or read the [changelog](CHANGELOG.md).

v0.3 focuses on design judgment: establish the freedom to redesign, extract the story independently of the old section list, explain inherited presentation, explore different ways to frame real content, and inspect composition before choreography. A metaphor, signature-interaction count, visual style or scroll-effect checklist is never mandatory. See [design direction](references/DESIGN_DIRECTION.md).

v0.4 adds proactive [motion direction](references/MOTION_DIRECTION.md). The director initiates motion discussion, develops concrete ideas from content and journeys, offers alternatives, recommends an approach and asks an informed experiential question. Composition and motion intent develop together; static-state review precedes detailed choreography. Clients need not invent effects or supply references. Explicit static-site choices and all scoped implementation approvals remain authoritative.

v0.4.1 makes [device experience](references/DEVICE_EXPERIENCE.md) explicit: develop phones and compact laptop windows from the start, author suitable motion adaptations, consider available height/input/browser behavior, and keep emulation distinct from real-device evidence. Reuse vector UI icons when consistent geometry is needed instead of relying on platform emoji presentation. Supported device/browser coverage follows the assignment, not a promise to test every device.

The platform plan explicitly considers Android, iOS/iPadOS, Windows, macOS and Linux where relevant, with representative browser/version targets. A report on one platform remains a regression case within that broader plan; shared icon/motion fixes need relevant cross-platform checks, not an OS-only assumption.

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

GitHub installation follows the remote default branch. To try this candidate before publication, install a local copy of this revision or its generated ZIP; the commands above do not select this unpublished branch automatically.

For manual installation, copy the complete directory to the target agent's configured skills location and confirm that the session can read it. This repository revision does not install the skill or external tools into your agent.

## Package guide

- [SKILL.md](SKILL.md): role, entry points, principles and routing.
- [Creative workflow](references/CREATIVE_WORKFLOW.md): discovery, redesign, storyboarding, approvals, prototypes, architecture, model handoff, sprints and critique.
- [Design direction](references/DESIGN_DIRECTION.md): redesign freedom, story/content, inherited choices, concept alternatives, composition, motion emphasis and design critique.
- [Motion direction](references/MOTION_DIRECTION.md): creative initiative, opportunity discovery, concrete temporal proposals, recommendations, client discussion and motion critique.
- [Device experience](references/DEVICE_EXPERIENCE.md): audience coverage, phone/compact-laptop/large-screen treatments, input, browser chrome, UI icons and evidence limits.
- [Design evaluation scenarios](evaluations/DESIGN_DIRECTION.md): synthetic client requests, minimal materials and separate review criteria for fresh-session trials.
- [Motion evaluation cases](evaluations/MOTION_DIRECTION.md): absent client ideas, existing client-originated animations, sparse briefs, static-site constraints and approved-sprint scope.
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
python3 -B scripts/package_release.py --version 0.4.1 --out dist/v0.4.1
```

This produces `dist/v0.4.1/cinematic-web-director-v0.4.1.zip` and `dist/v0.4.1/SHA256SUMS.txt`. The ZIP contains one `cinematic-web-director/` directory with the skill, tutorial, references, templates, evaluation scenarios, scripts and tests. Packaging uses an explicit file list and reproducible archive metadata; Git metadata, secrets, caches and previous build output are excluded. Creating the archive does not publish a GitHub release or update an installed skill.

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

The [v0.3 design scenarios](evaluations/DESIGN_DIRECTION.md) add a complete portfolio rethink, constrained refresh, brand-constrained product redesign, optional effect recipe, approved-sprint correction and conflicting reference qualities. They have received a manual instruction walkthrough; independent execution and rendered trials are pending. Their criteria remain separate from the input given to an evaluated agent.

The [v0.4 motion cases](evaluations/MOTION_DIRECTION.md) add five scenarios with separate reviewer criteria. A partial desktop/mobile inspection of a client-provided public website grounded the change and two motion proposals. It does not establish that another agent follows the candidate instructions or that the proposed motion succeeds. Independent session execution and implemented candidate-motion trials remain pending.

v0.4.1 adds four device scenarios: short-laptop/phone motion, iPhone emoji-style arrows, incomplete device evidence and wide touch input. A client screenshot/browser report and fresh public-source inspection grounded the compatibility changes. They do not establish a reproduced or fixed iPhone issue. Independent scenario execution and real-device candidate-site checks remain pending; two preflight PNGs do not certify the agreed matrix.

An additional platform-scope scenario checks that the iPhone report does not displace Android and desktop coverage. It has received manual instruction review only.

Local installation and discovery in Codex were confirmed for v0.2.0, and the v0.3 candidate was installed locally. Those observations do not establish candidate behavioral quality or live portability in other hosts. Independent session evaluations and rendered candidate-site trials remain necessary to establish creative effectiveness. The optional external skill validator requires PyYAML; when it is unavailable, do not claim that validator passed. Frontmatter, local links and package consistency can still be inspected without installing dependencies.

References:

- https://agentskills.io/specification
- https://github.com/vercel-labs/skills
- https://github.com/greensock/gsap-skills
