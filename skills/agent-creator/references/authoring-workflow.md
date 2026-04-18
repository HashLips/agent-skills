# Authoring Workflow

1. **Role** — One profession per `<descriptor>-agent.md`. Split combined asks into multiple agents or a thin coordinator.

2. **Name** — `<descriptor>-agent.md` (kebab-case). [naming-and-layout.md](naming-and-layout.md)

3. **Identity** — One **paragraph** from [agent-file-template.md](agent-file-template.md). Only `<Agent Name>` and `<profession>` change.

4. **Role summary** — Optional; 1–2 sentences if helpful.

5. **Five pillars** — Responsibilities, decision framework, constraints, outputs, collaboration. **Tight** bullets; merge sub-bullets when possible.

6. **Escalation** — Add only if not already clear in constraints.

7. **Brevity pass** — Remove repeated ideas, adjectives with no decision content, and **any** path to a specific repo. Keep **“optional: use named skills if your environment has them”** in **Collab** at most once.

8. **Review** — [ ] `<role>-agent.md` name [ ] five pillars [ ] one-paragraph identity [ ] no fake authority [ ] portable (no `../` or `skills/` hard dependency)

## Refactoring from a bloated agent

- Collapse “persona” into one line in **Role summary** or **Constraints** if needed.
- Move long examples to a second file; keep the agent as the **index**.
