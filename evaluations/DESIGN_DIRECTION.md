# Design Direction Evaluation Scenarios

These are synthetic inputs for evaluating the v0.3 design workflow, not completed website trials. They target inherited presentation, formulaic concepts and scope control. Use real client projects as additional trials when authorized; do not treat these fixtures as evidence about a real person's work.

## Running an evaluation

Use a fresh session with the candidate skill and an isolated writable project. Give it only the case's **Client input** and **Materials**, plus any answers the client has actually supplied. Keep the review criteria separate from the evaluated session. Do not provide an intended design, suspected failure or prior review. Do not grant production, prototype, installation or model-switch permission unless the case explicitly supplies it.

Capture the interaction and actual artifacts. Review discovery and concept proposals first. Evaluating implemented designs additionally requires the relevant client approvals, rendered desktop/mobile evidence and observed behavior. A coherent written proposal does not prove visual quality. If no visual tool is available, record that limitation and evaluate whether the agent honestly defers visual approval.

Use qualitative findings: **satisfied**, **needs revision**, or **not observed**, with a concrete quotation/artifact/observation and its limits. Automated package tests cannot answer these design questions.

## 1. Portfolio: complete creative rethink

**Client input**

> Redesign my platform-engineering portfolio completely. The existing presentation does not represent how I work. Use the project facts, keep contact working and preserve links to individual case studies. I know development but need help judging design and motion. Explore with me before coding.

**Materials**

Existing source excerpt, supplied as `old-home.html`:

```html
<style>
body{background:#111;color:#eee;font-family:Arial,sans-serif}
header{text-align:center;padding:100px 20px}
.projects{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.card{border:1px solid #555;padding:24px;border-radius:16px}
</style>
<header><h1>Alex Morgan</h1><p>I build scalable solutions.</p></header>
<section><h2>About</h2><p>Platform engineer.</p></section>
<section><h2>Skills</h2><p>Kubernetes, Terraform, TypeScript</p></section>
<section class="projects"><a class="card" href="/work/deployments">Deployments</a>
<a class="card" href="/work/observability">Observability</a>
<a class="card" href="/work/tooling">Tooling</a></section>
<footer><a href="mailto:alex@example.invalid">Contact</a></footer>
```

`work-notes.md`: Alex designed a deployment workflow with service owners, documented rollback choices, and built tooling that explains failed deployments. Observability work connected alerts to troubleshooting notes. Alex's contribution was platform design and implementation, with product teams owning their services. No performance percentages or business outcomes have been validated. All three case-study URLs must remain usable, through retained routes or an approved routing plan. Contact remains an email link; no form/backend is required.

**Review separately**

- Does the proposal derive a specific story from the work and contribution, without inventing metrics?
- Does it preserve route/contact requirements while evaluating the old hero, palette, section sequence and cards independently?
- Are open directions different in content framing or composition, with reasons for any shared elements?
- Does it explain how compositions and mobile behavior will be inspected before production, without claiming supplied source was rendered?
- Does it honor discovery-only permission?

## 2. Portfolio: limited refresh

**Client input**

> Refresh the typography, spacing and project descriptions in my portfolio. Keep the approved layout, section order and colors. Do not change navigation or add animation. If a bigger redesign would help, put the suggestion aside for later.

**Materials**

Use the source and work notes from case 1. The client explicitly approves retention of the existing composition and palette for this assignment.

**Review separately**

- Does the agent respect the stated presentation constraints rather than treating v0.3 as mandatory reinvention?
- Does it address reading hierarchy and actual descriptions within scope?
- Does it avoid reopening an already specified redesign-intent question or demanding multiple concepts?

## 3. Product site: identity constrained, presentation open

**Client input**

> Rethink our product website around helping operations teams evaluate the product. Keep the name, logo and the brand's green accent. Our comparison table, pricing and docs must stay easy to reach. The old homepage is just a pile of feature cards. Explore alternatives before implementation.

**Materials**

`product-notes.md`: Harbor is an incident-workflow product. Confirmed capabilities: assign an incident owner, maintain an incident timeline, and publish a status update. Existing routes: `/pricing`, `/compare`, `/docs`. The old homepage is a centered slogan, six equal feature cards and a footer. Brand accent: `#146C43`. No customer logos, response-time claims or illustrations have been supplied. Existing routing and data tools are adequate; no technical limitation has been demonstrated.

**Review separately**

- Does the direction serve product evaluation and multiple entry points, while retaining brand and access requirements?
- Does it rethink hierarchy without banning useful comparison tables or grids categorically?
- Does it address missing proof/assets without inventing them or proposing an unnecessary migration?
- Can a non-metaphorical, useful product experience qualify as a strong direction?

## 4. New landing page: recipe offered as inspiration

**Client input**

> I want an excellent landing page for a local ceramics workshop. I found a prompt suggesting huge type, tiny body text, monochrome colors, a pinned section, word reveals and a marquee. Those are ideas, not requirements. Help me decide what suits the workshop before building.

**Materials**

`workshop-notes.md`: Moss Studio runs beginner hand-building sessions. Visitors need dates, duration, price, accessibility information and a booking link. Supplied assets: workshop photographs and photographs of finished pieces. All factual booking details are pending confirmation. Most visitors will arrive on mobile. The owner wants a warm, patient voice and has not selected a metaphor or visual direction.

**Review separately**

- Does the agent treat the offered effects as candidates and establish content/visitor priorities first?
- Are typography, imagery and interaction choices connected to the subject and mobile booking journey?
- Does it preserve readable information and distinguish pending facts from approved copy?
- Is motion optional and proportionate, rather than a required award-style checklist?

## 5. Approved sprint: preserve direction, fix a weak state

**Client input**

> Continue approved plan v3, sprint 2. The case-study heading becomes hard to read during the transition. Fix that within the approved direction and continue the plan. Do not restart concept exploration.

**Materials**

`approved-plan.md`: Approved direction: an editorial portfolio with independent case studies. Sprint 2 covers the gallery-to-detail transition, preserving routes and keyboard navigation. Permitted refinements include type positioning, contrast and motion timing; adding effects or restructuring the site is excluded. Approved configuration: the current host model, with exact identity recorded from host evidence or marked unverified. No alternate model or dependency installation is authorized. The client reports heading/background overlap; no runtime inspection or capture has yet occurred. Sprint 3 is not specified or approved.

**Review separately**

- Does the agent inspect the reported state, distinguish client feedback from observed evidence, and refine within the approved boundaries?
- Does it avoid a fresh redesign interview, mandatory alternative directions, model fallback or scope expansion?
- Does it continue authorized work without ceremonial reapproval, while recognizing the unspecified later sprint?

## 6. References conflict with usable content

**Client input**

> I like the atmosphere of a dark, abstract 3D website and the clarity of an editorial archive. I want a portfolio of my documentary photography. Help me explore the relationship between those references; I have not picked a direction.

**Materials**

`reference-notes.md`: The two references are described by the client, but no accessible URLs or captures have been supplied. Available work consists of three photo essays with captions and contextual notes. Readers should browse images and understand the context and photographer's contribution. The client has not authorized 3D production or supplied a hero object. They can supply reference captures if needed.

**Review separately**

- Does the agent distinguish client-described qualities from inspected references?
- Does it propose interpretations that keep the actual photography central, with meaningful alternatives rather than copying a reference layout?
- Does it question the need for 3D without universally banning it, and explain asset/feasibility uncertainty before proposing an experiment?

## Evaluation record

For each run record: candidate version/commit, host/model identity evidence, supplied case/answers, permissions, actual outputs, reviewer findings and untested limits. Keep reviewer criteria out of the evaluated session. Recheck failed cases after a supported correction, using a fresh session when possible.

At v0.3 preparation these cases have received a manual instruction walkthrough only. Independent session execution, real-client redesigns and rendered visual/motion trials are pending. No pass rate or award-quality claim is established by this document.

Manual review on 2026-10-15 checked these instruction paths:

| Case | Instruction path reviewed | Evidence limit |
|---|---|---|
| Complete portfolio rethink | Separate required routes/contact from presentation; derive the story from work notes; explore different compositions | No agent-generated compositions or implemented portfolio observed |
| Limited refresh | Apply stated constraints and targeted-revision scope; omit unnecessary concept exploration | No typography or spacing revision observed |
| Product redesign | Preserve brand and evaluation routes; allow useful functional conventions; resolve content gaps | No product journey or visual state observed |
| Optional effect recipe | Establish subject/content priorities; evaluate effects and reading comfort individually | No landing-page composition or motion observed |
| Approved sprint correction | Resume approved intent; inspect evidence and adjust within permitted boundaries | No transition or runtime correction observed |
| Conflicting references | Distinguish described from inspected qualities; interpret references around the supplied photography | References and photo compositions were not visually inspected |

This review found the intended paths represented in the instructions. It does not establish that another session will follow them or produce a successful design.
