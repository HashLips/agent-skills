# Hyphen-Break Patterns

## Core rule (non-negotiable)

**Sanitized copy has zero hyphen joins between words** in sentences the author would read aloud.

| Instead of | Write |
| --- | --- |
| human-readable | readable, easy to read, plain language |
| re-scan | read again, check again |
| high-impact results | strong results, results that matter |
| AI-powered tool | tool that uses AI |

Use separate words or a short rephrase. **Do not** swap one hyphen pile for another.

Applies to editorial prefixes (`re-`, `de-`), label prefixes (`AI-`), stacked modifiers, and metric joins (`before/after` in running copy).

## Input vs output

| Phase | Rule |
| --- | --- |
| **Detect** | Every `\b\w+-\w+\b` in copy (plus prefix/slash joins). |
| **Edit** | Unpack or rephrase each one in readable sentences. |
| **Verify** | Zero hyphen joins remain in copy. |

## Exceptions (preserve literals)

Do not break:

- Proper nouns and official product names that include hyphens (user or dictionary standard)
- URLs, code, SKUs, and user-marked do-not-edit blocks ([preserve-regions.md](preserve-regions.md))

When a hyphen is part of a **fixed name or literal**, keep it. When it is **assembled prose**, unpack it.

## Forbidden on output

- New `word-word` forms in the rewrite
- Leaving glued compounds because they sound grammatical
- Unpacking trademark or legal names the user said to keep

## Self-check

1. Search copy for `\b[a-zA-Z]+-[a-zA-Z]+\b` and `\b(de|re)-[a-z]+`.
2. Confirm each remaining hyphen is an allowed literal, not prose glue.
3. Rephrase anything else.
