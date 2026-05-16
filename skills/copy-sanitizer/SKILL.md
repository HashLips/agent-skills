---
name: copy-sanitizer
description: Sanitizes and naturalizes generated copy by removing statistical fingerprints while preserving tone, structure, intent, and host-skill layout rules. Use when text sounds polished but obviously from a model, when cleaning drafts without rewriting voice, or when processing any length document as normal text.
---

# Copy Sanitizer

Light editorial pass on running prose. Removes clustered generated habits without breaking voice, host skills, or required markdown syntax.

## Disclaimer

This skill exists to support **creative authors who write with AI** as a collaborator. The goal is to smooth clustered model habits so the author's voice reads more naturally on the page.

It is **not** for bypassing human review, impersonation, or "proving" text is human. Do not use it to misrepresent authorship, evade disclosure policies, or game detectors. Use it to polish drafts the author already owns and intends to publish under their name.

## Core Rules

1. **Zero hyphen joins in prose** — Running prose must not contain words glued with hyphens (`human-readable`, `re-scan`, stacked modifiers). Unpack to separate words or rephrase. Never add hyphen joins in the rewrite. Details: [references/hyphen-break-patterns.md](references/hyphen-break-patterns.md).
2. **Pattern over word list** — Score shapes (joins, connectors, vagueness, sameness); reference examples are illustrative only.
3. **Context first** — Classify document type and host skills before editing ([references/context-allowlist.md](references/context-allowlist.md)).
4. **Prose only** — Do not strip kebab paths, list markers, `- **label** — value` lines, frontmatter, or code.
5. **Light touch** — Edit clustered repeats; preserve meaning, voice, and layout contracts.
6. **No fake humanity** — No typos, forced casualness, or invented mistakes.
7. **Read the whole document** — Treat the file as normal text end to end. No sidecar tracking files or session ledgers.

## Workflow

1. **Intake** — Confirm source document, context, and host skills (e.g. agent-skill-creator, md-design-system).
2. **Read and scan** — Analyze full text; mark prose vs syntax regions per [references/detection-patterns.md](references/detection-patterns.md).
3. **Sanitize** — Minimal edits per [references/editorial-principles.md](references/editorial-principles.md); strongest pattern clusters first.
4. **Verify** — Re-read prose; confirm **no hyphen joins** remain in sentences (allowlist syntax only).
5. **Deliver** — Sanitized document plus a short inline report. Run [references/quality-checklist.md](references/quality-checklist.md).

## Constraints

- Not for bypassing human verification, detectors, or disclosure requirements.
- Not a full rewrite, ghostwriting, or voice replacement engine.
- Not a pinned vocabulary ban or find-replace word list.
- Not a license to break agent-skill-creator or md-design-system layout when sanitizing skill repos.
- Not fake-error injection or hype stripping of domain-standard terms used once.
- **No hyphen joins in sanitized prose output**, including editorial coinages and "readable" style compounds.

## Output Contract

- **Sanitized copy** — Full document returned; meaning and layout contracts intact.
- **Short report** — Pattern types addressed, approximate change level, residual notes.
- **Hyphen join check** — Confirm prose has zero `word-word` hyphen joins outside the allowlist.

## Reference Index

- **Required dashes vs prose (allowlist):** [references/context-allowlist.md](references/context-allowlist.md)
- **Zero hyphen joins in prose:** [references/hyphen-break-patterns.md](references/hyphen-break-patterns.md)
- **Generic detection categories:** [references/detection-patterns.md](references/detection-patterns.md)
- **Density scoring:** [references/scoring-heuristics.md](references/scoring-heuristics.md)
- **What to change vs preserve:** [references/editorial-principles.md](references/editorial-principles.md)
- **Long documents (in-memory only):** [references/workflow.md](references/workflow.md)
- **Pre-delivery QA:** [references/quality-checklist.md](references/quality-checklist.md)

## When To Use This Skill

- Naturalize or sanitize copy without a full rewrite.
- Prose has glued words with hyphens that should be plain phrasing.
- Drafts sound too smooth, connector-heavy, or vague.
- Sanitize a skill repo without breaking `SKILL.md` or reference layout.
