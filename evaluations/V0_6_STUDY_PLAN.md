# v0.6 poster-wall study — proposal revision 1

Status: **revision 1 approved by the client, 2026-10-19** (reply: “Approve the bounded study”). This is the next experiment following the [diagnostic observations](V0_6_RESULTS.md), not approval of a portfolio redesign or the v0.6 release.

Outcome: the [comparison](../studies/v0.6-poster-wall/index.html) is implemented, with both permitted refinement rounds used and 15 passing local Chrome check groups. [Study notes](../studies/v0.6-poster-wall/README.md) distinguish actual observations from artistic/device limits. Client design adoption remains pending.

## Decision and source material

Does the baseline director's proposed poster handoff have a recognizable character when it actually moves, and does that character survive on a phone and a short laptop? Compare the same composition/content with two motion treatments and a still alternative. Either treatment can be rejected as bland, distracting or inappropriate.

Use fictional Dara Ishan's [brief](fixtures/v0.6/adventurous-portfolio/brief.md), [After Hours artwork](fixtures/v0.6/adventurous-portfolio/assets/after-hours.svg) and [Sideways artwork](fixtures/v0.6/adventurous-portfolio/assets/sideways.svg). Preserve the complete posters and factual labels/contribution. The existing contact address is a placeholder; the study contact action must reach a clearly labeled local note. No clients, awards, process footage or production claims may be invented.

The treatments originate in the actual v0.5 discovery output, retained at `dist/evaluations/v0.6/baseline/adventurous-portfolio/motion-review-02.md`. The study tests those proposals; the coordinator's implementation and refinements would not constitute independent end-to-end agent delivery or proof that Ponytail improves art direction.

## Smallest experience

One work collection and two inspectable detail states, with stable name/navigation/contact and complete artwork from the first usable state. Offset composition creates tension without covering essential artwork lettering. Selecting a poster gives it precedence, its companion yields, and the selected work settles beside its factual description. Stillness follows; there is no introductory wait or idle loop.

| Treatment | Observable character to attempt | Initial viewing score, adjustable within this study |
|---|---|---|
| A — Shove and hold, director's recommendation | Selected sheet leads; companion yields with a brief lag. Decisive early travel and one firm settle. Intended feeling: “Excuse me, this one.” | Approximately 0.45–0.55 s. No repeated wobble. |
| B — Overshoot and correct | Slower tug, longer sweep, one small pass beyond the resting position and one correction. Intended feeling: “Almost—there.” | Approximately 0.7–0.9 s. No repeated springing. |
| Still | Immediate readable destination with the same artwork, content and onward actions | Also the reduced-motion treatment; no forced replay when that preference is active. |

Provide ordinary labeled controls for A, B, stillness and replay. Keep the chosen variant separate from the reduced-motion preference. The complete artwork is staged as a whole; do not animate its lettering as a fabricated account of the artist's process. Direct entry opens settled detail. Latest selection wins during interruption; return/history restores useful orientation. Local fragment URLs may represent the study states; this does not validate production `/work/after-hours` or `/work/sideways` routing.

On phones, use normal vertical browsing and a short local lateral handoff at the selected detail, retaining each variant's onset/finish character. Do not fly an offscreen poster across a long page. Compact laptops use shorter travel and a readable image/copy spread that can flow vertically. Larger screens may widen the spatial relationship. Touch and keyboard expose the same actions; reduced motion remains independent of width/input. With script unavailable, the complete work and navigation remain readable.

## Permitted implementation and configuration

- New study files only under `studies/v0.6-poster-wall/`: HTML, CSS, JavaScript, README and a bounded browser-check harness. Read the supplied fixture SVGs; copy them into the study only if needed for portability. Store evidence under `dist/evaluations/v0.6/poster-wall/`. Do not edit the v0.5 study or raw fixtures.
- Plain HTML/CSS/SVG/JavaScript with browser-native animation and local/system fonts. No dependency installation, generated assets, audio, framework migration, backend, real contact delivery, deployment, publication or live-site changes.
- Coordinator implementation using the current inherited host configuration, with no requested model/reasoning switch. Exact model/version/effort remains unverified unless exposed. New configuration or observable fallback outside this agreement needs the existing handoff process.
- Use the current candidate's approved-scope workflow and Ponytail engineering guidance. The expressive design instructions remain those tested in v0.5. Run scoped prototype preflight; GSAP is not required by this experiment.
- Inspect the resting compositions before detailed choreography. Adjust typography, spacing, layering, travel, delay and easing within the stated character/content boundaries. A change of concept, new dependency or broader site build is outside this approval.

## Evidence and stopping boundary

Use available local Chrome at **360×640, 390×844, 1024×600 and 1440×900 CSS pixels**, recording its actual version. Phone dimensions/touch dispatch are emulation, not Android or iPhone evidence. No Safari, Firefox, Edge, physical-device, assistive-technology or field-performance result is inferred from this run.

Record actual wall-clock movement and settlement separately from staged frames. Inspect still/start/change/settled captures, plus keyboard/touch activation, rapid reselection, return/history, resize during movement, reduced motion at entry and changed during movement, no-script content and reachable contact/navigation. Note console errors and failed attempts. Check enlarged text/reflow on the narrow/short layout. Technical passes and still screenshots cannot establish motion quality.

Build one initial comparison, then allow **at most two design refinement rounds**, each tied to a named observed weakness. In-scope functional fixes are permitted; unresolved blockers or inconclusive motion at that boundary are reported rather than extending the study. Record source/evidence hashes and the actual conditions. No broad production or public-release acceptance is implied.

Show the client A, B and stillness with these viewing prompts: Which feels more deliberate, amusing, bland or distracting? Does the interruption strengthen the poster, or draw attention away from it? Does the phone retain the character? Capture the client's actual reaction before recommending adopt/revise/reject. If neither succeeds, record that outcome and use it to propose the next narrow instruction or craft change.

Approval record: **revision 1 approved, 2026-10-19**, with the inherited configuration, four viewport cases and at most two refinement rounds described above. Approval permits this experiment and its bounded refinements, not adoption of a final design.
