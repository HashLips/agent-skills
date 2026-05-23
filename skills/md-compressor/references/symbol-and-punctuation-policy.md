# Symbol and Punctuation Policy

## Goal

Lower token and character cost without changing facts. Rules vary by compression level.

## By Level

| Rule | light | medium | heavy | extreme |
| --- | --- | --- | --- | --- |
| Final period in bullets | keep | drop | drop | drop |
| Commas in short bullets | keep | drop if clear | drop if clear | drop if clear |
| Symbol substitutions | rare | yes | yes | yes |
| `and` → `&` | no | labels only | labels only | labels only |
| Blank lines between bullets | keep | keep | remove if safe | none |
| Blank lines between sections | keep | keep | min 0–1 | none |
| Spaces around delimiters (`\|`, `;`, `->`) | keep | trim if clear | trim if clear | remove if clear |
| Line breaks within body | keep | keep | minimize | remove/join aggressively |

## Safe Symbol Substitutions (medium and heavy)

- **leads to** / **maps to** / **results in** → `->`
- **greater than or equal to** → `>=`
- **less than or equal to** → `<=`
- **not equal to** → `!=`
- **versus** → `vs`
- **if X, then Y** → `if X -> Y` when unambiguous

## Punctuation Rules (All Levels)

- Keep punctuation that prevents ambiguity.
- Keep punctuation inside literals (code, commands, URLs, regex).
- Keep colon in `label: value` when it aids parsing (medium/heavy).

## light

- Keep sentence punctuation mostly intact.
- Symbols only for universal relations in technical lines (`->`, `<=`, `>=`).
- Keep conjunction words when they improve flow.

## medium

- Drop optional terminal periods in bullets.
- Remove commas that do not change parse meaning.
- Use `key: value` instead of full sentences when unambiguous.
- Replace safe phrase patterns with symbols from table above.

## heavy

- Apply medium rules plus maximal stripping.
- Prefer single-space separators; no trailing spaces.
- Allow packed line formats only when a machine can still extract distinct rules.
- Do not strip punctuation from negated requirements where scope could blur.

## extreme

- Apply **heavy** symbol and punctuation rules first.
- **Whitespace is a target:** no blank lines; join body into as few lines as possible.
- Remove spaces around packed delimiters when unambiguous (`a|b|c` not `a | b | c`).
- Keep one space after `#` in headings only if required for parsing.
- Do not remove spaces inside literals (code, URLs, paths, commands, frontmatter).
- Do not strip punctuation from negated requirements where scope could blur.
- If joining two lines creates ambiguity → keep a single line break between them.

## Do Not Apply (Any Level)

- Legal, safety, compliance, or policy language (minimize words only; keep clarity).
- Hard negation where punctuation affects scope — keep `must not` spelled clearly.
- Nested conditions likely to become ambiguous — keep structure or split bullets.

## Readability Floor

- **light / medium:** reviewer parses each line in one pass; revert if not.
- **heavy:** machine/agent must recover same requirements as source; revert line if not.
- **extreme:** same parse gate as heavy; human readability not required.
