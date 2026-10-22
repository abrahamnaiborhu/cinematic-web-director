# Ponytail engineering: deliver the approved experience

Use for implementation choices, in-scope refactoring and engineering review of an approved experiment or sprint. This is a self-contained, phase-scoped adaptation of [Ponytail](https://github.com/DietrichGebert/ponytail), not its session-wide prompt or plugin. Source/version and MIT notices are in [the attribution](../third_party/ponytail/NOTICE.md).

## Preserve the brief while reducing implementation burden

The complete task includes the approved creative intent: composition, expressive behavior, timing relationships, content, visitor control and device/reduced-motion treatments. A shorter implementation that drops these requirements is incomplete. Engineering simplicity is not a reason to replace an approved interaction with a fade, force an old component's appearance onto a redesign or make phones static without agreement.

When the direction is unresolved, use discovery and art direction to develop it. Do not shrink a vague creative request into the easiest website to build. During authorized production, optimize within the approved contract. If the contract conflicts with a demonstrated technical constraint, present the evidence, alternatives and recommendation for the affected decision; continue independent work. Preserve the existing model and scope agreements.

## Choose the smallest complete implementation

Before editing, inspect the touched code and connected callers, state/data ownership, tests, fixtures and configuration. Identify the real change boundary and expected use/load. A small diff can still break an untouched caller or leave event listeners active after navigation.

Use the required [jcodemunch workflow](JCODEMUNCH_WORKFLOW.md) for supported source discovery and connected-code retrieval, then verify live edit contents and refresh the index. Its coverage limits do not justify missing caller/lifecycle checks, and an index result does not replace tests or creative review.

Prefer an adequate existing component/pattern, then suitable platform/standard-library features and installed dependencies. Add a dependency or abstraction when the approved behavior, lifecycle or maintainability justifies it. Compare actual capabilities and total implementation burden; a clever one-liner or a hand-built replacement for a useful library can be harder to maintain.

Use shared fixes for shared causes, preserve the project's working interfaces and finish the affected integration. Avoid speculative configuration, unused extension points and unrelated rewrites. Keep code readable. Reuse implementation where it fits without inheriting presentation the client intended to replace.

For motion, verify event/observer/timeline ownership, teardown, repeated mounts, interruption and stale state across resize or route changes. Preserve content access, keyboard/touch paths and the actual reduced-motion state. For data-backed work, preserve validation, error handling, authorization and data integrity where relevant.

Choose meaningful checks proportional to the change. Risky state/branch/parser/data logic and defect fixes need a focused regression or reproducible self-check; use existing test patterns. Rendered motion and input behavior need runtime observation. Trivial documentation/style edits do not need tests that repeat their wording. Do not replace a needed observation with a source assertion.

If a shortcut has a material limitation, record that limit and when it needs revisiting in the existing treatment/iteration record or a useful code comment. A comment does not waive an acceptance criterion. No special comment prefix, line-count target or savings percentage is required.

## Review the connected behavior

Read the diff and surrounding execution path, including callers, cleanup and tests. Review in this order: correct behavior and creative-contract fidelity; safety/data integrity/accessibility; expected load and lifecycle; meaningful verification; performance under stated conditions; avoidable complexity/dependencies. Keep artistic critique alongside this review rather than treating minimal code as evidence of good art direction.

For each material finding provide its location, a concrete triggering situation, the resulting problem, the smallest sufficient correction and the consequence of leaving it unresolved. Verify the caller/input/state exists. Label an untested concern as a hypothesis with a next check; do not report speculative defects or invented performance measurements.

Distinguish blocking failures, worthwhile corrections and optional polish. Fix in-scope defects and continue authorized sprints; escalate changed intent, architecture, scope or configuration through the existing workflow. A review request alone authorizes a report, not unrelated code changes, deletion or publication. A whole-repository audit needs its own relevant scope.

Report the outcome, actual checks and material remaining limits concisely. Preserve the client's approved experience when proposing a leaner implementation.

## Integration boundary

This package supplies the guidance locally; no external Ponytail installation is required. Its attribution/version does not prove an upstream skill, plugin or hook is active. The full upstream plugin has separate modes, hooks and host-specific UI/metrics; adding this reference does not install or enable them. If the client independently uses that plugin, inspect its actual active behavior and resolve conflicts against the approved requirements without silently changing its mode or host configuration.
