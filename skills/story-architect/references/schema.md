# Metadata Schema

## Summary

- Defines canonical guidance for this reference area.
- Use this file to keep story-architect outputs consistent and canon-safe.


All entries must begin with YAML front matter.

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

---

## Category source of truth

Allowed category values are defined in `references/categories.md`.

## Field meanings

`category`  
Entry type. Must use a valid category from `references/categories.md`.

`name`  
Official name of the concept.

`region`  
Broader geographical context.

`parent_region`  
Immediate containing place.

`place_type`  
Scale of place when category is region.

`culture`  
Associated society or group.

`related`  
List of related entries.

`themes`  
Conceptual or symbolic themes.

`status`  
Canon truth level. Allowed values are defined in `references/canon-rules.md`.

## Field applicability by category

Always expected in all entries:

- `category`
- `name`
- `status`

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

- Do not invent extra metadata keys outside this schema.
- Leave unknown optional fields empty rather than guessing.
- If a later prompt provides previously unknown details, backfill those fields in the existing entry for any metadata key defined by this schema or category templates.
- Keep one concept per file.
- Use `related` and `themes` as lists when multiple values exist, and append new values instead of replacing established ones.
