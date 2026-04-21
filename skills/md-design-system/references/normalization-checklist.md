# Normalization Checklist

## Summary

- Use before merge and after refactors.
- Goal: profile-compliant, lean, and predictable Markdown.
- Treat every unchecked item as a failed gate to fix.

## Structure

- [ ] One H1 only.
- [ ] No heading level skips.
- [ ] Matches recommended section profile (`canonical-profiles.md`) or approved upstream template variant.
- [ ] If a source template defines required sections/order, that contract is preserved.
- [ ] Template-required extra sections are kept and placed consistently (not dropped).
- [ ] Filename matches naming rules from `canonical-profiles.md`.
- [ ] Agent files end with `-agent.md`.
- [ ] Skill entry file is exactly `SKILL.md` when formatting skill packages.

## Content shape

- [ ] Dense prose converted to bullets/steps where possible.
- [ ] Variables/interfaces use named-item format.
- [ ] No tables for fields/parameters.
- [ ] No factual content removed or rewritten semantically during styling.
- [ ] Decisions, constraints, values, and requirements remain intact.
- [ ] Unknown sections are mapped consistently using `canonical-profiles.md` fallback guidance.

## Syntax

- [ ] Bullets use `-`.
- [ ] Ordered steps use `1.` style.
- [ ] Links and code use canonical syntax.
- [ ] Undefined syntax cases were normalized using fallback rules from `canonical-syntax.md`.

## Lean limits

- [ ] Most sections are 3-7 bullets.
- [ ] No more than 2 consecutive prose paragraphs.
- [ ] Examples stay minimal and focused.
- [ ] Repetition removed.
- [ ] Trimming did not delete required facts or template-required fields.

## Ship rule

- [ ] **Pass** only when all boxes are checked.
- [ ] **Revise** if any box is unchecked; rerun checklist after fixes.
