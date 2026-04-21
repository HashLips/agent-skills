# Quality Checklist

## Fact Preservation

- [ ] No requirement, constraint, or decision was removed.
- [ ] Numbers, versions, dates, and limits are unchanged.
- [ ] Links, paths, commands, and code literals are unchanged.
- [ ] Negations are preserved (`must not` not changed to `must`).

## Compression Quality

- [ ] Filler and redundant prose removed.
- [ ] Paragraph-heavy sections converted to concise bullets where valid.
- [ ] Repeated content merged into one canonical statement.
- [ ] Sentence length reduced without ambiguity.

## Abbreviation Quality

- [ ] Abbreviations follow [abbreviation-map.md](abbreviation-map.md).
- [ ] First-use expansion added for uncommon abbreviations.
- [ ] Abbreviations do not reduce readability below acceptable level.
- [ ] No abbreviations inside code or command literals.

## Symbol and Punctuation Quality

- [ ] Symbol substitutions follow [symbol-and-punctuation-policy.md](symbol-and-punctuation-policy.md).
- [ ] Punctuation removed only where meaning remains identical.
- [ ] Optional punctuation stripping does not create run-on ambiguity.
- [ ] Output includes active profile (`standard` or `ultra`).

## Readability Gate

- [ ] Document remains scannable in a single pass.
- [ ] Heading hierarchy remains valid and logical.
- [ ] Each bullet communicates one clear fact or action.
- [ ] Output is still understandable by a human without source text.
