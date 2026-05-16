# Quality Checklist

Run before delivery. Aligns with agent-skill-creator ship gate and copy-sanitizer rules.

## Skill package shape (when editing this or any skill repo)

- [ ] `SKILL.md` has frontmatter, Core Rules, Workflow, Constraints, Output Contract, Reference Index, When To Use.
- [ ] Main `SKILL.md` is operational; depth lives in `references/`.
- [ ] Every reference file is linked from `SKILL.md` Reference Index.
- [ ] Kebab-case paths and md-design-system label lines preserved.

## Intent and scope

- [ ] Scope and context classified ([context-allowlist.md](context-allowlist.md)).
- [ ] Host skills noted.
- [ ] Prose vs syntax regions marked.
- [ ] First scan before edits.

## Generic detection

- [ ] Pattern categories only; examples are illustrative.
- [ ] Strongest clusters addressed first.
- [ ] No hyphen-pile swap for another pile.

## Preservation

- [ ] Meaning and voice intact in prose.
- [ ] No fake humanity.
- [ ] Layout contracts and links intact.

## Metrics and handoff

- [ ] Second scan complete.
- [ ] Comparison stats and residual level reported.
- [ ] Sanitized copy and tracking path delivered if used.

## Anti-patterns

- [ ] Not a synonym swap or global word ban.
- [ ] Skill `SKILL.md` shape not flattened into plain paragraphs.
