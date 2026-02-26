## Folder Structure

Create the essential directory structure for the Art Engine project.

### Create directories

**Cross-Platform Note**: These commands work on macOS, Linux, and Windows (PowerShell/Git Bash). Node.js path handling (`__dirname`, forward slashes in template strings) works cross-platform.

```bash
mkdir -p custom/inputs
mkdir -p custom/generators
mkdir -p custom/renderers
mkdir -p custom/exporters
mkdir -p data
mkdir -p output
```

**Windows CMD Alternative** (if needed):
```cmd
mkdir custom\inputs
mkdir custom\generators
mkdir custom\renderers
mkdir custom\exporters
mkdir data
mkdir output
```

### Directory Purpose

- **`custom/`**: Directory for custom plugins (organized by plugin type)
  - `custom/inputs/` - Custom input plugins
  - `custom/generators/` - Custom generator plugins
  - `custom/renderers/` - Custom renderer plugins
  - `custom/exporters/` - Custom exporter plugins
- **`data/`**: Directory for image layers organized by trait categories
- **`output/`**: Directory where generated artwork and metadata will be exported
- **`dist/`**: Directory for compiled TypeScript output (created automatically by build)

### Data Directory Structure

The `data/` directory should contain subdirectories for each trait category. For example:
- `data/Background/`
- `data/Body/`
- `data/Eyes/`
- `data/Mouth/`
- etc.

Each subdirectory should contain the image files for that trait category.

### Important Notes

- Users will add their image layers to the `data/` directory
- Image layers should be organized by trait category in separate folders
- The `custom/` directory is prepared for custom plugin development
