# Detection Patterns

Read the document as normal text. Scan for **pattern clusters** in running prose, not a fixed word list.

Classify context first ([context-allowlist.md](context-allowlist.md)).

## Hyphen joins in prose (priority)

**Every** `word-word` form in running prose is in scope, not only clusters.

| Check | Heuristic |
| --- | --- |
| Hyphen between words | `\b[a-zA-Z]+-[a-zA-Z]+\b` in prose |
| Editorial prefix | `\b(de\|re)-[a-z]{2,}\b` |
| Technology prefix | `\b[A-Z]{2,}-[a-z]+\b` |
| Stacked modifiers | 2+ hyphen modifiers before one noun |
| Slash joins in prose | `before/after`, `pre/post` in sentences |

**Output rule:** zero matches in prose after sanitize ([hyphen-break-patterns.md](hyphen-break-patterns.md)).

## Punctuation and Symbols

Track per 1,000 words in prose. Flag density or repetition ([scoring-heuristics.md](scoring-heuristics.md)).

| Pattern | What to measure |
| --- | --- |
| Em dash in prose | `—` in sentences (exclude label/value lines) |
| Double dash | `--` outside markdown/code |
| Semicolons, colons, ellipsis | density in prose |
| Parentheses, quote stacks | frequency |
| Bullet / section symmetry | templated prose bullets only |

## Connector Phrases (by function)

Flag repeated **function**, not a fixed phrase list.

| Function | Example shapes only |
| --- | --- |
| Summary pivot | wraps up a section |
| Hedge announcement | claims importance |
| Contrast pivot | switches direction |
| Addition chain | stacks points |
| Generalization frame | vague scope |

**Flag when:** same function 2+ times within ~500 words; identical phrase twice in one paragraph; 3+ pivot openings in a row.

## Vague Vocabulary (by category)

| Category | Role | Sample shapes only |
| --- | --- | --- |
| Corporate verbs | inflate action | streamline, optimize, leverage |
| Meta nouns | abstract process | framework, ecosystem |
| Intensifiers | empty emphasis | truly, remarkably |
| Hype adjectives | sales tone | innovative, seamless |

**Flag when:** 3+ from one category in a paragraph or heavy synonym repetition in a section.

## Structural Tells

Repeated openings, sentence/paragraph sameness, triple explain, summary-only endings, flat tone, templated prose sections (not required skill layout).

## Delivery check

- Prose: zero hyphen joins
- Syntax: allowlist intact
- Brief inline report (no tracking file unless user asks)
