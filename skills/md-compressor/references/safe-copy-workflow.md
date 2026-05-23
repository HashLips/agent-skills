# Safe Copy Workflow

## Goal

Produce compressed Markdown in a disposable copy. The source skill or file must remain unchanged.

## Before Any Edit

1. Identify the compression level: `light`, `medium`, `heavy`, or `extreme`.
2. Identify the source: skill folder, directory of MD files, or single file.
3. Create the duplicate (rules below).
4. Tell the user: source path, copy path, level.
5. Run compression only inside the copy path.

## Skill Folder Duplicate

When the target is a skill package (folder containing `SKILL.md`):

1. Copy the entire folder recursively to a sibling directory.
2. Use naming: `{original-folder-name}-cp-{level}`.
   - Examples: `skills/art-engine/` → `skills/art-engine-cp-medium/` or `skills/art-engine-cp-extreme/`
3. Preserve folder layout (`references/`, `assets/`, etc.).
4. Compress only `.md` and plain-text files inside the copy.
5. Leave binaries, images, fonts, and other non-text assets as byte-identical copies.

## Single Markdown File Duplicate

When the target is one file:

1. Duplicate in the same parent directory.
2. Use naming: `{basename}.cp-{level}.md`.
   - Example: `notes.md` → `notes.cp-light.md`
3. Compress only the duplicate file.

## Directory of Markdown (Not a Skill)

When the target is a folder without `SKILL.md` but with multiple MD files:

1. Duplicate the whole folder: `{folder-name}-cp-{level}/`.
2. Compress every `.md` file in the copy using the chosen level.

## Do Not

- Edit files in the original folder after duplication.
- Overwrite the source without creating a named copy first.
- Delete the source unless the user explicitly asks (compression never implies deletion).
- Reuse an old `-cp-*` folder as the source for a new run without user confirmation (prefer a fresh duplicate from pristine source).

## After Compression

- Report approximate token or character reduction if easy to estimate.
- List files compressed in the copy.
- **extreme skill packages:** include ref rename map (`old → new`) per [extreme-path-shortening.md](extreme-path-shortening.md).
- Remind the user that originals are untouched.
- For **heavy / extreme**, note that some nuance may be trimmed but the copy must still be agent-executable (what to do, order, constraints).
