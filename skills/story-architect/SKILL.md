---
name: story-architect
description: Converts fictional world ideas into classified lore files with canon-safe enrichment, and keeps each world's own rules in that world's repo. Use when a creator describes new lore, organizes or expands a world, or asks to remember how that world should be written.
---

# Story Architect

## Summary

- Turn each idea into one markdown file per concept.
- Classify, name, and place the file from the schema and category guide.
- Keep established canon. Fill only missing metadata when new canon arrives.
- Read this world's `AGENTS.md` before writing. If it is silent, use these defaults and continue.
- Store standing preferences in that repo's `agent/` folder.

## Core Workflow

When the creator describes a world idea:

1. Read root `AGENTS.md` and the `agent/` files it lists. If they are absent, use skill defaults.
2. Understand what the idea represents.
3. Run a canon check against related entries. If `agent/canon-safety.md` exists, follow it.
4. Classify the concept with the built-in categories, then any category registered in `agent/categories.md`.
5. Decide whether one file or several files are needed.
6. Ask one minimal question only when classification or a required field is unclear.
7. Generate the file or files from the schema and templates. Set `time_era` and `time_span` on every entry. Reuse an era label the repo already uses when one fits.
8. Enrich existing files when new canon fills missing metadata.
9. When the creator asks to remember a way of working, write it under `agent/` and index it from `AGENTS.md`.

World-kit behavior: [references/world-kit.md](references/world-kit.md).

## Non-Negotiable Rules

### Scope Rule

Write lore and house rules into the world repository. Register a new category only when the creator wants that kind of entry. Take facts, era lists, and external IDs from the creator or from existing entries. Keep this world's preferences out of this skill.

### World Kit Rule

Recorded preferences win over skill defaults. A missing preference does not block the task. Standing preferences are written into the repo, not left in chat. See [references/world-kit.md](references/world-kit.md).

### Classification Rule

Infer the category when the creator does not name one. Use [references/categories.md](references/categories.md), then categories registered for this world.

### Multi-Concept Rule

When one prompt describes several concepts, create one file per concept.

### Gap Question Rule

Ask only a minimal, targeted question when classification or a required field is unclear.

### Canon Check Rule

Run canon checks before creating entries. Report conflicts with canon-safe status framing. See [references/canon-rules.md](references/canon-rules.md).

### Link Rule

Each `related` value matches another entry's `name` exactly. After edits, fix or report names that do not resolve.

### Progressive Enrichment Rule

When the creator supplies new canonical details, fill empty, unknown, or placeholder metadata on existing entries.

- Update only fields that are empty, unknown, or clearly placeholders.
- Keep established canon unless the creator asks for a revision.
- Ask a targeted question when more than one value is plausible.
- Add new values onto `related` and `themes`.

See [references/canon-rules.md](references/canon-rules.md).

## Output Contract

- **Structure:** Use the frontmatter schema in [references/schema.md](references/schema.md).
- **Templates:** Use the category templates in [references/file-templates.md](references/file-templates.md).
- **Naming:** Use lowercase kebab-case from [references/naming-conventions.md](references/naming-conventions.md).
- **Placement:** Use the flat folders in [references/hierarchy.md](references/hierarchy.md), plus folders registered in `agent/categories.md`.
- **Status:** Set a canon status from [references/canon-rules.md](references/canon-rules.md).
- **Time:** Set `time_era` and `time_span` on every entry.
- **Definition:** The opening section (Overview, Summary, or Premise) states what the thing is, what it does, and what it is not.

## Reference Index

- **World kit:** how a world sets categories, time, links, and house rules: [references/world-kit.md](references/world-kit.md)
- **Schema:** frontmatter fields and where each one applies: [references/schema.md](references/schema.md)
- **Categories:** built-in types and how to classify a concept: [references/categories.md](references/categories.md)
- **Naming:** kebab-case file names: [references/naming-conventions.md](references/naming-conventions.md)
- **Templates:** category file shapes: [references/file-templates.md](references/file-templates.md)
- **Canon:** status values, conflicts, and safe enrichment: [references/canon-rules.md](references/canon-rules.md)
- **Hierarchy:** flat folders and place nesting: [references/hierarchy.md](references/hierarchy.md)

## When To Use This Skill

- A creator describes a new lore concept, or several at once.
- A creator asks to organize, expand, or keep a fictional world consistent.
- A creator asks the agent to remember how this world should be written from now on.
