# Scoring Heuristics

Apply to **prose regions** only. Syntax follows [context-allowlist.md](context-allowlist.md).

## Hyphen joins (hard gate)

| State | Rule |
| --- | --- |
| **Before** | Count every `\b\w+-\w+\b` and prefix/slash joins in prose |
| **After** | Count must be **zero** in prose |

No warn/flag tiers for output: all prose hyphen joins are removed. Clustering only sets edit order.

## Punctuation Density (per 1,000 prose words)

| Signal | Warn | Flag |
| --- | --- | --- |
| Em dashes in prose | ≥ 4 | ≥ 8 |
| Double dashes | ≥ 2 | ≥ 5 |
| Semicolons | ≥ 6 | ≥ 12 |
| Colons (prose) | ≥ 8 | ≥ 15 |
| Ellipsis | ≥ 3 | ≥ 6 |

Label/value list lines do not count toward em dash density.

## Connector and Vague Vocab Scores

Use category repetition from [detection-patterns.md](detection-patterns.md). Clustered = prioritize; isolated = fix if quick without voice drift.

## Structural Sameness

Flag when 3+ structural tells co-occur in a section.

## Residual Pattern Confidence (informal)

| Level | Meaning |
| --- | --- |
| **low** | Prose passes zero hyphen join check; few other clusters remain |
| **medium** | Hyphen joins cleared; some connector or vagueness clusters left by choice |
| **high** | Major clusters remain or voice would break if pushed further |

## Inline report (no tracking file)

Include in the message to the user:

- Whether prose passed zero hyphen join check
- Other pattern types touched
- Approximate change level and any leftover hotspots
