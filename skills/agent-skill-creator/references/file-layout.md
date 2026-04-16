# File Layout Guide

Use this layout as the default structure for new skills.

```text
skill-name/
├── SKILL.md
├── references/
│   ├── blueprint.md
│   ├── quality-checklist.md
│   └── [additional-reference].md
└── assets/ (optional)
```

---

## Layout Rules

- `SKILL.md` is required and should stay concise
- `references/` holds detailed guidance and long-form context
- `assets/` is optional and should only exist when it materially improves outputs

---

## Naming Conventions

- Skill folder: lowercase kebab-case
- Reference files: lowercase kebab-case with focused names
- Avoid generic names like `notes.md` or `misc.md`

---

## Reference Strategy

- Keep references topical and scoped
- Prefer multiple small references over one large mixed document
- Ensure every reference is reachable from `SKILL.md`

---

## Asset Guidance

Add assets when needed for:

- reusable templates
- canonical examples
- visual standards
- domain-specific files used repeatedly

Avoid adding assets that are rarely used or easy to regenerate.
