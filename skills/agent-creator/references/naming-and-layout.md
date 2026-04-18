# Naming and Layout

## File name (canonical for this library)

- **Pattern:** `<role-descriptor>-agent.md` in **kebab-case**
- The suffix **`-agent.md`** is required (e.g. `product-manager-agent.md`, not `product-manager.md`).
- The descriptor is the **role** (e.g. `sre`, `stakeholder-communication`), not a product codename unless the role is literally project-specific and documented as such.

## One role per file

- Do not combine distinct professions in one file unless the team explicitly defined a single “orchestrator” handoff spec.

## Where to put files

- Anywhere your org keeps agents (`agents/`, `docs/`, a cursor folder, a zip for clients). The agent text must **not** depend on a specific path.
- A small **index** (e.g. `README` table) helps discovery but is optional.

## Agents and skills (portable)

- An **agent** = role spec (`<role>-agent.md` in this library).
- A **skill** = separate reusable procedure (often `SKILL.md` elsewhere), **not** the same file.
- Reference skills **by title or short name** only when the user’s environment has them. Do not embed `../../../` links or a mandatory `skills/` path inside agent bodies.
