# World kit

## Summary

- The skill is generic. A world's preferences live in that repo.
- Read `AGENTS.md` before creating or editing lore. Follow what it records.
- If a preference is absent, use the skill default and continue.
- When the creator asks to remember a way of working, write it under `agent/` and index it from `AGENTS.md`.

## Read order

1. Root `AGENTS.md`, if it exists.
2. Every `agent/` file it lists.
3. Skill defaults in this package for anything still unset.

`agent/` holds instructions, plans, and maps. Lore stays in category folders. Do not store canon entries under `agent/`.

## When to create the kit

Create a thin `AGENTS.md` and the matching `agent/` file when any of these happen:

- the creator asks to remember, always do, or from now on
- the creator names ages, a new category, an external-ID rule, or a limit that must stay open
- the creator asks to start or organize a world repository

A single lore entry does not require the full kit. Use defaults and continue.

## Remember protocol

When the creator states a standing preference:

1. Write or update the matching file under `agent/`.
2. Add or update one line in `AGENTS.md` that points at that file.
3. Apply the preference on the current task.

Do not keep the preference only in chat.

## Defaults until the creator shapes them

- **Start path** — If none exists and they are organizing a world, seed a short human start note plus `agent/orientation.md` (hubs and where to read first). Leave the opening steps stable once people rely on them. Add later reading paths beside them.
- **Categories** — Built-in set in [categories.md](categories.md) and [hierarchy.md](hierarchy.md). A new kind of entry (characters, languages, organizations, plants, vehicles) is registered in `agent/categories.md`, then used as its own folder.
- **Time** — Every entry sets `time_era` and `time_span`. Spans are always `point`, `ongoing`, or `recurring`. Era names come from `agent/timeline.md` when that file exists. If it does not, reuse an era label the repo already uses when one fits; otherwise pick a short honest label and continue. When the creator names their ages, write `agent/timeline.md` as an ordered list. Leave old entries on their current labels unless asked to retag them.
- **Links** — Each `related` value matches another entry's `name` exactly. After edits, fix or report dangling names.
- **External IDs** — Mint an ID only when something must be referenced outside the repo. Store `id → file` in `agent/reference-map.yaml`. The creator chooses the prefix. Never reuse or retarget an ID. If a mapped file moves, update the map in the same change. Paths are relative to the repo root.
- **What to write next** — No phase plan until they ask. Then use `agent/plan.md` (one phase at a time) and `agent/stage-readiness.md` (safe next work, and what must stay open).
- **Canon limits** — Skill conflict framing stays in [canon-rules.md](canon-rules.md). This world's extra limits go in `agent/canon-safety.md`. Read it before enrichment when it exists.
- **Voice** — Lead with a plain definition: what it is, what it does, and what it is not. Unknowns stay labeled.
- **Repeated chores** — If they ask to always rebuild an index, pin a map, or run a check after lore edits, record that command or step in `AGENTS.md`.

## `AGENTS.md` shape

Keep it short. Point at files. Do not copy their full text.

```markdown
# Agent guidance

Lore lives in category folders. Instructions live under `agent/`.

## Before writing lore

1. Read this file.
2. Read the agent files linked below.
3. Follow Story Architect defaults for anything not listed here.

## Recorded preferences

- **`agent/orientation.md`** — where to start reading
- **`agent/categories.md`** — categories added for this world
- **`agent/timeline.md`** — era names, oldest to newest
- **`agent/canon-safety.md`** — limits that stay open
- **`agent/plan.md`** — active phase plan
- **`agent/stage-readiness.md`** — safe next work
- **`agent/reference-map.yaml`** — external ID to lore file
```

Omit lines for files that do not exist yet.

## `agent/categories.md` shape

One section per added category:

- folder name (plural, kebab-case, flat)
- when to classify a concept here
- extra frontmatter fields, if any
- when the world entry lists members of this category, add the new name there. Create a separate index only if the creator asked for one.

## `agent/timeline.md` shape

Ordered era list, oldest to newest. One line each: name and what it means. Spans stay the universal three: `point`, `ongoing`, `recurring`.

## `agent/reference-map.yaml` shape

```yaml
prefix: <PREFIX>-
entries:
  - id: <PREFIX>-<uuid>
    file: artifacts/example-object.md
```

`<PREFIX>` is whatever the creator asks to use. The skill does not ship a prefix. Omit optional notes. The map is a bridge, not a second lore database.
