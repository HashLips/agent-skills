# Canonical Profiles (Recommended Defaults)

## Summary

- These fixed layouts reduce variance.
- Use recommended order per document type.
- Upstream template-required sections always take precedence.

## Skill profile

Required order:

1. YAML frontmatter (`name`, `description` required)
2. `# <Skill Name>`
3. `## Core Rules`
4. `## Workflow`
5. `## Reference Index`
6. `## When To Use This Skill`

Optional:

- `## Context efficiency`

## Agent profile

Required order:

1. `# <Role Name>`
2. `## Identity`
3. `## Role summary`
4. `## Responsibilities`
5. `## Decision framework`
6. `## Constraints`
7. `## Failure modes and recovery`
8. `## Outputs`
9. `## Completion and handoff`
10. `## Collaboration`

Optional:

- `## Optional: Escalation`

## README / guide profile

Required order:

1. `# <Title>`
2. `## Summary`
3. `## Setup` or `## Installation`
4. `## Usage`
5. `## Reference index`

Optional:

- `## FAQ`
- `## Changelog`

## Spec / architecture profile

Required order:

1. `# <Title>`
2. `## Summary`
3. `## Scope`
4. `## Interfaces`
5. `## Decisions`
6. `## Workflow` (if process exists)
7. `## Examples`
8. `## Reference index`

Optional:

- `## Appendix`

## Generic agnostic profile (fallback)

Use this when a document does not cleanly match another profile.

Required order:

1. `# <Title>`
2. `## Summary`
3. `## Core Content`
4. `## Reference index`

Optional:

- `## Workflow`
- `## Examples`
- `## FAQ`
- `## Appendix`

## Profile selection rule

- Pick the closest specific profile first (`skill`, `agent`, `README/guide`, `spec/architecture`).
- If none fits without forcing content, use the **Generic agnostic profile**.
- Preserve template-required sections from upstream skills even when profile-mapping.
- If section intent is unclear, map unknown content into `## Core Content` and keep factual meaning unchanged.

## Extension rule (for upstream template requirements)

- Canonical profiles are defaults, not hard blockers.
- If a source skill/agent template requires extra sections, keep them.
- Place additional required sections in the nearest semantic position (for example decision-related sections near `## Decisions` or operational sections near `## Workflow`).
- If placement is unclear, append under `## Core Content` (or equivalent main body section) without deleting any existing facts.

## Profile rules

- Do not mix profile orders in one file.
- Omit irrelevant optional sections.
- Do not replace required section names with custom variants unless an upstream template explicitly requires the variant.

## File naming rules

- **General markdown files** — use kebab-case filenames (for example `architecture-overview.md`).
- **Agent files** — must use kebab-case and end with `-agent.md` (for example `frontend-developer-agent.md`).
- **Skill entry file** — must be exactly `SKILL.md` (uppercase) in the skill root folder.
- **Reference files** — use kebab-case in `references/` (for example `canonical-syntax.md`).
