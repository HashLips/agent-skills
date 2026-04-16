---
name: agent-skill-creator
description: Creates coherent Agent Skills with consistent format, minimal main SKILL.md files, and reference-driven documentation. Use when creating new skills, standardizing existing skills, defining skill structure, or improving skill maintainability and context efficiency.
---

# Agent Skill Creator

Create and maintain Agent Skills using a consistent blueprint that prioritizes clarity, discoverability, and low context cost.

This skill standardizes how skills are authored so they remain easy to use, easy to extend, and consistent across the repository.

## Core Goals

- Keep `SKILL.md` focused on operational instructions, not deep theory
- Move detailed knowledge into reference files
- Preserve consistent structure and naming across skills
- Avoid context bloat while keeping guidance complete

## Authoring Workflow

When creating or refactoring a skill, follow this sequence:

1. Define purpose and trigger scenarios
2. Create frontmatter (`name` and `description`)
3. Write a concise main `SKILL.md`
4. Move depth into `references/*`
5. Add assets only when they improve execution quality
6. Run the quality checklist before finalizing

See:

- [references/blueprint.md](references/blueprint.md)
- [references/file-layout.md](references/file-layout.md)
- [references/quality-checklist.md](references/quality-checklist.md)

## Non-Negotiable Rules

- Every skill must include valid frontmatter
- `name` must be lowercase kebab-case
- `description` must always explain both what the skill does and when to use it
- Use this description pattern: `<what it does>. Use when <trigger scenarios>.`
- `SKILL.md` should be concise and action-oriented
- Reference files must be one level deep and directly linked
- Every reference entry in `SKILL.md` must be description-first, then link
- Do not duplicate large guidance across `SKILL.md` and references

## When To Use This Skill

Use this skill when:

- Creating a new agent skill from scratch
- Refactoring an existing skill for consistency
- Reducing token/context overhead in skills
- Building a reusable template for team skill authoring
