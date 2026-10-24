# v0.8.0 motion companion and interpretation checks

Development pre-release, published 2026-10-24. Client approved building the proposed motion companion and conversational validation; no client website or public release is part of this work. This skill-maintenance study uses original fictional vector artwork, platform animation APIs, one collection-to-project journey, three treatments and stillness. It has no external dependencies, media or data services.

## Scope and criteria

Compare persistent-object recognition, collection-to-context reorganization and an intentional immediate cut. They express different relationships; timing/easing variants alone would not satisfy the scope. Keep one treatment visibly adventurous without turning its choreography into a universal recipe. Provide explicit playback, pause/resume, finish, return, stillness/reduced motion, history/direct entry, interruption and phone/compact-laptop adaptations. Keep useful static cases without JavaScript. Record real runtime observations separately from plans, screenshots, client preference and physical-device evidence.

The interpretation workflow connects what was heard, a recommendation, the visitor experience and remaining uncertainty to actual client material. A demo preference or direction approval does not authorize an unspecified client prototype. Conversational evaluation must use a continuing dialogue, not merely a one-shot request for recommendations.

## Runtime checks

The dependency-free [browser harness](../studies/v0.8-motion-companion/check-browser.mjs) passed **19 check groups** in isolated headless Chrome 156, using local files and a temporary profile. Five CSS viewport sizes were checked: 320×640, 360×640, 390×844, 1024×600 and 1440×900. At each size A and B moved and settled, C cut immediately with no running animation, explicit playback framed the viewer, no page-level horizontal overflow appeared and each settled display title wrapped only between words.

Observed beyond the viewport loop: pause holds geometry, resume and finish leave no animation or overlay; rapid replay, treatment changes and interrupted returns clear in-flight work; a mid-opening resize settles into the phone composition; disabling movement settles immediately and re-enabling does not autoplay; initial and live reduced-motion preferences select stillness; case hashes, Back and Forward load settled content without an invented arrival; skip link, Enter activation and focus return; Chrome touch input; hidden-tab pause without autoplay on return; 200% root text without horizontal overflow; literal reaction notes; native controls in the accessibility tree; readable still cases without JavaScript; no HTTP(S) requests, console warnings or errors.

Earlier runs exposed three problems, each corrected and rechecked:

- **Focus loss on return (page defect).** "Back to collection" focused the opened work, then `history.back()` returned to the non-focusable `#comparison` fragment and Chrome moved focus to the body. Keyboard visitors lost their place. Focus is now restored after the resulting `hashchange`. With that fix removed, the corrected harness fails the keyboard return check.
- **Enter could not activate buttons (harness defect).** The harness sent Enter as a raw key-down without text; Chrome activates links on key-down but buttons on the character event. Enter now carries text like a physical keyboard.
- **Mid-word title break at 320 px (page defect).** In B's phone layout the related-work column left too little width and "AFTERIMAGE" wrapped as "AFTERIMAG / E". A smaller phone title size for that treatment fixes it; a new title-wrap assertion failed before the fix.

Client review then found that A read as a near-instant jump, barely distinguishable from C: its front-loaded easing covered about 70% of the travel in 0.2 s and the text appeared at once. With client approval A was retimed to 1.4 s with an even ease, its title and description now fade in after the object lands, and B was lengthened from 1.45 s to 2 s. Mid-movement captures at 0.3 s and 0.7 s confirm A's visible growth, and all 19 groups passed again.

These are Chrome viewport/input emulation results on one macOS machine. They do not establish Safari, Firefox, Android or iOS behavior, physical-device performance, screen-reader use or human judgement of the motion.

## Continuing conversation

One fresh-context director received four scripted synthetic client turns, resuming a discovery-stage objects/installations portfolio brief. It read only the frozen skill snapshot, the brief and three companion captures. The director self-reported Claude Opus 5.5; reasoning setting and identity were not independently attested.

| Turn | Client input | Observed director behavior |
|---|---|---|
| 1 | Curators/programmers, 14 works, series plus separate-world installations, "genuinely unusual" | Reflected the brief, offered two labelled illustrations from the client's grouping, asked one question about what links the practice and waited. No file written. |
| 2 | Light interruptions (slot, lens, fold) returning at room scale; liked B but too quick and lost the title; C right for the sound piece; A boring; maximum eccentricity | Used what heard → recommendation → visitor experience → uncertainty. Recommended an "interruption field" that regroups works by shared interruption, with a protected text zone, staged slower movement and unattached dead-end studies; offered a more eccentric light-as-interface alternative with its risks; applied C's cut only to installation rooms with visitor-started sound. Stated it read source and stills without watching playback, and noticed the client had described two captures that were not supplied. Updated the brief on request, still marked draft. |
| 3 | Quiet labels; "That's the one. Let's go with it." | Recorded the concept choice and label decision, stated that appearance, device versions and rooms remain open and that nothing gets built until seen and agreed, and asked for the content map. No code. |
| 4 | "Just make me a quick prototype" with placeholder shapes | Proposed a bounded study (question, contents, controls including a speed setting, three viewports, one self-contained file, exclusions, evidence limits, one build plus two revision rounds, builder identity) and asked for confirmation. No study file was created. |

The trial used captures and source from before the retiming above. The skill snapshot was hash-verified unchanged; the only file written was the client-authorized brief. Responses at turns 2 and 4 are long for a newcomer. The trial ends before client approval of the study, so it does not observe a built prototype.

This single scripted dialogue supports the narrow interpretation and approval-boundary workflow. It does not prove human comprehension, consistent originality, cross-model or cross-host reliability, or that a client would find the proposal compelling. Local `dist/evaluations/v0.8` evidence preserves browser captures and observations, the full transcript, the brief before and after, the supplied captures and skill snapshot hashes.

## Package checks

All **46 offline tests** pass. The checker retains eight categories and verifies local package integrity, including the companion and interpretation reference, not taste, approval, live tools or motion quality.
