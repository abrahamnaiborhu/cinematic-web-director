# v0.6 diagnostic observations — work in progress

Baseline/study date: 2026-10-19. Contextual candidate and client feedback: 2026-10-20. The [plan](V0_6_PLAN.md) separates proposal quality from observed animation. These discovery observations do not establish improved finished work. [Ponytail engineering](PONYTAIL_INTEGRATION.md) has its own source-review trial and does not establish a creative improvement.

## Inputs and controls

Two fresh actors received the immutable published v0.5.0 package at commit `42fe52dabbee0bebc9e34757d1ef372a150de80f`, an isolated output directory and one synthetic raw request/material set:

- [Adventurous portfolio](fixtures/v0.6/adventurous-portfolio/request.txt): [brief](fixtures/v0.6/adventurous-portfolio/brief.md), inherited [HTML](fixtures/v0.6/adventurous-portfolio/index.html), original synthetic [After Hours](fixtures/v0.6/adventurous-portfolio/assets/after-hours.svg) and [Sideways](fixtures/v0.6/adventurous-portfolio/assets/sideways.svg) artwork. The brief asks for bold, playful, slightly abrasive character without supplying an animation solution.
- [Calm product](fixtures/v0.6/calm-product/request.txt): [brief](fixtures/v0.6/calm-product/brief.md), [workflow](fixtures/v0.6/calm-product/workflow.md) and inherited [HTML](fixtures/v0.6/calm-product/index.html). The client explicitly wants a calm, mostly static experience.

Neither actor received the evaluation plan, reviewer criteria, other actor outputs or candidate changes. Discussion only: no website/prototype coding, installations or publication. Each then received this exact case-specific follow-up:

Portfolio: “I’m leaning toward your recommendation. The concept interests me, but I still can’t picture how the movement would feel. Bring me what I need to judge its character before implementation, while keeping the work and contact easy to find. No prototype coding yet.”

Product: “I’m leaning toward your recommendation. Make Docs the main onward action and keep all four routes easy to find. Bring me the content and representative layouts I need to judge before implementation. Keep the experience calm and mostly static; no prototype coding.”

Configuration was inherited from the current host without a model override. Exact model/version and reasoning metadata were not independently exposed and remain unverified. These are small qualitative observations, not a fixed-model comparison or causal experiment. Snapshot/file hashes and actual outputs remain locally under `dist/evaluations/v0.6/`, in `baseline-snapshot/` and `baseline/{adventurous-portfolio,calm-product}/`.

## What the baseline actually did

| Case | Initial proposal | Follow-up material | Limits |
|---|---|---|---|
| Adventurous portfolio | Recommended an unruly poster wall tied to the studies' compression, interruption and offset. Selection brings a whole poster forward while its companion yields; an editorial sequence offered a materially different alternative. Phone/compact views and direct entry preserve access. | Draft copy, supplied artwork embeds and schematic frames compare “Shove and hold” with “Overshoot and correct.” The first uses a delayed companion response and firm 0.45–0.55 s settle; the second a slower tug, one correction and 0.7–0.9 s settle. Shorter phone travel retains onset/finish character. | Timing is a proposed viewing score, not observed motion. Text sketches and source inspection cannot establish the emotional effect, typography, actual fit or visitor response. |
| Calm product | Recommended a reading-first, mostly static page and replaced vague copy with the three confirmed capabilities. Did not impose an animated demonstration. | Revised Docs to the primary action, supplied exact draft content and phone/short-laptop/larger text wireframes, and kept all four routes visible. The conceptual sequence remains labeled and static. | No rendered composition, destination-page test, physical-device result or human usability evidence. Real documentation, pricing and demo sources remain missing. |

The coordinator read the actual responses and linked follow-up documents. The adventurous actor originated both spatial behavior and different rhythmic characters without the client supplying an effect. The calm control respected the client's static preference. These trials do **not** reproduce a general inability to propose eccentric ideas, and do not justify a universal effect quota or forced adventurous style.

## Diagnostic decision before the moving study

The remaining gap at that point was moving evidence: neither proposal showed whether the authored timing produced the intended character, or whether implementation would turn a specific concept into generic movement. The next decision was to preserve successful discovery behavior and observe a bounded moving/still comparison using the actual posters before adding more creative instructions.

No expressive-direction instruction was rewritten on the strength of those two sessions alone. At that stage a candidate comparison and held-out landing trial remained contingent on a supported change. No live client website, public release, physical device or model-fallback behavior was evaluated.

## Approved moving comparison

The client approved [poster-wall study revision 1](V0_6_STUDY_PLAN.md) on 2026-10-19. The coordinator built [A/B/still comparison](../studies/v0.6-poster-wall/index.html) with the supplied posters, factual descriptions, native browser animation and no dependencies. [Study notes](../studies/v0.6-poster-wall/README.md) record the two actual design refinements, failed acceptance attempts, API sources and exact evidence limits.

The initial interaction run passed, but capture review found incomplete initial visibility of the moving poster. Refinement 1 moved controls alongside the viewing context; a subsequent title-clipping regression led to refinement 2's title-based scroll anchor. The two-round boundary is reached. Final Chrome `155.0.8059.80` checks pass all 15 groups across 360×640, 390×844, 1024×600 and 1440×900 CSS viewports. Both the title and full moving poster are visible on selection; reduced motion, interruption, dispatched input, history, contact, enlarged root text and no-script behavior were exercised. Actual wall-clock transform samples are distinct from paused/seeked storyboard captures.

The handoff is local to the detail view rather than continuous shared-element travel from the collection. It tests two configured rhythmic treatments, not a complete site choreography. Source/evidence hashes are retained in `dist/evaluations/v0.6/poster-wall/evidence-manifest.json`; that historical manifest predates the client-decision documentation below. Technical passes establish neither eccentricity nor artistic success.

## Client reaction — 2026-10-20

The client said: “i like the correct (b) one. it's not that it's tame it' that for this specific situation that's alright but for other situation we need a different way to do the handoff”. Record **B preferred for this poster situation**. This is not approval of an entire portfolio design, a universal overshoot treatment or a requirement for greater intensity elsewhere.

This supports a narrow distinction in the motion reference: decide what relationship a connection expresses and select its mechanism before tuning rhythm. A/B in this study varies execution of one mechanism. Different content may call for a different connection, while a recurring relationship may justify repeating one. Two treatment/template fields record that reasoning and the scope of carried-forward client preferences. The discovery comparisons below inspect actual cross-context behavior; wording alone establishes no improvement.

## Contextual candidate — actual discovery observations

Three fresh actors used an isolated snapshot of the updated entrypoint, references, templates, offline checker and attribution (16 resources). The snapshot SHA-256 over sorted `(path, file SHA-256)` pairs is `6cceabbe316ae67c4239a43004e1cd085cdacdc16c9eede6385b606021ede4bf`. Raw materials and owned outputs were separated. Actors received no evaluation reports/criteria, prior conclusions or other trial outputs. They could read only the designated snapshot/materials/owned outputs, with read-only offline preflight permitted. No coding, rendering, generation, installs, nested agents or model overrides were authorized.

Portfolio and calm-product raw inputs and follow-ups were the same as the baseline cases above. The new [Night Window landing request](fixtures/v0.6/night-window/request.txt), [brief](fixtures/v0.6/night-window/brief.md) and [materials](fixtures/v0.6/night-window/materials.md) concern a fictional beginner sky-observation offer, not a portfolio. No animation solution appears in its initial input. Its follow-up introduced the earlier preference as client context, without directing reuse or rejection:

> We liked the overshoot-and-correct motion in another poster-site study. I’m leaning toward your recommendation here. Bring us the content and representative layouts we need to judge the direction and connections before implementation, keeping practical information and the request route easy to find. No prototype coding yet.

All three produced an initial response, continuation and review material. Requested configuration was inherited from the current host without an override; exact model/version/reasoning remains unverified. Raw requests/follow-ups match across the two baseline/candidate pairs, but orchestration prompts and tool choices are not established as byte-identical. The landing case has no baseline comparison. These are small qualitative observations, not a fixed-model experiment or proof of causal improvement.

| Case | Actual behavior | What this supports and leaves open |
|---|---|---|
| Adventurous portfolio | Follow-up compares keeping the same poster recognizable during travel with a deliberate cut into a still viewing room. Within the continuous mechanism it separately compares a firm push and comic correction. Reuses the mechanism for the other poster because its collection/detail relationship recurs. | Explicit distinction between connection and rhythm, plus reasoned recurrence. The earlier baseline already offered subject-specific concepts/rhythms; this is not evidence it lacked creativity. No moving candidate execution was observed. |
| Calm product | Keeps all reading static, makes Docs primary and offers ordinary navigation with immediate functional feedback. Provides source-grounded draft copy and phone/short-laptop/larger document sketches. | Respects the static control rather than adding variation for its own sake. Both baseline and candidate did so. Typography, fit, routes and visitor understanding remain untested. |
| New Night Window landing | Develops a shared conceptual field/framing direction. After hearing the prior overshoot preference, proposes one provisional correction of the viewing frame, distinguishes shared-field versus cut mechanisms, uses changing framing for the recurring attention relationship and a clean cut into practical information. Request/return remain ordinary navigation. | Selective interpretation instead of applying the poster trajectory everywhere. It explicitly says the earlier study was not inspected and warns that correction could suggest inaccurate pointing. Whether this interpretation feels appropriate requires actual motion and client judgment; one written transfer case is limited evidence. |

The coordinator inspected the actual initial responses and continuation boards, including the named mechanisms, rhythm comparisons, practical sections and evidence limits. Outputs and snapshot manifest remain at `dist/evaluations/v0.6/context-candidate/`; `followups.json` records the exact continuations. They are proposals/document sketches, not rendered layouts, approved new directions or human usability results. No new coded experiment is implied by their proposed next steps.

The source and extracted 51-file ZIP pass all 45 offline tests. All 99 local Markdown targets in the payload resolve; all 16 behavioral-snapshot resources match the package and the upstream MIT license is preserved. These verify resource/package integrity separately from the qualitative findings. The optional external Skill Creator validator remains unavailable due to missing PyYAML. The earlier browser study was not rerun because its HTML/CSS/JavaScript did not change; only its client-decision notes changed.
