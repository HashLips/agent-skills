# Self-Healing

## Summary

- The generator reports its own health; the skill verifies and recovers without reading the generated HTML.
- One machine-readable line plus the exit code is the whole verification contract.
- Recovery is ordered: cheapest fix first, patching the script last.

## Verification contract

Every run ends with one line:

```text
PROJECT_GRAPH_RESULT {"ok": true, "stage": "verified", "generator_script": "/path/to/skill/scripts/generate-graph.py", "output": "...", "files": 369, "connections": 1007, "flows": 7, "external_packages": 31, "html_kb": 281, "knowledge": {"present": true, "file_on_disk": true, "total_entries": 12, "technologies": 6, "services": 3, "flow_insights": 2, "flow_diagrams": 1, "file_notes": 4, "notes": 1}, "warning_count": 0, "warnings": []}
```

- **ok** — `true` only when generation and all self-checks passed.
- **generator_script** — absolute path to `generate-graph.py` that ran; reuse for the next regeneration on this machine (see [portability.md](portability.md)).
- **stage** — where the run ended: `verified`, `verification`, `generation`, or `arguments`.
- **files / connections / flows** — headline counts to sanity-check against the project.
- **knowledge** — merge status from `project-graph.knowledge.json`:
  - `file_on_disk` — whether the knowledge file exists at the project root.
  - `present` — whether it parsed and merged successfully.
  - `total_entries` — sum of overview + technologies + services + file notes + topic notes + documented flows; **must increase when you add a new entry** (or stay stable when you only corrected an existing one).
  - Per-type counts: `technologies`, `services`, `flow_insights`, `flow_diagrams`, `file_notes`, `notes`.
  After any knowledge change, confirm `present` true and the relevant count moved before telling the user the dashboard updated.
- **warnings** — up to 8 per-file parse problems (the file became a bare node; the run still succeeded). Knowledge problems (unparseable file, flow keys matching no flow, notes on deleted files) also land here as soft warnings - fix the knowledge file keys rather than treating the run as failed.
- **problems** — present only on verification failure (unreplaced placeholder, truncated HTML, zero files, size mismatch).

Exit codes:

- **0** — generated and verified.
- **1** — bad arguments (root is not a directory).
- **2** — generation crashed; `error` holds the exception, nothing was trusted as written.
- **3** — HTML was written but failed self-verification; `problems` lists why.

## Verification rules for the skill

1. Check the exit code, then parse the `PROJECT_GRAPH_RESULT` line.
2. Never read the generated HTML wholesale; it can be megabytes. At most grep it for a specific marker when debugging.
3. Treat suspicious-but-ok results as soft failures worth investigating: `files` near zero on a real project, `connections` of 0 on a source-heavy project, or a large `warning_count`.

## Recovery protocol

Work down this list; re-run and re-verify after each step.

1. **Bad arguments (exit 1)** — fix the root path; remember symlink-only folders resolve to zero files.
2. **Zero files on a real project (exit 3)** — the folder is probably not the project root, or everything is gitignored; point the script at the correct root.
3. **Crash blamed on one path (exit 2)** — re-run with `--exclude "<that path or glob>"` to route around it, then report the exclusion to the user.
4. **Many parse warnings on one file type** — usually an exotic syntax; acceptable as-is (files still appear as nodes), mention it to the user.
5. **Crash inside the script (exit 2, no obvious path)** — read only the function named in the error inside `scripts/generate-graph.py`, apply a minimal defensive fix (guard, try/except, regex tweak), and re-run. Keep the fix generic so the script stays project-agnostic.
6. **Verification problems (exit 3)** — placeholder or truncation problems indicate a template edit went wrong; restore or fix the `TEMPLATE` string near the reported placeholder.
7. **Knowledge file exists but merge failed (exit 3, `problems` mentions knowledge)** — open `project-graph.knowledge.json`, fix invalid JSON or wrong keys, regenerate. Check flow keys match dashboard names; file keys use exact project-relative paths.
8. **Agent wrote knowledge but user sees no change** — almost always skipped step 5 (regenerate) or the browser tab was not reloaded. Re-run the generator, verify `total_entries`, tell the user to reload `project-graph.html`.

## Constraints

- Never "fix" a failure by disabling the privacy rules (dotfile exclusion, gitignore handling).
- Never bypass verification by declaring success without `"ok": true`.
- Script patches must stay generic; do not hardcode the current project's paths into the script.
