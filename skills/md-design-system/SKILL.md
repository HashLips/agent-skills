---
name: md-design-system
description: Lightweight Markdown formatter contract for consistent structure across docs, skills, and agents. Use when you need format normalization (headings, sections, lists, syntax) without changing facts or template-required content.
---

# MD Design System

Use this as a lightweight formatter contract.

## Core Rules

1. **Format only** — never change facts, decisions, constraints, or values.
2. **Template first** — if another skill defines required sections/fields, keep them.
3. **One H1 + no heading skips** — `#` then `##` then `###` then `####`.
4. **Lists over prose** — prefer bullets and steps for scanability.
5. **Named items over tables** — use `- **name** — value` for fields/interfaces.
6. **Canonical syntax** — `-` bullets, `1.` ordered lists, fenced code, `[label](url)`.
7. **Lean output** — remove decorative noise and repetition.
8. **Canonical filenames** — enforce kebab-case, `-agent.md` for agents, and `SKILL.md` as skill entry file.

## Workflow

1. Choose scope:
   - Single-file edit -> follow lightweight flow.
   - Package refactor -> use package mode from [references/context-budget.md](references/context-budget.md).
2. Pick document profile from [references/canonical-profiles.md](references/canonical-profiles.md).
3. Keep template-required sections and field placement intact.
4. Normalize headings, lists, variables/interfaces, and code formatting.
5. Run [references/normalization-checklist.md](references/normalization-checklist.md).

## Reference Index

- **Profiles (section order):** [references/canonical-profiles.md](references/canonical-profiles.md)
- **Molecules (section shapes):** [references/molecules.md](references/molecules.md)
- **Syntax rules:** [references/canonical-syntax.md](references/canonical-syntax.md)
- **QA and fact-preservation checks:** [references/normalization-checklist.md](references/normalization-checklist.md)
- **Context policy:** [references/context-budget.md](references/context-budget.md)

## When To Use This Skill

- Formatting/refactoring Markdown for consistent structure.
- Applying style contracts without changing meaning.
- Enforcing predictable, lean outputs across skills and agents.
