# Naming and Layout

## Summary

- Standardized naming keeps agent packs predictable.
- Layout should stay portable across repositories and tools.

## File naming

- Pattern: `<role-descriptor>-agent.md` (kebab-case).
- Suffix `-agent.md` is required.
- Descriptor should represent the role, not arbitrary codename.

## One role per file

- Do not combine distinct professions unless the file is a defined orchestrator role.

## Placement

- Files may live in any agent folder structure.
- Agent content must not depend on fixed paths.

## Agents vs skills

- Agent: role behavior and decision boundaries.
- Skill: reusable procedural guidance.
- Reference skills by name only when available.
