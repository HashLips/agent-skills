---
name: md-compressor
description: Compresses Markdown to minimal token form while preserving facts and agent-executable intent; duplicates sources first and compresses skill packages (SKILL.md plus reference MD). Use when reducing context cost in docs, skills, or prompts at light, medium, heavy, or extreme compression.
---

# MD Compressor

Shrink Markdown to the smallest workable form for agents. **Never edit originals** — duplicate first, compress the copy only.

## End Goal

**The machine must still know what to do** after compression — at every level, including **extreme**.

- **Always preserve:** actionable requirements, constraints, steps, decisions, numbers, commands, paths (per level rules), and skill triggers (`name`, usable `description`).
- **May be reduced as levels increase:** tone, encouragement, examples, edge-case color, and duplicate explanations — some context and “feel” can be lost; that is an expected tradeoff.
- **Never acceptable:** an agent reading only the compressed copy cannot determine what action to take, what order to do it in, or what must not be violated.
- **If executability is at risk:** keep the longer form, revert that fragment, or step down one compression level for that line or file.

Heavier compression = fewer tokens, not a different skill. When reporting results, note that **heavy / extreme** copies may omit nuance but must remain **agent-executable**.

## Non-Negotiable Safety

1. **Duplicate before compress** — copy the target skill folder or MD file; write all compressed output into the copy.
2. **Source stays intact** — do not save compression edits to the original path.
3. **Confirm target** — state source path, copy path, and compression level before editing.

## Core Rules

1. **Facts are immutable** — requirements, constraints, numbers, paths, commands, and decisions stay exact.
2. **Level is explicit** — default `light` unless the user asks for `medium`, `heavy`, or `extreme`.
3. **Skill = whole package** — compress `SKILL.md` and every `.md` under `references/` in the duplicated folder; copy non-text assets unchanged.
4. **Text only** — compress Markdown and plain text; skip binaries, images, and non-text assets.
5. **No semantic drift** — if shortening risks changing meaning or what the agent should do, keep the longer form.
6. **Agent-executable over minimal** — prefer tokens saved only when the compressed copy still answers: what to do, in what order, under what constraints.
7. **Valid skill output** — preserve YAML frontmatter keys (`name`, `description`); keep `description` trigger-clear even when shortened.

## Compression Levels

| Level | Goal | Human-readable |
| --- | --- | --- |
| **light** | Tight sentences; keep structure and punctuation | Yes |
| **medium** | Light + abbreviations, symbol swaps, denser lists | Mostly |
| **heavy** | Minimum tokens; machine-parseable over readable | Optional |
| **extreme** | Heavy + whitespace strip + short ref filenames and links | No |

Level definitions: [references/compression-levels.md](references/compression-levels.md).

## Workflow

1. **Intake** — single file, folder, or skill package; pick `light`, `medium`, `heavy`, or `extreme`.
2. **Duplicate** — [references/safe-copy-workflow.md](references/safe-copy-workflow.md).
3. **Scope files** — skill packages: [references/skill-package-handling.md](references/skill-package-handling.md).
4. **Compress** — per-file pass: [references/compression-workflow.md](references/compression-workflow.md).
5. **QA** — [references/quality-checklist.md](references/quality-checklist.md).

## Output Contract

- First line of each compressed file body: `Compression: light|medium|heavy|extreme` (after frontmatter when present).
- **light / medium / heavy:** output remains valid Markdown (heavy may be dense but parseable).
- **extreme:** whitespace-stripped; may be a few very thin lines — facts and literals intact; agent-parseable over human-readable.
- **extreme (skill packages):** may rename `references/*.md` to short names and rewrite all internal links; see [references/extreme-path-shortening.md](references/extreme-path-shortening.md).
- Preserve heading hierarchy unless flattening is lossless (light/medium); heavy/extreme may collapse when intent is unchanged.
- Keep external URLs, CLI paths, and fenced code literals intact; internal ref paths may shorten at **extreme** only.
- Add a one-line abbreviation legend at top only when heavy/extreme uses non-map shorthand (omit legend at extreme if it costs more tokens than it saves).

## Reference Index

- **Duplicate-first safety and naming:** [references/safe-copy-workflow.md](references/safe-copy-workflow.md)
- **Light / medium / heavy / extreme behavior:** [references/compression-levels.md](references/compression-levels.md)
- **Skill folder scope and frontmatter:** [references/skill-package-handling.md](references/skill-package-handling.md)
- **Per-file compression order:** [references/compression-workflow.md](references/compression-workflow.md)
- **Canonical abbreviations:** [references/abbreviation-map.md](references/abbreviation-map.md)
- **Symbol and punctuation by level:** [references/symbol-and-punctuation-policy.md](references/symbol-and-punctuation-policy.md)
- **Extreme path shortening:** [references/extreme-path-shortening.md](references/extreme-path-shortening.md)
- **Final QA:** [references/quality-checklist.md](references/quality-checklist.md)

## When To Use This Skill

- Shrinking verbose Markdown or full skill packages for lower context cost.
- Testing how small a skill can get while staying agent-usable.
- Preparing dense handoff or archive copies without touching source skills.
