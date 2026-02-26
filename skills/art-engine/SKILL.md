---
name: art-engine
description: Sets up an Art Engine 2.0 project for creating generative layered NFT artworks. Use when you need to initialize a complete Art Engine project with proper structure, dependencies, and configuration. Automatically configures plugins based on user requirements (blockchain, image size, NFT count, datasets) and supports custom plugin development.
---

## ⚠️ IMPORTANT: Disclaimer

**CRITICAL - MUST EXECUTE FIRST:** Before proceeding with any setup steps, you MUST present the following disclaimer to the user:

---

### Disclaimer

This skill is provided for **educational purposes only**. This automated setup process will:

- Create directories and files on your system
- Install Node.js packages and dependencies
- Modify your system configuration
- Execute commands that may affect your development environment

**WARNING:** Skills can be dangerous if not trusted or if executed without understanding what they do. Please review the skill documentation before proceeding.

**Liability Disclaimer:** Hashlips will not be liable for any damages, data loss, or issues that may occur from using this skill, especially if the user has not read and understood the skill documentation before execution. Use this skill at your own risk.

**By continuing with the setup, you acknowledge that you have read and understood this disclaimer.**

---

**IMPORTANT:** Present the disclaimer above to the user and wait for them to acknowledge or continue. Once they proceed (by asking to continue, accepting, or providing any input), you may proceed with the setup steps.

---

## Steps (apply in order)

**EXECUTE ALL STEPS:** Execute all steps sequentially in one go to fully set up the Art Engine project.

1) Initialize Node.js project → references/initialize-project.md
2) Install dependencies → references/install-dependencies.md
3) Create folder structure → references/folder-structure.md
4) TypeScript configuration → references/tsconfig.md
5) Art Engine configuration → references/art-engine-config.md
   - Read references/core-plugins-overview.md before configuring
   - Interpret user requirements (blockchain, image size, NFT count, datasets)
   - Configure plugins dynamically based on user needs
6) Data directory structure → references/data-structure.md

## Verification

After completing all steps, verify setup → references/checklist.md

**IMPORTANT:** After setup is complete, notify the user that they must ensure Node.js 20+ is active in their terminal before running `npm run start`. Provide instructions on how to switch to Node.js 20 using nvm (see checklist.md for details).

## Additional Information

- Important notes and requirements → references/important-notes.md
- Custom plugin development → references/custom-plugins-overview.md

