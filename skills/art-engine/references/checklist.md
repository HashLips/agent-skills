# Setup Checklist

After completing all setup steps, verify that everything is in place:

- [ ] Node.js version 20+ verified
- [ ] Node.js project initialized with package.json (with engines field)
- [ ] @hashlips-lab/art-engine installed as dependency
- [ ] TypeScript installed as dependency (not dev dependency)
- [ ] Essential folder structure in place (custom/, data/, output/)
- [ ] TypeScript configuration file created (tsconfig.json)
- [ ] index.ts configured with correct import syntax and core plugins
- [ ] index.ts includes required config: cachePath, outputPath, useCache
- [ ] Data directory structure ready for image layers (with README.md)
- [ ] Project ready for users to add images and run `npm run start`

## Important Reminder

**Before running `npm run start` or any npm commands, ensure Node.js 20+ is active in your terminal:**

1. Check your current Node.js version:
   ```bash
   node --version
   ```

2. If the version is below 20, switch to Node.js 20 using nvm:
   ```bash
   # Load nvm (if not already loaded)
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   
   # Switch to Node.js 20
   nvm use 20
   
   # Verify the switch
   node --version
   ```

3. If you don't have nvm installed, you'll need to install Node.js 20+ manually or install nvm first.

**Note:** You must have Node.js 20+ active in your terminal session before running `npm run start` or any other npm commands.
