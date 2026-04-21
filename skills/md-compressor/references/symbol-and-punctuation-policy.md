# Symbol and Punctuation Policy

## Goal

Lower token/char cost with safe punctuation removal and symbol substitution.

## Punctuation Rules

- Keep punctuation that prevents ambiguity.
- In bullets, final periods are optional; remove in `ultra`.
- Remove commas only when clause boundaries stay obvious.
- Keep colon after label-value patterns when useful (`Goal:`, `Risk:`).
- Keep punctuation inside literals unchanged (code, commands, URLs, regex).

## Safe Symbol Substitutions

- **leads to** -> `->`
- **maps to** -> `->`
- **results in** -> `->`
- **greater than or equal to** -> `>=`
- **less than or equal to** -> `<=`
- **not equal to** -> `!=`
- **versus** -> `vs`
- **and** -> `&` (only in short labels/titles, not dense prose)

## Optional Structural Compression

- Use `key: value` lines instead of full sentences.
- Replace repeated heading scaffolding with compact labels.
- Merge two short bullets when they share one subject.
- Convert "if X, then Y" to `if X -> Y` when unambiguous.

## Do Not Apply

- Legal, safety, compliance, or policy language.
- Statements containing hard negation where punctuation affects scope.
- Sentences with nested conditions likely to become ambiguous.

## Readability Floor

- If a reviewer cannot parse the line in one pass, revert to less compressed form.
- Prefer one extra token over potential misinterpretation.
