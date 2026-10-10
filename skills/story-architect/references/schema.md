# Metadata Schema

## Summary

- Every lore file starts with this frontmatter.
- Templates decide which keys a category includes.
- Extra keys are allowed only when this world registers them.
- Copy the keys that apply. Leave the rest off the file.

---

category:
name:
region:
parent_region:
place_type:
culture:
related:
themes:
status:
time_era:
time_span:

---

## Category source of truth

Built-in category values are defined in [categories.md](categories.md).
This world may add categories in `agent/categories.md`. Those are valid here.

## Field meanings

- **category** — Entry type. Use a built-in category, or one registered in `agent/categories.md`.
- **name** — Official name of the concept.
- **region** — Broader geographical context.
- **parent_region** — Immediate containing place.
- **place_type** — Scale of place when category is region.
- **culture** — Associated society or group.
- **related** — List of related entries. Each value matches another entry's `name` exactly.
- **themes** — Conceptual or symbolic themes.
- **status** — Canon truth level. Allowed values are defined in [canon-rules.md](canon-rules.md).
- **time_era** — Where the entry sits on this world's soft timeline. If `agent/timeline.md` exists, use one of its names. If it does not, reuse an era label the repo already uses when one fits; otherwise use a short honest label. A numbered calendar waits until the creator defines one.
- **time_span** — How the concept sits in time. Always one of:
  - `point` — one event, founding, or singular deed
  - `ongoing` — still true, lived, or practiced
  - `recurring` — seasonal or cyclic

Place both fields by the entry's primary focus.

## Field applicability by category

Always expected in all entries:

- `category`
- `name`
- `status`
- `time_era`
- `time_span`

Commonly used in most non-world entries (use when relevant):

- `region`
- `culture`
- `related`
- `themes`

Region-specific fields (required when `category: region`):

- `place_type`
- `parent_region`

Category-specific optional fields:

- `scope` for `rule`
- `artifact_type` for `artifact`
- `nature` for `inhabitant`
- `story_type` for `story`
- `medium`, `edition`, `year`, `based_on` for `artwork`

## Authoring rules for optional and list fields

- Do not invent extra metadata keys outside this schema unless `agent/categories.md` or `AGENTS.md` defines them for this world.
- Leave unknown optional fields empty rather than guessing.
- If a later prompt provides previously unknown details, backfill those fields in the existing entry for any metadata key defined by this schema or category templates.
- Keep one concept per file.
- Use `related` and `themes` as lists when multiple values exist, and append new values instead of replacing established ones.
