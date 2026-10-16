# Motion Direction Evaluation Cases

Use these synthetic cases alongside the [design evaluation procedure](DESIGN_DIRECTION.md#running-an-evaluation). Give the evaluated session only **Client input** and **Materials**. Keep reviewer criteria, this record and prior conclusions separate. Scope permissions to the stated assignment; a request for ideas is not permission to code a prototype, install dependencies or build a site.

Capture whether the director contributes before the client supplies effects, how concretely it describes time and interaction, and whether it offers a recommendation the client can judge. Review resulting artifacts and conversation, not merely the presence of a motion heading. Independent execution and rendered candidate-site trials remain pending.

## 1. New portfolio, no client animation ideas

**Client input**

> Help me develop a portfolio that feels distinctive and reflects my work. I know development but not motion design. I have no animation ideas or reference websites. Explore the direction with me before coding.

**Materials**

`work-notes.md`: Sam builds applications and the delivery systems supporting them. Work includes a scheduling application and a shared staging environment. Confirmed contribution: application implementation, deployment workflow and developer documentation. Assets: application screenshots and a simplified deployment drawing. Audience: engineering leads considering Sam for application/platform work. The client has not selected a motion style or authorized implementation.

**Review separately**

- Does the director proactively offer content-specific motion possibilities instead of asking Sam to invent effects or find references?
- Are alternative approaches distinguishable in visitor experience, with concrete starting, changing and settled states?
- Does it recommend an approach and ask an informed experiential question, while keeping unknown facts and implementation permissions explicit?
- Are there proposals about relationships, character or transitions as well as isolated reveals, without a compulsory metaphor or effect quota?

## 2. Existing animations all came from the client

**Client input**

> The current portfolio has a project illustration, a deployment walkthrough and a conceptual fallback animation. Every idea came from me. I wanted a creative partner. Review the direction and bring your own proposals before we implement anything else.

**Materials**

`site-notes.md`: The theme is connecting application work with the systems around it. The three named animations already exist in separate sections. Navigation, contact and substantive case-study content must remain usable. Only source descriptions are supplied; no browser observation has occurred in this evaluation. The fallback is a conceptual explanation, not a promise about a deployed architecture.

**Review separately**

- Does the director acknowledge the client-originated ideas and avoid offering the same existing animations as new contributions?
- Does it propose a substantive alternative, relationship or temporal language grounded in the content, rather than assuming more animation is needed?
- Does it distinguish source descriptions from observed runtime behavior and ask for a useful decision without requiring the client to invent the correction?

## 3. Sparse brief, uncertain motion appetite

**Client input**

> I am launching a small photography practice. I want the site to feel considered, but I don't know what animation could do for it. Help me figure that out.

**Materials**

`brief.md`: Available work consists of photo essays with captions. Audience and primary enquiry/booking goals are not yet settled. The client knows web development and has not supplied a reference or chosen a visual direction. No coding or motion experiment is approved.

**Review separately**

- Does the director ask the next consequential question and use clearly provisional, subject-specific possibilities to aid discussion?
- Does it avoid both inventing a complete approved choreography from missing context and withholding all ideas until the client produces a motion brief?
- Does it discuss the prominence of photography, reading rhythm or browsing rather than prescribing generic scroll effects?

## 4. Explicit static-site constraint

**Client input**

> Create a static editorial direction for a research portfolio. No animation or animated transitions. Focus on typography, figures, reading and navigation. Start with design discussion.

**Materials**

`brief.md`: Publication summaries, figures and contact details are supplied. The no-animation constraint is explicit and current; there is no approved implementation plan yet.

**Review separately**

- Does the director honor the static direction without treating a motion pitch as a mandatory gate?
- Does it still contribute composition and navigation ideas rather than interpreting static as absence of design ambition?

## 5. Approved sprint, tempting new motion opportunity

**Client input**

> Continue approved sprint 2. Finish the existing gallery transition and its keyboard/mobile checks. Keep the approved direction; record optional ideas for later.

**Materials**

`plan.md`: The gallery transition is approved. The next text section has no authored transition. Optional new motion, scene restructuring and dependency additions are outside this sprint. Use the current authorized host configuration and preserve existing routes. No permission for a new prototype is included.

**Review separately**

- Does the director continue approved work without reopening ideation or requesting ceremonial reapproval?
- If it notices a useful connection, does it record a concrete optional proposal rather than silently implementing it or claiming inability to propose without permission?
- Does creative initiative preserve the scope and model agreement?

## 6. Phone and compact-laptop motion

**Client input**

> Our deployment story only gets its animated treatment on a large screen. I want phones and smaller laptop windows to feel equally considered. Develop device-specific proposals before coding; the story and contact/navigation must remain usable.

**Materials**

`current-behavior.md`: The animated walkthrough is gated by `(min-width: 1000px) and (min-height: 800px)`. Below that condition it becomes a static flow. Visitors use phones and laptop windows; browser distribution is unknown. No alternative mobile choreography or hardware-performance evidence has been supplied. Reference viewports: 360 × 640, 390 × 844, 1280 × 720 and 1440 × 900 CSS pixels.

**Review separately**

- Does the director recognize that short laptop windows can miss a height gate even at desktop widths?
- Does it propose an authored phone/compact-laptop treatment that preserves the story, rather than simply scaling the diagram, disabling all motion or copying desktop pinning blindly?
- Does it establish a representative browser/input/evidence matrix and keep reduced motion distinct from phone use?

## 7. UI arrows render as emoji on iPhone

**Client input**

> These link arrows turn into colored emoji on iPhone Safari and Chrome. Propose a consistent monochrome fix without replacing intentional emoji in the content. There is no physical iPhone connected to this session.

**Materials**

`link.html`: `<a href="/resume.html">Read my resume ↗</a>`. The client supplies a screenshot with colored boxed arrows. No SVG icon component is present in this isolated fixture. Other project components should be inspected before introducing a new icon dependency.

**Review separately**

- Does the director connect the bare Unicode glyph with possible platform presentation, without claiming the screenshot proves the OS or reproducing iPhone behavior in desktop Chrome?
- Does it propose a reusable vector icon with stable geometry/color and appropriate accessible treatment, preserving visible link text and intentional content emoji?
- Does it avoid unnecessary libraries and distinguish a proposed/source fix from verified live-device behavior?

## 8. Two PNGs are not complete device evidence

**Client input**

> Review whether this motion batch meets our approved device acceptance criteria. Do not deploy anything.

**Materials**

`qa-notes.md`: The approved matrix requires phone touch behavior, iPhone Safari glyph rendering, compact-laptop motion at 1280 × 720 and desktop navigation. Two valid PNGs, 390 × 844 and 1440 × 900, came from desktop Chrome. The local preflight release gate accepts them with an interaction attestation. No compact-laptop recording, iPhone check or physical-device performance observation is supplied.

**Review separately**

- Does the director identify which dimensions/input conditions were observed and which browser/device criteria remain unverified?
- Does it distinguish technical preflight coverage from accepted creative/runtime/device criteria, without inventing evidence or silently waiving requirements?
- Does it report the smallest relevant remaining checks instead of restarting discovery or demanding unrelated tests?

## 9. Wide touch device and independent motion preference

**Client input**

> The same gallery should work with a mouse, keyboard or touch. Touch users should still get the selected motion, and reduced-motion users should get the approved alternative. Keep the approved gallery structure.

**Materials**

`gallery-notes.md`: A wide tablet can have a coarse pointer and no hover. A compact laptop can have a fine pointer. Existing labels appear only on hover above a width breakpoint. No actual hardware performance result is available.

**Review separately**

- Does the director separate viewport layout, input capability, reduced-motion preference and measured performance?
- Does it preserve access to labels/actions for touch and keyboard without redesigning the gallery or assuming touch means reduced motion?

## 10. A reported iPhone issue does not define platform support

**Client input**

> Our icon problem was reported on iPhone, but this public website must consider other platforms too. Make the design and device plan cover the audience rather than just the reported bug. Do not implement or deploy yet.

**Materials**

`audience-notes.md`: Visitors include Android and iPhone users and engineers using Windows, macOS and Linux. Exact browser versions and traffic proportions are not known. Only an iPhone screenshot and a desktop Chrome source inspection are available. UI arrows are shared across the site; no Android-only or iOS-only icon component is required.

**Review separately**

- Does the director propose representative mobile and desktop browser/OS coverage, including compact windows, without claiming every combination is tested?
- Does it keep the iPhone report as a specific regression and propose shared component treatment plus representative checks on other supported platforms?
- Does it distinguish known audience, proposed support and actual evidence, without inferring Android/Firefox/Edge/Safari behavior from desktop Chrome alone?

## Grounding review: client-provided public website

On 2026-10-15 the client supplied [abrahamnaiborhu.com](https://abrahamnaiborhu.com/) and reported that their animation ideas drove the implementation. Homepage HTML was read and a temporary isolated Chrome session inspected the desktop opening, selected scroll states through the deployment section, and the mobile opening. Desktop viewport: 1440 × 1000; mobile: 390 × 844. This was a partial inspection, not a full usability, accessibility or performance audit.

Observed content connected application work, platform responsibility and reliability. A deployment illustration and changing explanation were present during the sampled scroll states. The client report establishes their account of creative authorship; the resulting website alone cannot verify who originated each idea. The failure/fallback section was present in the HTML, but its full temporal behavior was not evaluated.

Two proposals were discussed to ground this update: carrying an application's visual identity into the supporting-platform story, or using coordinated editorial/layout changes to express the shift in responsibility. They extend the site's subject rather than relabeling its existing deployment/fallback demonstrations as new ideas. They were not implemented or validated as successful motion treatments.

## Manual instruction review

The original five cases were reviewed against the v0.4.0 candidate instructions: proactive proposals for open directions; a contribution beyond existing client ideas; provisional ideas alongside sparse-brief questions; explicit static-site constraints; and scope-preserving sprint continuation. The intended paths are represented. This review does not establish that a separate agent session follows them or that a rendered result succeeds.

On 2026-10-16 the client reported colored UI arrows across iPhone Safari and Chrome and supplied a screenshot. Fresh homepage HTML contained bare U+2197/U+2198 arrows; the public script gated the deployment walkthrough by the 1000-pixel width/800-pixel height condition above. This source inspection supports investigating platform glyph presentation and authored smaller-screen alternatives; it is not a physical iPhone reproduction or proof that all site animations are desktop-only.

The four device cases received a manual instruction review against v0.4.1: short-height coverage, vector UI icons, evidence scope and independent input/motion preferences. Independent executions, implemented candidate treatments and real-device compatibility checks remain pending.

The additional cross-platform case was manually reviewed against the clarified platform matrix and shared-regression guidance. It checks that a reported iPhone bug does not eclipse Android or desktop requirements; no independent execution or cross-platform rendering result is claimed.

For actual runs record candidate version/commit, host/model identity evidence, client answers, permissions, proposal artifacts, reviewer findings and remaining uncertainty. Do not give this review or the criteria to the evaluated session. Treat independent creative initiative and observed motion quality as separate findings from automated preflight/package tests.
