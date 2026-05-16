# Editorial Principles

## Preserve (Default)

- Meaning, facts, numbers, proper nouns, domain terms
- Author register and intentional repetition
- **Host skill layout** ([context-allowlist.md](context-allowlist.md)): kebab paths, `- **label** — value`, list markers, frontmatter, code

## Change (When Flagged in Prose)

Smallest change that breaks the **pattern**.

| Pattern | Fix |
| --- | --- |
| **Any hyphen join in prose** | Separate words or rephrase; **never** keep or add `word-word` |
| Em dash chain in prose | Sentences, comma, or period |
| Semicolon stack | Separate sentences |
| Connector cluster | Drop or merge; one pivot |
| Vague vocab cluster | Keep strongest term; plain words already in doc |
| Uniform sentence length | One longer, one shorter |
| Repeated opening | Vary first words |
| Parallel bullet prose | Vary one item (not required skill bullets) |
| Summary ending | Cut recap |
| Obvious triple explain | Cut restatement |
| Modifier stack | One plain modifier or separate clause, no hyphens |

## Word Choice

- Reuse vocabulary from the same document.
- Prefer plain verbs and nouns when rewriting a cluster.
- Do not import slang or hype the source lacks.

## Forbidden Tactics

- Any new hyphen join in prose output
- Fake typos or forced casualness
- Global stripping of allowlisted syntax (paths, label lines, code)
- Thesaurus parade
- Breaking agent-skill-creator or md-design-system layout

## Final prose gate

Before delivery, every sentence in running prose must pass the **zero hyphen join** check ([hyphen-break-patterns.md](hyphen-break-patterns.md)).

## Voice Check

Compare untouched and edited **prose** paragraphs. Revert if flatter or more corporate.

## Change Volume

Light ≤ 10%; standard ≤ 20%; heavy per user. Report approximate percent of prose sentences touched.
