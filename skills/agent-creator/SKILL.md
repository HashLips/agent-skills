---
name: agent-creator
description: Authors lean, role-driven agent definitions in Markdown (responsibilities, decision framework, constraints, outputs, completion and handoff, collaboration) for use in any project or product. Use when creating `*-agent.md` files, standardizing a portable agent library, or refactoring ad-hoc prompts so they stay scannable and under a reasonable context budget.
---

# Agent Creator

Use this skill to define role-driven agents for professional software work. An agent is not a voice-only persona: it is a short job spec the model follows—duties, how to decide, what it must not do, what it produces, when it is done, and who receives the work next.

**Portable use:** These definitions are environment-agnostic. They must not assume a specific repository, a `skills/` tree, or hyperlinks to internal docs. Anyone may copy an agent into another repo, IDE, or orchestration product. If the user’s environment provides agent skills (e.g. reusable `SKILL.md` libraries), they may follow those by name when relevant—treat that as optional enrichment, not a dependency.

## Core Workflow

1. Name the file with kebab-case and the `<role>-agent.md` pattern (see [references/naming-and-layout.md](references/naming-and-layout.md)).
2. Fill Identity as one short paragraph (from the template); only `<Agent Name>` and `<profession>` change. Keep the paragraph mostly plain text (see **Readable Markdown** below).
3. Add Role summary (1–2 sentences) if it helps; skip if Identity is already enough.
4. Add responsibilities, decision framework, constraints, outputs, collaboration using tight bullets first (default 1 line each).
5. Add a short **Failure modes and recovery** micro-section: missing/contradictory input, unavailable tool/context, and role conflict/tie-break path (see [references/failure-modes.md](references/failure-modes.md)).
6. Add the required **Completion and handoff** block: definition of done, stop when, hand over to (next role + package), and start rule for the next role (see [references/completion-and-handoff.md](references/completion-and-handoff.md)).
7. Add optional sections only when they add signal (e.g. Escalation), or split out a second file for deep procedures.
8. Run a compression pass: dedupe repeated rules, convert prose to bullets, collapse "why + how + examples" into one rule plus a reference when possible.
9. Run the hard QA gate and fix all failures before final output (see [references/qa-rubric.md](references/qa-rubric.md)).

## Non-Negotiable Rules

- **File name:** `<descriptor>-agent.md` (e.g. `product-manager-agent.md`); see naming reference.
- **Role-driven content:** every agent includes responsibilities, decision framework, constraints, outputs, collaboration, and the **Completion and handoff** section—tone alone is not enough.
- **Failure handling is mandatory:** every agent includes a concise failure/recovery clause for ambiguous inputs, missing dependencies/tools, and ownership conflicts.
- **Definition of done and exit:** every agent must state (1) checkable “done for this role,” (2) when this role stops owning the thread, and (3) the explicit handover to the next role with artefacts and a start condition for that next role. See [references/completion-and-handoff.md](references/completion-and-handoff.md).
- **Identity:** a single paragraph (no hard line breaks in the middle of the Identity copy).
- **Readable Markdown (emphasis):** do not fill bullets with `**bold**` on most words. Prefer plain sentences, headings, and lists; use bold sparingly for a few real distinctions or omit it. If a line is hard to read from emphasis noise, strip the bold and rewrite. This applies to the skill text and to every `*-agent.md` produced.
- **Brevity by default:** use short bullets before paragraphs; avoid repeating the same rule across sections; keep each section to only decision-critical content.
- **Size guardrail:** target roughly 250-500 words per agent file. If it exceeds that, trim, collapse, or split advanced procedures into a separate reference/skill.
- **Reference over repetition:** if details are reusable or procedural, point to a named reference/skill instead of embedding long walkthroughs in the agent file.
- **No repo lock-in:** do not hardcode paths to `skills/`, `../`, or “this repository.” Optional: if the environment exposes named skills, use them by name when they match the task.
- **Agents vs skills:** this skill defines who and how the role decides, plus when the role is done. A *skill* (reusable how-to maintained elsewhere) is separate—reference by name if available; do not merge unless the team explicitly co-locates them.

## Output Contract

- Usable as-is when pasted into a system or instruction block, without a specific codebase.
- A reader can state boundaries, outputs, **and** the stop/handoff contract without re-reading a novel.
- The completion block makes it obvious to another human or **another** agent *what* to pick up, *in what form*, and *only after* what is true.
- Clarity and low token use over exhaustive policy manuals; minimal bold in the file body.
- Most sections are list-first and scannable in under 60 seconds.

## Reference Index

- **Completion, definition of done, stop, and handover (required in every agent):** [references/completion-and-handoff.md](references/completion-and-handoff.md)
- **One-paragraph Identity, layout, and readable-Markdown guidance:** [references/agent-file-template.md](references/agent-file-template.md)
- **Kebab-case and `<role>-agent.md` naming:** [references/naming-and-layout.md](references/naming-and-layout.md)
- **Authoring order, review checklist:** [references/authoring-workflow.md](references/authoring-workflow.md)
- **Hard pass/fail quality gate for each generated agent:** [references/qa-rubric.md](references/qa-rubric.md)
- **Failure-mode micro-section patterns (required):** [references/failure-modes.md](references/failure-modes.md)
- **Compact gold exemplars by role family (engineering/product/compliance):** [references/role-family-exemplars.md](references/role-family-exemplars.md)
- **Role vs persona (short):** [references/role-vs-persona.md](references/role-vs-persona.md)
- **Handoffs without assuming a monorepo:** [references/collaboration-patterns.md](references/collaboration-patterns.md)

## When To Use This Skill

- Creating or trimming role agents (PM, design, security, SRE, etc.).
- Building a portable agent pack for public or multi-repo use.
- Converting a bloated or over-bold “character sheet” into a scannable role spec with an explicit **done** and **next**.
