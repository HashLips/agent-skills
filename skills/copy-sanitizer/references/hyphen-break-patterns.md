# Hyphen-Break Patterns

## Core rule (non-negotiable)

**Sanitized running prose has zero hyphen joins between words.**

If two ideas were glued as `word-word`, unpack them:

| Instead of | Write |
| --- | --- |
| human-readable | readable, easy to read, plain language |
| re-scan | scan again |
| high-impact results | strong results, results that matter |
| AI-powered tool | tool that uses AI, tool with AI features |

Use separate words, a short rephrase, or one plain modifier. **Do not** replace one hyphen join with another.

This applies to **all** prose hyphen joins: editorial prefixes (`re-`, `de-`), technology labels (`AI-`), stacked modifiers, metric joins (`before/after`), and consultant compounds (`end-to-end` → `from start to finish` or `full`).

## Input vs output

| Phase | Rule |
| --- | --- |
| **Detect** | Flag every `\b\w+-\w+\b` in prose (plus prefix/slash join shapes). |
| **Edit** | Remove or rephrase every flagged join in prose. |
| **Verify** | Final pass: prose must match zero hyphen joins. |

Clustering still guides priority; a single join in prose should still be fixed on the final pass.

## What is not prose (do not unpack)

See [context-allowlist.md](context-allowlist.md):

- Paths and filenames (`copy-sanitizer`)
- Frontmatter, code, URLs, inline code
- List markers (`- item`)
- Label lines (`- **name** — value`)
- Em dash between label and value is layout, not a word join

## Detection shapes (illustrative)

| Shape | Sample forms only |
| --- | --- |
| Editorial prefix join | `re-…`, `de-…` |
| Technology prefix join | `AI-…`, `ML-…` |
| Stacked modifiers | two+ hyphen modifiers before one noun |
| `over-` repetition | several in one section |
| Metric-style join | `before/after`, `pre/post` in a sentence |

## Forbidden on output

- Inventing new `word-word` forms in the rewrite
- Swapping piles (`machine-written` → `model-written`)
- Leaving "readable" style compounds because they sound grammatical

## Self-check before delivery

1. Search sanitized **prose** for `\b[a-zA-Z]+-[a-zA-Z]+\b` and `\b(de|re)-[a-z]+`.
2. Search for `AI-` and similar prefix joins in sentences.
3. If any match outside the allowlist, rephrase again.
