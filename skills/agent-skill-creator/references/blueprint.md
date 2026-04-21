# Skill Blueprint

## Summary

- Use this blueprint to create coherent, low-noise skills.
- Keep intent, structure, and output contract explicit.

## Define Skill Intent

Capture:

- primary job,
- trigger scenarios,
- expected output behavior,
- constraints and non-goals.

Split broad intent into multiple skills instead of creating one overloaded skill.

## Author Frontmatter

Required fields:

- `name` (lowercase kebab-case),
- `description` (what + when).

Recommended sentence pattern:

`<what it does>. Use when <trigger scenarios>.`

## Keep Main SKILL.md Minimal

Include only:

- role and goal,
- core workflow,
- strict rules/output contract,
- reference links.

Move deep theory and large examples to references.

## Progressive Disclosure

Store detailed content in references:

- design decisions,
- edge cases,
- templates,
- anti-patterns.

Use description-first links in `SKILL.md`.

## Define Output Contract

Specify:

- structure and format,
- naming and location rules,
- validation checks.

## Final Validation

Before shipping:

1. check consistency with repository style,
2. remove repeated guidance,
3. verify all reference links,
4. confirm discoverable descriptions,
5. verify terminology consistency.
