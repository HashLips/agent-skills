# Task lifecycle and handoff safety

## Task transitions

- `planned` -> `in-progress`: task scope and next action are understood.
- `in-progress` -> `blocked`: a dependency, question, environment, or permission prevents safe progress.
- `in-progress` -> `verification`: implementation is believed finished; acceptance checks still pending.
- `verification` -> `done`: criteria met, evidence recorded, required review obtained.
- `blocked` -> `in-progress`: blocker resolved and documented.

Work may move backward when regressions or changed requirements are discovered. Do not infer completion merely from an agent's statement, a passing compile, or a missing TODO. User acceptance is required whenever explicitly specified, and failed/unavailable checks stay visible.

## Completion procedure

1. Read task acceptance criteria and actual changed artifacts.
2. Run checks available and appropriate to the project; record exact commands, observed results, and limitations. If manual/visual acceptance is required, request it rather than self-approve.
3. Update the task to `done`; add completion date and evidence, then move the file unchanged in identity from `tasks/active/` to `tasks/done/` (use a safe file move or `git mv` where suitable).
4. Remove its pointer from the active section of `NOW.md`. Preserve consequential reasoning in `DECISIONS.md`; keep history in the completed task.
5. Set the next objective from remaining active tasks. Do not fabricate the next task simply to keep work moving.
6. Check the final diff for accidental removals and unrelated changes. Do not stage, commit, push, or deploy without authorization.
7. When the user asks to commit or push, stop once that git operation finishes. Do not update `INTENT.md`, `DECISIONS.md`, `NOW.md`, or task files afterward, and do not record the commit itself as a decision or an intent change.

## Handing off between tools

Before a handoff, summarize in `NOW.md`:

- Which project and worktree were inspected. Do not add an entry just because something was committed or pushed.
- Completed vs incomplete changes, with paths and task IDs.
- Validation that **actually** ran (and what did not).
- Relevant local modifications not synchronized to the source the next agent can access.
- Explicit next action and blockers.

The receiving agent must re-read current files and reconcile them against its own accessible worktree. Treat `.project/NOW.md` as a helpful snapshot, **not** as authority over actual files or Git history. Remote-only agents must not claim awareness of another machine's uncommitted files. Do not copy private local diffs into public project documents.

## Concurrent work and conflicts

- Prefer separate branches or worktrees for agents changing the same project.
- For simultaneous tasks, assign a distinct owner and avoid editing the same `NOW.md` or `DECISIONS.md` concurrently without coordination.
- Before writing, re-read target file and compare with the version examined at the start. If changed unexpectedly, reconcile explicitly; never clobber another agent's work.
- Resolve inconsistent task status or duplicated IDs before further transitions. Keep both versions available if reconciliation is uncertain.

## Self-maintenance rules

At the end of substantive work, remove completed task references from `NOW.md`, retain a compact next action, and update timestamps only for real changes. Keep completed task history in `done/`. Rewrite `INTENT.md` when the intent has actually changed, and compact `DECISIONS.md` when it is past the size limit in [state-contract.md](state-contract.md). A handoff that adds no new evidence should not churn files.

## Continuity check

Run this after bootstrap and before a handoff. Fix every structural problem before treating the handoff as ready.

- `AGENTS.md`, `.project/INTENT.md`, `.project/NOW.md`, and `.project/DECISIONS.md` exist and are normal files.
- `.project/tasks/active/` and `.project/tasks/done/` exist and are normal directories.
- None of those managed paths is a symlink.
- `AGENTS.md` contains exactly one `<!-- project-relay:start -->` and one `<!-- project-relay:end -->`, with the start marker first.
- Every task file is named `TASK-0000-short-slug.md`, with at least four digits and a lowercase slug.
- Each task ID appears once across `active/` and `done/`.
- A file in `active/` does not have status `done`.
- A file in `done/` has status `done` and recorded evidence.
- Every `tasks/active/*.md` link in `NOW.md` points at a file that exists.
- When `NOW.md` still says "not yet established", intent is unconfirmed.

A clean check means the handoff files agree with each other. It does not prove the implementation works, that decisions are correct, that Git is synchronized, or that tests passed.

## Failure or restricted tool access

If unable to inspect code, run checks, edit files, or synchronize with Git, report the exact limitation, label state unverified, and provide patch-ready text rather than pretending the handoff occurred. Skills cannot guarantee compliance in every host; operational verification remains essential.
