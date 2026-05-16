# Workflow

Same flow for snippets, chapters, and full books: **read the document as normal text**, sanitize, verify, deliver. No tracking files.

## Standard flow

1. Read the full source (or user-selected section) in order.
2. Classify context and mark prose vs syntax ([context-allowlist.md](context-allowlist.md)).
3. Scan for pattern clusters ([detection-patterns.md](detection-patterns.md)).
4. Edit prose: hyphen joins first ([hyphen-break-patterns.md](hyphen-break-patterns.md)), then connectors, vagueness, punctuation, structure.
5. Final pass: confirm **zero hyphen joins** in prose.
6. Return sanitized document and a short inline report.

## Long documents

For books or large markdown files:

- Work through the file in reading order (optional mental chunks by chapter).
- Keep rolling awareness of repeated patterns; no external ledger.
- Deliver one complete sanitized file plus report when done.

Do not create `.copy-sanitizer-track.md` or similar side files unless the user explicitly asks.

## Edit pass order (prose)

1. Hyphen joins (remove all in prose)
2. Structure and rhythm
3. Connector load
4. Vague vocabulary clusters
5. Punctuation density
6. Template symmetry (not required skill layout)

## Stop conditions

- Prose passes zero hyphen join check
- Residual patterns are low or further edits risk voice
- User change cap reached
