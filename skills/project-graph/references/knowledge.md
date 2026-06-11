# Living Knowledge

## Summary

- `project-graph.knowledge.json` at the project root is the graph's living memory: AI-authored, merged into the dashboard on every regeneration.
- The static script answers "what connects to what"; the knowledge file answers "what is this, what does it use, how does it behave at runtime".
- It grows incrementally as the user asks questions; the agent records small entries, never bulk-analyzes the whole project.
- Every "Copy & ask AI" prompt in the dashboard instructs the agent to record findings here and regenerate, closing the loop.

## File contract

- Location: `<root>/project-graph.knowledge.json` (same directory as `project-graph.flows.json` and the output HTML).
- Always merge: read the existing file, update only the keys you learned about, write it back. Never wipe or regenerate it wholesale.
- It is a normal project file (commit it if the user wants the knowledge shared with the team).
- Never put secrets, env values, or large code excerpts in it; short prose and structured steps only.

## Schema

```json
{
  "updated": "2026-06-11",
  "overview": "2-4 sentence project summary.",
  "technologies": [
    { "name": "Next.js", "role": "web framework", "detail": "App router, server components." }
  ],
  "services": [
    { "name": "Supabase", "role": "database + auth", "detail": "Postgres via @supabase/supabase-js." }
  ],
  "flows": {
    "Send OTP": {
      "insight": "2-4 sentences on what this flow does and how.",
      "diagram": {
        "steps": [
          { "id": "s1", "label": "User submits phone number", "kind": "start", "file": "src/app/login/page.tsx" },
          { "id": "s2", "label": "Valid number?", "kind": "decision" },
          { "id": "s3", "label": "Send OTP via provider", "kind": "external" },
          { "id": "s4", "label": "Show error", "kind": "end" }
        ],
        "edges": [
          { "from": "s1", "to": "s2" },
          { "from": "s2", "to": "s3", "label": "yes" },
          { "from": "s2", "to": "s4", "label": "no" }
        ]
      }
    }
  },
  "files": { "src/lib/otp.ts": "1-3 sentence note about the file's real role." },
  "notes": [
    { "topic": "Rendering pipeline", "body": "Free-form insight uncovered while answering a user question." }
  ]
}
```

Field rules (the generator validates leniently and drops what it cannot use):

- **flows keys** — match by flow name (as shown in the dashboard), slug, or `flow:` id; unmatched keys are reported as warnings, not errors.
- **diagram.steps** — 2-40 steps; `kind` is one of `start`, `action`, `decision`, `io`, `external`, `end` (anything else becomes `action`); `file` is optional and makes the step clickable when it matches a project file.
- **diagram.edges** — `from`/`to` must reference step ids; `label` optional (use for decision branches like yes/no). Steps without edges render as a simple chain.
- **files keys** — project-relative paths; notes pointing at deleted files are dropped and warned about.
- Long strings are truncated by the generator (overview/insight ~2000 chars, labels ~140), so keep entries short by design.

## Growth protocol

Follow this whenever the user asks about the mapped project (a flow, a file, "what tech does this use", "how does X work"):

1. Answer the question by investigating only what is needed (see context budget below).
2. Distill the durable part of the answer into the smallest knowledge entry that captures it: a flow insight, a diagram, a file note, a technology/service entry, or a topic note.
3. Merge it into `project-graph.knowledge.json` (create the file on first use).
4. Set `updated` to today's date.
5. Re-run the generator and verify as usual; the `PROJECT_GRAPH_RESULT` line reports knowledge counts (`technologies`, `services`, `flow_insights`, `flow_diagrams`, `file_notes`, `notes`).
6. Mention to the user that the dashboard now includes what was uncovered.

First generation on a project is intentionally basic: generate the graph, then offer to populate the overview, technologies, and services (the dashboard's Insights tab has a "Copy & ask AI to analyze" prompt for exactly this).

## Context budget

Knowledge must grow without ever requiring a whole-project read:

- Investigate top-down: manifests (`package.json`, `pyproject.toml`, lock-file names) and config files answer most technology/service questions alone.
- For a flow, read the entry point first, then only the step-1/step-2 files needed to trace the runtime path; the flow's member list in the dashboard prompt already tells you which files matter.
- Prefer the graph's own data (connections, flows, summaries) over re-reading files the graph already describes.
- Write summaries, not transcripts: every entry should be readable in seconds and cost little to re-load next session.
- Never paste file contents into the knowledge file; reference paths instead.
- One question, one or two entries. Do not opportunistically analyze unrelated areas.

## Diagram authoring

- Describe runtime behavior (what happens when the flow runs), not the import tree - the dashboard already shows imports.
- 5-15 steps is the sweet spot; one `start`, one or more `end`s, `decision` steps should branch with labeled edges.
- Use `io` for reads/writes (DB, filesystem, network payloads) and `external` for third-party services.
- Attach `file` to steps where the behavior lives so users can click through.
- The dashboard renders the diagram with a built-in layered SVG layout; no mermaid or external libraries are involved.

## Diagram refresh

Diagrams can go stale when code changes. Two ways to keep them current:

**Dashboard (on demand)** — when a flow already has a diagram, the flow detail view shows an "Update diagram" button. It copies a prompt that includes the current insight and diagram JSON and asks the agent to re-verify against the entry point; update only if behavior changed.

**On regeneration (automatic skill step)** — whenever the skill regenerates the graph and `flow_diagrams` > 0 in the result, before telling the user it is done:

1. Read `project-graph.knowledge.json` and list flows that have a `diagram`.
2. For each (context-cheap, one flow at a time): read the flow's entry point, then only files referenced in diagram steps (skip if a referenced file no longer exists - treat as stale).
3. Compare runtime behavior to the stored diagram. If still accurate, leave it. If steps, branches, labels, or file refs are wrong, merge an updated `insight` and/or `diagram` and set `updated`.
4. If any flow entry changed, re-run the generator once and verify again.

Skip the automatic refresh when the user explicitly asked for a fast/no-AI regeneration, or when there are many diagrams (>5) unless the user asked to refresh them - in that case offer to spot-check instead of doing all silently.
