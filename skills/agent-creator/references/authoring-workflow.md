# Authoring Workflow

1. **Role** — One profession per `<descriptor>-agent.md`. Split combined asks into multiple agents or a thin coordinator.

2. **Name** — `<descriptor>-agent.md` (kebab-case). [naming-and-layout.md](naming-and-layout.md)

3. **Identity** — One **paragraph** from [agent-file-template.md](agent-file-template.md). Only `<Agent Name>` and `<profession>` change. Keep body text **mostly** unbolded.

4. **Role summary** — Optional; 1–2 sentences if helpful.

5. **Pillars** — Responsibilities, decision framework, constraints, **Failure modes and recovery**, outputs, collaboration, plus **required** [Completion and handoff](completion-and-handoff.md). Tight bullets; **minimal** `**bold**` in the agent file (readable Markdown).

6. **Compression pass** — Convert paragraphs to bullets, delete repeated rules, and keep "how-to" detail in references/skills instead of the agent body.

7. **Escalation** — Add only if not already clear from constraints and completion.

8. **Brevity pass** — Remove duplicate ideas, strip unnecessary emphasis, and cut repo-specific links.

9. **Style calibration** — Compare density/structure with [role-family-exemplars.md](role-family-exemplars.md) and tighten if your draft is bulkier.

10. **Hard QA gate** — Apply [qa-rubric.md](qa-rubric.md). Any "fail" must be fixed before delivery.

11. **Review** — [ ] `*-agent.md` naming [ ] role pillars + failure micro-section + **Completion and handoff** [ ] one-paragraph identity [ ] no fake authority [ ] portable (no `../` or `skills/` hard dependency) [ ] **DoD + handoff** are testable, not “when done” [ ] target size ~250-500 words [ ] sections are list-first and scannable

## Refactoring a noisy agent

- If half the line is in `**bold**`, **rewrite** the line as plain text and use a heading or list instead of shouting.
- Merge **Definition of done** from **Outputs** if they duplicated: Outputs = catalogue of artefacts; **Completion and handoff** = stop rule + next **role** + start rule for them.
- If a section exceeds ~7 bullets, combine adjacent bullets or move deep examples to a reference.
