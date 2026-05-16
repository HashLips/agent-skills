# Tracking File

Use `.copy-sanitizer-track.md` for section and document mode. Holds analysis state across sessions and large books.

## Location

- Default: same directory as source document
- User may override path
- Never store secrets in the tracking file

## Template

```markdown
---
skill: copy-sanitizer
source: path/to/source.md
mode: document
created: 2026-05-16
updated: 2026-05-16
---

# Copy Sanitizer Track

## Progress

- **status:** `in_progress` | `complete` | `paused`
- **current_chunk:** identifier or heading slug
- **chunks_total:** number
- **chunks_done:** number

## Document Baseline (first pass)

- **context:** skill package | spec | narrative | other
- **host_skills:** optional list
- **word_count:**
- **em_dash:**
- **semicolon:**
- **colon:**
- **ellipsis:**
- **connectors:**
- **hyphen_joins:**
- **vague_vocab_score:**
- **structural_flags:** list
- **initial_confidence:** low | medium | high

## Scan Results

<!-- Repeat per chunk -->

### Chunk: {slug}

- **range:** lines or heading
- **metrics_first_pass:** object
- **hotspots:** [{ type, location, note }]
- **metrics_second_pass:** object (after edit)
- **chunk_residual:** low | medium | high

## Replacement Summaries

<!-- Brief, not full diff -->

- **chunk:** {slug}
- **patterns_addressed:** [transition_cluster, em_dash_density, hyphen_join, ...]
- **edit_count_approx:** number
- **notes:** optional

## Unresolved Sections

- **chunk:** reason editing stopped (voice risk, domain terms, user cap)

## Final Report (second pass)

- **word_count:**
- **metrics_delta:** punctuation and phrase counts, first pass → second pass
- **structural_flags_remaining:**
- **residual_confidence:** low | medium | high
- **rationale:** 1–3 sentences
- **sentences_touched_pct:** approximate

## Session Log

| timestamp | action |
| --- | --- |
| 2026-05-16 | first scan chunk 1 |
```

Field keys stay snake_case for scripts. Prose in `notes` and `rationale` must follow [hyphen-break-patterns.md](hyphen-break-patterns.md).

## Rollup Rules

- **Document metrics** = sum of chunk counts (dedupe overlapping boundary windows for rolling metrics only).
- **Residual confidence** = worst chunk after sanitize, unless user fixed only part of the doc (say so in rationale).
- Update `updated` on every session write.

## Privacy

Tracking file holds analysis metadata only, not full source duplicates, unless the user asks for excerpts in `hotspots.notes`.
