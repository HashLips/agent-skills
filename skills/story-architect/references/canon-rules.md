# Canon Rules

## Summary

- Existing entries stay in place unless the creator asks for a revision.
- Empty and placeholder fields can be filled when new canon arrives.
- A conflict keeps the existing value and takes a status such as `myth`, `rumor`, or `contradicted`.


## World limits

If `agent/canon-safety.md` exists, read it before creating or enriching entries. It records what this world must not casually solve. Skill status framing still applies.

If `agent/reference-map.yaml` lists a file, that file is protected. On rename, move, or delete, update the map in the same change. Never reuse an ID.

## Canon Integrity

Existing entries are protected canon records.

Default behavior:
- read existing entries
- reference existing entries
- create new entries
- enrich existing entries when new canon fills missing metadata

Do not rewrite established canon unless explicitly instructed to edit, rewrite, update, expand, or refactor.

## Progressive Metadata Enrichment

Allowed without explicit edit request when the creator's latest prompt supplies missing details:
- fill empty, `unknown`, or placeholder metadata values for any schema/template-defined metadata field
- add newly discovered `related` or `themes` values
- set unresolved hierarchy fields such as `region` or `parent_region`
- set `culture` when now clearly identified

Guardrails:
- do not remove or replace established values unless the creator explicitly asks
- if a new detail conflicts with an established value, treat it as a canon conflict (do not silently overwrite)
- ask a minimal clarification question when two or more plausible values exist

## Conflict Handling

When a new idea conflicts with canon:

- report the conflict
- preserve existing records
- resolve with framing (for example `myth`, `rumor`, or `contradicted`) instead of rewriting canon

## Plain definition

The opening section (Overview, Summary, or Premise) states what the thing is, what it does, and what it is not. Unknowns stay labeled as unknown. Lead with that operating fact, then any atmosphere.

## Exact links

`related` values match another entry's `name` field exactly. After a batch of edits, report names that do not resolve.

## Allowed Status Values

- `canonical`
- `myth`
- `rumor`
- `unknown`
- `contradicted`
