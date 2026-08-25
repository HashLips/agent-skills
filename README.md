# Experimental agent skills

This is a work in progress and a build in public snapshot. We use it ourselves first; you are welcome to look around. Nothing here is a product, a service, or a guarantee that it is safe or fit for your use case.

**This repository contains a collection of skills.** A skill is a reusable instruction pack for how an assistant should work: procedures, patterns, constraints, and guidance, usually as a folder with a `SKILL.md` entry file and optional references. You can copy, adapt, or read them for ideas.

The **[agent skill creator](skills/agent-skill-creator/SKILL.md)** is the blueprint we use to create the rest: a tight `SKILL.md`, references for depth, and consistent structure. If you want to build similar skills yourself, start there (it depends on the MD design system skill; see below).

---

## Disclaimer

**Most of the content here is made with AI** (or with significant AI help), then edited by us. We try to keep it useful, but we cannot promise accuracy, completeness, or that it will fit your situation. Please check anything you adopt.

**These skills are experimental.** Behaviour and side effects depend on your environment, tools, and how you use them. Content may change at any time. Review commands, file changes, and security related guidance before you act. Nothing here is legal, financial, or professional advice.

**Use at your own risk.** If you use or copy anything from this repository, you do so on your own judgment. The authors and contributors to this repository are not responsible for any loss, damage, or other harm that may result.

---

## How to use

1. Clone or download this repository.
2. Pick the skill folder you want from `skills/`.
3. Copy that folder into your agent's skills directory.

### Cursor

Copy the skill folder into `.cursor/skills/`, either in the project (local to that repo) or in your user home directory (available across projects).

### Creating your own skills

To use **agent skill creator**, copy **both** of these folders into `.cursor/skills/`:

- `skills/agent-skill-creator`
- `skills/md-design-system`

The creator skill uses the MD design system for the final formatting pass. Without both installed, it cannot follow that contract. Same choice as above: project folder if you only want them in one repo, home directory if you want them everywhere.

### Other agents

The process is the same: copy the skill folder into that agent's configuration skills directory. The path depends on the agent you use, for example:

- Cursor: `.cursor/skills/`
- Claude: `.claude/skills/`
- other agents: `.agent/skills/` (or whatever that product documents)

Project-local copies usually live at the repo root. Machine-wide copies usually live in your home directory.

---

Thanks for stopping by.
