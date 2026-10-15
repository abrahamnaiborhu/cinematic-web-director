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

## Grounding review: client-provided public website

On 2026-10-15 the client supplied [abrahamnaiborhu.com](https://abrahamnaiborhu.com/) and reported that their animation ideas drove the implementation. Homepage HTML was read and a temporary isolated Chrome session inspected the desktop opening, selected scroll states through the deployment section, and the mobile opening. Desktop viewport: 1440 × 1000; mobile: 390 × 844. This was a partial inspection, not a full usability, accessibility or performance audit.

Observed content connected application work, platform responsibility and reliability. A deployment illustration and changing explanation were present during the sampled scroll states. The client report establishes their account of creative authorship; the resulting website alone cannot verify who originated each idea. The failure/fallback section was present in the HTML, but its full temporal behavior was not evaluated.

Two proposals were discussed to ground this update: carrying an application's visual identity into the supporting-platform story, or using coordinated editorial/layout changes to express the shift in responsibility. They extend the site's subject rather than relabeling its existing deployment/fallback demonstrations as new ideas. They were not implemented or validated as successful motion treatments.

## Manual instruction review

The five cases were reviewed against the candidate instructions: proactive proposals for open directions; a contribution beyond existing client ideas; provisional ideas alongside sparse-brief questions; explicit static-site constraints; and scope-preserving sprint continuation. The intended paths are represented. This review does not establish that a separate agent session follows them or that a rendered result succeeds.

For actual runs record candidate version/commit, host/model identity evidence, client answers, permissions, proposal artifacts, reviewer findings and remaining uncertainty. Do not give this review or the criteria to the evaluated session. Treat independent creative initiative and observed motion quality as separate findings from automated preflight/package tests.
