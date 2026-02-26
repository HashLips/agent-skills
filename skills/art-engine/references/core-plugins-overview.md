# Core Plugins Overview

This document provides an overview of all core Art Engine plugins and common configuration patterns.

## Plugin Categories

### Inputs
- **ImageLayersInput**: Loads image layers from a directory structure
  - Parameter: `assetsBasePath` (required) - Path to folder containing image layers
  - Use for: Loading image layers organized by trait categories

### Generators
- **ImageLayersAttributesGenerator**: Generates random layer combinations and attributes
  - Parameters: `dataSet` (required), `startIndex` (required), `endIndex` (required)
  - Use for: Generating NFT attributes based on image layer inputs

### Renderers
- **ImageLayersRenderer**: Combines image layers into final artwork images
  - Parameters: `width` (required), `height` (required), `imageProcessor` (optional)
  - Use for: Rendering layered images at specified dimensions
- **ItemAttributesRenderer**: Renders item attributes metadata
  - Parameters: `name` (optional function), `description` (optional function)
  - Use for: Rendering metadata attributes for exporters

### Exporters
- **ImagesExporter**: Exports generated images to a folder
  - Parameter: `imagesFolder` (optional, default: "images")
  - Use for: Exporting rendered artwork images
- **Erc721MetadataExporter**: Exports ERC721 (Ethereum) NFT metadata
  - Parameters: `metadataFolder` (optional, default: "erc721_metadata"), `imageUriPrefix` (optional)
  - Use for: Creating Ethereum/ERC721 compatible metadata
- **SolMetadataExporter**: Exports Solana NFT metadata
  - Parameters: `metadataFolder` (optional), `symbol` (optional), `sellerFeeBasisPoints` (optional), `collectionName` (optional), `collectionFamily` (optional), `creators` (optional), `imageUriPrefix` (optional)
  - Use for: Creating Solana compatible metadata

## Common Configuration Patterns

### Pattern 1: Ethereum Only (Default)

```typescript
const {
  ArtEngine,
  inputs,
  generators,
  renderers,
  exporters,
} = require("@hashlips-lab/art-engine");

const BASE_PATH = __dirname;

const ae = new ArtEngine({
  cachePath: `${BASE_PATH}/cache`,
  outputPath: `${BASE_PATH}/output`,
  useCache: false,

  inputs: {
    apes: new inputs.ImageLayersInput({
      assetsBasePath: `${BASE_PATH}/data`,
    }),
  },

  generators: [
    new generators.ImageLayersAttributesGenerator({
      dataSet: "apes",
      startIndex: 1,
      endIndex: 100,
    }),
  ],

  renderers: [
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
    new exporters.ImagesExporter(),
    new exporters.Erc721MetadataExporter({
      imageUriPrefix: "ipfs://__CID__/",
    }),
  ],
});

(async () => {
  await ae.run();
  await ae.printPerformance();
})();
```

### Pattern 2: Solana Only

```typescript
exporters: [
  new exporters.ImagesExporter(),
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
```

### Pattern 3: Both Ethereum and Solana

```typescript
exporters: [
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
```

### Pattern 4: Multiple Datasets (Mixed Collection)

```typescript
inputs: {
  group1: new inputs.ImageLayersInput({
    assetsBasePath: `${BASE_PATH}/data/group1`,
  }),
  group2: new inputs.ImageLayersInput({
    assetsBasePath: `${BASE_PATH}/data/group2`,
  }),
},

generators: [
  new generators.ImageLayersAttributesGenerator({
    dataSet: "group1",
    startIndex: 1,
    endIndex: 100,
  }),
  new generators.ImageLayersAttributesGenerator({
    dataSet: "group2",
    startIndex: 101,
    endIndex: 200,
  }),
],
```

### Pattern 5: 4K Resolution

```typescript
renderers: [
  new renderers.ImageLayersRenderer({
    width: 4096,
    height: 4096, // 4K
  }),
  new renderers.ItemAttributesRenderer(),
],
```

### Pattern 6: Custom Image Sizes

- **1K**: `width: 1024, height: 1024`
- **2K**: `width: 2048, height: 2048` (default)
- **4K**: `width: 4096, height: 4096`
- **Custom**: Any width/height values

## Important Notes

- **Inputs Structure**: Must be an object with string keys, NOT an array
- **Dataset Matching**: The `dataSet` in generators must match a key in the `inputs` object
- **Index Ranges**: Generator indices should not overlap unless intentionally creating duplicates
- **Image Dimensions**: Square images are most common, but rectangular dimensions are supported
- **Exporters**: You can include multiple exporters (e.g., both Ethereum and Solana)
- **Layer Order**: Layer order is automatically determined by folder structure in the data directory
- **Multiple Generators**: Each generator can reference a different dataset, allowing mixed collections
- **BASE_PATH**: Use `__dirname` to get the current directory path in CommonJS
