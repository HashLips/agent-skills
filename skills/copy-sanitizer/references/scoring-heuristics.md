# Scoring Heuristics

Apply only to **prose regions** unless noted. Down-weight or skip syntax under [context-allowlist.md](context-allowlist.md).

## Punctuation Density (per 1,000 prose words)

| Signal | Warn | Flag |
| --- | --- | --- |
| Em dashes in prose | ≥ 4 | ≥ 8 |
| Double dashes | ≥ 2 | ≥ 5 |
| Semicolons | ≥ 6 | ≥ 12 |
| Colons (prose) | ≥ 8 | ≥ 15 |
| Ellipsis | ≥ 3 | ≥ 6 |
| Parenthetical pairs | ≥ 10 | ≥ 18 |

**Cluster rule:** warn threshold in two consecutive prose paragraphs flags those paragraphs.

Label/value list lines (`- **name** — value`) do not count toward em dash density.

## Hyphen-Break Join Score

Per prose section:

- +3 per editorial prefix join (`de-`, `re-`, minus allowlist)
- +2 per technology-style prefix join in prose
- +2 per noun phrase with 2+ hyphen modifiers
- +1 per extra `over-` form beyond the first

Section score ≥ 4 → hyphen join pass.

## Connector Phrase Score

- +2 per repeated **function** within 500 words (exact phrase or clear synonym role)
- +1 per prose paragraph opening with a pivot (cap +5 per section)

≥ 6 → `medium` residual; ≥ 10 → `high`.

## Vague Vocabulary Score

Per section, by **category** (corporate verb, meta noun, intensifier, hype adjective):

- +3 per category with 3+ clustered terms in one paragraph
- +2 per category with 5+ terms in one section
- +1 per near-synonym repeat (same meaning, different buzz word)

Normalize per 1,000 prose words: `< 4` low; `4–9` medium; `≥ 10` high.

## Structural Sameness

Flag when 3+ structural tells co-occur ([detection-patterns.md](detection-patterns.md)).

## Rolling Window (Chunked Documents)

Last **1,500 prose words:** connectors, vague vocab clusters, em dashes, hyphen joins.

## Residual Pattern Confidence

| Condition | Residual |
| --- | --- |
| No `high`; ≤ 20% sections `medium` | low |
| Any `high` OR > 35% `medium` | medium |
| Multiple `high` or cluster rules still firing | high |

Aim for **low** after sanitize without breaking voice or host-skill layout.

## When to Edit

Edit when pattern clusters, replacement matches register, meaning unchanged.

Defer when:

- Term or dash is required by host skill or MD design system
- Syntax region (paths, keys, list markers, label lines)
- Domain-standard for audience
- Intentional rhythm or user-supplied phrasing

## Comparison Report Fields

- Words processed (prose vs syntax split optional)
- Punctuation, connectors, vague vocab, hyphen joins, structure (first pass → second pass)
- Active context / host skills noted
- Residual confidence and brief rationale
