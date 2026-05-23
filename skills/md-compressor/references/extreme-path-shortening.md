# Extreme Path Shortening

## When This Applies

**extreme** skill-package runs only, inside the duplicate copy. **light**, **medium**, and **heavy** must not rename files or change relative link targets.

Goal: shrink tokens spent on paths and filenames so an **agent** can navigate the package — not humans browsing a folder tree.

## What May Change (Copy Only)

| Item | extreme action |
| --- | --- |
| Files under `references/` | Rename to short, unique `.md` names |
| Relative links in any `.md` | Rewrite to match renames |
| Link label text | Shorten or drop if path carries meaning |
| `SKILL.md` filename | **Do not rename** |
| Frontmatter `name` | **Do not rename** |
| `assets/**`, binaries | **Do not rename** unless another file links to them by path — then shorten only when link rewrites are updated |
| External URLs, CLI paths, env vars in body | **Unchanged** |

## What Must Not Change

- Facts, requirements, and command literals inside file bodies.
- Skill id (`name` in frontmatter).
- Target of each link — same document after rename, not a different file.

## Naming Rules

1. **Plan a rename map first** — list every `references/*.md` (and any other linked `.md` in the copy) before renaming.
2. **Unique stems** — no two files may collide after rename.
3. **Machine-clear** — short but still guessable by an agent, e.g. `boiled-egg.md` → `boil.md`, `equipment-and-ingredients.md` → `eq.md`, `safety-and-troubleshooting.md` → `saf.md`.
4. **Prefer shortest unambiguous token** — often 2–8 characters before `.md`.
5. **kebab-case** — lowercase, hyphens only; no spaces.
6. **Keep `.md` extension** — parsers and skill tooling expect it.
7. **Use abbreviation-map tokens** when they match the topic (`refs` folder name stays `references/` unless user requests otherwise — see below).

## Optional Folder Shortening

Only when **every** link in the copy is rewritten and tooling still resolves paths:

- `references/` → `r/` saves tokens on repeated links.
- Default: **keep `references/`** unless the package has many cross-links and a full link pass to `r/` is done.
- Never leave a mix of `references/` and `r/` in one package.

## Workflow (Extreme Package)

1. Duplicate folder → `…-cp-extreme/`.
2. Inventory linked `.md` files (from `SKILL.md` index + cross-refs in refs).
3. Draft rename map: `old-name.md` → `new.md` (short, unique).
4. Rename files on disk in the copy.
5. Rewrite **all** relative links in **every** `.md` file (including ref-to-ref).
6. Compress content: **heavy** → whitespace pass per [compression-workflow.md](compression-workflow.md).
7. Verify every link resolves (no broken targets).

## Link Rewrite Hints

- Prefer minimal paths: `[refs/boil.md](refs/boil.md)` or `[boil.md](references/boil.md)` — pick one style for the whole package.
- Drop verbose link labels when the path is enough: `[references/fried-egg.md](references/fried-egg.md)` → `[references/fr.md](references/fr.md)` or `references/fr.md` inline in extreme index lines.
- If two refs had similar short names, lengthen one stem (`saf.md` vs `safe.md`) until unique.

## Example Map (Illustrative)

| Original | Extreme |
| --- | --- |
| `references/boiled-egg.md` | `references/boil.md` |
| `references/fried-egg.md` | `references/fr.md` |
| `references/scrambled-egg.md` | `references/scr.md` |
| `references/equipment-and-ingredients.md` | `references/eq.md` |
| `references/safety-and-troubleshooting.md` | `references/saf.md` |

## Reporting

Include in the delivery report:

- Copy path
- Full rename map (`old → new`)
- Confirmation that all internal links were rewritten
- Note that the original package paths are unchanged

## Revert Rule

If a short name is ambiguous for an agent (two topics could match `egg.md`) → use a longer stem (`boil.md`, `fr.md`) or revert that one file to **heavy** naming only (keep longer filename, still compress body).
