---
name: intent-replay
description: Tracks intent, decisions, and handoffs in .project when this repository's code or other source material changes. Use before that work. First check whether .project exists. If it does not, bootstrap it before continuing. If it does, update intent when the goal changes and record the decisions later work must follow. A commit or push is not a reason to write these files. After a commit or push, leave the tree as it is.
license: MIT
compatibility: Works with any agent that can read and edit project files.
metadata:
  version: "1.0.0"
  category: project-continuity
---

# Intent Replay

## Purpose

Maintain one durable, agent-independent source of project intent, decisions, active work, and verified handoffs. **The repository owns project context; no agent's conversation is authoritative.** Intent Replay coordinates context, not model selection, commits, or deployments.

## Non-Negotiable Rules

1. **Start with Intent Replay.** Before other work in the repository, look for `.project/` and the Intent Replay block in `AGENTS.md`. If either is missing, bootstrap. If both exist, read them and keep the tracking files current as the work changes. Do not skip this step, and do not start a second tracking system. The `AGENTS.md` block is the standing order that tells the next agent to do the same. A commit or push does not start this update.
2. **Bootstrap safely.** At the intended project root, create missing Intent Replay files and the `AGENTS.md` integration. Never reset, truncate, replace, or delete existing project content. If initialization cannot be performed, explain the blocker and provide the exact proposed changes.
3. **Read before acting.** Inspect `AGENTS.md`, `.project/NOW.md`, `.project/INTENT.md`, the relevant active task, and only the decisions needed for the task. Reconcile the snapshot with the repository and accessible Git state before trusting it.
4. **Validate continuity.** After bootstrap and before the final handoff, run the continuity check in [references/lifecycle.md](references/lifecycle.md). Fix structural problems. A clean check is not proof the implementation works.
5. **Never fabricate progress.** Label facts as observed, reported, planned, or unverified. Never represent an unrun test, remote-only view, or prior agent claim as verified.
6. **Update at meaningful boundaries, not per message.** Update `INTENT.md` when the goal, audience, scope, or a constraint actually changes. Record a decision only when a later agent would choose wrong without it. Update tasks when scope, implementation, blockers, or validation changes. Refresh `NOW.md` so it matches the current intent and the decisions still in force. Keep both files short. A commit, push, or sync to GitHub is not one of these updates.
7. **Stop after a commit.** When the user asks to commit or push, or when a commit or push has just happened, do not edit `.project/` or the Intent Replay block afterward. Do not record that the commit happened in intent, decisions, or `NOW.md`. Leave any uncommitted Intent Replay edits out of that follow-up. The tree stays as the commit left it.
8. **Archive tasks; compact old decisions.** Move accepted and verified tasks from `tasks/active/` to `tasks/done/`. Keep task IDs and evidence. When `DECISIONS.md` grows past about 120 lines, compact superseded decisions, and accepted decisions that no longer affect the work, down to one line each. Keep every decision ID. Do not silently complete work or remove task files.
9. **Respect permissions and conflicts.** Do not commit, push, merge, deploy, install integrations, or run destructive commands without authorization. Detect concurrent edits and discrepancies; preserve both sides and request a resolution rather than overwriting.
10. **Do not store secrets or personal data.** `.project/` records where the project is and what it is trying to do. Never write secret keys, credentials, tokens, raw environment values, private chat transcripts, or personal data into these files.

## Workflow

### 1. Bootstrap, or continue

1. Identify the *actual* workspace/repository root. In a monorepo use the intended repository or explicitly scoped subproject, not an arbitrary parent directory.
2. If `.project/` or the Intent Replay block is missing, follow [references/bootstrap.md](references/bootstrap.md). Copy missing files from this skill's `assets/` templates. Create only missing paths.
3. If `.project/` and the Intent Replay block already exist, do not bootstrap again. Continue with the resume, record, and handoff steps below.
4. Inspect existing `AGENTS.md` instructions for conflicts. A generated Intent Replay block supplements, never supersedes, existing rules.
5. Report what was added and what already existed. For a new project, **ask for the intent when unknown**; placeholders are explicitly unconfirmed, not project facts.

### 2. Resume reliably

1. Read `.project/NOW.md` first, then `.project/INTENT.md` and the referenced active task. Read matching entries in `.project/DECISIONS.md` only as needed.
2. Inspect actual code, files, and available Git state (`status`, branch, recent changes) within available permissions. Distinguish local uncommitted changes from remote history and record the visibility boundary.
3. Identify stale claims, conflicting plans, missing tasks, or unverified results. Reconcile only what can be established; otherwise flag the uncertainty and stop any action that could overwrite work.
4. State the current objective and next safe action briefly before executing.

### 3. Work and record

1. For substantial work, create or reuse an active task using [references/state-contract.md](references/state-contract.md). Do not invent tasks for trivial edits.
2. Keep acceptance criteria, progress, links to changed artifacts, and validation evidence on that task. Preserve the original user intent and decisions.
3. Add a consequential decision to `DECISIONS.md` with reasoning and scope. Supersede an older decision by a new ID. Compact the log when it grows past the limit in [references/state-contract.md](references/state-contract.md).
4. If an agent lacks write access, provide a proposed change or patch; never claim the shared project state was updated.

### 4. Complete, clean, and hand off

1. Apply [references/lifecycle.md](references/lifecycle.md): verify acceptance criteria, record actual check results, and confirm approvals if required.
2. Move a task to `done/` only when genuinely complete; otherwise leave it in `active/` with the precise blocker or remaining work. Do not delete completed tasks automatically.
3. Rewrite `NOW.md` as a compact, accurate current snapshot: goal, active task pointers, verified state, blockers, next action, handoff provenance, and visibility limits. Remove stale completed work from the active snapshot, not from history.
4. Compare files against their pre-write state to avoid lost updates. If concurrent work changed the same file, reconcile or stop instead of clobbering it.
5. Run the continuity check, resolve any consistency errors, then tell the user what changed, what was validated, where the work lives, and what remains. Never imply a commit or synchronization occurred unless confirmed.
6. Do this recording before a requested commit, never after one. If the user asked only to commit or push, skip the recording and leave the files untouched.

## Working set

```text
AGENTS.md
.project/
  INTENT.md
  NOW.md
  DECISIONS.md
  tasks/
    active/
    done/
```

## Reference Index

Load a reference only when that operation is needed.

- **Initialization and existing-file protection:** [references/bootstrap.md](references/bootstrap.md)
- **File contracts, task IDs, and decision records:** [references/state-contract.md](references/state-contract.md)
- **Completion, cleanup, and cross-agent handoffs:** [references/lifecycle.md](references/lifecycle.md)

## When To Use This Skill

- Before a change to this repository's code or other source material.
- When `.project/` is missing, so it is bootstrapped before that work continues.
- When `.project/` already exists, so intent and decisions stay current.
- When resuming in another agent, completing work, or handing off.
- A request to commit or push is not a trigger to update these files.
