# Project state contract

The protocol is human-readable Markdown about the project itself. Avoid extra indexes, duplicate summaries, chat transcripts, and speculative facts. Never store secret keys, credentials, tokens, raw environment values, or personal data in these files.

## `.project/INTENT.md`: slow-changing context

Include: purpose, problem, target users, outcomes, in-scope, out-of-scope, constraints, and open questions. Label unresolved items. When the goal, audience, scope, or a constraint actually shifts, rewrite those sections in place and make `NOW.md` agree. Leave the file alone when the intent has not changed. Do not silently reinterpret the user's objective.

## `.project/NOW.md`: short-lived handoff snapshot

Keep approximately 30–80 lines where practical. Include:

- **Updated:** timestamp in ISO 8601 with timezone where known.
- **Objective:** one clear sentence, or `Not established`.
- **Active tasks:** links to actual task files, or `None`.
- **Observed state:** what the current agent actually examined, including branch/commit if available.
- **Verification:** passed/failed/not run/unavailable for relevant checks, with evidence where available.
- **Blockers or discrepancies:** exact uncertainty and impact.
- **Next action:** one actionable step; additional steps only if needed.
- **Handoff:** last actor/tool if known and the visibility of local vs remote changes.

Never mark GitHub as up to date simply because local files were modified. If no Git or file access exists, say so.

## `.project/DECISIONS.md`: decisions still in force

Record a decision only when a later agent would choose wrong without it. Each one gets a unique ID:

```markdown
### DEC-0001: Adopt a project-local reporting module
- Status: accepted
- Date: YYYY-MM-DD
- Context: Why a choice was needed.
- Decision: What was selected.
- Reason: Why this option was preferred.
- Scope: Which parts of the project it affects.
- Supersedes: None
```

Use `proposed`, `accepted`, or `superseded` as status labels. To change a decision, add a new entry that names the old ID, and mark the old one `superseded`. Record a tradeoff only when it still matters.

Read the entries that constrain the current task. Do not load the whole log when a few IDs are enough.

When `DECISIONS.md` grows past about 120 lines, compact it before the handoff:

- Replace each `superseded` entry with one line: ID, date, what it was, and which ID replaced it.
- Replace an `accepted` entry the same way when it no longer affects the current intent or active work.
- Leave the full text of every `accepted` or `proposed` decision that still constrains the work.
- Keep every ID. Never reuse one. Do not compact a decision whose meaning is still in dispute.

## `.project/tasks/active/`: unfinished work

File name: `TASK-0001-short-slug.md`; allocate the next unused numeric ID by checking both `active/` and `done/`. Never reuse IDs. Do not rename IDs during a move.

Recommended template:

```markdown
# TASK-0001: Clear task title

- Status: planned
- Owner: unassigned
- Created: YYYY-MM-DD
- Updated: YYYY-MM-DD
- Depends on: None

## Outcome
Describe what success looks like.

## Acceptance criteria
- [ ] A verifiable result.

## Work log
- YYYY-MM-DD: Summary, agent/tool, relevant artifacts.

## Verification
- Not run. Record exact commands/results or manual review evidence.

## Remaining work
- Next actionable step.
```

Possible status values: `planned`, `in-progress`, `blocked`, `verification`, `done`. Tasks in `active/` must not have `done` status. Tasks in `done/` must have `done` status and supporting evidence. Status is not proof on its own.

## `.project/tasks/done/`: durable archive

Preserve original ID, outcome, evidence, and completion date. Do not delete, squash, or periodically truncate completed tasks without explicit retention approval. Point to history from decisions where useful. A large archive can be selectively searched rather than loaded wholesale.

## What should not enter project context

Raw conversation transcripts, copied tool dumps, full diffs, secret keys, credentials, tokens, raw environment values, personal data, duplicated README content, irrelevant meeting notes, and unsupported claims. Link to the authoritative code, issues, PRs, or documentation instead.
