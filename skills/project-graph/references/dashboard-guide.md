# Dashboard Guide

## Summary

- The output is a five-tab, dark-themed dashboard plus a detail drawer and global search.
- Files are nodes; import/include/link relationships are edges; flows group reachable files.
- Everything is clickable: files open the drawer, flows open the flow view.
- The layout is responsive; all tabs work in narrow windows.

## Tabs

- **Explorer** — card grid of all files with category pills, text filter, and sorting (name, most connected, most lines, largest). The default landing view.
- **Flows** — flow list on the left; selecting a flow shows its files grouped by step depth (entry point, then each import layer). If the knowledge file has an entry for the flow, an "AI insight" paragraph appears and a "Flow diagram" button renders the AI-authored runtime diagram (layered SVG; decision diamonds, labeled branches, steps clickable when tied to a file). When a diagram exists, "Update diagram" copies a prompt that includes the current diagram JSON and asks the agent to verify and refresh it if the code changed. Otherwise an "Ask AI for flow diagram" button copies a prompt instructing the agent to author the diagram into the knowledge file and regenerate. "Copy & ask AI" copies a ready-made prompt about the flow; "Highlight in graph" isolates the flow in the Graph tab.
- **Folders** — collapsible directory tree mirroring the repository, with file counts and cumulative sizes per folder.
- **Graph** — static mind-map: files clustered by top-level folder with connection lines. Pan by dragging, zoom by scrolling, click a node for details. No physics simulation, so it stays fast on large projects. Rail filters: categories, flow focus, label and edge toggles.
- **Insights** — stat cards (files, connections, flows, languages, lines, size, source tested %, code documented %) plus panels: AI-uncovered Technologies and Services (from the knowledge file; when empty they show a "Copy & ask AI to analyze" bootstrap prompt), AI topic notes, files by category and language, testing (test reach, documentation, flow coverage, most connected untested files), lines of code by folder, most connected files, largest files, risk hotspots (large and highly connected), top flows, unconnected source files, and external packages. An AI overview banner appears above the stat cards when the knowledge file has one.

## File drawer

Clicking any file (in any tab) opens a drawer showing:

- category, language, size, line count, in/out connection counts,
- the file's leading comment or docstring as a summary,
- the AI note from the knowledge file, when one exists,
- flows the file participates in (clickable chips),
- "Imports / references" (outgoing) and "Used by" (incoming) file lists,
- external packages the file imports,
- "Copy & ask AI" and "Locate in graph" actions.

## Copy & ask AI

- Bright buttons on the flow detail view and the file drawer copy a short, self-contained prompt to the clipboard for pasting into an AI chat.
- Flow prompts include the flow name, kind, description, entry points, reach (files and layers), key files, and any existing AI insight, then ask for an end-to-end walkthrough.
- File prompts include the path, category, language, line count, direct imports, dependents, flows, and any existing AI note, then ask for an explanation of the file's role.
- Diagram prompts (flow view) and the Insights bootstrap prompt carry the knowledge-file schema inline so the agent can author entries without reading the skill first.
- "Update diagram" prompts include the stored diagram JSON and ask the agent to verify against current code; update only if stale.
- Every prompt mentions that `project-graph.html` exists and instructs the agent to record what it learned in `project-graph.knowledge.json` (merge, never wipe) and regenerate - this is how the dashboard grows with use.
- Copying works from `file://` pages via a clipboard fallback; the button confirms with "Copied!".

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
