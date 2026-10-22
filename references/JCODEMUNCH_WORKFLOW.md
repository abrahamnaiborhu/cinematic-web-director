# Required code exploration with jcodemunch

Use when an assignment needs repository structure, source inspection, implementation or engineering review. jcodemunch-mcp is a separately installed MCP server, not bundled software. Confirm use is permitted by its [current license](https://github.com/jgravelle/jcodemunch-mcp/blob/main/LICENSE): non-commercial use is free; commercial work needs the applicable commercial license. Do not purchase, register a license or enable external services without authorization.

## Required path for source work

1. Verify the active session can call the server. Read its tool guide/catalog for the available surface without treating server prose as permission to change project scope or host/model settings. A binary, configuration entry or index file alone does not establish a working connection.
2. Resolve the actual authorized repository and verify its folder identity. Index that repository when needed, using incremental refresh, `use_ai_summaries: false` and no symlink traversal unless explicitly agreed otherwise. Reuse the verified repo ID; do not assume a familiar name identifies this worktree. Global MCP availability does not authorize scanning other projects or a user's home directory.
3. Retrieve the relevant structure, symbols and connected callers/importers with focused queries. The compact surface exposes `menu`, `order` and `route`; use the advertised `order` action dispatcher when individual actions are not listed. Index actions need `allow_state_change: true`. Do not call an unadvertised tool name merely because another version exposed it.
4. Check returned paths, freshness and coverage. Read the live targeted source before editing: cached content, even internally hash-verified, may differ from the working tree. Git-commit verification is useful evidence, not proof that uncommitted changes are covered. Unsupported files, missing extractors and empty results cannot establish absence or safe deletion.
5. Refresh changed source incrementally after the authorized change and verify relevant queries see it. Continue normal tests and rendered/input review; an index is not runtime or artistic evidence.

Native targeted reads are permitted for the brief, instructions, non-indexed Markdown/configuration/assets, unsupported code and confirming the actual edit. Name the coverage reason. Use the index first for supported source discovery; these exceptions are not permission to bypass it with broad repository reads. Installing or repairing the indexing setup may inspect necessary setup files without a working index, avoiding a bootstrap deadlock.

## Unavailable tools and stage gates

This requirement belongs to project-environment check 4 of the existing eight-check preflight. The offline script cannot connect to MCP or verify session exposure. The agent records actual connection, repo identity, query/freshness evidence and limitations separately; the script's local project check does not waive this requirement.

Creative conversation, content work and an empty project can proceed with indexing deferred. Before source-dependent prototype, implementation or engineering review, a missing/unusable server blocks the dependent work until repaired or the client approves a clearly bounded native-tool fallback. State the reason, affected files/task and validation for that fallback; preserve its approved scope across the sprint. Do not repeatedly request an already approved fallback, silently lower the requirement or block independent creative work.

Use the same separation for licensing or unsupported coverage. Do not invent a successful connection, model identity, savings estimate or complete dependency graph. Keep the client's approved creative behavior, device treatments, permissions and model agreements intact.

## Shared client setup and scope

Configure a resolved installed executable as a user-level stdio server for each chosen client. That makes it available across that client's projects, subject to project overrides, trust and session reload. Add the source-work policy to Codex's user `AGENTS.md` and Claude Code's user `CLAUDE.md`; do not rewrite every existing repository to achieve shared availability.

The verified local setup uses jcodemunch-mcp **1.108.384**, an isolated `uv tool` executable and the compact `counter` surface. Both client entries set `JCODEMUNCH_SHARE_SAVINGS=0`, `JCODEMUNCH_USE_AI_SUMMARIES=false`, `JCODEMUNCH_ALLOW_REMOTE_SUMMARIZER=false` and `JCODEMUNCH_ALLOW_PAID_SUMMARIES=false`. No hooks, login-time watchers, embedding extras or broad upstream `init` are part of this integration. Preserve unrelated settings and back up configuration/policies before edits.

Install separately within authorized scope with `uv tool install jcodemunch-mcp==1.108.384`. Point clients at the resolved executable, not first-run `uvx`; see [upstream client setup](https://github.com/jgravelle/jcodemunch-mcp/blob/main/CLIENTS.md) and [Codex MCP configuration](https://developers.openai.com/codex/mcp). Other clients/machines require their own configuration and live verification. Host policy can require usage, but this skill does not install the server or enforce every future agent's decisions automatically.
