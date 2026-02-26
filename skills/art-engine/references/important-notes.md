## Important Notes

### Requirements

- **Complete Setup**: All steps must be executed in sequence to fully configure the project. Do not stop after individual steps.

### Technical Details

- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux. All commands work in bash/zsh/PowerShell. Node.js path handling works cross-platform automatically.
- **CommonJS Syntax**: The Art Engine package uses CommonJS exports. Use `require` syntax: `const { ArtEngine, inputs, generators, renderers, exporters } = require("@hashlips-lab/art-engine");`
- **Inputs Structure**: Inputs must be an object with string keys (e.g., `{ apes: ... }`), not an array.

### Plugin System

- **Architecture**: Art Engine uses a plugin-based architecture with Inputs, Generators, Renderers, and Exporters
- **Execution Flow**: Seed → Inputs → Generators → Renderers → Exporters (see custom-plugins-overview.md)
- **Core Plugins Reference**: Always consult `references/core-plugins-overview.md` for detailed plugin options and configuration patterns

### Dynamic Configuration

The skill should interpret user requirements and configure plugins accordingly:

- **Blockchain Selection**: Include `Erc721MetadataExporter` for Ethereum, `SolMetadataExporter` for Solana, or both
- **Image Size**: Configure `ImageLayersRenderer` width/height based on user request (1K=1024, 2K=2048, 4K=4096, or custom)
- **NFT Count**: Set `startIndex` and `endIndex` in generators based on requested quantity
- **Multiple Datasets**: Create multiple inputs/generators for mixed collections or groups

### Custom Plugins

When users request custom plugins:

- Read `references/custom-plugins-overview.md` to understand the plugin system
- Consult the appropriate interface documentation:
  - `references/custom-plugin-inputs.md` - Loading data from any source
  - `references/custom-plugin-generators.md` - Generating attributes with any logic
  - `references/custom-plugin-renderers.md` - Rendering any media type
  - `references/custom-plugin-exporters.md` - Exporting to any destination
- Create the plugin file in the appropriate `custom/` subdirectory
- Import and use it in `index.ts` alongside or instead of core plugins

### Documentation

- Reference https://lab.hashlips.io/docs/art-engine for detailed plugin documentation
