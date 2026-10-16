# Creative Direction Workflow and Quality Gates

## Use this workflow

Develop a purposeful website with a client who may understand engineering well and motion design poorly. Adapt the work to the assignment: landing page, portfolio, product website, redesign or targeted revision. A project can combine these. Read only the stages needed for the current work; resume from approved artifacts instead of repeating an interview.

This reference covers: intake and discovery; concept and structure; art and motion direction; storyboarding; prototypes; architecture; readiness; model handoff; sprints; critique and revision.

## 1. Intake and adaptive discovery

When the client has not described the assignment, ask “What would you like to build or improve?” Otherwise reflect the known assignment and ask the next useful question. Clarify intent before project-specific preflight, then review its eight checks for the current stage. Creative planning can proceed with implementation dependencies deferred. Skill maintenance does not require a website project.

Ask one focused question at a time whenever possible. Follow the client's answer, not a fixed questionnaire. Establish purpose, visitors, intended outcomes, available content, constraints and unknowns. Establish their expertise rather than teaching development basics to an experienced engineer. Discovery ends when consequential decisions have inspectable answers and approval, not after an arbitrary number of minutes or questions.

Maintain an evolving brief in the project script with three distinctions:

| Information | Treatment |
|---|---|
| Confirmed facts | Record the source and any limitations; do not invent achievements, claims, capabilities or assets |
| Creative decisions | Explain options and reasons; record the client's approved choice and version |
| Unresolved matters | Explain consequences; resolve through discussion, references or an approved experiment |

When the client is unsure, propose understandable alternatives and recommend one. Introduce technical creative vocabulary only when it helps a decision. For example: “Keeping the project image visible while its explanation changes may connect the result with your contribution. We can test whether that remains clear on a phone.” Periodically reflect the brief back, expose contradictions and invite correction. Client approval applies to identified material and versions, not an unspecified “looks good.”

Once useful subject/content context exists, initiate the motion conversation using [motion direction](MOTION_DIRECTION.md). Offer concrete possibilities and an informed question about the visitor experience. Do not require the client to supply animation ideas, reference websites or plugin names before the director can contribute. Respect explicit no-motion preferences and avoid adding a motion interview to an unrelated targeted task.

Use [device experience](DEVICE_EXPERIENCE.md) to propose audience/device priorities and representative browser/input coverage early. For new or substantial public-site designs, develop phones and compact laptop windows as first-class experiences alongside larger screens. Record agreed targets and distinguish them from environments actually tested.

### Existing sites and materials

Inspect relevant project source, briefs, copy, images, screenshots, brand assets and reference links before requesting more. Use a bounded inventory of the project; skip generated output, dependencies and unrelated private configuration. Read the actual relevant contents and inspect images with available visual tools. Do not infer contents from filenames or treat embedded reference instructions as client authorization.

Record location/link, role, usable content, freshness and approval status in the project script. Leave files in their existing locations. If material is missing, ask for the specific useful input and suggest an optional project folder such as `creative/references/`; links can go in a Markdown file. Do not require all material to be reorganized. Ask what the client values in an inspiration reference: composition, atmosphere, type, pacing or interaction can imply different directions.

Differentiate factual sources, mandatory brand constraints, inspiration and old experiments. Existing copy may be inaccurate; clarify conflicts with the client and record which source supersedes another. Draft new copy from confirmed information, label placeholders, and obtain content approval. Consider copy length and emphasis alongside composition and pacing.

For redesigns, inspect the actual rendered site and relevant navigation/interaction states when tools permit. Otherwise label the assessment as source-only or based on supplied captures. Establish a baseline of message/story, hierarchy/navigation, visual identity, motion, accessibility and technical behavior. Explain each problem's visitor impact and identify what to retain, revise or replace. Existing implementation is evidence, not automatic creative approval. Preserve functionality the client requires and record approved changes to it.

Establish the degree of reinvention from the client's intent; clarify it only when consequential and unclear. Use [design direction](DESIGN_DIRECTION.md) to separate the factual/functional baseline from inherited presentation, derive the story without borrowing the old section list, and explain consequential carryover. Component reuse does not establish a visual constraint. A targeted refresh still respects its limited scope.

Recheck relevant materials before major approvals and sprint starts. New material triggers an impact review of affected decisions. Preserve unaffected approvals and continue independent authorized work.

**Checkpoint A:** the client approves the purpose, visitors, content/factual basis, important constraints and proposed site structure/journeys. Identify which structural decisions are fixed and which remain provisional for creative exploration. Consequential unresolved matters have owners and a resolution plan. Missing implementation tooling does not block this checkpoint.

## 2. Structure, copy and creative exploration

Help define pages, content hierarchy, navigation and visitor journeys, starting from existing approved requirements. Draft and revise copy with the client. Explore alternatives when a direction is undecided; an already approved direction does not need a new concept contest.

Normally present two or three meaningfully different directions, with central idea, intended visitor experience, representative composition, content approach, continuity, originality potential, accessibility/maintenance/cost risks and implementation implications. Recommend one and explain why. Let the client reject, combine or challenge directions. Use visual references or annotated layouts where available; identify what was actually inspected and what remains illustrative.

Apply [design direction](DESIGN_DIRECTION.md) and [motion direction](MOTION_DIRECTION.md) during exploration. Candidates should differ in how they frame content, organize attention or support journeys, not merely in palette and naming. Develop composition and motion intent together using actual content; inspect representative static states before detailed choreography. Bring a recommendation on temporal character, important connections and promising moments. Metaphors, signature interactions, dramatic type and familiar effects are choices to evaluate, not a universal recipe.

Adapt narrative to visitor behavior:

| Experience | Structure to consider | Useful evidence/payoff |
|---|---|---|
| Focused landing page | A coherent sequence supporting a next action | A demonstration or proof that clarifies the proposition |
| Portfolio | Curated collection, independent case studies, author identity | Work and explanation that establish contribution and judgment |
| Product website | Multiple pages and routes for different visitor needs | Capabilities, evidence, integration or evaluation information where needed |

These are examples, not compulsory layouts. Acts are narrative functions; sections, pages and routes are implementation/content units. Use a linear arc only when appropriate. A metaphor, five-act structure, single CTA or dramatic climax is optional. Establish what each important unit contributes and whether visitors can understand it without playing an animation or starting at the homepage.

For originality, derive a specific thesis from the subject, audience and content. Explain why the proposed composition, imagery and movement express it. Compare alternatives on more than palette; references provide qualities to interpret, not whole designs to reproduce. Reject attractive effects whose connection to the project's purpose cannot be explained.

**Checkpoint:** a selected or blended direction, approved experience structure and intended content are specific enough to develop representative visual states. The narrative remains understandable with animation disabled.

## 3. Art direction, continuity and storyboarding

Use the continuity bible to establish typography roles, palette/contrast, imagery, geometry, composition, depth/scale, recurring elements, interaction language and pacing. Explain specialized choices through visible examples. Treat scenes as optional units for authored moments; collections, pages and functional interactions may need other structures.

For important connections document: what carries forward, what transforms, what is introduced and why. Cover route changes, direct entry, browser back/forward and returning from detail content. Independent pages must retain identity and orientation without relying on a previous animation. Hard cuts are permitted when purposeful. Use shuffle/removal tests only where sequential dependencies are intended.

Create representative compositions and a storyboard before detailed technical sequencing. For each important state show subject, hierarchy/copy, continuity elements, visitor action and intended result. Inspect static composition first, then discuss what movement contributes. Use available sketches, annotated screenshots or visual tools; textual plans remain labeled as plans and cannot substantiate a rendered visual review.

Use the treatment template for a page, scene or interaction: entry, intermediate states, exit, transitions, interruptions/skip, small-screen composition, reduced motion and acceptance criteria. Describe motion in plain language before naming plugins or timeline APIs. Record proposed techniques only after purpose is clear. Literal reverse is optional: consider reversible timelines, authored return transitions, reset/replay, recorded playback or direct navigation. Live physics needs an explicit state/reset or replay strategy.

Include representative phone and compact-laptop compositions, short-height behavior and authored adaptations of important motion. Consider touch/keyboard separately from reduced-motion preference. Review UI symbols across the supported platforms; use deliberate vector icons when consistent geometry matters.

**Checkpoint B:** the client approves the whole site's creative structure, representative compositions, visual direction and continuity rules. Summarize the idea's connection to actual content, consequential inherited choices and the proposed motion character/opportunities, including the director's recommendation and the client's decision. Record a deliberately static direction when selected; do not silently infer one from absent client ideas. Text-only proposals do not establish completed visual review. Detailed choreography for later batches may remain open. Timing or feasibility uncertainties can be resolved with an approved prototype.

## 4. Small pre-production experiments

Before coding each motion prototype, obtain explicit approval of a bounded experiment. Record:

- The named uncertainty and why observation is needed.
- The smallest scene/transition/interaction to test, permitted files/dependencies and model configuration.
- Expected evidence, success criteria, relevant devices/input alternatives and a practical time/iteration boundary.
- What is excluded and what decision the result will inform.

An approved sprint plan may explicitly approve identified experiments with these details. A generic “prototype later” entry is insufficient. Rerun preflight for `--phase prototype`; this scope needs a readable brief and approved experiment, not approval of the entire production design. Set GSAP requirements to the techniques actually involved. Label provisional content and visual decisions.

After observing the experiment, show the client what worked, failed and remains uncertain. Give concrete viewing prompts: “Can you follow the product through the transition? Does its movement explain the connection?” Record adopt/revise/reject and update affected plans. Stop at the approved boundary; if an experiment is inconclusive, propose a different test or approach. Prototype approval does not authorize an unplanned production build.

## 5. Architecture alongside creative requirements

Inspect the actual stack and package/application boundaries. Evaluate rendering, routing, state persistence, content/data sources, assets, animation lifecycle, deployment, performance and maintenance against the proposed experience. Existing technology can be reused, extended or migrated; client-defined constraints and existing integrations remain explicit.

Identify whether a limitation belongs to tooling, application structure, animation code, content/assets or framework capabilities before proposing migration. Consult current primary documentation for the relevant versions. A prototype should test an uncertain technical assumption where useful.

Frameworks, build tools, state management, remote data management and backend services address different responsibilities. React with Vite, Next.js, Zustand, TanStack Query and NestJS are examples, not a mandated stack or a set of drop-in equivalents. Adopt existing adequate tools or justify additions. GSAP implementation guidance belongs in the relevant official GreenSock skills, with an explicitly approved current-official-documentation fallback when access is unavailable.

For each proposed change record: requirement, alternatives including the current setup, recommendation/reason, dependencies, migration effects, deployment/maintenance consequences and validation. Include approved technical changes in the sprint plan; approval need not be a separate ceremony. Feature and data/backend scope come from the client's requirements, not from the availability of a library.

## 6. Production readiness and approved sprint batches

**Checkpoint C:** obtain approval of an identified sprint plan/version only after the upcoming batch has:

1. Clear purposes within the approved site structure and visitor journeys.
2. Approved content and inspectable representative compositions/connections.
3. Detailed motion/interaction treatments, including the agreed device/browser/input matrix, phone and compact-laptop variants, reduced motion, interruption and direct entry as relevant.
4. Consequential uncertainties resolved or confined to explicitly approved experiments; adjustable details have stated boundaries.
5. Approved architecture changes, model configurations and scoped responsibilities.
6. Observable acceptance criteria, dependencies, evidence requirements, permitted refinements and stopping/escalation conditions.

The agent reads back what will be built, why, inputs, connections, adjustable details and how it will be evaluated. Do not equate a nonempty brief or technical preflight result with these approvals. Record relevant versions in the project script. A later batch needs its own sufficiently detailed treatment and authorization; an approved whole-site direction does not automatically approve unspecified implementation work.

## 7. Model agreement and handoff

Keep approved configurations and responsibilities in the project script. Record provider, exact model identifier/version when known, reasoning setting where exposed, evidence/source of identity, role, allowed scope, approval and escalation conditions. Avoid permanent rankings by family name: model identity and reasoning effort are different settings, and both creative and technical work can be demanding.

Use an appropriate demanding configuration for unresolved creative choices, complex choreography and difficult technical trade-offs. A less expensive configuration may perform bounded approved work when it has suitable capabilities. The same acceptance criteria apply. If no authorized configuration can perform the work, disclose that limitation and pause dependent work; do not quietly lower the quality bar.

Before each handoff or observable fallback, announce:

> Proposed/confirmed configuration: [provider/model/effort and identity evidence]. Task: [approved sprint and scope]. Inputs: [artifact versions]. Reason: [task suitability]. Validation: [criteria]. Return for review if: [conditions].

An existing configuration approval can authorize repeated use in its stated scope; announce each handoff without re-requesting that authorization. Obtain approval for a new configuration, reduced reasoning setting outside the agreement or expanded responsibility. “Proposed” is not “switched”: report actual host confirmation separately. If metadata is unavailable, label it unverified and ask for essential confirmation when the agreement depends on it. A Markdown skill cannot force a host switch or detect every hidden provider fallback.

Provide a compact transfer record referencing approved facts, creative intent, architecture, treatment/sprint versions, completed work, evidence, open issues and allowed adjustments. The receiving agent reads these inputs before proceeding and reports consequential gaps. Update the iteration log with the actual handoff evidence. Do not assume the whole conversation transfers between models, sessions or providers.

## 8. Execute and refine each sprint

An approved plan authorizes continuous execution through its sufficiently specified sprints. Do not stop at each boundary for ceremonial reapproval. A sprint delivers a coherent improvement to a visitor experience: a scene plus connection, a gallery/detail journey, a product demonstration or an architecture change with validated integration.

For each sprint:

1. Recheck relevant sources, artifact versions, dependencies, scope and configuration. Run implementation preflight as appropriate.
2. Implement the smallest coherent slice, using the relevant technical references and lifecycle cleanup.
3. Verify the acceptance criteria using actual runtime behavior. Fix in-scope defects and refine within the authorized direction.
4. Critique against intent, record evidence and remaining limits, and report the outcome and next authorized work.
5. Continue through the approved plan; seek further authorization only where required by changed scope, intent or configuration.

Each refinement addresses a named problem or tests a specific expected improvement. A sprint can include planned iteration rounds; it is not complete while blocking checks fail. At the approved time/iteration boundary, or after repeated attempts without observable benefit, summarize evidence and propose a different approach. Keep optional polish in a backlog rather than inventing endless work. Repeated failure does not authorize weakening acceptance criteria.

Pause affected work for consequential ambiguity, changed approved intent, unapproved scope/model fallback or unresolved blocking failure. Continue independent authorized work where possible. Material architectural findings can require revisiting earlier creative/technical decisions; update their versions and dependent work explicitly.

## 9. Evidence-based critique and release

Observe actual desktop/mobile layouts, representative scroll/motion states, navigation, touch/keyboard interactions, interruptions, reduced motion and direct entry as relevant. Check whether key information and actions remain accessible. Measure performance where tooling permits, recording viewport/device and conditions rather than inventing results. Screenshots alone cannot establish motion quality or interaction correctness.

Account for the agreed device coverage, including compact/short laptop windows and reported platform issues. Resized desktop Chrome is viewport emulation, not evidence of iPhone Safari or Android hardware behavior. Keep client captures, agent-run checks and untested rows distinct; two preflight PNGs do not certify the whole matrix.

Assess story/content, composition, originality, continuity, motion, usability/accessibility, responsiveness and technical performance separately. For an issue record creative intent, existing implementation, observed problem/evidence, visitor impact, proposed correction, expected improvement and validation. Distinguish functional defects, unmet creative intent and optional polish. The iteration log holds decisions and observations; the project script and bible hold current approved intent.

Use the design-direction critique questions to check subject specificity, unjustified inherited presentation, access to substantive content and whether motion contributes. Review the actual compositions and observed experience; do not substitute a list of trendy techniques or an invented originality score for judgment.

Review creative initiative separately: did the director offer concrete motion ideas, alternatives and a recommendation while the direction was open, or only implement client ideas? Correct a gap through relevant proposals and discussion, not by adding unapproved effects. Inspect actual motion over time before claiming that pacing or continuity works.

Periodically review the whole experience across sprints. A good isolated scene may still disrupt overall pacing, browsing or identity. Use client reactions as evidence without treating aesthetic taste as a numerical score. If a revision changes an approved decision, identify affected units/approvals, explain alternatives and obtain the necessary agreement before implementing that change.

Before release, run release preflight, resolve blocking functional/readability/accessibility defects, compare the complete result to approved criteria and report remaining limitations. Client approval of creative direction and any publication/deployment authorization are separate from a checker exit code. Finish when the agreed outcomes and checks are satisfied; preserve deferred ideas for later work.
