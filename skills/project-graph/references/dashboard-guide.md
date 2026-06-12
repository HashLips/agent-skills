# Dashboard Guide

## Summary

- The output is a six-tab, dark-themed dashboard plus a detail drawer and global search.
- Files are nodes; import/include/link relationships are edges; flows group reachable files.
- Everything is clickable: files open the drawer, flows open the flow view.
- The layout is responsive; all tabs work in narrow windows.

## Tabs

- **Explorer** — card grid of all files with category pills, text filter, and sorting (name, most connected, most lines, largest). The default landing view.
- **Flows** — flow list on the left; selecting a flow shows its files grouped by step depth (entry point, then each import layer). If the knowledge file has an entry for the flow, an "AI insight" paragraph appears and a "Flow diagram" button toggles the AI-authored runtime diagram (layered SVG; decision diamonds, labeled branches, steps clickable when tied to a file). One primary copy button: "Copy & explain" when the flow is undocumented (prompt asks for both insight and diagram); "Copy & update" when both already exist (prompt includes the stored insight and diagram JSON and asks the agent to verify and refresh only if stale). "Highlight in graph" isolates the flow in the Graph tab.
- **Folders** — collapsible directory tree mirroring the repository, with file counts and cumulative sizes per folder.
- **Graph** — static mind-map: files clustered by top-level folder with connection lines. Pan by dragging, zoom by scrolling, click a node for details. No physics simulation, so it stays fast on large projects. Rail filters: categories, flow focus, label and edge toggles.
- **Insights** — stat cards (files, connections, flows, languages, lines, size, source tested %, code documented %) plus panels: a single **Project analysis** AI card with one "Copy & explain" (or "Copy & update" when already analyzed) that bootstraps overview, technologies, and services into the knowledge file; separate Technologies and Services panels appear below only after the agent records them. Also AI topic notes, files by category and language, testing (test reach, documentation, flow coverage, most connected untested files), lines of code by folder, most connected files, largest files, risk hotspots (large and highly connected), top flows, unconnected source files, external packages, and an **About** panel (generation date, knowledge entry count, regenerate command). An AI overview banner appears above the stat cards when the knowledge file has one.
- **Config** — last tab; dashboard preferences saved in the browser: **Go to file** editor scheme (`vscode`, `cursor`, `vscodium`, `wsl`) and **project root** override for path resolution. Extensible home for future dashboard settings.

## File drawer

Clicking any file (in any tab) opens a drawer showing:

- category, language, size, line count, in/out connection counts,
- the file's leading comment or docstring as a summary,
- the AI note from the knowledge file, when one exists,
- flows the file participates in (clickable chips),
- "Imports / references" (outgoing) and "Used by" (incoming) file lists,
- external packages the file imports,
- "Copy & explain" (or "Copy & update" when an AI note already exists), "Go to file" (opens the file in your IDE via `vscode://file/…`, `cursor://file/…`, etc.; scheme is auto-detected from the host IDE at generation time and in the browser when opened inside an IDE preview, with manual override in the **Config** tab), and "Locate in graph" actions.

## Copy prompts

- Bright buttons on the flow detail view, file drawer, and Insights tab copy a short, self-contained prompt to the clipboard for pasting into an AI chat.
- Label is **Copy & explain** when nothing is stored yet; **Copy & update** when the target already has knowledge (flow: insight + diagram; file: note; Insights: overview/technologies/services).
- Flow prompts always ask for a 2-4 sentence insight and a runtime diagram (steps + edges). Update prompts include the stored insight and diagram JSON and ask the agent to verify against current code; change only if stale.
- File prompts include the path, category, language, line count, direct imports, dependents, flows, and any existing AI note, then ask for an explanation or a verification pass.
- Insights bootstrap prompts carry the knowledge-file schema inline so the agent can author entries without reading the skill first.
- Every prompt mentions that `project-graph.html` exists and instructs the agent to record what it learned in `project-graph.knowledge.json` (merge, never wipe) and regenerate - this is how the dashboard grows with use.
- Copying works from `file://` pages via a clipboard fallback; the button shows "Copied! Paste it in your AI chat" for five seconds before reverting.

## Node semantics

- **Categories** — `source`, `component`, `style`, `config`, `test`, `docs`, `data`, `asset`, `script`, `other`; each has a fixed color used consistently across tabs.
- **Node size (graph)** — scales with connection count, so hubs stand out.
- **Edge kinds** — `import`, `re-export`, `require`, `dynamic import`, `style import`, `include`, `link`, `doc link`, `source`, `mod`, `use`.

## Reading the output

1. Start in Explorer sorted by "Most connected" to find the project's hubs.
2. Open Flows to see what the project does (routes, APIs, custom business flows).
3. Use Graph with a flow focus to show only the files behind one feature.
4. Check Insights for test reach, risk hotspots, unconnected source files (possible dead code), and the external dependency surface.

## Metric caveats

- **Source tested %** — counts source/component files imported directly by a test file; indirect coverage through helpers is not counted, so real coverage may be higher.
- **Code documented %** — counts code files whose first lines are a comment or docstring.
- **Risk hotspots** — ranked by lines multiplied by connection count; large hubs where changes ripple furthest.
- **Unconnected source files** — may be loaded dynamically (CLI args, reflection, string-built paths) rather than dead.
