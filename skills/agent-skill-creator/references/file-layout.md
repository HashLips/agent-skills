# File Layout Guide

## Summary

- Use this as the default layout for new skills.
- Keep structure simple and predictable.

## Default layout

```text
skill-name/
├── SKILL.md
├── references/
│   ├── blueprint.md
│   ├── quality-checklist.md
│   └── [additional-reference].md
└── assets/ (optional)
```

## Layout rules

- `SKILL.md` is required and concise.
- `references/` stores long-form guidance.
- `assets/` is optional and must be justified.

## Naming conventions

- Skill folder: lowercase kebab-case.
- Reference files: lowercase kebab-case with focused names.
- Avoid generic filenames (`notes.md`, `misc.md`).

## Reference strategy

- Keep references topical and scoped.
- Prefer several focused files over one mixed document.
- Ensure every reference is linked from `SKILL.md`.

## Asset guidance

Add assets only for reusable templates, canonical examples, visual standards, or repeatedly used domain files.
