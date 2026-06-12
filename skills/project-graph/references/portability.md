# Portability

## Summary

- The skill maps **any** project root on **any** machine with Python 3.8+.
- The skill install folder and the project being mapped are **independent** — never assume they live in the same repo or path.
- Generated `project-graph.html` does not embed absolute project paths; dashboard **Config** resolves paths per browser.

## Requirements

| Requirement | Notes |
|-------------|--------|
| Python 3.8+ | Stdlib only; no `pip install` |
| Git (optional) | Preferred file discovery via `git ls-files`; non-git folders use a safe directory walk |
| Write access | Only to `<project_root>/project-graph.html` (and optional knowledge/flows files the agent authors) |

Works on macOS, Linux, and Windows. Tested path handling includes `file://` URLs, Windows drive letters, and IDE preview hosts (`vscode-resource` CDN URLs).

## Where the skill can live

The generator is always `scripts/generate-graph.py` inside the skill folder. Common install locations:

| Location | Typical use |
|----------|-------------|
| `<workspace>/.cursor/skills/project-graph/` | Skill vendored into the repo being mapped |
| `~/.cursor/skills/project-graph/` | User-global Cursor skill |
| `~/.claude/skills/project-graph/` | User-global Claude skill |
| Any custom path | Copy the skill folder anywhere |

The mapped project does **not** need a `.cursor` folder. A global install can generate graphs for `/any/path/to/any-repo`.

## Resolving the generator script

When running or re-running, resolve `generate-graph.py` in this order:

1. **`generator_script` in `PROJECT_GRAPH_RESULT`** — reuse the exact path from the last successful run on this machine.
2. **Skill path from the active agent session** — the `project-graph` skill's `scripts/generate-graph.py` (path shown in the skill package the agent loaded).
3. **Workspace vendored skill** — `.cursor/skills/project-graph/scripts/generate-graph.py` under the project root (if present).
4. **User-global installs** — `~/.cursor/skills/project-graph/scripts/generate-graph.py` or `~/.claude/skills/project-graph/scripts/generate-graph.py`.

Then run:

```bash
python3 "<resolved>/generate-graph.py" [project_root]
```

- **`project_root`** — the codebase to map (default: current directory). Use an absolute path when the shell cwd is not the project root.
- **Output** — defaults to `<project_root>/project-graph.html`; override with `-o` if needed.

## What stays machine-local

| Artifact | Scope |
|----------|--------|
| `project-graph.html` | Written to the mapped project; safe to share (no baked-in project root) |
| `project-graph.knowledge.json` | Project artifact; commit if the team should share AI notes |
| `project-graph.flows.json` | Optional project manifest |
| Config tab (`localStorage`) | Per browser: editor scheme, project root override |
| `PROJECT_GRAPH_RESULT.output` | Stdout only; absolute path on the machine that ran the generator |
| `PROJECT_GRAPH_RESULT.generator_script` | Stdout only; path to the script that ran |

## Agent rules

- Never hardcode one developer's home directory or repo name in commands or knowledge entries.
- Never assume the skill only exists at `.cursor/skills/project-graph/` inside the mapped project.
- Always pass an explicit `[project_root]` when the shell cwd might not be the codebase root.
- After knowledge changes, regenerate using a resolved `generate-graph.py` path and verify `PROJECT_GRAPH_RESULT` before telling the user the dashboard updated.

## Sharing the skill publicly

- Ship the skill folder (`SKILL.md`, `references/`, `scripts/`).
- Exclude `scripts/project_graph/__pycache__/` (see `.gitignore` in the skill folder).
- Do not bundle generated `project-graph.html` or project-specific `project-graph.knowledge.json` unless intentional.
