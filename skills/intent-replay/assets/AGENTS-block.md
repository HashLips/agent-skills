<!-- intent-replay:start -->
## Intent Replay

Before other work in this repository:

1. Use the `intent-replay` skill.
2. If `.project/` is missing or incomplete, bootstrap the missing Intent Replay files. Do not overwrite existing content.
3. If `.project/` already exists, read `.project/NOW.md` first, then intent, the active task, and the decisions that still apply. Reconcile them with the files and Git state you can actually see. Update intent when it actually changes. Record only decisions a later agent would need, and keep that log short. Update task progress, validation, and `NOW.md` as the work changes.
4. Move tasks to `tasks/done/` only after their acceptance criteria are met and evidenced. Preserve history.
5. Ask before destructive or remote actions. Never record secret keys, credentials, tokens, or personal data in `.project/`. Do not claim unsynchronized local changes are visible remotely.
6. When the user asks to commit or push, or just after a commit or push, do not update intent, decisions, or `NOW.md`. Leave the tree as the commit left it.

The project files, not previous chats, are the handoff. In a conflict, keep both sides and surface the uncertainty.
<!-- intent-replay:end -->
