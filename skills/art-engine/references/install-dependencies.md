# Install Dependencies

Install the required dependencies for the Art Engine project.

**CRITICAL:** Before installing dependencies, verify that Node.js 20+ is active in the current shell session:
```bash
node --version  # Must show v20.x.x or higher
```

If Node.js 20+ is not active, refer back to the Node.js version check in `initialize-project.md` and use nvm to switch to Node.js 20 before proceeding.

### Command

Install the Art Engine package and TypeScript:

**Cross-Platform Note**: These commands work on macOS, Linux, and Windows (PowerShell/Git Bash).

**CRITICAL PERMISSION NOTE**: This command must be run with `required_permissions: ['all']` from the start to avoid npm cache permission errors. Do not attempt without full permissions first.

```bash
npm install @hashlips-lab/art-engine typescript
```

**Required Permissions**: Use `required_permissions: ['all']` when executing this command to prevent npm cache permission issues that would otherwise require a retry.

### Dependencies

- **@hashlips-lab/art-engine**: The core Art Engine 2.0 package (required)
- **typescript**: TypeScript compiler for the project (required, not a dev dependency in the template)

### Important Notes

- **TypeScript as Dependency**: In the Art Engine template, TypeScript is installed as a regular dependency, not a dev dependency, to ensure it's available in all environments
- **Network Access**: This step requires network access to download packages from npm
- **Permissions**: Always use `required_permissions: ['all']` when running npm install to avoid cache permission errors
