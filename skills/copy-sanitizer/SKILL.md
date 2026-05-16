---
name: copy-sanitizer
description: Sanitizes and naturalizes generated copy by removing statistical fingerprints while preserving tone, structure, intent, and host-skill layout rules. Use when text sounds polished but obviously from a model, when cleaning drafts without rewriting voice, or when processing long documents with tracked comparison metrics.
---

# Copy Sanitizer

Light editorial pass on running prose. Removes clustered generated habits without breaking voice, host skills, or required markdown syntax.

## Disclaimer

This skill exists to support **creative authors who write with AI** as a collaborator. The goal is to smooth clustered model habits so the author's voice reads more naturally on the page.

It is **not** for bypassing human review, impersonation, or "proving" text is human. Do not use it to misrepresent authorship, evade disclosure policies, or game detectors. Use it to polish drafts the author already owns and intends to publish under their name.

## Core Rules

1. **Pattern over word list** — Score shapes (joins, connectors, vagueness, sameness); reference examples are illustrative only.
2. **Context first** — Classify document type and host skills before editing ([references/context-allowlist.md](references/context-allowlist.md)).
3. **Prose only** — Do not strip kebab paths, list markers, `- **label** — value` lines, frontmatter, or code for naturalness.
4. **Light touch** — Edit clustered repeats; preserve meaning, voice, and layout contracts.
5. **No fake humanity** — No typos, forced casualness, or invented mistakes.
6. **Measure first** — Scan, edit, scan again; use [references/scoring-heuristics.md](references/scoring-heuristics.md).

## Workflow

1. **Intake** — Scope, output path, tracking file, context, host skills (e.g. agent-skill-creator, md-design-system).
2. **First scan** — Prose regions per [references/detection-patterns.md](references/detection-patterns.md); log to [references/tracking-file.md](references/tracking-file.md).
3. **Plan** — Strongest clusters first; skip allowlisted syntax.
4. **Sanitize** — Minimal edits per [references/editorial-principles.md](references/editorial-principles.md).
5. **Second scan** — Update metrics and residual level.
6. **Deliver** — Sanitized copy, report, tracking file on large jobs. Run [references/quality-checklist.md](references/quality-checklist.md).

## Constraints

- Not for bypassing human verification, detectors, or disclosure requirements.
- Not a full rewrite, ghostwriting, or voice replacement engine.
- Not a pinned vocabulary ban or find-replace word list.
- Not a license to break agent-skill-creator or md-design-system layout when sanitizing skill repos.
- Not fake-error injection or hype stripping of domain-standard terms used once.

## Output Contract

- **Sanitized copy** — Same meaning and structure; layout contracts intact.
- **Change log** — Pattern types addressed, not every micro-edit.
- **Comparison stats** — Punctuation, connectors, vague vocab clusters, hyphen joins, structure (first pass vs second pass).
- **Residual level** — `low`, `medium`, or `high`, with hotspot notes.
- **Tracking file** — `.copy-sanitizer-track.md` for section/document mode (schema in reference).

## Reference Index

- **Required dashes and host-skill layout:** [references/context-allowlist.md](references/context-allowlist.md)
- **Hyphen-break shapes in prose:** [references/hyphen-break-patterns.md](references/hyphen-break-patterns.md)
- **Generic detection categories:** [references/detection-patterns.md](references/detection-patterns.md)
- **Density scoring and residual levels:** [references/scoring-heuristics.md](references/scoring-heuristics.md)
- **What to change vs preserve:** [references/editorial-principles.md](references/editorial-principles.md)
- **Chunked document workflow:** [references/workflow.md](references/workflow.md)
- **Tracking file template and rollup:** [references/tracking-file.md](references/tracking-file.md)
- **Pre-delivery QA:** [references/quality-checklist.md](references/quality-checklist.md)

## When To Use This Skill

- Naturalize or sanitize copy without a full rewrite.
- Prose sounds too smooth, connector-heavy, or vague.
- Sanitize a skill repo without breaking `SKILL.md` or reference layout.
- Long markdown or books need session tracking and comparison metrics.
