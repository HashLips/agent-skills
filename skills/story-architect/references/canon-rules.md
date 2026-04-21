# Canon Rules

## Summary

- Defines canonical guidance for this reference area.
- Use this file to keep story-architect outputs consistent and canon-safe.


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

## Allowed Status Values

- `canonical`
- `myth`
- `rumor`
- `unknown`
- `contradicted`
