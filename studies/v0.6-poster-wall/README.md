# Poster wall — bounded motion comparison

An isolated implementation of the client-approved [study plan revision 1](../../evaluations/V0_6_STUDY_PLAN.md), completed 2026-10-19. It uses fictional portfolio content and original synthetic artwork, not Abraham's live website. This is a study of a local poster handoff, not a finished portfolio or a v0.6 quality certification.

## Try the actual movement

Open [index.html](index.html) in a browser. Select either poster, choose **A · Shove**, **B · Correct** or **Still**, then use **Replay handoff**. Both variants end on the same readable artwork and factual description. Compare them on a phone-sized window and a short laptop window as well as a larger one.

- **A:** selected sheet takes the foreground, its companion yields after a short lag, then a firm settle. Configured selected-sheet duration: 510 ms.
- **B:** slower start, a sweep past the resting position and one correction. Configured selected-sheet duration: 840 ms.
- **Still:** immediate destination. Reduced-motion preference independently suppresses animation and disables replay, without changing the chosen radio option.

The complete posters are staged as whole images; their lettering is not independently animated. Phones use shorter travel. Direct entry opens settled detail; native scrolling, keyboard/touch, interruption and local history remain available. Study states use `#after-hours` and `#sideways`; they do not validate production route paths. Contact goes to an explicit fictional-study note. Functional arrow icons are inline SVG, not platform emoji.

This implementation uses a local stacked handoff at the detail view. It does not track a poster continuously from its former collection coordinates into detail. That limits what this study can establish about whole-site spatial continuity. Draft headline/type/layout are provisional framing, not an adopted design or a claim about the artist's commissioned work.

## Actual checks and refinements

Local Chrome **155.0.8059.80**, with CSS viewports **360×640, 390×844, 1024×600 and 1440×900**. The final run passed **15 check groups**: four viewport comparisons; direct entry; temporal samples; resize interruption; reduced motion at entry/during movement; dispatched touch and second selection; keyboard Tab/Enter/Space; return/history; contact during motion; 200% root-text reflow; no-script navigation/content; captured errors.

The harness compares actual transforms over wall-clock time and verifies settlement. Its separate storyboard PNGs pause/seek animations; those images are not timing measurements. The configured durations above are source settings, not measured precision claims. Root-text enlargement is not full browser zoom or assistive-technology testing.

| Stage | Actual observation and action |
|---|---|
| Static composition | Inspected actual collection/detail captures before implementing motion. Four static viewport checks passed. |
| Before behavior | The acceptance harness failed because the static links did not produce the enhanced detail/motion state. Preserved as `before-motion/`. |
| Initial motion | All 15 interaction groups passed, but capture review found that the controls/title left part of the moving poster below the shortest viewport. Passing checks had not established a usable comparison. |
| Refinement 1 | Moved comparison controls below the selected title and reduced surrounding text. Added a full-moving-poster visibility assertion. Four viewport comparisons and the interaction groups passed. |
| Refinement 2 | Capture review found title clipping from the scroll anchor. Added a title visibility regression (failed against refinement 1), then anchored from the actual title rectangle. Final captures retain both title and full moving poster. Functional icons were also made vector-based; the final run includes that source. |

Two design refinement rounds used; the approved boundary is reached. Initial failed preflight output routing was corrected to a workspace-relative output path before motion implementation. The actual eight-category prototype preflight had no blockers and reported `DEGRADED`; the offline checker does not detect the macOS Chrome application path or independently attest the model/creative approval. Approval comes from the recorded client reply, and browser capability from the actual run.

Evidence remains under `dist/evaluations/v0.6/poster-wall/`: `preflight.json`, `static/`, `before-motion/`, `initial-motion/`, `refinement-1/`, `title-regression/`, `refinement-2-before-vector-icons/`, and final `observations.json`/PNGs under `final/`. `evidence-manifest.json` hashes study sources, raw SVGs and retained observations/captures. The final source was inspected for navigation/state ownership, cancellation, stale-run completion and the no-script/reduced-motion alternatives.

Run with existing Node (native WebSocket/fetch support) and a local Chrome installation, without installing dependencies:

```bash
node studies/v0.6-poster-wall/check-browser.mjs dist/evaluations/v0.6/poster-wall/rerun
```

The default Chrome binary is the macOS application path. Override `CINEMATIC_CHROME_BINARY` for another installation. Each run uses an isolated temporary browser profile and deletes that owned profile afterward. Choose a fresh output directory to retain prior evidence. `--static` captures resting collection/direct-detail views without exercising the motion checks.

Relevant API sources consulted: [Element.animate](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate), [Animation.cancel](https://developer.mozilla.org/en-US/docs/Web/API/Animation/cancel), [hashchange](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event). Existing host configuration was inherited without a model override; exact model/version/reasoning remains unverified. No new dependency, model handoff, public release or live-site change occurred.

## Client decision and scope

On 2026-10-20 the client preferred **B · Correct** for this particular situation, explaining that other situations need a different handoff. This establishes an actual contextual preference, not a universal overshoot recipe, approval of the whole portfolio design or a mandate to intensify every movement. The comparison retains both variants and stillness for inspection.

The coordinator's inspected captures and temporal samples establish different trajectories and settlement. The client's reaction supports B here; no human newcomer task or broader audience response is inferred. The resulting skill change distinguishes selecting a connection mechanism from tuning its rhythm, and scopes reuse to the relationship it serves. Cross-context discovery still needs its own observation.

Viewport/touch checks are Chrome emulation. No physical Android/iPhone, Safari, Firefox, Edge, assistive-technology, production-network or field-performance result is claimed. Subsequent contextual discovery comparisons, including a new landing brief, are recorded in the [v0.6 result report](../../evaluations/V0_6_RESULTS.md); they do not establish broader rendered quality or compatibility.
