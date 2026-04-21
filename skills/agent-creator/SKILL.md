---
name: agent-creator
description: Authors lean, role-driven agent definitions in Markdown (responsibilities, decision framework, constraints, outputs, completion and handoff, collaboration) for use in any project or product. Use when creating `*-agent.md` files, standardizing a portable agent library, or refactoring ad-hoc prompts so they stay scannable and under a reasonable context budget.
---

# Agent Creator

## Summary

- Build role-driven agent files that are portable and scannable.
- Keep agents concise while preserving operational clarity.
- Require explicit completion and handoff behavior in every agent.

## Core Workflow

1. Name the file in kebab-case using `<role>-agent.md`.
2. Fill Identity as one paragraph from the template.
3. Add role summary only if Identity is not enough.
4. Add responsibilities, decision framework, constraints, outputs, and collaboration.
5. Add required `Failure modes and recovery` micro-section.
6. Add required `Completion and handoff` section.
7. Add optional sections only when they add signal.
8. Run compression pass (dedupe, shorten, reference reusable detail).
9. Run hard QA gate before delivery.
10. Apply final formatting pass using the available **MD Design System** skill.

## Non-Negotiable Rules

- **File name** — Must be `<descriptor>-agent.md`.
- **Required sections** — Responsibilities, decision framework, constraints, failure modes, outputs, collaboration, completion and handoff.
- **Completion contract** — Must include DoD, stop condition, next role + package, and start rule.
- **Identity format** — Single paragraph only.
- **Readable Markdown** — Minimal bold; list-first; no emphasis noise.
- **Brevity target** — Roughly 250-500 words per agent.
- **Portability** — No mandatory repo-local paths.
- **Skill boundary** — Agent defines role behavior; separate skills define reusable procedures.
- **Final formatter** — Before final output, run generated files through the local MD design system formatter.

## Output Contract

- Agent file is usable as-is in system instructions.
- Reader can quickly identify boundaries, outputs, and handoff rules.
- Next role can start from the handoff package without ambiguity.

## Reference Index

- **Completion and handoff requirements:** [references/completion-and-handoff.md](references/completion-and-handoff.md)
- **Agent template and section order:** [references/agent-file-template.md](references/agent-file-template.md)
- **Naming and layout rules:** [references/naming-and-layout.md](references/naming-and-layout.md)
- **Authoring process and review flow:** [references/authoring-workflow.md](references/authoring-workflow.md)
- **Hard pass/fail QA gate:** [references/qa-rubric.md](references/qa-rubric.md)
- **Failure-mode section patterns:** [references/failure-modes.md](references/failure-modes.md)
- **Role-family compact exemplars:** [references/role-family-exemplars.md](references/role-family-exemplars.md)
- **Role vs persona distinction:** [references/role-vs-persona.md](references/role-vs-persona.md)
- **Collaboration patterns:** [references/collaboration-patterns.md](references/collaboration-patterns.md)
- **Final Markdown formatting contract:** available **MD Design System** skill

## When To Use This Skill

- Creating or rewriting role-based agent files.
- Standardizing agent libraries across repos.
- Converting verbose persona prompts into operational role specs.
