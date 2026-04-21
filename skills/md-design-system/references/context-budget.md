# Context Budget

## Summary

- Use minimum sufficient context when applying this skill.
- Choose mode by scope: single-file edit or package refactor.

## Mode selection

- **Single-file mode** — small edits in one file. Start with `SKILL.md`, then load one targeted reference.
- **Package mode** — formatting/refactoring a skill pack or related doc bundle. Load `SKILL.md` plus required core references before editing.

## Single-file mode (default for small tasks)

- Start with `SKILL.md`.
- Escalate to one file when uncertainty appears.

## Package mode (required for bundle formatting)

Load this minimum set before reformatting multiple related files:

- `SKILL.md`
- `canonical-profiles.md`
- `molecules.md`
- `canonical-syntax.md`
- `normalization-checklist.md`

Optional in package mode:

- No extra files needed in normal operation; `canonical-syntax.md` includes inline shape examples.

## Targeted reference routing

- **Syntax shape** — `canonical-syntax.md`
- **Section/molecule naming** — `molecules.md`
- **Doc layout profile** — `canonical-profiles.md`
- **Final QA pass** — `normalization-checklist.md`

## Layer usage map (atoms → molecules → organisms)

- **Atom-level task** — line and token formatting (list markers, emphasis, links, code fences).
  - Load: `canonical-syntax.md`.
- **Molecule-level task** — section block shapes (Variables, Interfaces, Example, Footer).
  - Load: `molecules.md`.
- **Organism-level task** — document section order and profile selection.
  - Load: `canonical-profiles.md`.
- **Safety task** — ensure formatting pass preserves facts and template contract.
  - Load: `normalization-checklist.md`.

## Anti-patterns

- Loading all reference files before small edits.
- Treating package refactors as single-file edits and skipping related files.
- Copy-pasting large reference text into prompts.
- Duplicating this entire system inside other skills.
