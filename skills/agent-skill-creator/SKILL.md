---
name: agent-skill-creator
description: Creates coherent Agent Skills with consistent format, minimal main SKILL.md files, and reference-driven documentation. Use when creating new skills, standardizing existing skills, defining skill structure, or improving skill maintainability and context efficiency.
---

# Agent Skill Creator

## Summary

- Build coherent, reusable Agent Skills with low context cost.
- Keep main `SKILL.md` operational; move depth into references.
- Standardize structure and naming across repository skills.

## Core Goals

- Keep `SKILL.md` concise and action-oriented.
- Store long-form guidance in `references/`.
- Use consistent naming, layout, and discoverability patterns.
- Avoid duplicated guidance across files.

## Authoring Workflow

1. Define skill intent and trigger scenarios.
2. Write frontmatter (`name`, `description`).
3. Draft minimal operational `SKILL.md`.
4. Move depth into references.
5. Add assets only if execution quality materially improves.
6. Run quality checklist before finalizing.
7. Apply final formatting pass using the available **MD Design System** skill.

## Non-Negotiable Rules

- Frontmatter is required.
- `name` is lowercase kebab-case.
- `description` states what the skill does and when to use it.
- `description` pattern: `<what it does>. Use when <trigger scenarios>.`
- Reference links are one-level deep and description-first.
- Do not duplicate large guidance across main and reference files.
- Before delivery, format produced Markdown with the local MD design system skill.

## Reference Index

- **Authoring model and structure strategy:** [references/blueprint.md](references/blueprint.md)
- **Default file layout and naming:** [references/file-layout.md](references/file-layout.md)
- **Final quality gate checklist:** [references/quality-checklist.md](references/quality-checklist.md)
- **Final Markdown formatting contract:** available **MD Design System** skill

## When To Use This Skill

- Creating a new skill from scratch.
- Refactoring existing skills for consistency.
- Reducing token overhead in skill packages.
- Standardizing team skill authoring patterns.
