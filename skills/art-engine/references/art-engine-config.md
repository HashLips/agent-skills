# Art Engine Configuration

Create the main `index.ts` file that configures and runs the Art Engine with core plugins.

**IMPORTANT**: Before creating the configuration, read `references/core-plugins-overview.md` to understand all available plugin options and configuration patterns. Interpret the user's requirements from their request and configure plugins dynamically based on their needs.

## Summary

- Defines the canonical `index.ts` setup for Art Engine.
- Requires dynamic configuration based on user requirements.
- Uses CommonJS imports and project-root-aware path resolution.

## File
`index.ts`

## Configuration

**CRITICAL IMPORT NOTE**: The Art Engine package uses CommonJS exports. Use `require` syntax, not ES6 imports.

**CROSS-PLATFORM NOTE**: The path handling in this configuration works on both Windows and macOS/Linux. Node.js automatically handles path separators (`/` vs `\`), and `__dirname` works correctly on all platforms.

**PATH RESOLUTION NOTE**: When TypeScript compiles to the `dist/` directory, `__dirname` will point to `dist/`, not the project root. Use `path.join(__dirname, "..")` to correctly resolve paths to the project root (where `data/`, `output/`, and `cache/` directories are located).

**DYNAMIC CONFIGURATION**: The configuration below is a DEFAULT example. You MUST customize it based on user requirements:

- **Blockchain**: Include exporters based on user request (Ethereum, Solana, or both)
- **Image Size**: Set width/height based on user request (1K, 2K, 4K, or custom dimensions)
- **NFT Count**: Set startIndex/endIndex based on requested quantity
- **Datasets**: Create multiple inputs/generators if user wants multiple groups or mixed collections

See `references/core-plugins-overview.md` for all configuration options and common patterns.

```typescript
const {
  ArtEngine,
  inputs,
  generators,
  renderers,
  exporters,
} = require("@hashlips-lab/art-engine");
const path = require("path");

// Get project root (one level up from dist directory when compiled)
const BASE_PATH = path.join(__dirname, "..");

const ae = new ArtEngine({
  cachePath: `${BASE_PATH}/cache`,
  outputPath: `${BASE_PATH}/output`,
  useCache: false,

  inputs: {
    // Define the input plugin (ImageLayersInput) to load image layers
    apes: new inputs.ImageLayersInput({
      assetsBasePath: `${BASE_PATH}/data`,
    }),
  },

  generators: [
    // Define the generator plugin (ImageLayersAttributesGenerator) to generate attributes for each item
    new generators.ImageLayersAttributesGenerator({
      dataSet: "apes", // Must match the key in inputs object
      startIndex: 1,   // First item ID
      endIndex: 10,    // Last item ID (generates items 1-10)
    }),
  ],

  renderers: [
    // Define the renderer plugins to render the attributes and image layers
    new renderers.ItemAttributesRenderer({
      name: (itemUid: string) => `Ape ${itemUid}`,
      description: (attributes: any) => {
        return `This is a token with "${attributes["Background"][0]}" as Background`;
      },
    }),
    new renderers.ImageLayersRenderer({
      width: 2048,
      height: 2048,
    }),
  ],

  exporters: [
    // Define the exporter plugins to export the generated artwork and metadata
    new exporters.ImagesExporter(),
    new exporters.Erc721MetadataExporter({
      imageUriPrefix: "ipfs://__CID__/",
    }),
    new exporters.SolMetadataExporter({
      imageUriPrefix: "ipfs://__CID__/",
      symbol: "APES",
      sellerFeeBasisPoints: 200,
      collectionName: "The Apes",
      creators: [
        {
          address: "__SOLANA_WALLET_ADDRESS_HERE__",
          share: 100,
        },
      ],
    }),
  ],
});

(async () => {
  await ae.run();
  await ae.printPerformance();
})();
```

## Configuration Details

- **Import Syntax**: Must use CommonJS `require` syntax: `const { ArtEngine, inputs, generators, renderers, exporters } = require("@hashlips-lab/art-engine");`
- **Path Module**: Import `path` module: `const path = require("path");`
- **BASE_PATH**: Use `path.join(__dirname, "..")` to get the project root path (one level up from the compiled `dist/` directory)
- **Inputs Structure**: `inputs` must be an **object** with string keys (e.g., `{ apes: ... }`), NOT an array
- **ImageLayersInput**: 
  - Parameter is `assetsBasePath` (path to data directory)
  - Loads image layers from the specified directory
- **ImageLayersAttributesGenerator**: 
  - Requires `dataSet` (must match input key), `startIndex`, and `endIndex`
  - Generates items from `startIndex` to `endIndex` (inclusive)
  - Layer order is determined by folder structure in `data/`, not by a parameter
- **ImageLayersRenderer**: Renders the combined layers into final images (default 2048x2048)
- **ItemAttributesRenderer**: Renders item attributes metadata with optional name/description functions
- **Exporters**: 
  - **ImagesExporter**: Exports to `outputPath/images/` (or custom folder)
  - **Erc721MetadataExporter**: Exports to `outputPath/erc721_metadata/` (or custom folder)
  - **SolMetadataExporter**: Exports to `outputPath/sol_metadata/` (or custom folder)
- **Required Config Properties**:
  - `cachePath`: Directory for cache files (e.g., `${BASE_PATH}/cache`)
  - `outputPath`: Base output directory (e.g., `${BASE_PATH}/output`)
  - `useCache`: Boolean to enable/disable caching (typically `false` for fresh generation)

## Configuration Based on User Requirements

**You MUST interpret user requirements and configure accordingly:**

1. **Blockchain Selection**:
   - "Ethereum" or "ERC721" → Include `Erc721MetadataExporter` only
   - "Solana" → Include `SolMetadataExporter` only
   - "Both" or "Ethereum and Solana" → Include both exporters
   - Default (if not specified) → Include `Erc721MetadataExporter` only

2. **Image Size**:
   - "1K" or "1024" → `width: 1024, height: 1024`
   - "2K" or "2048" → `width: 2048, height: 2048` (default)
   - "4K" or "4096" → `width: 4096, height: 4096`
   - Custom dimensions → Use specified width/height

3. **NFT Count**:
   - User says "200 NFTs" → `startIndex: 1, endIndex: 200`
   - User says "100 items" → `startIndex: 1, endIndex: 100`
   - User specifies range → Use specified startIndex/endIndex

4. **Multiple Datasets/Groups**:
   - User mentions "two groups", "mixed", "multiple datasets" → Create multiple inputs and generators
   - Each group needs its own input (different `assetsBasePath`) and generator (different `dataSet` and non-overlapping indices)

**Reference**: See `references/core-plugins-overview.md` for detailed plugin options, all configuration parameters, and common configuration patterns.

## Using Custom Plugins

When users request custom plugins, refer to `references/custom-plugins-overview.md` and the appropriate interface documentation:
- Input plugins: `references/custom-plugin-inputs.md`
- Generator plugins: `references/custom-plugin-generators.md`
- Renderer plugins: `references/custom-plugin-renderers.md`
- Exporter plugins: `references/custom-plugin-exporters.md`

Import and use custom plugins in the configuration:
```typescript
const { ExampleInput } = require("./custom/inputs/example-input");

const ae = new ArtEngine({
  inputs: {
    custom: new ExampleInput(),
    // Mix with core plugins as needed
  },
  // ... rest of config
});
```

## Important Notes

- **CommonJS Syntax**: Use `require` instead of ES6 imports
- **Inputs vs Generators**: The `dataSet` in the generator must match the key used in the `inputs` object
- **Item Count**: Adjust `startIndex` and `endIndex` to control how many NFTs are generated
- **Layer Order**: Layer order is automatically determined by the folder structure in `data/` directory
- **Image Dimensions**: Adjust `width` and `height` in `ImageLayersRenderer` as needed
- **Plugin Reference**: Always consult `references/core-plugins-overview.md` for complete plugin documentation
- **Custom Plugins**: When creating custom plugins, follow the interfaces in `references/custom-plugin-*.md` files
- **Documentation**: See https://lab.hashlips.io/docs/art-engine for detailed plugin options
