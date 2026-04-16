# Skill Blueprint

Use this blueprint to produce coherent, low-noise skills.

---

## 1) Define Skill Intent

Capture:

- primary job the skill performs
- trigger phrases or scenarios
- expected output behavior
- constraints or guardrails

If intent is broad, split into multiple skills instead of creating one overloaded skill.

---

## 2) Author Frontmatter

Required fields:

- `name`: lowercase kebab-case, stable identifier
- `description`: one concise paragraph with:
  - WHAT the skill does
  - WHEN the skill should be used

Recommended sentence form:

`<what it does>. Use when <trigger scenarios>.`

Avoid vague descriptions like "helps with coding."

---

## 3) Keep Main SKILL.md Minimal

Main file should contain only:

- role and goal of the skill
- core workflow or execution steps
- strict rules and output contract
- links to reference files

Do not place deep examples, long theory, or verbose explanation in `SKILL.md`.

---

## 4) Use Progressive Disclosure

Store deeper guidance in references, for example:

- design decisions
- detailed examples
- templates
- edge-case rules
- anti-patterns

Link references directly from `SKILL.md` (one level deep).

When listing references in `SKILL.md`, annotate each one with a short description so the model knows when to consult it.

Recommended format:

- `What this file covers and when to read it: [references/file.md](references/file.md)`

---

## 5) Define Output Contract

Specify what "good output" looks like:

- structure
- formatting
- naming rules
- location rules
- validation checks

If output quality is variable, include a checklist-driven review step.

---

## 6) Final Validation

Before shipping:

1. Ensure format consistency with existing repository skills
2. Remove repeated guidance
3. Confirm reference links resolve
4. Confirm descriptions are discoverable and specific
5. Ensure tone and terminology are consistent
