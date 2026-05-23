---
name: token-estimator
description: Gives a consistent rough token-size estimate for a file or folder of text using fixed integer rules. Use when you need repeatable ballpark token counts for Markdown or plain text without calling a provider API.
---

# Token Estimator

## Disclaimer

**Rough estimate only — not billing-grade.** Same file on disk → same numbers every run. Real token counts depend on the model’s tokenizer; this skill uses a fixed heuristic (`⌈chars ÷ 4⌉`, English-oriented). Use for ballparks and comparisons, not hard limits.

## What It Does

- **One file** — report `chars` and `est_tokens`.
- **Folder** — recursively count every `.md`, `.txt`, `.mdx` file; report per file plus **total**.
- **Read-only** — never modify targets.

## Workflow

1. Confirm path (file or directory).
2. Run [scripts/estimate_tokens.py](scripts/estimate_tokens.py) when possible; otherwise apply [references/estimation-method.md](references/estimation-method.md).
3. Reply with totals first, then per-file lines only if there is more than one file.

## Rules

1. **Deterministic** — fixed extensions, alphabetical order, integer formula `(chars + 3) // 4`.
2. **Recursive** — walk subdirectories; skip `.git`, `node_modules`, `__pycache__`, `.venv`, binaries.
3. **Label** — always say `est_tokens` or `~tokens`, never imply exact provider counts.

## Output (Minimal)

```text
total: 5376 chars, ~1344 est_tokens
references/foo.md: 1112 chars, ~278 est_tokens
```

One path in the reply is enough unless the user asked for several.

## Reference

- **Formulas and file rules:** [references/estimation-method.md](references/estimation-method.md)

## When To Use

- Ballpark size of a doc, skill folder, or prompt file.
- Same metric applied twice should match (sanity check, before/after edits).
