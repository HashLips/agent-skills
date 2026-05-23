# Quality Checklist

## Safety (Run First)

- [ ] Original source path was not modified.
- [ ] A duplicate exists (`-cp-{level}/` folder or `.cp-{level}.md` file).
- [ ] Compression edits were written only inside the copy.
- [ ] User was told source path, copy path, and level.

## Agent Executability (End Goal)

- [ ] An agent reading only the compressed copy can determine what to do, in what order, and what must not be violated.
- [ ] Acceptable loss at higher levels: tone, encouragement, redundant examples — not steps, constraints, or safety rules.
- [ ] Any line that fails this gate was reverted or compressed at a lighter level.

## Fact Preservation

- [ ] No requirement, constraint, or decision needed for execution was removed.
- [ ] Numbers, versions, dates, and limits are unchanged.
- [ ] External URLs, CLI paths, commands, and code literals in body text are unchanged.
- [ ] **extreme:** internal ref paths may be shortened; each link still targets the correct file.
- [ ] Negations preserved (`must not` not weakened to `must`).

## Skill Package (If Applicable)

- [ ] `SKILL.md` and all `references/**/*.md` in the copy were compressed.
- [ ] Frontmatter keys `name` and `description` remain valid YAML.
- [ ] `name` unchanged; `description` still usable as a skill trigger.
- [ ] Reference links in `SKILL.md` still resolve to files in the copy.
- [ ] Non-text assets copied unchanged.

## Compression Level

- [ ] Each file starts with `Compression: light|medium|heavy|extreme` (after frontmatter if any).
- [ ] **light:** human-readable; structure and punctuation largely intact.
- [ ] **medium:** abbreviations follow [abbreviation-map.md](abbreviation-map.md); symbols per policy.
- [ ] **heavy:** token-minimal; machine-recoverable; legend present if non-map dense tokens used.
- [ ] **extreme:** heavy density applied; no blank lines in body; spaces/newlines stripped per policy; literals and frontmatter intact.
- [ ] **extreme (skill package):** ref files renamed to short unique stems; all internal links rewritten; rename map reported.

## Compression Quality

- [ ] Filler and redundant prose removed.
- [ ] Paragraph-heavy sections converted to bullets where valid for level.
- [ ] Repeated content merged into one canonical statement.
- [ ] No abbreviations inside code or command literals.

## Readability / Parse Gate

- [ ] **light / medium:** scannable in one pass; heading hierarchy valid; agent-executable.
- [ ] **heavy / extreme:** agent can execute skill intent from copy alone (same bar; lower human readability OK).
- [ ] **extreme:** body is visually thin (few lines); whitespace pass completed; executability preserved.
- [ ] If a line fails its level gate, it was reverted to a less aggressive form.

## Delivery

- [ ] Report lists copy path, level, and files touched.
- [ ] **extreme:** report includes `old → new` rename map when refs were shortened.
- [ ] User reminded originals are untouched.
- [ ] **heavy / extreme:** user informed that nuance or context may be reduced but the copy must remain agent-executable.
