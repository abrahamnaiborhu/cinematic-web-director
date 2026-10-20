# Cinematic Web Director — Getting Started (v0.6.0 candidate)

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

v0.6.0 is an unpublished candidate. Build its ZIP from this repository revision:

```bash
python3 -B scripts/package_release.py --version 0.6.0 --out dist/v0.6.0
```

Use `cinematic-web-director-v0.6.0.zip` and `SHA256SUMS.txt` in `dist/v0.6.0/`. For a published package, download the matching files from [GitHub releases](https://github.com/abrahamnaiborhu/cinematic-web-director/releases), including [v0.5.0](https://github.com/abrahamnaiborhu/cinematic-web-director/releases/tag/v0.5.0), and substitute its version below. Save the skill ZIP and its checksum in the same folder; optional evidence bundles are not needed for installation.

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
Get-FileHash .\cinematic-web-director-v0.6.0.zip -Algorithm SHA256
```

Extract into a new folder so different releases stay separate:

```bash
unzip cinematic-web-director-v0.6.0.zip -d cinematic-web-director-v0.6.0
```

The extracted package is inside `cinematic-web-director-v0.6.0/cinematic-web-director/`. From your website project, install that local source (replace the example path):

```bash
npx skills add "/absolute/path/to/cinematic-web-director-v0.6.0/cinematic-web-director" --agent codex
```

Choose `claude-code` or `cursor` instead if appropriate. Add `--global` for a user-wide installation. You may also copy the complete inner package directory to your agent's configured skill location. Keep its references, templates and scripts together.

Confirm in your agent that it can discover and read `cinematic-web-director/SKILL.md`; reopen the session if needed. An installation command succeeding does not prove that a particular session has loaded the skill.

## 2. Begin with what you want to build or improve

Ask the agent to use Cinematic Web Director. In Codex, you can explicitly invoke it with `$cinematic-web-director`, followed by your request. Use it inside the website project you want to create or redesign.

For a new site:

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

### Expect the director to bring motion ideas

You do not need to arrive with animation ideas or references. Once the subject and some content are understood, the director should initiate a motion discussion: offer concrete possibilities, explain what viewers see first, what changes and where attention lands, recommend an approach, and ask which experience feels closer to your intent. It should discuss motion while composition is still open, rather than waiting to decorate a finished static site.

For example, a portfolio about connecting applications and their supporting systems could explore visual continuity between those responsibilities, or a quieter editorial approach. These are possible interpretations, not required diagrams or effects. Atmosphere, character and rhythm are legitimate purposes alongside explanation and feedback.

If you supply an idea, the director should acknowledge it, develop it critically and bring useful alternatives or connections. Repeating your existing animation as a new proposal is insufficient. You remain free to prefer a calm or static site. Proposals do not authorize implementation; explicitly bounded motion studies and approved sprint plans still govern coding. See [motion direction](references/MOTION_DIRECTION.md).

### Agree on the device experience

For a new or substantial public-site design, the director should consider phones and compact laptop windows from the beginning, then develop larger-screen enhancements. Important motion needs an intentional treatment at the supported sizes; it need not use the same pinning or choreography everywhere. A static phone fallback is a choice to discuss, not automatic completion.

Ask to see the same moment in a narrow phone, a short laptop window and a larger composition. Available height matters as well as width. Touch input, keyboard access and reduced-motion preference are separate considerations. The director should propose a practical browser/device coverage matrix and record what was actually checked. Resizing desktop Chrome does not establish how iPhone Safari renders or how Android hardware performs.

That matrix should consider Android and iOS/iPadOS, plus Windows, macOS and Linux where relevant to the audience. Browser examples include Chrome, Safari, Firefox, Edge and Samsung Internet on their relevant platforms. Agree on representative supported versions rather than assuming every combination is covered. A bug reported on iPhone does not turn the project into an iPhone-only design; shared fixes should receive appropriate checks across the supported scope.

If UI arrows become colorful emoji, inspect the actual characters and use the existing vector icon system or a reusable SVG icon when consistent geometry/color is intended. Preserve meaningful link labels and intentional content emoji. The [device-experience reference](references/DEVICE_EXPERIENCE.md) includes a small decorative-arrow example and evidence guidance. A skill update does not itself patch a separate live website.

The director maintains approved versions using the [project script](templates/PROJECT_SCRIPT.md), [continuity bible](templates/CONTINUITY_BIBLE.md), [treatment](templates/SCENE_TREATMENT.md) and [iteration log](templates/ITERATION_LOG.md), or equivalent documents you already use. You do not need to fill out all templates before the conversation begins.

### Review a concrete package

Expect a concise recommendation, a clear decision and links to the actual material. The [review package](templates/REVIEW_PACKAGE.md) can combine content, compositions, storyboard states and asset decisions without making you assemble the answer from multiple technical documents. Early document sketches are useful; they do not establish rendered visual quality or motion feel. Review meaningful content beyond the opening and its phone/compact-laptop treatment.

The director should explain which images support the story, how they will be treated and what specifically is missing. A conceptual diagram is not a real product screenshot, and an illustration is not a workshop photograph. Missing assets need a next action and an explanation of which decision they block.

Define a few visitor tasks before judging the result, then record what an actual newcomer understands or does without supplying the answers. Label an AI-only review as synthetic. For implemented work, ask for expected versus observed behavior during loading, movement, interruption, resize/input and reduced motion where relevant. Proposed checks and actual results belong in separate columns. See [creative review](references/CREATIVE_REVIEW.md).

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

During approved implementation and engineering review, the director applies [Ponytail engineering](references/PONYTAIL_ENGINEERING.md): inspect the connected code, reuse adequate components/platform features, keep changes readable and verify the actual risks. Your approved choreography, visual direction, device behavior and accessibility remain part of the task. A shorter implementation does not justify replacing them with something simpler. This adaptation is included in the skill; it requires no separate Ponytail plugin, hook or session-wide mode.

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
| Agent waits for you to invent every animation | Point to motion direction: it should bring content-specific alternatives, a recommendation and an informed experiential question |
| Agent repeats a handoff you liked in another context | Ask which relationship it expresses here; compare different connection mechanisms before tuning timing, while retaining useful coherence |
| Motion only works on a large screen | Review width and height gates; ask for an authored phone/compact-laptop treatment and the relevant runtime evidence |
| Link arrows render as emoji | Confirm the reported OS/browser and actual glyphs; reuse deliberate vector icons and verify in those environments |

## What this release establishes

v0.6.0 is a development candidate adding phase-scoped engineering discipline. Its expressive-direction work is in progress. The earlier [v0.5 result report](evaluations/V0_5_RESULTS.md) records six discovery trials and an approved rendered study, with their limits; [open that study](studies/v0.5-moss/index.html) to compare replay with stillness. Automated checks validate the local checker and archive. Neither those checks nor Ponytail's upstream benchmark claims establish improved art direction, human usability, cross-host portability or physical-device compatibility here. The skill offers a creative process and makes no promise of awards.
