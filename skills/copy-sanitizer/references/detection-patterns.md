# Detection Patterns

Scan the **copy** the user provides. Flag **pattern clusters**, not a fixed word list.

Respect [preserve-regions.md](preserve-regions.md).

## Hyphen joins (priority)

Every glued `word-word` in readable sentences is in scope.

| Check | Heuristic |
| --- | --- |
| Hyphen between words | `\b[a-zA-Z]+-[a-zA-Z]+\b` |
| Editorial prefix | `\b(de\|re)-[a-z]{2,}\b` |
| Technology prefix | `\b[A-Z]{2,}-[a-z]+\b` |
| Stacked modifiers | 2+ hyphen modifiers before one noun |
| Slash joins | `before/after`, `pre/post` in sentences |

**Output:** zero prose hyphen joins after sanitize ([hyphen-break-patterns.md](hyphen-break-patterns.md)).

## Punctuation rhythm

Per 1,000 words. Flag density or repetition ([scoring-heuristics.md](scoring-heuristics.md)).

| Pattern | What to measure |
| --- | --- |
| Em dashes | `—` in sentences |
| Double dashes | `--` in copy |
| Semicolons, colons, ellipsis | density |
| Parentheses, quote stacks | frequency |

## Connectors (by function)

| Function | Role |
| --- | --- |
| Summary pivot | wraps up |
| Hedge announcement | claims importance |
| Contrast pivot | switches direction |
| Addition chain | stacks points |
| Generalization frame | vague scope |

**Flag when:** same function 2+ times within ~500 words; identical phrase twice in one paragraph; many paragraphs in a row opening with a pivot.

## Vague phrasing (by category)

| Category | Role | Sample shapes only |
| --- | --- | --- |
| Corporate verbs | inflate action | streamline, optimize |
| Meta nouns | abstract | framework, ecosystem |
| Intensifiers | empty emphasis | truly, remarkably |
| Hype adjectives | sales tone | innovative, seamless |

**Flag when:** 3+ from one category in a paragraph or heavy synonym pile in a section.

## Structural tells

- Same sentence openings repeated
- Very uniform sentence or paragraph length
- Define → example → repeat with no new info
- Endings that only restate the intro
- Flat, hedged tone with no concrete detail
- Every section with the same rhetorical shape

## Delivery

- Sanitized copy
- Hyphen check passed
- Short inline report
