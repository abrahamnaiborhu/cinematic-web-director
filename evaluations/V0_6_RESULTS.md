# v0.6 diagnostic observations — work in progress

Date: 2026-10-19. These are discovery observations from published v0.5.0, not evidence that a new expressive-motion instruction improves finished work. The [plan](V0_6_PLAN.md) separates proposal quality from observed animation. [Ponytail engineering](PONYTAIL_INTEGRATION.md) has its own source-review trial and does not establish a creative improvement.

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

## Supported next decision

The remaining gap is moving evidence: neither proposal shows whether the authored timing produces the intended character, or whether implementation turns a specific concept into generic movement. Preserve the successful discovery behavior. Observe a bounded moving/still comparison using the actual poster material before adding more creative instructions. Client reaction and a named refinement would give better evidence for a narrow skill change.

No expressive-direction instruction has been rewritten on the strength of these two sessions. A candidate comparison and held-out landing trial remain contingent on a supported change; they have not run. No live client website, public release, physical device or model-fallback behavior was evaluated here.

## Approved moving comparison

The client approved [poster-wall study revision 1](V0_6_STUDY_PLAN.md) on 2026-10-19. The coordinator built [A/B/still comparison](../studies/v0.6-poster-wall/index.html) with the supplied posters, factual descriptions, native browser animation and no dependencies. [Study notes](../studies/v0.6-poster-wall/README.md) record the two actual design refinements, failed acceptance attempts, API sources and exact evidence limits.

The initial interaction run passed, but capture review found incomplete initial visibility of the moving poster. Refinement 1 moved controls alongside the viewing context; a subsequent title-clipping regression led to refinement 2's title-based scroll anchor. The two-round boundary is reached. Final Chrome `155.0.8059.80` checks pass all 15 groups across 360×640, 390×844, 1024×600 and 1440×900 CSS viewports. Both the title and full moving poster are visible on selection; reduced motion, interruption, dispatched input, history, contact, enlarged root text and no-script behavior were exercised. Actual wall-clock transform samples are distinct from paused/seeked storyboard captures.

The handoff is local to the detail view rather than continuous shared-element travel from the collection. It tests two configured rhythmic treatments, not a complete site choreography. The coordinator inspected captures and temporal samples; no independent artistic judgment or client reaction is yet recorded. Source/evidence hashes are retained in `dist/evaluations/v0.6/poster-wall/evidence-manifest.json`. Technical passes establish neither eccentricity nor artistic success. Client adopt/revise/reject remains open; no new design rule or public creative-quality claim is justified yet.
