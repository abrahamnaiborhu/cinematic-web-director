# v0.5 development candidate — observed results

Date: 2026-10-16. Status: development candidate, not a public release or a certification of creative quality. This report distinguishes independent discovery outputs, the coordinator's implementation checks, an independent synthetic visitor review and decisions still requiring the client.

## What changed and why

The baseline did **not** reproduce a failure to originate motion ideas: all three directors proposed content-specific movement, alternatives and recommendations before the scripted client supplied any effects. Preserve that behavior. The approved v0.5 additions make the next review more explicit: asset treatment and gaps, newcomer tasks, expected versus observed runtime cases, and a concise decision linked to actual material.

The new [creative-review reference](../references/CREATIVE_REVIEW.md) and [review package](../templates/REVIEW_PACKAGE.md) supplement the existing workflow. No new visual style, effect quota, framework or model fallback is mandated. Existing scoped prototypes, sprint autonomy and model disclosure boundaries remain in force.

## Trial controls and actual materials

Six fresh-context sessions: three using v0.4.1 at commit `1a59610`, three using the candidate snapshot. Each received its corresponding [raw request and fixture](V0_5_PLAN.md#controlled-discovery-trials), the selected skill and an isolated output folder. They received neither the reviewer criteria nor prior conclusions. The coordinator supplied one further reply per case, identical across versions:

- Portfolio: “I’m leaning toward your recommendation. Keep the three case-study routes and contact easy to find. We still only have the supplied illustrations; I don’t have additional process images yet. Please bring me what I need to judge the direction before approving implementation. No prototype coding yet.”
- Landing: “I’m leaning toward your recommendation. Keep the practical details and booking easy to find. We still only have the supplied illustration, not real workshop photos. Please bring me what I need to judge the direction before approving implementation. No prototype coding yet.”
- Product: “I’m leaning toward your recommendation. Keep all four routes easy to find. We still only have the conceptual workflow; real product screenshots can come later. Please bring me what I need to judge the direction before approving implementation. No prototype coding yet.”

Requested configuration was the current inherited host with no override in all sessions. Exact model/version/reasoning identity was not exposed and remains unverified. These are same-host qualitative observations, not verified fixed-model experiments, statistical results or Codex/Claude comparisons. The orchestration prompts were not byte-identical; they imposed the same discussion-only constraints, raw requests and follow-up replies. Tool choices and stochastic variation can affect outcomes; the baseline product director chose image generation while the document-only actors did not.

Candidate snapshot SHA-256: `8c435c16e1965af06630c2cc95600267caecc609bda9d98c3d8557ef5a4c88df`, computed over sorted `(path, file SHA-256)` pairs for its 21 files. Its manifest and immutable copy are retained in the evidence bundle. Later release documentation and packaging additions are distinct from the evaluated instruction snapshot; instruction resources must match that snapshot when the final package is checked.

Actual local outputs: `dist/evaluations/v0.5/{baseline,candidate}/{portfolio,landing,product}/`, including each `response.md`, `response-02.md` and linked review material. The companion evidence ZIP preserves these outputs, inputs, snapshots and observations. It includes local machine paths in preflight/host records; no live client data or credentials were used. Synthetic fixture biographies/services/products must not become public claims.

## Discovery outcomes

| Case | Baseline v0.4.1 | Candidate v0.5 | Evidence scope and limits |
|---|---|---|---|
| Existing portfolio | Editorial collection versus shape investigations; complete artwork carried into detail; preserved case URLs/contact. Follow-up embeds supplied artwork with collection/case/device sketches and navigation storyboard | Editorial collection, comparison table or guided looking; follow-up includes substantive case context, still/moving alternative, asset decisions, explicit newcomer tasks and planned runtime cases | Both are source observations and document sketches. SVG rendering attempts failed. Neither establishes typography/fit, observed motion, human comprehension or live routes |
| New landing page | Welcoming vessel-settle versus crop-to-whole inspection; follow-up prioritizes booking/facts on phones and labels missing service content | Welcoming still life, optional making explanation or practical answers; follow-up develops entry/substantive sketches, asset gaps and planned visitor/runtime checks | Both label the illustration honestly and defer unsupported workshop claims. No trial coded or observed a site; documentation is useful for hierarchy, not completed visual approval |
| Product website | Ownership/timeline/update thread versus responsibility-based reading. Follow-up supplies inspected raster entry/substantive/phone/route-family boards, clearly labeled conceptual | Persistent incident record, evaluation notebook or capability comparison. Follow-up supplies actual-content entry/substantive/device/route sketches, still comparison, asset plan, four newcomer tasks and nine planned runtime cases | Baseline has actual generated visual boards, not browser captures or real product screenshots. Candidate review remains document sketches, explicitly labeled; its visitor/runtime cases are all unrun |

Examples from actual outputs, rather than instruction headings:

- Baseline portfolio: “the complete Field Notes image is visible first”; its frame opens into case context, with direct entry and reduced-motion cuts. The client supplied no such effect.
- Baseline landing: “the vessel makes a small downward movement toward its shadow, comes to rest, and stays still”; facts and booking precede the image on phones.
- Baseline product: the director refined accumulation into reader-controlled emphasis because a conceptual diagram should not imply live product behavior. It corrected a duplicate selected marker in an actual generated board.
- Candidate portfolio: “No newcomer or independent reviewer has attempted them. Predictions about clarity are not observed understanding.” Its planned cases include script failure, direct entry, interruption, Back, touch/keyboard, resizing and reduced motion, all marked “Not run.”
- Candidate landing: it proposes a newcomer attempt to understand the offer/find attendance information while explicitly stating that no such observation has happened.

An independent fresh reviewer assessed all actual trial responses and linked review artifacts, including the selected baseline product boards. Its qualitative comparison found strong subject/factual/proactive motion behavior in both versions and more explicit candidate visitor/runtime planning; it did not observe actual visitor/runtime outcomes in the discovery trials. Full assessment is retained as `dist/evaluations/v0.5/independent-review.md` in the evidence bundle. Small discovery trials can show useful behavior; they do not establish that the candidate is uniformly better, produces distinctive finished sites or follows an entire production sprint. Rendering access remains a practical limitation, rather than a reason to invent visual evidence or approve a build.

## Approved bounded study

The client explicitly approved [Moss Studio study plan revision 1](V0_5_STUDY_PLAN.md). The coordinator implemented [one isolated opening](../studies/v0.5-moss/index.html), adapting the baseline director's vessel-settle idea. This is an implementation of a trial-originated proposal, not an end-to-end site independently delivered by the candidate director.

The study uses the supplied SVG geometry, browser-native animation, local fonts and no installed dependencies. Workshop facts/actions remain available from the first state. The booking action goes to a clearly labeled local placeholder note. Reduced motion/no script show the complete still composition. Review controls compare replay with stillness.

The first actual phone review found that controls after the attendance text left most of the vessel outside the viewport when replaying. One design refinement moved the controls beside the illustration. The browser harness was also corrected to avoid artificial center-scrolling, establish a known keyboard starting point and dispatch the complete Enter key. Failed attempts are preserved; correcting a check is not evidence of a design improvement.

Final local Chrome `155.0.8059.80` checks passed at 360×640, 390×844, 1280×720 and 1440×900 CSS viewports. The 15 recorded cases cover those four views, wall-clock motion, staged storyboard captures, resize interruption, scrolling during movement, reduced motion, dispatched touch input, keyboard order/activation, placeholder navigation, history return, disabled-script navigation and captured console errors.

Evidence: `dist/evaluations/v0.5/study/final-verification/observations.json` plus its PNG captures; source/evidence hashes in `study/evidence-manifest.json`. Wall-clock samples showed changing transforms followed by no running animations. Separate start/change/settled PNGs use paused/seeked animations for inspectable frames; those staged pictures alone are not timing evidence. The coordinator inspected representative opening/moving/fallback captures.

Local navigation timing is recorded under a file URL, with inline SVG/system fonts. It is not a production performance budget, FPS measurement, network-loading test, mobile field result or hardware benchmark. No Safari/Firefox/Edge, physical iPhone/Android, assistive-technology or complete accessibility certification is claimed. The browser checker can be rerun with the instructions in [the study notes](../studies/v0.5-moss/README.md).

## Visitor understanding and decision

An independent fresh synthetic reviewer saw only four actual rendered captures, without source, brief or intended answers. It identified the beginner hand-building offer, two-hour duration, materials, group size and fictional price, and chose “Find a date” as the likely next action. It identified dates/address/real currency/booking/outcomes/access as unresolved. It also noted that the illustrated cup could imply an outcome the copy does not establish.

This is an actual captured synthetic response, not a human usability test or a measured conversion result. It did not click controls or observe animation. Its next content action is to obtain confirmed session outcomes and attendance details rather than infer them from the image. Human newcomer review and the client's aesthetic adopt/revise/reject decision remain open. Approval to run the study is not approval to adopt the design.

## Validation and remaining release criteria

All 45 offline tests pass. The 42-file explicit release payload has no missing local Markdown targets; Python/JavaScript syntax checks pass. All 13 evaluated entrypoint/reference/template/preflight resources match the immutable candidate snapshot. Packaging verifies archive contents, checksum and reproducibility separately from creative quality. The optional external Skill Creator validator fails because PyYAML is unavailable; no external-validator pass is claimed and no dependency was installed to run it.

Completion of the approved evaluation work:

| Criterion | Actual outcome |
|---|---|
| Three baseline and three candidate discovery trials | Complete, each with initial response and identical case-specific scripted follow-up |
| Supported workflow changes | Complete; preserves successful ideation and adds explicit review/asset/visitor/runtime procedures |
| Review-package behavior | Observed in all candidate follow-ups as actual documents; rendered quality remains unestablished in those trials |
| One scoped, approved rendered study | Complete within scope, with one design refinement and 15 passing Chrome cases |
| Visitor evidence | One explicitly synthetic independent response; no human usability claim |
| Offline/package integrity | Pass within the stated scope; optional external validator unavailable |
| Client design adoption, real-device/cross-browser acceptance | Pending; study authorization does not supply these decisions or results |

The development candidate is reviewable without claiming every follow-up criterion is achieved. Before a public quality claim or production use of the study, obtain the client's judgment, relevant human visitor feedback and the agreed platform/browser evidence. Cross-host and fallback-model behavior need their own authorized trials with disclosed actual configuration. This work does not change `abrahamnaiborhu.com` or publish a GitHub release.
