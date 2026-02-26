## Initialize Node.js Project

**CRITICAL:** This is the first step and must be executed before any other steps.

### Node.js Version Check and Setup

**REQUIREMENT:** Node.js version 20 or higher MUST be active before proceeding with any npm commands.

**CRITICAL:** Execute these commands to ensure Node.js 20+ is installed and active:

1. Check current Node.js version:
```bash
node --version
```

2. If the version is below 20, use nvm to install and switch to Node.js 20:
```bash
# Load nvm if available (nvm is a shell function, not a binary)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # Load nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # Load nvm bash_completion

# Install Node.js 20 if not already installed, then switch to it
if type nvm &> /dev/null; then
  nvm install 20  # This installs Node 20 if not present, or uses existing if available
  nvm use 20      # Switch to Node 20
  node --version  # Verify Node 20+ is now active
else
  echo "ERROR: nvm not found. Node.js 20+ must be installed and active before proceeding."
  echo "Please install Node.js 20+ manually or install nvm first."
fi
```

3. **VERIFY:** After the above steps, confirm Node.js 20+ is active by running `node --version` again. Only proceed with project initialization once Node.js 20+ is confirmed active.

**Important:** All subsequent npm commands (including `npm init` and `npm install`) must run with Node.js 20+ active in the same shell session.

### Command

Initialize a new Node.js project in a new directory. By default, use `art-engine-project` as the directory name, or use the directory name specified by the user in their prompt:

**Cross-Platform Note**: These commands work on macOS, Linux, and Windows (PowerShell/Git Bash). For Windows CMD, use separate commands or `mkdir` without `-p`.

**Default (art-engine-project directory):**
```bash
mkdir -p art-engine-project && cd art-engine-project && npm init -y
```

**User-specified directory:**
If the user specifies a different directory name in their prompt, replace `art-engine-project` with the specified directory name:
```bash
mkdir -p [DIRECTORY_NAME] && cd [DIRECTORY_NAME] && npm init -y
```

**Windows CMD Alternative** (if needed):
```cmd
mkdir art-engine-project
cd art-engine-project
npm init -y
```

### Package.json Configuration

After initialization, update the `package.json` to include:
- `"engines"` field specifying Node.js 20+ requirement: `"engines": { "node": ">=20.0.0" }`
- `"scripts"` section with build and start scripts that clean the dist directory:
  ```json
  "scripts": {
    "start": "rm -rf ./dist && tsc && node dist/index.js",
    "build": "rm -rf ./dist && tsc"
  }
  ```
- Appropriate project metadata (description, keywords, etc.)

**Important Scripts Note**: The scripts must clean the `dist/` directory before building to ensure fresh compilations and correct path resolution. Use `rm -rf ./dist` (macOS/Linux) or equivalent for Windows.

**Important:** 
- The directory must be empty or non-existent before running this command
- This creates the foundation for the Art Engine project
