# Custom Exporter Plugins

This document describes how to create custom exporter plugins for the Art Engine.

## Interface

All exporter plugins in the Art Engine implement the `ExporterInterface` interface:

```typescript
interface ExporterInterface {
  init: (props: ExporterInitPropsInterface) => Promise<void>;
  export: () => Promise<void>;
}
```

- `ExporterInterface`: This interface outlines the structure that exporter plugins should adhere to.
- `init(props: ExporterInitPropsInterface) => Promise<void>`: This method initializes the exporter plugin. It takes an object of type `ExporterInitPropsInterface` as an argument, containing the necessary initialization properties. The method returns a promise that resolves when the initialization is complete.
- `export() => Promise<void>`: This method is responsible for executing the export process. It returns a promise that resolves when the export process is complete.

### ExporterInitPropsInterface

```typescript
interface ExporterInitPropsInterface {
  seed: string;
  outputPath: string;
  rendersGetter: ItemsDataManager["getRenders"];
}
```

- `seed`: A string value that serves as a seed for deterministic behavior. Similar to other plugins, this can be used to ensure consistent results when exporting.
- `outputPath`: A string representing the path where the exporter plugin should export its content. This could be a directory where generated files, metadata, or assets will be saved.
- `rendersGetter`: A reference to a function called `getRenders` from the `ItemsDataManager`. This function is used to access the rendered data produced by the renderers.

## Example Implementation

```typescript
import * as path from "path";
import * as fs from "fs";
import ExporterInterface, {
  ExporterInitPropsInterface,
} from "@hashlips-lab/art-engine/dist/common/exporters/exporter.interface";
import ItemsDataManager from "@hashlips-lab/art-engine/dist/utils/managers/items-data/items-data.manager";
import { ItemPropertiesInterface } from "@hashlips-lab/art-engine/dist/utils/managers/items-data/items-data.interface";

// Create a class for the Exporter plugin
export class ExampleExporter implements ExporterInterface {
  private rendersGetter!: ItemsDataManager["getRenders"];
  private outputPath!: string;

  public async init(props: ExporterInitPropsInterface) {
    this.rendersGetter = props.rendersGetter;
    this.outputPath = props.outputPath;
    // Initialization tasks can be performed here
    // Create output directory if it doesn't exist
    if (!fs.existsSync(this.outputPath)) {
      fs.mkdirSync(this.outputPath, { recursive: true });
    }
  }

  public async export(): Promise<void> {
    for (const [itemUid, renders] of Object.entries(this.rendersGetter())) {
      // Filter renders by kind to find the ones this exporter processes
      const relevantRender = renders.find(
        (render: ItemPropertiesInterface<any>) =>
          "AnyUniqueRenderDataIdentifier@v1" === render.kind
      );

      if (relevantRender) {
        // Export the render data
        const sourcePath = relevantRender.data.path;
        const destinationPath = path.join(this.outputPath, `${itemUid}.txt`);
        fs.copyFileSync(sourcePath, destinationPath);
      }
    }
  }
}
```

## Implementation Steps

1. **Import Required Interfaces**:
   ```typescript
   import ExporterInterface, {
     ExporterInitPropsInterface,
   } from "@hashlips-lab/art-engine/dist/common/exporters/exporter.interface";
   import ItemsDataManager from "@hashlips-lab/art-engine/dist/utils/managers/items-data/items-data.manager";
   import { ItemPropertiesInterface } from "@hashlips-lab/art-engine/dist/utils/managers/items-data/items-data.interface";
   ```

2. **Implement the Interface**:
   - Create a class that implements `ExporterInterface`
   - Store `rendersGetter` and `outputPath` from `init()`
   - Implement the `init()` method to set up the exporter
   - Implement the `export()` method to process renders and export them

3. **Filter Renders by Kind**:
   Use the `kind` identifier to find the renders your exporter should process:
   ```typescript
   const relevantRender = renders.find(
     (render) => render.kind === "YourRendererKind@v1"
   );
   ```

4. **Place in Custom Directory**:
   Save your plugin in `custom/exporters/your-exporter.ts`

5. **Use in Configuration**:
   ```typescript
   const { ExampleExporter } = require("./custom/exporters/example-exporter");
   
   const ae = new ArtEngine({
     exporters: [
       new ExampleExporter(),
     ],
     // ... rest of config
   });
   ```

## Accessing Renders

Use the `rendersGetter` function to access renders produced by renderers:

```typescript
// Get all renders for all items
const allRenders = this.rendersGetter();

// Iterate over items
for (const [itemUid, renders] of Object.entries(allRenders)) {
  // Process renders for this item
  // Filter by kind to find relevant renders
  const relevantRender = renders.find(
    (render) => render.kind === "YourRendererKind@v1"
  );
  
  if (relevantRender) {
    // Export the render data
  }
}
```

## Output Path

The `outputPath` is the base output directory. You can create subdirectories within it:

```typescript
const customOutputPath = path.join(this.outputPath, "my-custom-folder");
if (!fs.existsSync(customOutputPath)) {
  fs.mkdirSync(customOutputPath, { recursive: true });
}
```

## Use Cases

Custom exporter plugins can be used to:
- Export to custom file formats
- Upload to cloud storage
- Send to APIs
- Create custom metadata formats
- Package files in specific ways
- Any other export logic

## Interface Capabilities

The `ExporterInterface` interface is **completely flexible**, allowing you to:

- **Export Any Media Type**: Images, videos, audio, 3D models, metadata, or any other content
- **Use Any Export Method**: File system writes, cloud storage uploads, API calls, database writes, or any other export mechanism
- **Access Any Renders**: Use `rendersGetter()` to access renders from any renderer plugin, then filter by `kind` to find the ones you need
- **Perform Any Operations**: Since `export()` is async, you can perform file I/O, HTTP requests, database operations, format conversions, etc.

### Examples of What's Possible

The interface supports exporting:
- **File Formats**: Any file format (images, videos, audio, 3D models, documents, etc.)
- **Cloud Storage**: AWS S3, IPFS, Google Cloud Storage, Azure Blob Storage, or any cloud service
- **APIs**: REST APIs, GraphQL, webhooks, or any external service
- **Databases**: SQL databases, NoSQL databases, or any data store
- **Multiple Formats**: Export the same content in multiple formats simultaneously
- **Custom Packaging**: ZIP files, tarballs, custom archives, or any packaging format
- **Metadata Formats**: JSON, XML, YAML, CSV, or any custom metadata format

### Using External Libraries

You can use **any npm package** in your exporter plugin. For example:
- **Cloud Storage**: `aws-sdk`, `@aws-sdk/client-s3`, `ipfs-http-client` for cloud uploads
- **APIs**: `axios`, `node-fetch`, `graphql-request` for API calls
- **File Processing**: `sharp`, `fluent-ffmpeg` for format conversion
- **Archives**: `archiver`, `yauzl` for creating/extracting archives
- **Databases**: `pg`, `mysql2`, `mongodb` for database writes
- Any other package you need

Simply install the package and import it in your plugin file.

### Processing Multiple Renders

You can process renders from multiple renderers:

```typescript
for (const [itemUid, renders] of Object.entries(this.rendersGetter())) {
  const imageRender = renders.find(render => render.kind === "ImageRender@v1");
  const videoRender = renders.find(render => render.kind === "VideoRender@v1");
  const metadataRender = renders.find(render => render.kind === "MetadataRender@v1");
  // Process and export as needed
}
```

### Output Organization

The `outputPath` is the base directory. You can organize exports however you need:

```typescript
// Create subdirectories for different content types
const imagesPath = path.join(this.outputPath, "images");
const videosPath = path.join(this.outputPath, "videos");
const metadataPath = path.join(this.outputPath, "metadata");

// Or organize by item
const itemPath = path.join(this.outputPath, `item-${itemUid}`);
```

## Important Notes

- The `kind` identifier must match the `kind` from the renderer renders you want to process
- Exporters run last in the Art Engine execution flow
- Multiple exporters can be used simultaneously
- Always create output directories if they don't exist
- The `outputPath` is the base path - create subdirectories as needed
- Exporters receive renders from all renderers, so filter by `kind` to find the ones you need
- The `export()` method is async, so you can perform any asynchronous operations (file I/O, API calls, uploads, etc.)
- You can use any npm package - there are no restrictions on dependencies
- You can export to multiple destinations (local files, cloud storage, APIs, databases) in a single exporter