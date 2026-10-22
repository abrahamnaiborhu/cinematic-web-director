# Plan the whole website experience

Use during new-site or substantial redesign direction, before detailed choreography and sprint approval. For targeted work, inspect only the affected journey and preserve existing agreements. The director proposes how the parts cooperate; do not wait for the client to discover loading, navigation or performance requirements. Explain consequences through the visitor's experience and ask about consequential tradeoffs.

## Connect the creative direction to runtime behavior

Maintain a concise experience plan in the project script or equivalent existing document. Cover relevant paths from arrival through use, departure and return. Link detailed scene treatments rather than duplicating them. A simple static landing page may need only a paragraph; do not impose a state library, diagram, loader or new document on every site.

For each important journey identify:

- Entry: first visit, cached return, direct route/hash and restored scroll position. State what is readable/actionable immediately and which introduction, if any, repeats.
- Readiness: the resources/layout/initialization needed for the next interaction, what can arrive later and how waiting or failure is communicated.
- Control: scroll, touch, keyboard and navigation during entry, transitions and settling. Decide interruption, skip, rapid/repeated input and ownership when two interactions overlap.
- Departure/return: route changes, Back/Forward, resize/orientation and hidden-tab/resume behavior where relevant. Identify who owns state, starts/stops work and removes listeners, observers, timelines and graphics resources.
- Recovery: slow or failed assets/data/scripts and unsupported graphics. Preserve essential information/actions with an appropriate fallback, retry or exit; distinguish proposed behavior from verified behavior.

Use these relationships to assess an effect's total cost and dependencies. Several well-designed scenes can still produce a broken journey. Keep the approved expressive intent while solving integration problems; discuss material tradeoffs rather than silently replacing important motion with stillness.

## Loading is a readiness decision

Distinguish resource loading, initialization and an authored introduction. A loader can communicate real waiting but cannot make an unsafe initialization or scroll layout correct. Do not invent progress percentages or delay usable content simply to finish a decorative counter. An intentional timed introduction is a creative choice to disclose and approve, not a claim that resources are still loading.

Define what must be ready for the specific opening: for example an essential decoded image, required typography or a usable fallback, layout dimensions and initialized controls/scroll ranges. Do not wait for every offscreen image, video or optional scene. `DOMContentLoaded` does not wait for images; neither that event nor a universal fixed delay proves the interaction is ready. See [MDN event semantics](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event).

If a temporary interaction/scroll lock is justified, name its owner, unlock condition and bounded recovery deadline. Release it on success, timeout, failure, skip and navigation/teardown as applicable, with usable content or an actionable recovery state. Preserve keyboard/focus access and restored scroll behavior. If a critical resource fails, do not keep visitors trapped behind a loader or expose a half-initialized effect. Prefer local placeholders/fallbacks when the rest of the page can already work.

Plan cold/slow loading separately from cached returns and direct entry. Reserve space for late assets, and remeasure relevant geometry after consequential changes without duplicating animation instances. Decide what happens if someone starts scrolling before initialization completes.

## Make resource cost part of art direction

Turn "lightweight" into proportionate, measurable criteria before approving expensive treatments. Propose project-specific budgets for initial transferred assets/scripts, meaningful content availability and important interaction responsiveness; include graphics/memory or concurrent-work limits when material. Record the value/unit, test device/browser/network/cache conditions, measurement method and response to exceeding the limit. Distinguish proposed targets, measured baseline and actual results. No universal byte count, FPS promise or desktop score certifies all devices. [Performance budgets](https://web.dev/articles/performance-budgets-101) help guide creative and technical choices.

Explain which resources are essential now and which can be deferred; avoid lazily withholding the opening's essential content. Account for image/video/fonts, decoding, script execution, drawing and repeated navigation, not just library bundle size. Reuse adequate platform/project capabilities; justify heavier dependencies by the approved experience and measured cost.

For expensive continuous work, define when it runs, pauses or releases resources: offscreen, hidden tab, route departure and resume. [Page visibility](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) supplies a relevant signal, not a complete lifecycle policy. Plan deliberate lower-cost treatments and reduced-motion access separately. A small viewport is not evidence of weak hardware; emulated throttling is not physical-device evidence.

## Validate a connected slice early

Include an early integrated journey in the approved production plan: arrival/readiness, opening, interaction/scroll, onward navigation and return as applicable. Add a representative slow/failing resource case where resources are consequential. A minimal one-page site may use direct hash entry and return instead of inventing routes. Continue approved sprints without repeated approval; this guidance does not itself authorize a coded prototype or expand existing scope.

Before calling the slice complete, exercise the connected path and relevant interruptions against the plan. Record build, environment, input, cache/network conditions, expected/actual behavior and evidence. Check that loading/locks settle, content/actions remain accessible, returns do not duplicate work and budgets are observed under agreed conditions. Screenshots cannot establish timing, cleanup or resource cost. Label untested cases and tool/device limitations explicitly; do not turn this planning document or an offline preflight pass into runtime proof.
