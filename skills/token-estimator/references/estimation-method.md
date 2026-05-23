# Estimation Method

## Formula

```text
est_tokens = (chars + 3) // 4    # integer ceiling, chars ÷ 4
```

`chars` = Unicode length of UTF-8 file contents. Same file → same result.

Based on the common English heuristic (1 token ≈ 4 characters). Less accurate for other languages, code, and symbol-heavy text; `chars` stays comparable everywhere.

## Files To Count

**Include:** `.md`, `.txt`, `.mdx`  
**Skip dirs:** `.git`, `node_modules`, `__pycache__`, `.venv`, `venv`  
**Skip:** non-text files, unreadable UTF-8, files over 2 MB

**Walk:** recurse into all subdirectories. Sort paths alphabetically before summing.

## Manual Steps (No Script)

1. List files per rules above.
2. Read each as UTF-8; sum `chars`.
3. Per file: `est_tokens = (chars + 3) // 4`.
4. Total: sum chars, then apply formula once on the total (same as summing per-file estimates).

## Optional Exact Reference

If `tiktoken` is installed, `len(encoding.encode(text))` with `cl100k_base` may be reported separately as `ref_tokens` — still model-specific, not universal.

## Do Not

- Claim exact tokens without naming a model tokenizer.
- Change the divisor per run or per language.
