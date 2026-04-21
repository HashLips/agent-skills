---
name: md-compressor
description: Compresses Markdown into the lowest-context readable form while preserving facts and intent. Use when agents need to reduce token usage in docs, skills, or prompts without losing meaning.
---

# MD Compressor

Convert verbose Markdown into a dense, human-readable version with minimal context cost.

## Core Rules

1. **Facts are immutable** - never change decisions, requirements, constraints, numbers, or references.
2. **Compression over style** - remove filler, hedging, and rhetorical text first.
3. **Abbreviate aggressively** - abbreviate recurring words and phrases using the canonical map.
4. **Use compression profiles** - apply `standard` by default; use `ultra` only when requested.
5. **Keep scanability** - prefer lists, compact headings, and short clauses.
6. **No semantic drift** - if shortened text risks changing meaning, keep the longer form.

## Workflow

1. Parse source content and identify factual statements.
2. Remove non-factual prose and redundant phrasing.
3. Rewrite remaining content into compact list-first structures.
4. Apply canonical abbreviations from [references/abbreviation-map.md](references/abbreviation-map.md).
5. Apply punctuation and symbol compression from [references/symbol-and-punctuation-policy.md](references/symbol-and-punctuation-policy.md).
6. Run validation with [references/quality-checklist.md](references/quality-checklist.md).

## Compression Profiles

- **standard** - remove filler, shorten syntax, keep normal punctuation.
- **ultra** - remove optional punctuation, use approved symbols, and allow denser phrasing.
- **readability floor** - if `ultra` output is hard to parse in one pass, fall back to `standard`.

## Output Contract

- Output is valid Markdown.
- Preserve heading hierarchy unless flattening is lossless.
- Keep links, paths, command literals, and code blocks intact.
- Add a short abbreviation legend only when non-obvious abbreviations are used.
- State active profile at top: `Profile: standard` or `Profile: ultra`.

## Reference Index

- **Compression method and rewrite order:** [references/compression-workflow.md](references/compression-workflow.md)
- **Canonical abbreviations and expansion policy:** [references/abbreviation-map.md](references/abbreviation-map.md)
- **Symbol and punctuation compression rules:** [references/symbol-and-punctuation-policy.md](references/symbol-and-punctuation-policy.md)
- **Final QA checks for fact and readability safety:** [references/quality-checklist.md](references/quality-checklist.md)

## When To Use This Skill

- Shrinking verbose Markdown for lower context cost.
- Standardizing compact writing across skill and agent docs.
- Preparing dense handoff notes that stay human-readable.
