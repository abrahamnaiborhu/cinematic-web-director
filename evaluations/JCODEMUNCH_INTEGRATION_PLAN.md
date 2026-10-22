# jcodemunch-mcp integration — local verification record

Client authorization, 2026-10-20: shared setup for **Codex and Claude Code**, for **non-commercial projects only**. Implemented on `feature/jcodemunch-workflow` as a local v0.7.0 candidate. Published v0.6.0 remains unchanged; this work has not been published.

## Installed scope

- Upgraded the existing isolated uv package from 1.108.378 to pinned **1.108.384**. Both clients use the resolved executable directly, following [upstream client guidance](https://github.com/jgravelle/jcodemunch-mcp/blob/main/CLIENTS.md).
- Backed up both clients' user configuration and existing policies before adding the named stdio server and shared source-exploration requirement. Parsed comparisons confirmed unrelated configuration was preserved. Backup locations and detailed machine evidence remain local, outside the distributed payload.
- Disabled aggregate savings sharing, AI summaries, remote summarizers and paid summaries. No hooks, login watchers, embedding extras or broad upstream `init` were enabled.
- Shared configuration makes the server available across projects; it does not index every repository. Index only the current authorized project on use. No bulk project-folder changes were made.

## Verification

Actual MCP SDK stdio initialization exposed six compact-surface tools, including the advertised `order` dispatcher. Indexing and focused source retrieval succeeded for this repository: 12 code files and 235 symbols. The final incremental refresh retrieved `build_release` with current line offsets and source exactly matching the working tree. A separate temporary fixture changed from returning 1 to returning 2; incremental refresh detected one changed file and returned the updated source.

Coverage is incomplete: Markdown is excluded, CSS analysis is limited and some HTML files have no extracted symbols. Targeted native reads remain required for those materials and live edit confirmation. Cached verification alone is insufficient: an earlier retrieval retained old line offsets after a source edit, which the final refresh corrected.

Both client CLIs recognize the user-level registration. Claude Code's connection check reports Connected. Codex reports its entry enabled. This ongoing Codex conversation does not expose jcodemunch tools; new/reloaded sessions must confirm actual tool availability before dependent source work. SDK protocol success and host registration are recorded separately from session exposure.

The skill now routes code preflight, implementation and engineering review through [the required workflow](../references/JCODEMUNCH_WORKFLOW.md). Readiness is an agent responsibility within preflight check 4; the offline checker cannot attest MCP access. Creative work and empty projects can defer indexing. Unavailable source access requires repair or an explicitly approved bounded fallback.

The offline suite passes **45 tests**, including missing/blank required-guidance coverage and package allowlist checks. These tests verify local behavior and packaging, not future agents' compliance or browser/device quality. No independent behavioral trial of the new requirement has been performed.

## Distribution and licensing

The candidate package contains workflow guidance, not upstream server software. The [upstream license](https://github.com/jgravelle/jcodemunch-mcp/blob/main/LICENSE) permits free non-commercial use and requires an applicable license for commercial work. No commercial license was purchased or assumed.

Configuration basis: [official Codex MCP documentation](https://developers.openai.com/codex/mcp) and [upstream client setup](https://github.com/jgravelle/jcodemunch-mcp/blob/main/CLIENTS.md). Other machines need separate installation and connection verification. User policy requires usage; it is not an automatic enforcement hook.
