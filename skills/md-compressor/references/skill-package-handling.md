# Skill Package Handling

## When This Applies

Use this reference when the source is a skill folder: contains `SKILL.md` at the root (typical layout per agent-skill-creator).

## Scope in the Copy

Compress in the duplicated folder only:

| Path | Action |
| --- | --- |
| `SKILL.md` | Compress |
| `references/**/*.md` | Compress each file |
| Other `**/*.md` | Compress if present |
| `assets/**` | Copy only; do not compress binaries |
| Non-text files | Copy unchanged |

Do not compress `SKILL.md` in the original folder. Do not skip reference MD in the copy — the package should shrink as a unit.

## Order of Work

1. Duplicate folder per [safe-copy-workflow.md](safe-copy-workflow.md).
2. **extreme only:** plan rename map, rename linked `.md` under `references/`, rewrite all relative links per [extreme-path-shortening.md](extreme-path-shortening.md).
3. Compress `SKILL.md` first (entry point; sets tone for level).
4. Compress each file in `references/` (alphabetical or dependency order is fine).
5. **extreme only:** whitespace pass if not already done per [compression-workflow.md](compression-workflow.md).
6. Run package QA from [quality-checklist.md](quality-checklist.md).

## Frontmatter Rules

`SKILL.md` must keep valid YAML frontmatter:

- **Required keys:** `name`, `description` — never remove keys.
- **`name`:** unchanged (kebab-case skill id).
- **`description`:** may shorten phrasing at medium/heavy/extreme but must remain a usable trigger (`what it does` + `Use when`).
- Do not add compression metadata inside frontmatter; use the `Compression: {level}` body line after `---`.

## Reference Link Integrity

- **light / medium / heavy:** keep filenames and relative paths unchanged; shorten link label text only if the path is unchanged.
- **extreme:** may rename `references/*.md` to short unique stems and rewrite every internal link; see [extreme-path-shortening.md](extreme-path-shortening.md).
- After any rename, every link in `SKILL.md` and all refs must resolve in the copy.
- One-level-deep link style from skill-creator still applies; paths may be shorter at **extreme**.

## Relationship to Other Skills

- Structural formatting of compressed output may use **MD Design System** for headings/lists — **format only**, no fact changes.
- This skill does not replace skill-creator authoring rules; it only shrinks copy in a duplicate package.

## Reporting

After a skill package run, report:

- Copy path (e.g. `skills/foo-cp-heavy/` or `skills/foo-cp-extreme/`)
- Level used
- Files compressed (count and paths)
- **extreme:** full rename map (`old → new`) and confirmation that links were rewritten
- Note that original `skills/foo/` is unchanged
