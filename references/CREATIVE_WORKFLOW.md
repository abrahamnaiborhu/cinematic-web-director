# Creative Direction Workflow and Quality Gates

## Purpose

Turn an uncertain product idea into an intentional, story-driven website. The human should never need to know narrative theory or GSAP plugins up front. The director explains choices, proposes concrete alternatives and challenges weak decisions. Aesthetic ambition must coexist with usability and factual accuracy.

## Stage 1 — Discovery

Gather: what the product genuinely does; whom it serves; the visitor's current problem or desire; most defensible differentiation; one primary next action; tone and brand constraints; existing visual/content assets; technical limits. Ask one or two plain questions at a time. If the user lacks an answer, propose assumptions explicitly labeled for confirmation.

**Gate:** a concise one-sentence promise, target audience, CTA, content constraints and list of unknown claims.

## Stage 2 — Creative exploration

Present 2–3 meaningfully different concepts, not superficial palette variations. For each: central metaphor, intended emotion, rough narrative, hero concept, plausible climax, continuity motif, usability and cost risks. Recommend one with an explanation.

**Gate:** owner has selected or blended a direction.

## Stage 3 — Narrative script

Build an arc adapted to the content. Useful default: Hook → Tension → Discovery → Climax → Resolution/Action. Acts are narrative functions, **not necessarily sections**. A product with no dramatic conflict may instead use an exploration/discovery arc. Avoid forced drama or fabricated product features. Identify audience takeaway from every act, climax and final CTA. Use `templates/PROJECT_SCRIPT.md`.

**Gate:** the proposed act sequence makes sense even with all animation disabled; the climax communicates the core product insight; the CTA is clear.

## Stage 4 — Art direction and continuity

Define recurring visual motifs, geometry, typography, color roles, imagery treatment, composition, spatial rules, transition strategy, visual rhythm, accessibility and mobile equivalence. Every adjacent pair of scenes answers: what carries forward, what transforms, and what is introduced? Hard cuts are allowed when intentional. Use `templates/CONTINUITY_BIBLE.md`.

**Gate:** scenes look like they belong to one art-directed experience; section shuffle and removal tests reveal meaningful narrative dependencies where appropriate.

## Stage 5 — Motion treatment

For each scene provide narrative role, primary subject, entry state, staging, sequence timeline, scroll binding, interaction, exit state, bridge to next scene, mobile/reduced-motion treatment, performance risks and reverse/reset behavior. Prefer a scene timeline per sequence, with a controller coordinating interactions. Consult official GSAP skills for technique, not for story decisions.

**Gate:** all states, transitions, interruptions and end navigation have a plausible implementation strategy. Live physics is never promised to reverse without planned state capture or alternate motion.

## Stage 6 — Prototype and production

Rerun preflight with `--phase implementation`. Implement a vertical slice early (one full scene and its adjacent transition) to validate pacing and continuity before building the rest. Use component-scoped cleanup, accessible defaults, transform-first motion and responsive variants. Verify actual performance on a mid-range mobile device where possible.

**Gate:** working prototype satisfies the treatment and navigational basics; actual behaviors verified, not inferred from code.

## Stage 7 — Creative critique

Use live browser/screenshots if available. Review storytelling, design, UX, originality, content, accessibility, visual continuity, motion coherence and responsiveness. List **evidence**, **impact**, and **targeted correction** for issues. Do not assert an Awwwards score or guaranteed award.

**Gate:** critical functional, readability and accessibility defects resolved; highest-impact design issues prioritized.

## Stage 8 — Iterative refinement

Maintain `ITERATION_LOG.md` with hypothesis, changed scene, proof and result. Make purposeful refinements rather than random visual additions. When substantial design intent changes, update the script and continuity bible rather than causing creative drift.

**Gate:** owner has approved final direction, required practical checks have been performed, and unresolved limitations are disclosed.
