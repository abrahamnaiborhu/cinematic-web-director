# Ponytail workflow integration — v0.6 candidate

Date: 2026-10-19. Client scope: integrate Ponytail into Cinematic Web Director's implementation/review workflow. This is a local guidance adaptation, not an upstream plugin installation or a claim about its runtime hooks, modes, UI or metrics.

## Source and adaptation

Upstream [Ponytail revision `09c434ab73ca43761c5d8b0c5d341926c2fba710`](https://github.com/DietrichGebert/ponytail/tree/09c434ab73ca43761c5d8b0c5d341926c2fba710) was inspected; its Codex plugin metadata reports `5.3.2`. Core instructions, review instructions, license and metadata were fetched as data and hashed in the local source manifest. No upstream executable or installer was run.

The [engineering reference](../references/PONYTAIL_ENGINEERING.md) adapts complete-change scope, adequate reuse, readable implementation, meaningful checks and connected-code review. Its first constraint is preservation of the approved creative contract. Discovery still develops the client's actual request; implementation economy cannot silently shrink an expressive direction into a minimal static page. The [MIT license and attribution](../third_party/ponytail/NOTICE.md) are distributed with the skill.

## Mechanical verification

The existing integrity regression now checks missing/blank engineering guidance; the explicit archive payload includes it and both third-party notices. The new regression expectations failed before the checker/package changes and pass afterward with the rest of the offline suite. These checks establish resource availability and packaging, not agent behavior or code quality.

## Independent source-review trial

Raw request/material: [request](fixtures/v0.6/engineering-review/request.txt), [synthetic contract](fixtures/v0.6/engineering-review/brief.md), [preview source](fixtures/v0.6/engineering-review/preview.js), [router caller](fixtures/v0.6/engineering-review/router.js), [markup](fixtures/v0.6/engineering-review/index.html).

A fresh actor receives only those raw files and the fixed engineering-candidate skill snapshot. It writes a source-review report in an isolated output folder. It does not receive this document, reviewer criteria or intended findings. No input/source edits, browser execution, installs, external messages or nested agents are permitted. Configuration is inherited without a model override; exact model/reasoning identity remains unverified unless exposed by the host.

Reviewer criteria: Does the actor inspect the caller/lifecycle, ground findings in actual source, propose sufficient corrections, preserve the approved expressive behavior/input/reduced-motion contract and distinguish source reasoning from runtime evidence? A low line count, a heading or an assumed upstream activation does not satisfy those criteria.

Actual outcome: the actor read all five inputs and followed the router's `show()` → `mountPoster()` → disposer/`leave()` path. It found that disposal cancels the animation and removes the button handler but leaves the window resize and media-query change listeners registered. It described the concrete repeated-navigation trigger and proposed removing both listeners with their original callback references. It preserved the existing anticipation/release keyframes, native button and reduced-motion behavior rather than proposing an opacity-only replacement or new dependency.

The report proposed focused lifecycle and interruption checks, clearly marked as unrun, and reserved visual feel, browser/input behavior and performance for actual runtime inspection. Its read-only preflight reviewed all eight categories with a `DEGRADED` result; that inventory did not certify browser availability or creative approval. No implementation was changed by this review.

The coordinator inspected both actual outputs, retained locally at `dist/evaluations/v0.6/engineering-review/{response.md,review-notes.md}`, against the supplied source. The trial supports the narrow observation that this candidate can produce a concrete connected-code finding while preserving the approved motion contract. It has no baseline comparison and cannot establish broad code-review effectiveness, artistic quality, cross-host behavior or any of Ponytail's published cost/code-size benchmark results.

All 45 offline tests pass. Final packaging additionally checks payload/source equality, local Markdown targets and the exact upstream license. The optional Skill Creator validator remains unavailable because its PyYAML dependency is absent; no external-validator pass is claimed. The diagnostic fixture deliberately retains its review defect; it is evaluation input, not a production implementation or example to copy.
