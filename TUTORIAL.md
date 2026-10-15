# Cinematic Web Director — Getting Started (v0.3.0 candidate)

This guide is for people who can develop websites but want help with storytelling, visual direction and motion. You can start a landing page, portfolio or product website, or improve an existing one. You do not need to arrive with a storyboard, animation vocabulary or a chosen GSAP plugin.

## 1. Install the skill

You need a compatible coding agent that can read Agent Skills. The optional installer uses Node.js/npm. The Python preflight and package tools use Python 3.10+ and its standard library.

### Install from GitHub

Run from your website project's folder for a project-scoped installation. Choose the command for your agent:

```bash
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent codex
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent claude-code
npx skills add https://github.com/abrahamnaiborhu/cinematic-web-director --agent cursor
```

Run one command, not all three unless you use all three agents. The GitHub source follows the repository's current default branch. To reuse the skill across projects, or start planning before a website folder exists, add `--global` to the chosen command.

### Install the exact ZIP release

For this unpublished candidate, build the ZIP from this repository revision:

```bash
python3 -B scripts/package_release.py --version 0.3.0 --out dist/v0.3.0
```

Use `cinematic-web-director-v0.3.0.zip` and `SHA256SUMS.txt` from that output directory. For a published version, download its matching ZIP and checksum from [GitHub releases](https://github.com/abrahamnaiborhu/cinematic-web-director/releases); v0.2.0 is the latest published release when this candidate is prepared. Substitute that version in the examples below. Save the archive and its matching checksum in the same folder, then run verification from that folder.

Check the archive's checksum. On macOS:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

On Linux:

```bash
sha256sum -c SHA256SUMS.txt
```

On Windows PowerShell, compare this result with the hash in `SHA256SUMS.txt`:

```powershell
Get-FileHash .\cinematic-web-director-v0.3.0.zip -Algorithm SHA256
```

Extract into a new folder so different releases stay separate:

```bash
unzip cinematic-web-director-v0.3.0.zip -d cinematic-web-director-v0.3.0
```

The extracted package is inside `cinematic-web-director-v0.3.0/cinematic-web-director/`. From your website project, install that local source (replace the example path):

```bash
npx skills add "/absolute/path/to/cinematic-web-director-v0.3.0/cinematic-web-director" --agent codex
```

Choose `claude-code` or `cursor` instead if appropriate. Add `--global` for a user-wide installation. You may also copy the complete inner package directory to your agent's configured skill location. Keep its references, templates and scripts together.

Confirm in your agent that it can discover and read `cinematic-web-director/SKILL.md`; reopen the session if needed. An installation command succeeding does not prove that a particular session has loaded the skill.

## 2. Begin with what you want to build or improve

Ask the agent to use Cinematic Web Director. For a new site:

> Use Cinematic Web Director to help me create a website for my work. I know development but am new to motion design. Help me clarify the structure and creative direction, ask one focused question at a time, and explain your recommendations before production.

For an existing site:

> Use Cinematic Web Director to redesign this website. Inspect its source and the materials in this project. Assess its story, copy, structure and visual presentation, then explore a direction with me before implementing it.

State how much reinvention you want when you know it. For example:

> I want a complete creative rethink of this portfolio. Use the real work and preserve contact and case-study links, but reconsider the existing layout, colors, typography and section order. Develop the story and show different ways to present it before production.

For a limited refresh, name what should stay. The director should use your stated intent rather than repeatedly asking you to choose a redesign category. Existing presentation can remain when it serves the assignment; it is not automatically a requirement because it already exists.

If your request is still vague, the director starts with “What would you like to build or improve?” If you already answered, it should ask the next useful question instead of restarting.

The director reviews technical readiness without making missing implementation dependencies a barrier to creative discovery. It should never claim to have viewed a website, read a file or confirmed a tool that it cannot access.

## 3. Supply existing materials and references

Keep useful files wherever they already live in your project. The director should inspect relevant materials before asking you for more. If you want a convenient collection point, use an optional `creative/references/` folder.

Useful materials include current site source, project descriptions, actual product information, brand assets, screenshots and links to websites or videos you admire. A Markdown file can hold links and short notes explaining what you like.

For example:

> I like the way this reference keeps one object visible through several transitions. Its colors and layout are not requirements. The PDF contains current product facts; the old homepage has outdated claims.

This helps distinguish confirmed information, mandatory constraints and inspiration. The agent should clarify conflicts and draft copy from confirmed facts. It should not invent projects, achievements or product capabilities.

## 4. Develop and approve the direction

Spend time understanding the choices. Ask for alternatives, annotated compositions or representative storyboard states when a verbal description is unclear. You can reject, combine or revisit ideas.

The director should help establish three checkpoints:

1. **Brief and structure:** purpose, visitors, content, pages and important journeys.
2. **Creative direction:** the selected concept, representative compositions, visual language and continuity.
3. **Upcoming production batch:** detailed treatments, architecture changes, model responsibilities, acceptance criteria and sprint scope.

A landing page can use a focused sequence. A portfolio can use independent case studies and exploratory browsing. A product website can offer several routes. A dramatic climax, a single CTA and scroll-driven scenes are optional.

Ask what visitors should understand and which actual work or evidence supports it. During exploration, the director should show alternatives that differ in content framing, composition or browsing behavior, rather than changing only palette and fonts. Fixed constraints stay explicit; provisional structure can evolve with the direction.

Review representative compositions using real content, including substantive work and smaller-screen views where relevant. Text descriptions explain a proposal but do not prove its visual quality. If a coded study is needed to judge composition, agree on a bounded prototype before it is built. You can approve or reject the composition separately from unresolved motion details.

A central metaphor and a signature interaction can be helpful; neither is required. Huge type, small body text, pinning, text reveals and marquees are not a recipe for every project. Ask how each prominent choice helps people understand or use this particular website. The [design-direction reference](references/DESIGN_DIRECTION.md) explains the process.

The director maintains approved versions using the [project script](templates/PROJECT_SCRIPT.md), [continuity bible](templates/CONTINUITY_BIBLE.md), [treatment](templates/SCENE_TREATMENT.md) and [iteration log](templates/ITERATION_LOG.md), or equivalent documents you already use. You do not need to fill out all templates before the conversation begins.

## 5. Approve a small motion experiment when needed

Motion can be difficult to judge from still frames. Before coding a prototype, agree on the question, scope, model configuration, evidence and stopping boundary. For example:

> I approve the proposed experiment for the gallery-to-case-study transition. Test whether the project image remains easy to follow on desktop and mobile. Use the agreed model configuration and existing dependencies. Limit it to this transition and two refinement passes; bring back observations before expanding the work.

The agent should show the result, explain what it observed and recommend adopting, revising or rejecting the approach. Your approval of an experiment applies to that experiment. Production still needs an approved plan.

## 6. Agree on architecture and model handoffs

Review technical choices alongside the experience. Existing frameworks and libraries can be reused, extended or migrated when justified. Each proposal should explain the requirement, alternatives, effects on functionality/deployment and validation. No particular state library, backend or visual effect is mandatory.

Agree on model configurations and allowed responsibilities. A configuration includes the provider, exact model and reasoning setting where available. Complex creative or implementation work needs a suitable model; bounded approved work may use a less expensive configuration.

Before a handoff, expect a notice naming the configuration, reason, task, approved inputs, checks and conditions for returning to review. A pre-approved configuration can be reused within its scope without asking permission again. A new fallback or expanded scope needs the relevant agreement.

A skill cannot force model changes without host support or detect every hidden provider fallback. The agent must label unavailable identity information as unverified. It should report a proposed switch separately from one confirmed by the host.

## 7. Approve a sprint batch and let the agent execute

A sprint should deliver a coherent visitor experience or a justified technical increment. Review the outcomes, scope, inputs, dependencies, acceptance criteria and permitted refinements. Then approve the identified plan/version, for example:

> I approve plan v3, sprints 1–3, with the listed treatments and model configurations. Continue through those sprints, including in-scope fixes and refinements. Report each outcome. Return for a decision if the creative intent, scope or authorized configuration needs to change.

The agent can continue through that approved plan without stopping at every boundary. It still verifies actual behavior, critiques the result and records decisions. Later unspecified batches require sufficiently detailed treatment and authorization.

Iteration should address a named weakness or expected improvement. If repeated attempts provide no benefit, the agent should explain the evidence and propose a different approach instead of refining indefinitely.

## 8. Give useful feedback and resume later

Plain-language feedback is enough:

> The movement is attractive, but I lose track of the product when the headline changes. Please explain what causes that and propose a correction within the approved direction.

The director should connect your observation to intent, describe a specific change and explain how it will judge improvement. Revisions that change approved intent identify affected decisions and obtain the necessary agreement.

To resume in a later session or another supported agent:

> Read the approved project script, continuity bible, current treatments and iteration log. Summarize the current state and next authorized sprint before continuing. Identify missing context rather than guessing.

When you add new materials, tell the agent where they are. It should review their effect on relevant decisions before major approvals and sprint starts, while preserving unaffected work.

## 9. Understand preflight and validation

The director normally runs preflight for you. From the installed skill's directory, you can run it directly:

```bash
python3 -B scripts/preflight.py --project /path/to/website --agent codex --phase discovery
```

All eight checks are reviewed. `DEGRADED` can simply mean that declarations or runtime observations cannot be independently verified by the local script. `8/8 reviewed` does not mean eight successful installations. Creative approval remains a separate gate.

Use [the preflight protocol](references/PREFLIGHT_PROTOCOL.md) for prototype/implementation phases, unusual source paths, official GSAP resources, scoped runtime observations and release evidence. Required GSAP topics follow the treatment. A batch without GSAP work can declare `--gsap not-required`.

Before releasing your website, the agent should observe its actual layouts, motion, navigation, relevant input modes and reduced-motion behavior. Screenshots support visual assessment but cannot establish timing or interaction correctness by themselves.

## Troubleshooting

| Situation | Next step |
|---|---|
| Skill not visible | Confirm the installation scope and agent; ask whether the session can read the actual SKILL.md |
| Missing GSAP or browser tools during discovery | Continue creative planning with those requirements deferred |
| Multiple applications or an unusual layout | Identify the actual application with `--source-root` and an existing brief with `--script` |
| Reference cannot be opened | Ask for an accessible project copy or useful description; keep the assessment's limits explicit |
| Agent starts building too soon | Point it to the missing checkpoint or unapproved experiment/sprint scope |
| Agent reports a model switch without evidence | Ask for host confirmation or an explicit unverified identity record |
| Story or design still feels weak | Ask for evidence, visitor impact, alternatives and a recommended correction |
| Redesign repeats the old layout | Ask which inherited presentation choices are required, which are proposed, and how each serves the new story |
| Alternatives look like the same template | Compare content framing, composition and visitor behavior, using representative real content |
| Agent adds effects from a style recipe | Ask for each effect's purpose and compare a calmer alternative before expanding the treatment |

## What this release establishes

v0.3.0 is an unpublished development candidate focused on design judgment. Automated tests validate the local checker and release packaging; the [design scenarios](evaluations/DESIGN_DIRECTION.md) support behavioral evaluation. Manual walkthroughs are not independent agent executions or rendered website trials. v0.2.0 was installed and discovered in Codex, but independent v0.3 session evaluations and rendered redesign trials remain pending. The skill offers a structured creative process and makes no promise of awards.
