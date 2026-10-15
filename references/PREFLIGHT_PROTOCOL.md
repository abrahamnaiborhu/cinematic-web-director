# Phase 0 — Preflight Protocol

## Purpose and scope

Clarify what the client wants to build or improve, then inspect readiness for that assignment. Preserve all eight checks. Missing implementation dependencies do not prevent creative discovery. For skill maintenance, inspect the package itself; do not require a separate website project.

The checker is offline and read-only unless `--out` is supplied. It reports local findings and explicitly supplied agent attestations. It cannot inspect live agent tools, switch/identify a model, certify creative approval or perform website QA. The director combines this evidence with actual session observations and the creative gates in `CREATIVE_WORKFLOW.md`.

## Eight checks

| # | Check | Local evidence | Agent responsibility and stage consequence |
|---|---|---|---|
| 1 | AI agent identification | Explicit declaration or tentative environment inference | Confirm the active agent and permissions in-session; declarations/inferences remain UNVERIFIED in the script |
| 2 | Cinematic Web Director Skill | Readable entry point, two references and four templates; basic name metadata | Confirm loaded instructions; an incomplete package blocks every phase |
| 3 | Official GreenSock Skills | Relevant readable skill files in configured roots | Confirm active access and read relevant resources; missing required topics block GSAP prototype/production unless scoped access evidence or an approved docs fallback is supplied |
| 4 | Project environment | Individual manifests or a static `index.html`; selected application root | Confirm real sources, architecture and unusual layouts; ambiguity blocks coding until a source is selected |
| 5 | Project script | Readable nonempty script/brief, including an explicitly supplied path | Read facts, readiness, approval versions and scope; missing brief is normal in discovery and blocks coding; file presence never proves approval |
| 6 | GSAP runtime | Valid GSAP package metadata for the declaring application, including project-local hoisting | Verify real imports/CDN and required plugins; a declaration alone is UNVERIFIED; missing runtime blocks GSAP coding unless actual scoped runtime observation is supplied |
| 7 | Browser and visual testing | Potential tools; supplied PNG structure and dimensions | Perform real rendered QA; release requires distinct desktop/mobile capture widths plus explicit attestation that navigation, relevant motion/interactions and accessibility alternatives were checked |
| 8 | Optional creative tools | Declared optional libraries and executable locations | Select and verify tools only where the approved treatment needs them; absence does not block or degrade readiness |

The inventory keeps application dependencies separate. It does not assume that a sibling app's GSAP installation, framework or state library belongs to the selected website. Relevant framework guidance is inferred from the selected manifest, not proof that the app runs.

## Status and gate meanings

- **VERIFIED:** the stated local evidence was inspected, within its `evidence_scope`. It does not certify runtime behavior, source authenticity or agent activation.
- **UNVERIFIED:** an inference, declaration, potential tool or agent attestation is recorded; the checker cannot independently establish the broader capability.
- **MISSING:** evidence was not found in the inspected locations; this is not a claim about the whole computer or session.
- **DEFERRED:** this item is not needed for the current declared scope. Deferred items are not caveats.
- **BLOCKED:** a stage-critical technical requirement lacks acceptable evidence.
- **DEGRADED:** no technical blockers, but caveats remain. This is a normal result for declarations and agent attestations.
- **READY:** all applicable checks have locally verified evidence with no caveats. This is a technical scope assessment, not creative or release approval.

Every result records its evidence scope. Explicit agent identity is a declaration; environment detection is an inference. Scoped observations preserve `local_status`, remain UNVERIFIED and can satisfy a technical requirement without pretending that local files were found. The report always includes `creative_approval_verified: false` because the director must establish those approvals separately.

Exit code `0` means technically not blocked, possibly DEGRADED. Exit code `2` means BLOCKED or invalid input. **8/8 reviewed is inspection coverage, never eight passed installations.**

## Phases and invocation

From the skill directory:

```bash
python3 scripts/preflight.py --project /path/to/site --agent codex --phase discovery
python3 scripts/preflight.py --project /path/to/site --agent cursor --phase prototype
python3 scripts/preflight.py --project /path/to/site --agent claude-code --phase implementation
```

- `discovery`: review all checks; missing brief/runtime/skills/source does not block creative planning.
- `prototype`: require the relevant technical prerequisites and a readable brief; the director separately confirms explicit approval of the bounded experiment.
- `implementation`: require prerequisites for the approved sprint batch; the director separately verifies content, treatment, architecture and plan approvals.
- `release`: include implementation requirements and visual evidence; the director assesses the full result and any publication authorization separately.

The default scope requires GSAP. Use `--gsap not-required` only when the approved batch does not use it (for example, static composition or backend work). Checks 3 and 6 remain reviewed and DEFERRED. Do not use this flag to hide a missing dependency for planned GSAP work.

Core and performance skills form the GSAP baseline. The selected React/Next.js or Vue/Svelte family adds its relevant framework skill. Add topics needed by the treatment:

```bash
python3 scripts/preflight.py --project /path/to/site --agent codex --phase implementation --gsap-skill gsap-timeline --gsap-skill gsap-scrolltrigger
```

Use `--gsap-skill gsap-plugins` for relevant plugin guidance and other known topics as needed. The checker does not load or verify plugin imports; the agent must test them in the target runtime.

## Explicit paths and portability

```bash
python3 scripts/preflight.py --project /path/to/repo --source-root apps/showcase --script materials/client-brief.md --skill-root /path/to/shared/skills --agent other --phase implementation
```

`--source-root`, `--script` and repeatable `--skill-root` may be absolute or relative to the project. The source must be inside the project. `--source-root` identifies an unusual layout or disambiguates multiple applications. `--script` locates an existing equivalent brief instead of requiring a duplicate document.

Conventional Claude Code, Cursor, Codex and shared `.agents/skills` locations are inspected. Codex honors `CODEX_HOME`; explicit skill roots support other compatible agents and unusual installs. Claude's known GSAP plugin inventory paths are also inspected. These searches are bounded, not an exhaustive agent registry. Ancestor-repository roots, remote resources and other plugin layouts may need explicit paths or actual session evidence. A file on disk cannot prove that an agent loaded it.

Prefer installed [official GreenSock skills](https://github.com/greensock/gsap-skills). If installation is needed, propose it within the authorized environment/sprint scope:

```bash
npx skills add https://github.com/greensock/gsap-skills --agent codex
```

Do not execute an install merely to inspect readiness. Existing plan authorization need not be requested again. If official skills are inaccessible, an explicitly approved current-official-documentation fallback can be recorded and passed as `--allow-gsap-docs-fallback`. This waives only the skill-file blocker, not runtime or creative requirements.

## Scoped agent observations

For capabilities visible only in the active session, supply an existing JSON record with `--observations /path/to/observations.json`. Create such a record only after doing the stated checks; the preflight itself does not write it. Example structure (illustrative, not evidence):

```json
{
  "project_root": "/absolute/path/to/repo",
  "source_root": "/absolute/path/to/repo/apps/showcase",
  "phase": "implementation",
  "checks": {
    "3": "The active agent read the required official GSAP resources exposed by its session; record their actual identifiers here.",
    "6": "The agent observed successful GSAP and required plugin imports in the target runtime; record URL, conditions and evidence here."
  }
}
```

Only checks 3 (skill access), 4 (unusual source layout) and 6 (runtime access) accept observation text. Each requires nonempty evidence identifying what was actually observed. Check 4 cannot disambiguate multiple apps without `--source-root`. Observations cannot override missing package resources, a missing brief or visual-release requirements.

The CLI binds the record to the resolved project, selected source and phase. For the project root itself, `source_root` may be omitted. Re-observe after relevant source, runtime or environment changes; binding does not prove freshness or truth. The report labels accepted observations as agent attestations, keeps their local status and remains DEGRADED. Never copy sample text as if it were an observation.

## Release evidence

```bash
python3 scripts/preflight.py --project /path/to/site --agent codex --phase release --desktop-screenshot ./qa/desktop.png --mobile-screenshot ./qa/mobile.png --interactions-verified
```

Screenshot paths are relative to the command's working directory. Supply non-interlaced 8-bit grayscale/RGB PNGs, optionally with alpha. The standard-library checker verifies bounded chunk integrity, dimensions, compressed scanline length and filter bytes. Other encodings/formats remain unsupported; export appropriate PNG captures using available tools rather than relabeling a file. Limits: 32 MiB compressed file and 128 MiB decompressed scanlines.

Desktop width must exceed mobile width. One file cannot stand for both viewports. Valid PNG data still cannot prove capture provenance, page content, timing, accessibility or correct interactions. Check 7 remains UNVERIFIED with `filesystem+attestation` scope when accepted. Attest only after actual rendered QA at the declared representative widths, including the relevant navigation/motion and input alternatives. Keep detailed observations and conditions in the iteration log.

## Reports and boundaries

Skill integrity includes the creative workflow, design-direction and motion-direction references, preflight protocol and all four project templates. Missing or blank required guidance blocks the package check even during discovery. This establishes resource availability, not design judgment or creative initiative; behavioral scenarios and rendered trials are separate evaluations.

```bash
python3 scripts/preflight.py --project /path/to/site --agent codex --phase discovery --format json
python3 scripts/preflight.py --project /path/to/site --agent codex --phase discovery --format json --out ./preflight.json
```

Only `--out` writes a report. `--observations` reads an existing record. The checker performs no network calls, installs, browser launches, credential access or website changes. It does not arbitrate model suitability or creative decisions. Review the agent's live evidence and approved artifacts before declaring a project ready to build or release.
