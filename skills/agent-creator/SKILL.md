---
name: agent-creator
description: Authors lean, role-driven agent definitions in Markdown (responsibilities, decision framework, constraints, outputs, collaboration) for use in any project or product. Use when creating `*-agent.md` files, standardizing a portable agent library, or refactoring ad-hoc prompts so they stay under a reasonable context budget.
---

# Agent Creator

Use this skill to define **role-driven agents** for professional software work. An agent is **not** a voice-only persona: it is a **short job spec** the model follows—duties, how to decide, what it must not do, what it produces, and how it works with other roles.

**Portable use:** These definitions are **environment-agnostic**. They must **not** assume a specific repository, a `skills/` tree, or hyperlinks to internal docs. Anyone may copy an agent into another repo, IDE, or orchestration product. If the user’s **environment** provides **agent skills** (e.g. reusable `SKILL.md` libraries), they may follow those **by name** when relevant—treat that as **optional** enrichment, not a dependency.

## Core Workflow

1. Name the file with **kebab-case** and the **`<role>-agent.md`** pattern (see [references/naming-and-layout.md](references/naming-and-layout.md)).
2. Fill **Identity** as **one short paragraph** (from the template); only `<Agent Name>` and `<profession>` change.
3. Add **Role summary** (1–2 sentences, optional if Identity is already enough for small agents).
4. Add **responsibilities**, **decision framework**, **constraints**, **outputs**, **collaboration**—enough to be unambiguous, **as brief as** still reviewable.
5. Add **optional** sections only when they save tokens (e.g. a tight Escalation block) or put detail in a **separate** companion doc if the role is huge.
6. Self-check: length, no repo-specific URLs, five pillars present.

## Non-Negotiable Rules

- **File name:** `<descriptor>-agent.md` (e.g. `product-manager-agent.md`); see naming reference.
- **Role-driven content:** every agent includes **responsibilities**, **decision framework**, **constraints**, **outputs**, and **collaboration**—not tone alone.
- **Identity:** a **single paragraph** (no hard line breaks in the middle of the Identity copy).
- **Brevity:** default to **tight** bullets; avoid long prose and duplicate guidance between sections. If a role needs more than ~1–2 “screens” of text, **split** into a second file (e.g. an appendix) or a separate skill—do not stuff everything into one agent.
- **No repo lock-in:** do not hardcode paths to `skills/`, `../`, or “this repository.” Optional line: *if* the environment exposes named skills, use them *when* they match the task.
- **Agents vs skills:** this skill defines *who* and *how the role decides*. A **skill** (e.g. maintained with an agent-skill-creator style workflow elsewhere) is *reusable how-to*—reference **by name** if available; never merge the two unless the team explicitly co-locates them.

## Output Contract

- Usable as-is when pasted into a system or instruction block, **without** a specific codebase.
- Another reader can name **boundaries, outputs, and handoffs** without rereading a novel.
- Prefer **clarity + low token use** over exhaustive policy manuals inside one file.

## Reference Index

- **One-paragraph Identity, compact section layout, size guidance**: [references/agent-file-template.md](references/agent-file-template.md)
- **Kebab-case and `<role>-agent.md` naming**: [references/naming-and-layout.md](references/naming-and-layout.md)
- **Authoring order, brevity review, and checklist**: [references/authoring-workflow.md](references/authoring-workflow.md)
- **Role vs persona (short)**: [references/role-vs-persona.md](references/role-vs-persona.md)
- **Handoffs without assuming a monorepo**: [references/collaboration-patterns.md](references/collaboration-patterns.md)

## When To Use This Skill

- Creating or trimming role agents (PM, design, security, SRE, etc.).
- Building a **portable** agent pack for public or multi-repo use.
- Converting a bloated “character sheet” into a **scannable** role spec.
