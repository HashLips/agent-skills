# Detection Patterns

Scan before editing. Flag by **density**, **repetition**, **proximity**, and **structural sameness** — not single hits and not a fixed vocabulary list.

Classify context first ([context-allowlist.md](context-allowlist.md)). Score **running prose**; do not penalize required skill or markdown syntax.

## Punctuation and Symbols

Track per 1,000 words in prose regions. Flag when density exceeds [scoring-heuristics.md](scoring-heuristics.md) or the pattern repeats in nearby paragraphs.

| Pattern | What to measure |
| --- | --- |
| Em dash in prose | `—` in sentences (exclude label/value list lines per allowlist) |
| Double dash | `--` not part of markdown or code |
| Semicolons | ratio to sentences |
| Colons | prose uses; exclude time, URLs, `::`, code |
| Ellipsis | `...` or `…` |
| Quote stacks | repeated aphorism-style `"..."` clauses |
| Parentheses | frequency per paragraph |
| Bullet symmetry | same grammar on every adjacent bullet **in prose sections** |
| Numbered symmetry | identical step templates across sections |
| Separators | repeated `---` / `***` bands |

One em dash in a chapter is fine. Four in three prose paragraphs is a cluster.

## Hyphen-Break Joins (prose only)

See [hyphen-break-patterns.md](hyphen-break-patterns.md). Detect **shape**, not specific words.

| Shape | Example forms (illustrative only) | Heuristic |
| --- | --- | --- |
| Editorial prefix join | `re-…`, `de-…` + verb/noun | `\b(de\|re)-[a-z]{2,}\b` minus dictionary allowlist |
| Technology prefix join | `AI-…`, `ML-…` + modifier | `\b[A-Z]{2,}-[a-z]+\b` in prose |
| Stacked modifiers | two+ `word-word` before one noun | count hyphen modifiers per noun phrase |
| Repeated `over-` | multiple in one section | count per section |
| Metric-style join | `before/after`, `pre/post` in sentences | slash or hyphen join between role words |
| Jargon pile | clustered consultant compounds | density of hyphen joins + vague nouns |

**Fix:** unpack to plain words. Do not swap one pile for another.

## Connector Phrases (by function, not fixed list)

Infer connectors dynamically. Flag **repeated function**, not a single magic phrase.

| Function | What it does | Example shapes (not exhaustive) |
| --- | --- | --- |
| Summary pivot | wraps up a section | "in conclusion", "overall", "to sum up" |
| Hedge announcement | claims importance | "it's important to note", "worth noting" |
| Contrast pivot | switches direction | "however", "on the other hand", "that said" |
| Addition chain | stacks points | "furthermore", "moreover", "additionally" |
| Generalization frame | vague scope | "when it comes to", "at the end of the day" |
| Reframe | restates prior point | "in other words", "simply put" |

**Flag when:** same function appears 2+ times within ~500 words; identical phrase twice in one paragraph; 3+ paragraphs in a row open with a pivot.

Use phrase similarity (shared first 2–3 words, shared function) in addition to exact matches.

## Vague or Hype Vocabulary (by category, not word list)

Detect **clustering** of near-synonyms and category repetition. Examples below are **samples**; apply the category in any domain.

| Category | Typical role | Example samples (extend per domain) |
| --- | --- | --- |
| Corporate verbs | inflate action | streamline, optimize, leverage, facilitate |
| Meta nouns | abstract process | framework, ecosystem, landscape, paradigm |
| Intensifiers | empty emphasis | truly, remarkably, incredibly, fundamentally |
| Hype adjectives | sales tone | innovative, seamless, transformative, cutting-edge |

**Flag when:** 3+ terms from one category in a paragraph, or the same root idea repeated with synonyms in one section. Do **not** flag a single domain-appropriate term.

## Structural Tells

| Tell | Detection |
| --- | --- |
| Repeated openings | same first 3 words on 3+ sentences in 10-sentence window |
| Sentence length sameness | very low variance in words per sentence |
| Paragraph size sameness | 3+ paragraphs within ±15% word count |
| Repeated cadence | similar clause and comma patterns |
| Obvious triple explain | define → example → restate with no new info |
| Summary endings | closing paragraph only restates intro |
| Predictable section shape | same rhetorical steps every section |
| Too-uniform rhythm | no short lines where author elsewhere uses them |
| Flat tone | hedged positivity, no concrete detail |
| Template markdown | identical heading+bullet blocks (exclude required skill layout) |

## Regex Aids (shapes only)

```text
\b(de|re)-[a-z]{2,}\b
\b[A-Z]{2,}-[a-z]+\b
(?<![\w-])--(?![\w-])
```

Confirm with context and allowlist. No static buzzword regex list.

## Scan Output Shape

Per section:

- `context`, `punctuation`, `hyphen_joins`, `connectors`, `vague_vocab`, `structure`, `hotspots`
