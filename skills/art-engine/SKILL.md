---
name: art-engine
description: Sets up an Art Engine 2.0 project for creating generative layered NFT artworks with correct structure, dependencies, configuration, and plugin scaffolding. Use when you need to initialize a complete Art Engine project or regenerate its setup based on updated requirements.
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

**IMPORTANT:** Present the disclaimer above to the user and wait for them to acknowledge or continue. Once they proceed (by asking to continue, accepting, or providing any input), you may proceed with the setup steps.

---

## Core Workflow

When setting up a new Art Engine 2.0 project:

1. Initialize the Node.js project and base configuration.
2. Install core dependencies.
3. Create the required folder structure.
4. Configure TypeScript.
5. Configure Art Engine itself and its core plugins based on user requirements.
6. Set up data directories for assets, layers, and metadata.
7. Run the verification checklist and surface any issues to the user.

---

## Non-Negotiable Rules

- Always present and honor the disclaimer before executing any setup commands.
- Execute setup steps in order; do not skip required steps.
- Never hard-code secrets or wallet keys into generated files.
- Use Node.js 20+ for reliable engine behavior.
- Keep custom plugin logic in the dedicated plugin folders.

---

## Output Contract

A correctly initialized Art Engine project should:

- have all required folders and config files in place
- have dependencies installed and TypeScript configured
- have Art Engine config wired to the requested blockchain, image size, NFT count, and datasets
- have data directories ready for artwork layers and metadata
- pass the verification checklist without blocking errors

---

## Reference Index

- Node.js project initialization and base package setup: [references/initialize-project.md](references/initialize-project.md)
- Dependency installation steps and required packages: [references/install-dependencies.md](references/install-dependencies.md)
- Required folder structure for the Art Engine project: [references/folder-structure.md](references/folder-structure.md)
- TypeScript configuration for Art Engine projects: [references/tsconfig.md](references/tsconfig.md)
- Art Engine configuration details and core settings: [references/art-engine-config.md](references/art-engine-config.md)
- Overview of built-in core plugins and behavior: [references/core-plugins-overview.md](references/core-plugins-overview.md)
- Data directories for layers, assets, and metadata: [references/data-structure.md](references/data-structure.md)
- Verification checklist for completed setup and Node.js version guidance: [references/checklist.md](references/checklist.md)
- Important notes, requirements, and caveats: [references/important-notes.md](references/important-notes.md)
- Custom plugin development overview and plugin types: [references/custom-plugins-overview.md](references/custom-plugins-overview.md)
- Custom plugin renderer contracts and patterns: [references/custom-plugin-renderers.md](references/custom-plugin-renderers.md)
- Custom plugin generator contracts and patterns: [references/custom-plugin-generators.md](references/custom-plugin-generators.md)
- Custom plugin exporter contracts and patterns: [references/custom-plugin-exporters.md](references/custom-plugin-exporters.md)
- Inputs and parameters for custom plugins: [references/custom-plugin-inputs.md](references/custom-plugin-inputs.md)

