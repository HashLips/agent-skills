---
name: project-graph
description: Generates an interactive HTML map of any coding project showing all files, their connections, and entry-point flows, enriched by a living AI knowledge file that grows as the project is explored. Use when asked to generate a project graph, visualize project structure, map file connections or flows, get a high-level overview of a codebase, or answer questions about a project that already has a generated graph (technologies, services, how a flow works).
---

# Project Graph

## Core Rules

- Run `scripts/generate-graph.py` with `python3`; it has no third-party dependencies. The CLI is a thin wrapper over the `scripts/project_graph/` package (discovery, parsing, flows, knowledge, build, render).
- Privacy first: the script never opens or includes dotfiles or dot-folders (`.env*`, `.git/`, `.github/`, `.vscode/`, and so on); the only dotfile it reads is `.gitignore`, and only to learn which paths to ignore. Never weaken this rule.
- The script respects `.gitignore` automatically (via `git ls-files`, with a manual fallback), so `node_modules`, build output, and machine-local files never enter the graph.
- Output is a single self-contained file, `project-graph.html`, written to the project root by default. It does not embed absolute machine paths; **Go to file** resolves the project root from where each user opens the HTML (with an optional per-browser override in the **Config** tab).
- Flows are first-class: routes, API handlers, and entry files are auto-detected; important business flows (for example "send OTP") should be defined in a `project-graph.flows.json` manifest so users can click a flow and see every file it touches.
- The graph is a living artifact: `project-graph.knowledge.json` at the project root holds AI-authored understanding (overview, technologies, services, flow insights and diagrams, file notes) and is merged into every regeneration. **Writing the JSON alone does not update the dashboard** — you must always regenerate `project-graph.html` afterward and verify the merge (see Knowledge update loop below).
- Knowledge grows incrementally and context-cheaply: investigate only what the question needs (manifests first, then entry files), write short summaries, and always merge into the existing knowledge file - never rewrite it wholesale and never bulk-analyze the project.
- When regenerating the graph, if `project-graph.knowledge.json` contains flow diagrams, re-verify each against its entry point (and only files referenced in the diagram) before finishing; update any stale insight or diagram, leave accurate ones unchanged. See [references/knowledge.md](references/knowledge.md) diagram refresh rules.
- Always verify the run via the exit code and the `PROJECT_GRAPH_RESULT` line; never read the generated HTML wholesale to check it.
- Works on any project (API, client app, monorepo, docs repo) on any machine with Python 3.8+; never assume a specific framework, repo layout, or skill install path. See [references/portability.md](references/portability.md).
- The skill install folder and the mapped project are independent — resolve `generate-graph.py` per [references/portability.md](references/portability.md); never hardcode one developer's paths.
- Do not commit `project-graph.html` unless the user asks for it.

## Workflow

1. Identify the project root to map (default: the workspace root).
2. Check for important flows the auto-detection will miss; if the user names flows or the project has clear business flows, author `project-graph.flows.json` at the project root per [references/flows.md](references/flows.md).
3. Resolve and run the generator (see [references/portability.md](references/portability.md)):

```bash
python3 "<path-to-skill>/scripts/generate-graph.py" [project_root]
```

Use `generator_script` from a previous `PROJECT_GRAPH_RESULT` when available; otherwise the skill path from this session, `.cursor/skills/project-graph/` in the workspace, or `~/.cursor/skills/project-graph/`. Pass an explicit `[project_root]` when cwd is not the codebase root.

4. Verify: exit code `0` and `"ok": true` in the final `PROJECT_GRAPH_RESULT` JSON line. Sanity-check the reported file/connection/flow counts against expectations.
5. If the knowledge file has flow diagrams (`flow_diagrams` > 0 in the result), spot-check each diagram against its entry point and referenced step files; merge updates for any that are stale, then re-run once more if you changed the knowledge file.
6. If the run failed, was suspicious, or reported problems, follow the recovery protocol in [references/self-healing.md](references/self-healing.md) until a verified generation succeeds.
7. Tell the user to open `project-graph.html` in a browser and summarize what the graph shows, using [references/dashboard-guide.md](references/dashboard-guide.md) for tab semantics. On a first generation, offer to populate the project's overview, technologies, and services into the knowledge file.
8. From then on, treat the graph as a conversation: each time the user asks about a flow, file, or aspect of the project (often via a dashboard "Copy & explain" prompt), follow the **Knowledge update loop** below — never stop after writing JSON only.

## Knowledge update loop (mandatory)

Use this whenever you add or change anything in `project-graph.knowledge.json` (including "Copy & explain" / "Copy & update" prompts from the dashboard). **Do not mark the task complete until every step passes.**

1. **Answer** — investigate only what the question needs ([references/knowledge.md](references/knowledge.md) context budget).
2. **Merge** — read the existing `project-graph.knowledge.json` (create on first use), update only the keys you learned about, set `"updated"` to today. Never wipe other keys.
3. **Regenerate** — always run the generator immediately after a knowledge change (resolve path per [references/portability.md](references/portability.md)):

```bash
python3 "<path-to-skill>/scripts/generate-graph.py" [project_root]
```

4. **Verify merge** — check exit code `0` and parse `PROJECT_GRAPH_RESULT`:
   - `"ok": true`
   - `knowledge.present` is `true` when the knowledge file exists
   - `knowledge.total_entries` increased (or matches expectations if you only updated an existing entry)
   - the specific count for your entry type increased when adding something new (`file_notes`, `flow_insights`, `technologies`, etc.)
   - no `problems` mentioning the knowledge file
5. **Tell the user** — say what was added and ask them to **reload `project-graph.html` in their browser** (the open tab does not auto-refresh).

If verification fails: fix the knowledge file (invalid JSON, wrong flow key, wrong file path) per [references/knowledge.md](references/knowledge.md) and [references/self-healing.md](references/self-healing.md), then regenerate again. Never assume the dashboard updated without a successful generator run.

## Package layout

`scripts/project_graph/` — stdlib-only modules the skill and agents can import individually:

| Module | Role |
|--------|------|
| `constants.py` | File-type sets, ignore rules, output filenames |
| `discovery.py` | Git-aware file listing (privacy-safe) |
| `categorize.py` | Node category classification |
| `refs.py` | Import/link extraction per language |
| `resolver.py` | Specifier → project path resolution |
| `parsing.py` | Docstring/summary extraction |
| `flows.py` | Auto/manifest flow detection and reachability |
| `knowledge.py` | `project-graph.knowledge.json` load and flow matching |
| `build.py` | Assemble nodes, edges, flows, knowledge payload |
| `render.py` + `template.html` | Self-contained HTML dashboard |
| `verify.py` | Output verification and `PROJECT_GRAPH_RESULT` |
| `cli.py` | Argument parsing and orchestration |

Import example (e.g. to inspect a payload without writing HTML): `from project_graph.build import build_payload`.

## Reference Index

- **CLI flags, privacy rules, file discovery, import resolution, supported languages:** [references/script-usage.md](references/script-usage.md)
- **Flow auto-detection rules and the flows manifest schema:** [references/flows.md](references/flows.md)
- **Living knowledge file: schema, growth protocol, context budget, flow diagram authoring:** [references/knowledge.md](references/knowledge.md)
- **Verification contract, exit codes, and recovery protocol:** [references/self-healing.md](references/self-healing.md)
- **Dashboard tabs, node and edge semantics, reading the output:** [references/dashboard-guide.md](references/dashboard-guide.md)
- **Any machine, any project, skill install locations, path resolution:** [references/portability.md](references/portability.md)

## When To Use This Skill

- Generating a visual map or mind map of a codebase.
- Explaining how files in a project connect to each other.
- Documenting flows (routes, APIs, business processes) and the files behind them.
- Onboarding someone onto an unfamiliar project with a high-level overview.
- Answering questions about a mapped project (technologies, services, how a flow behaves) - record findings in the knowledge file and regenerate so the answer is preserved in the dashboard.
- Authoring a flow diagram for a flow the user selected in the dashboard.
- Verifying or refreshing stale flow diagrams (dashboard "Copy & update" on a documented flow, or automatically on graph regeneration when diagrams exist).
