# Compression Workflow

## Goal

Smallest workable Markdown for the chosen level. **Zero loss of actionable intent** — requirements, steps, and constraints the agent needs to execute. Heavier levels may drop tone and optional context; they must not drop what to do.

## Prerequisites

- Duplicate exists per [safe-copy-workflow.md](safe-copy-workflow.md).
- Level chosen: `light`, `medium`, `heavy`, or `extreme` per [compression-levels.md](compression-levels.md).
- Skill scope resolved per [skill-package-handling.md](skill-package-handling.md) if applicable.

## Per-File Step Order

1. **Read source in copy** — never read-only-then-write-to-original.
2. **Extract facts** — requirements, constraints, numbers, names, decisions, `must` / `must not`, links, code.
3. **Insert level header** — `Compression: {level}` after frontmatter when present.
4. **Delete low-value prose** — motivation, framing, duplicate rules, empty qualifiers.
5. **Refactor shape**
   - **light:** short clauses; list-first; keep section boundaries.
   - **medium:** `key: value` lines; merge duplicate bullets; compact headings text only.
   - **heavy:** inline dense rules where unambiguous; minimize blank lines.
   - **extreme:** apply **heavy** first; path pass (step 10) for skill packages; whitespace pass (step 11).
6. **Apply abbreviations** — none (light), [abbreviation-map.md](abbreviation-map.md) (medium/heavy/extreme).
7. **Apply symbols/punctuation** — per level in [symbol-and-punctuation-policy.md](symbol-and-punctuation-policy.md).
8. **Protect literals** — code fences, paths, URLs, CLI, env vars, frontmatter values for `name`.
9. **Quality gate** — [quality-checklist.md](quality-checklist.md).
10. **Extreme path pass** (extreme skill packages only, before or after heavy compress — prefer **before** whitespace pass):
    - Plan rename map for all linked `references/*.md`.
    - Rename files in the copy; rewrite every relative link in every `.md` file.
    - See [extreme-path-shortening.md](extreme-path-shortening.md).
11. **Extreme whitespace pass** (extreme only, after step 9 passes at heavy density):
    - Remove every blank line in the body.
    - Join lines; pack bullets/sections with `|` or `;` where unambiguous.
    - Strip redundant spaces (around delimiters, trailing, double spaces); never strip inside literals or frontmatter.
    - Target the fewest physical lines possible (often 1–3 lines plus frontmatter for a reference file).

## Level-Specific Rewrite Hints

### Light targets

- Filler: "In order to", "It is important to note", "Basically", "really", "just", "actually".
- Hedging unless required: "might", "somewhat", "quite", "very".
- Redundant pairs: "each and every", "final outcome".

### Medium adds

- Repeated terms → map abbreviations.
- "leads to" / "maps to" → `->` when obvious.
- Two short bullets same subject → one bullet.

### Heavy adds

- Optional section intros → delete if bullets carry facts.
- Multiple short bullets → single line with `;` or `|` only when parse stays unambiguous.
- Legend line at top when using non-map tokens (one line max).

### Extreme adds

- Short ref filenames + rewritten internal links (skill packages; see step 10).
- Everything in **heavy**, then flatten to minimal lines (see step 11).
- Treat each space, newline, and path character as token cost — remove when safe.
- File may look like one continuous strip; that is expected.
- Revert any fragment that becomes ambiguous after joining, space removal, or shortening.

## Never Compress Blindly

- Exact requirement language (`must`, `must not`, `required`).
- Numeric thresholds, dates, versions, limits.
- CLI commands, code snippets, paths, identifiers.
- Legal, security, or safety statements.
- Skill frontmatter `name` field.

## Package Pass (Skills Only)

After all MD files in the copy are compressed:

1. Cross-check that `SKILL.md` reference index links still resolve (use post-rename paths at **extreme**).
2. **extreme:** verify ref-to-ref links and report rename map.
3. Ensure no file in the copy still has pre-compression verbosity while siblings match the chosen level (consistent level unless user asked per-file levels).
