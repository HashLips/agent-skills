# Token Estimation & Context Savvy

**Rough `est_tokens` only — not billing-grade.** Formula: `est_tokens = (chars + 3) // 4` (UTF-8 char count).

## Count

- Include: `.md`, `.txt`, `.mdx`, script sources in package
- Skip dirs: `.git`, `node_modules`, `__pycache__`, `.venv`
- Package total: sum file chars, then one package `est_tokens`

Report in metadata: **Files found**, **Package `est_tokens`**, **Context savvy enough?** (`Yes` / `No` + one-line note).

## Context savvy enough?

| Result | When |
| --- | --- |
| **Yes** | Package ≤ **10,000** `est_tokens`; `SKILL.md` ≤ **5,000**; visible workflow in `SKILL.md`; no `fail` on `POI-01` / `POI-03` / `INJ-05` |
| **No** | Package > **15,000**; or `SKILL.md` > **8,000** without workflow; or flooding `fail`; or package 10,001–15,000 (note: heavy) |

Does **not** affect security verdict.
