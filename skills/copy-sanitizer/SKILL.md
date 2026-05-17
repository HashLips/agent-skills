---
name: copy-sanitizer
description: Naturalizes AI-assisted copy by removing statistical fingerprints while preserving the author's tone, meaning, and intent. Use when drafts sound polished but machine-smooth, when glued hyphen words need plain phrasing, or when any body of text needs a light pass to read more naturally.
---

# Copy Sanitizer

Standalone skill for **copy and prose only**: articles, emails, books, scripts, ads, social posts, blurbs, essays, and any pasted text. Format agnostic (plain text, HTML, markdown, or other). Not a formatter, not a rewriter.

## Disclaimer

This skill supports **creative authors who write with AI** as a collaborator. The goal is to smooth clustered model habits so the author's voice reads more naturally.

It is **not** for bypassing human review, impersonation, or gaming detectors. Do not misrepresent authorship or evade disclosure. Polish drafts the author owns and intends to publish.

## Core Rules

1. **Copy first** — Edit readable text the author would speak or publish. Ignore file format unless the user marks regions to preserve.
2. **Zero hyphen joins in copy** — No `word-word` glued forms in output (`human-readable` → `easy to read`). Never add hyphen joins. See [references/hyphen-break-patterns.md](references/hyphen-break-patterns.md).
3. **Pattern over word list** — Fix shapes (joins, connectors, vagueness, sameness); examples in references are illustrative.
4. **Light touch** — Small edits where patterns cluster; keep meaning, facts, and voice.
5. **No fake humanity** — No typos, slang spikes, or forced casualness.
6. **Read all of it** — Work through the full text the user gives. No side tracking files.
7. **Strip markup for readers** — If the paste has markdown (`**bold**`, `#` headings, link syntax), remove symbols; deliver plain copy for books and print ([references/preserve-regions.md](references/preserve-regions.md)).

## Workflow

1. **Intake** — Confirm the copy, audience, and any lines or blocks the user says not to touch.
2. **Read and scan** — [references/detection-patterns.md](references/detection-patterns.md).
3. **Sanitize** — [references/editorial-principles.md](references/editorial-principles.md); strongest clusters first.
4. **Verify** — Zero hyphen joins in copy; preserve regions per [references/preserve-regions.md](references/preserve-regions.md).
5. **Deliver** — Sanitized copy plus a short inline report. [references/quality-checklist.md](references/quality-checklist.md).

## Constraints

- Not a full rewrite or ghostwriting.
- Not a vocabulary ban or find-replace list.
- Not fake errors or hype stripping of a single precise domain term.
- Not bypassing disclosure, review, or detector policies.

## Output Contract

- **Sanitized copy** — Full text returned; same meaning and intent.
- **Short report** — Patterns addressed, change level, hyphen check passed or notes.
- **Voice** — Should still sound like the same author, more natural.

## Reference Index

- **Regions not to edit:** [references/preserve-regions.md](references/preserve-regions.md)
- **Zero hyphen joins:** [references/hyphen-break-patterns.md](references/hyphen-break-patterns.md)
- **What to detect:** [references/detection-patterns.md](references/detection-patterns.md)
- **How hard to push:** [references/scoring-heuristics.md](references/scoring-heuristics.md)
- **How to edit:** [references/editorial-principles.md](references/editorial-principles.md)
- **Long text:** [references/workflow.md](references/workflow.md)
- **QA:** [references/quality-checklist.md](references/quality-checklist.md)

## When To Use This Skill

- AI-assisted draft sounds smooth but not like the author.
- Copy has hyphen-glued words that should be plain speech.
- Connectors, buzz phrasing, or rhythm feel templated.
- Author wants a light naturalizing pass, not a new article.
