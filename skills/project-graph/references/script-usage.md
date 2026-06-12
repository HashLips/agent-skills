# Script Usage

## Summary

- `scripts/generate-graph.py` scans a project, builds a file graph, and writes one self-contained HTML dashboard.
- Implementation is split into `scripts/project_graph/` (see the package layout table in `SKILL.md`); the CLI script is a thin entry point.
- Standard library only; requires Python 3.8+.
- Safe to run on any project: read-only except for the output file.
- The skill never leaves `scripts/project_graph/__pycache__` behind: bytecode writes are disabled at import time and any existing cache is removed when the CLI exits.

## Package modules

Run from the `scripts/` directory (or ensure it is on `PYTHONPATH`) to import internals:

```python
from project_graph.build import build_payload
from project_graph.render import render_html

payload, warnings = build_payload(root, excludes=[])
html = render_html(payload)
```

Useful when an agent needs only part of the pipeline (e.g. rebuild payload after editing `project-graph.knowledge.json` without re-scanning, or inspect flow reachability in a REPL).

## CLI

Run from the skill's `scripts/` directory, or pass the full path to `generate-graph.py` from anywhere:

```bash
python3 "<path-to-skill>/scripts/generate-graph.py" [project_root] [-o OUTPUT] [--exclude GLOB]
```

- **project_root** — directory to scan; defaults to the current directory. Prefer an absolute path when cwd is not the codebase root.
- **-o, --output** — output HTML path; defaults to `<root>/project-graph.html`.
- **--exclude** — extra glob matched against relative paths; repeatable (for example `--exclude "docs/archive/*"`).

Skill install locations and path resolution: [portability.md](portability.md). Each run prints `generator_script` in `PROJECT_GRAPH_RESULT` so agents can reuse the same entry point on that machine.

## Privacy rules

- Dotfiles and dot-folders are never opened, parsed, or included as nodes: `.env` and every `.env.*` variant, `.git/`, `.github/`, `.vscode/`, `.cursor/`, and any other `.`-prefixed path. Secrets never reach the script or the output.
- The single exception is `.gitignore`, which is read only to learn which paths to ignore (fallback mode); it still never becomes a node.
- Gitignored paths are treated as machine-local and stay out of the graph entirely.

## File discovery

1. Preferred: `git ls-files --cached --others --exclude-standard`, which lists tracked plus untracked files while honoring every `.gitignore`.
2. Fallback (non-git folders): manual walk that skips a built-in ignore set (`node_modules`, `dist`, `build`, `.venv`, `__pycache__`, `.next`, `target`, and similar) plus simple root `.gitignore` patterns.
3. Always excluded: every dot-prefixed path (see privacy rules), the output HTML itself, OS junk files, and any `--exclude` globs.
4. Files over 1.5 MB and binary files are listed as nodes but not parsed for connections.
5. A file that fails to parse degrades to a bare node and is reported as a warning; it never aborts the run.

## Connection extraction

- **JavaScript/TypeScript family** (`.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs`, `.vue`, `.svelte`, `.astro`) — `import`, `export ... from`, `require()`, dynamic `import()`.
- **Python** — `import x`, `from x import`, including relative imports.
- **Styles** (`.css`, `.scss`, `.sass`, `.less`) — `@import`, `@use`, `@forward`.
- **HTML** — `src` and `href` attributes pointing at local files.
- **Go** — import blocks resolved by path suffix.
- **Rust** — `mod x;` and `use crate::...`.
- **Java/Kotlin/Scala/C#** — dotted imports resolved by path suffix.
- **C/C++** — `#include "..."`.
- **Ruby/PHP/Shell** — `require_relative`, `include`/`require`, `source`.
- **Markdown** — relative links to other project files.

## Import resolution

- Relative specifiers resolve against the importing file, trying common extensions and `index` / `__init__` / `mod` files.
- `tsconfig.json` / `jsconfig.json` `paths` aliases are honored; `@/`, `~/`, and bare `baseUrl`-style specifiers are tried against `src/` and the root.
- Specifiers that resolve to nothing inside the project are counted as external packages (shown in Insights and per file).

## Knowledge input

- If `<root>/project-graph.knowledge.json` exists (the AI-authored living knowledge file, see [knowledge.md](knowledge.md)), it is validated leniently and merged into the dashboard: overview, technologies, services, flow insights and diagrams, file notes, and topic notes.
- Unparseable knowledge, unmatched flow keys, and notes on deleted files degrade to warnings; they never fail the run.

## Output contract

- One HTML file, no external assets, openable directly from disk. The payload does **not** embed an absolute project path (so the HTML is portable across machines and safe to share). **Go to file** resolves the project root at open time from where `project-graph.html` lives (`file://` parent directory, or the served URL path); override in the **Config** tab (saved in `localStorage` on that machine). **Editor scheme** auto-detects the host IDE when the graph is generated (`CURSOR_*` / `VSCODE_*` environment variables), re-checks in the browser when the page is opened inside an IDE preview, and falls back to `EDITOR_SCHEME` in `constants.py`. Override with `--editor-scheme` or the Config tab.
- Final stdout line: `PROJECT_GRAPH_RESULT {json}` with `ok`, `generator_script`, counts, a `knowledge` summary (entry counts per kind), warnings, and any problems; see [self-healing.md](self-healing.md) for the full contract.
- Exit codes: 0 verified success, 1 bad arguments, 2 generation crashed, 3 failed self-verification.

## Troubleshooting

- **Zero or few connections** — project may use uncommon aliases; check `tsconfig.json` paths or define flows manually so reachability is still visible.
- **Folder yields zero files** — folder may contain only symlinked directories (neither git nor the walker follow them); run against the real target instead.
- **Huge repos** — the graph view caps drawn edges above 4500 and shows connections on selection; everything else stays fast because there is no physics simulation.
