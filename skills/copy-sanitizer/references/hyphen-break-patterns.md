# Hyphen-Break Patterns

## Core rule

**No banned-word list. No banned punctuation everywhere.** Target **join patterns in running prose** and **statistical repetition**.

Fix how words are glued. Keep meaning. Use separate words or a normal phrase.

## What to flag (shapes)

| Pattern type | Shape | Illustrative samples only |
| --- | --- | --- |
| Editorial prefix join | `de-…`, `re-…` + word | `re-scan`, `de-AI` |
| Technology prefix join | `XX-…` label + modifier | `AI-powered` |
| Stacked modifiers | 2+ hyphen modifiers + noun | `high-impact, data-driven rollout` |
| `over-` repetition | several in one section | `over-optimize`, `over-explain` |
| Metric-style join | role words joined | `before/after`, `pre/post` |
| Jargon pile | clustered vague compounds | consultant-style `-` chains |

Samples are **not** exhaustive. Apply the shape in any domain.

## What is not the target

See [context-allowlist.md](context-allowlist.md). In short:

- Skill `name` and paths (`copy-sanitizer`, `references/foo.md`)
- List markers `-` and ordered `1.`
- Label/value bullets per MD design system (`- **field** — value`)
- Code, frontmatter, URLs, tracking keys
- One correct hyphen in running prose

## Rewrite direction

Unpack joins in **prose** only. Examples:

| Shape | Plain rewrite |
| --- | --- |
| `re-…` verb | scan again, run a second pass |
| `de-…` coinage | clean the draft, remove generated habits |
| prefix + hype adjective | plain noun phrase |
| stacked modifiers | one modifier or separate clause |
| `before/after` in prose | first pass and second pass |

Never swap one hyphen pile for another.

## Skill package prose

This skill's **instructions** use plain words. Its **layout** follows agent-skill-creator and md-design-system (kebab names, label lines, `-` lists).

## Self-check

1. Classify context ([context-allowlist.md](context-allowlist.md)).
2. Search **prose only** for editorial joins and modifier stacks.
3. Read aloud. Product-copy rhythm → unpack joins in sentences, not in required list syntax.

## User documents

Flag clustering in prose. Respect host skill and repo markdown contracts.
