# Compression Levels

## End Goal (All Levels)

Compression saves tokens. **Heavier levels may lose non-essential context** (tone, stories, extra examples) — that is expected.

**Non-negotiable at every level:** an agent using only the compressed copy can still determine **what to do**, **in what order**, and **what must not be violated**. Facts, constraints, and executable literals stay exact.

| May trim more at higher levels | Must never sacrifice |
| --- | --- |
| Encouragement, personality, “why this matters” | Required steps and decisions |
| Redundant examples and duplicate explanations | Numbers, limits, versions, timings |
| Edge-case color when core rule is preserved elsewhere | `must` / `must not` and safety negations |
| Human scan comfort | Links, literals, and triggers that enable execution |

**Parse gate:** if a human or agent cannot recover actionable intent from a line → revert that line or use a lighter level for that fragment. **extreme** has the lowest human readability but the same executability bar as **heavy**.

## Overview

Four levels trade readability and optional context for token savings.

| Level | Primary tactic | Structure | Whitespace | Abbreviations |
| --- | --- | --- | --- | --- |
| **light** | Remove filler; shorten clauses | Keep | Keep | Rare; expand uncommon terms |
| **medium** | Dense lists; key:value lines | Keep | Trim optional | Canonical map |
| **heavy** | Token minimum; machine-first | Collapse if lossless | Minimal blank lines | Map + dense shorthand |
| **extreme** | Heavy + whitespace strip + short ref paths | Flatten to few lines; may rename linked `.md` | Remove blank lines, extra spaces, most line breaks | Map + heavy tokens freely |

## Light

**Intent:** Smallest human-readable version that still scans like normal Markdown.

- Remove motivational framing, hedging, and duplicate explanations.
- Convert long paragraphs to short bullets when meaning is unchanged.
- Shorten sentences; one idea per bullet.
- Keep headings, list markers, blank lines between sections, and normal punctuation.
- Do not use abbreviation map except universally clear forms (`e.g.`, `i.e.`).
- Readability floor: a human should parse each section in one pass.
- Executability: agent can follow the skill intent with minimal loss of nuance.

## Medium

**Intent:** Light plus systematic density — still usable by humans, optimized for agents.

- Apply everything in **light**.
- Apply [abbreviation-map.md](abbreviation-map.md) for repeated domain terms.
- Apply [symbol-and-punctuation-policy.md](symbol-and-punctuation-policy.md) at **medium** tier.
- Prefer `label: value` over full sentences where unambiguous.
- Drop final periods in bullets; remove commas that do not change parse meaning.
- Merge adjacent bullets that share one subject.
- First-use expansion only when an abbreviation is ambiguous.

## Heavy

**Intent:** Strong token reduction; **machine-parseable** beats human-readable.

- Apply **medium** tactics where they still save tokens.
- Strip nearly all decorative whitespace: one blank line max between major sections; none between bullets when safe.
- Use canonical abbreviations freely; add a one-line legend at file top only for non-map dense tokens.
- Allow dense patterns when facts stay exact:
  - `if X -> Y` for conditionals
  - `req|must|...` style packed rules (same line only when unambiguous)
  - `&` in short labels; `->`, `>=`, `<=`, `!=` per symbol policy
- Collapse redundant heading scaffolding if intent is unchanged (e.g. merge two thin `##` sections).
- Do not break YAML frontmatter, fenced code, URLs, paths, or command literals.
- **Skill `description` in frontmatter:** shorten wording but keep `what + Use when` trigger pattern intelligible.

## Extreme

**Intent:** Maximum token reduction — **whitespace is cost**. Files may look like a single thin strip of text; agents must still recover full intent.

- Apply **heavy** semantic compression first (facts, abbreviations, symbols).
- Then run a **whitespace pass** on the copy only:
  - **No blank lines** in the body (zero `\n\n`).
  - **No decorative line breaks** — join bullets, sections, and short headings onto as few physical lines as possible.
  - **Minimize spaces** — remove spaces around `|`, `;`, `->`, `,` when parse stays unambiguous; no double spaces; no trailing spaces.
  - Prefer `##Title` or `## Title` with one space only when the parser requires it.
  - Pack list items inline with `|` or `;` instead of one item per line when safe.
- **Keep required structure only:**
  - YAML frontmatter block (`---` … `---`) on its own lines — do not collapse frontmatter.
  - `Compression: extreme` line immediately after frontmatter (one line).
  - Fenced code blocks, URLs, paths, CLI, and regex — literals unchanged; do not remove spaces inside them.
- **Skill `description`:** shorten to shortest usable trigger; `name` unchanged.
- **Readability:** not a goal.
- **Executability:** an agent reading the copy alone must still know what to do — same actionable requirements as the source; tone and optional context may be gone.
- **Parse gate:** if executability fails, revert fragment to **heavy** or restore the dropped requirement.
- If a line becomes ambiguous after whitespace stripping → keep one line break or one space, or revert that fragment to **heavy** form.
- **Path shortening (skill packages):** rename `references/*.md` (and other linked `.md` in the copy) to minimal unique stems; rewrite every relative link. Details: [extreme-path-shortening.md](extreme-path-shortening.md). Do not rename `SKILL.md` or frontmatter `name`.

## Level Selection

- User says nothing → **light**.
- User says "medium", "aggressive", or "more compression" → **medium**.
- User says "heavy", "minimum tokens", or "machine only" → **heavy**.
- User says **"extreme"**, "max compression", "strip whitespace", or "thinnest possible" → **extreme**.
- If **extreme** would drop a requirement or break a literal → step down to **heavy** for that fragment only.
- If **heavy** would drop a requirement → step down to **medium** for that line only.

## File Header

First line of every compressed file body (after frontmatter `---` block for skills):

```text
Compression: light
```

Use `Compression: medium`, `Compression: heavy`, or `Compression: extreme` accordingly. Place immediately after closing `---` when frontmatter exists.
