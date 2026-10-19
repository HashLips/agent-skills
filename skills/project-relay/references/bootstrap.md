# Bootstrap

Create the Relay files in the project the user is working in. Copy text from this skill's `assets/` templates. Create only what is missing.

## Before creating anything

1. Use the real repository root. In a monorepo, use the intended repo or the scoped subproject. Skip an arbitrary parent directory.
2. Stop if that root is a symlink or the filesystem root.
3. Stop if any managed path below is a symlink, or exists as the wrong kind (a file where a directory belongs, or the reverse). Create nothing in that case.
4. Read `AGENTS.md` when it exists. Stop, and create nothing, when the Relay markers are incomplete, repeated, or out of order:
   - `<!-- project-relay:start -->` and `<!-- project-relay:end -->` must occur the same number of times.
   - More than one start marker is a conflict.
   - The start marker must come before the end marker.

Managed paths:

- `.project/`
- `.project/INTENT.md`
- `.project/NOW.md`
- `.project/DECISIONS.md`
- `.project/tasks/`
- `.project/tasks/active/`
- `.project/tasks/done/`
- `.project/tasks/active/.gitkeep`
- `.project/tasks/done/.gitkeep`
- `AGENTS.md`

## Create missing files

1. Create any missing directory in the list above.
2. Copy `assets/INTENT.md`, `assets/NOW.md`, and `assets/DECISIONS.md` only when the matching file is absent.
3. When `tasks/active/` or `tasks/done/` is empty, add an empty `.gitkeep` so the directory can be committed.
4. When `AGENTS.md` is absent, create it with a short heading and the full text of `assets/AGENTS-block.md`.
5. When `AGENTS.md` exists and has no start marker, re-read it. If it changed since the preflight read, stop. Otherwise append `assets/AGENTS-block.md`, with a blank line before it when the file does not already end in a newline.
6. When the complete block is already present, leave `AGENTS.md` unchanged.
7. Report what was created and what was already there.

A second pass must not change the bytes of files that already existed. A partial project is repaired by adding only the missing paths. Report conflicts. Do not reset files to the templates.

## After creation

Template lines that say "not yet established" or "unverified" are unconfirmed. Inspect the repo, README, tickets, and the user's request, then ask for intent that is still unknown. Bootstrap does not invent a product vision, completed tasks, or Git state.

The Relay block in `AGENTS.md` is what the next session sees even when it does not open this skill. That block tells the agent to use Project Relay, bootstrap when `.project/` is missing, and update the tracking files when they already exist.

Creating these files is not permission to commit or push. Run the continuity check in [lifecycle.md](lifecycle.md).
