# Workflow

Extended steps for **section** and **document** mode. Snippet flow matches main `SKILL.md` workflow.

## Modes

| Mode | Scope | Tracking file |
| --- | --- | --- |
| **snippet** | Paragraph to few pages | Optional |
| **section** | One chapter or major section | Recommended |
| **document** | Full article, report, or book | Required |

## Intake (section and document)

1. Classify context ([context-allowlist.md](context-allowlist.md)).
2. Record host skills and prose vs syntax regions.
3. Create or open `.copy-sanitizer-track.md` ([tracking-file.md](tracking-file.md)).

## Document chunk loop

1. Split at `##` or chapter boundaries; overlap 1–2 paragraphs if a cluster spans edges.
2. Per chunk: first scan → sanitize → second scan → append tracking rows.
3. Roll up document metrics; write `final_report`.
4. Deliver sanitized document and tracking file.

## Edit pass order (prose only)

1. Structure and rhythm
2. Connector load
3. Vague vocabulary clusters
4. Punctuation density
5. Hyphen-break joins ([hyphen-break-patterns.md](hyphen-break-patterns.md))
6. Template symmetry (not required skill layout)

## Stop and handoff

- Stop at residual `low`, voice risk, or user change cap.
- Update `progress`, `unresolved_sections`, and context in `notes` when pausing.
