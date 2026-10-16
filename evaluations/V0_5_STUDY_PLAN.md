# Moss Studio — bounded motion study, revision 1

Status: client approved revision 1 on 2026-10-16: “Approve the bounded study.” This authorizes the stated experiment, not adoption of the design or production work. This is a synthetic evaluation fixture, not a real workshop or a production website.

## Question and scope

Does a short, gentle settling movement of the supplied illustrated vessel make the opening feel welcoming while leaving workshop information and booking immediately usable? Compare the moving opening with its settled, still composition. The director's baseline landing trial originated this proposal; the client did not supply an effect.

Use only the fixture's known facts: beginner hand-building, two hours, materials included, six places and 45 fictional currency units. Label the illustration as an illustration; dates/location/accessibility information remain unknown. The booking control must expose its placeholder status without inventing availability.

Start: text and controls available, complete vessel near its resting position. Change: a small downward movement with restrained shadow adjustment. Settled: complete illustration remains still. No repeated ambient loop or waiting for content. Reduced motion and unavailable JavaScript show the settled state immediately. Provide a still/moving comparison and stop/replay controls for review; these are study controls, not a production design decision.

## Implementation and boundaries

- Files: isolated `studies/v0.5-moss/` HTML, CSS, JavaScript, fixture SVG and study notes; captures/observations under ignored `dist/evaluations/v0.5/study/`.
- Dependencies: browser-native CSS/SVG/JavaScript, no installs or framework migration. GSAP is not needed for this question.
- Configuration: current inherited host configuration, no model override. Exact model/reasoning metadata remains unverified unless exposed by the host.
- Boundary: one implemented opening and up to two refinement rounds addressing observed defects; no full site, production integration, live booking, deployment or publication.
- Decision: adopt, revise or reject the motion after comparing it with stillness. Approval to run the study does not approve a final design.

## Evidence and acceptance

Capture actual rendering at 360×640, 390×844, 1280×720 and 1440×900 CSS viewports. Observe movement at start/intermediate/settled states; check text/action access during motion, stop/replay, resize/interruption, keyboard focus, touch emulation, reduced motion, no-script fallback and console errors. Record loading and rendering observations without claiming production performance from a local fixture.

The information must remain readable and reachable throughout; no horizontal overflow or clipped action; controls must work with keyboard and touch; reduced motion and no-script state must be complete. A synthetic independent reviewer may assess visitor understanding from supplied captures and the actual artifact, with its limitations explicit. Real visitor response remains a separate validation step.

Available initial runtime is local Chrome with viewport/input emulation. It is not iPhone, Android, Safari, Firefox or physical-device evidence. Record those platform checks as pending rather than treating the four sizes as cross-platform certification. Artistic welcome/weight remains a client judgment; automated checks cannot establish it.
