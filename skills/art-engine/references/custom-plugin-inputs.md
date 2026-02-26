# Custom Input Plugins

This document describes how to create custom input plugins for the Art Engine.

## Interface

All input plugins in the Art Engine implement the `InputInterface<InputDataType>` interface:

```typescript
interface InputInterface<InputDataType> {
  init: (props: InputInitPropsInterface) => Promise<void>;
  load: () => Promise<InputDataType>;
}
```

- `InputInterface<InputDataType>`: This is the main interface for an input plugin. It's parameterized with a generic type, `InputDataType`, which represents the type of data that the input plugin will produce.
- `init(props: InputInitPropsInterface) => Promise<void>`: This method is used to initialize the input plugin. It takes an object of type `InputInitPropsInterface` as an argument, which contains the seed. The method returns a promise that resolves when the initialization is complete.
- `load() => Promise<InputDataType>`: This method is responsible for loading and retrieving the input data. It returns a promise that resolves to an object of type `InputDataType`, which is the actual input data produced by the plugin.

### InputInitPropsInterface

```typescript
interface InputInitPropsInterface {
  seed: string;
}
```

- `seed`: This is a string value that serves as a seed for deterministic behavior. The seed can be used to ensure that the same input plugin produces the same output when initialized with the same seed.

## Example Implementation

```typescript
import InputInterface, {
  InputInitPropsInterface,
} from "@hashlips-lab/art-engine/dist/common/inputs/input.interface";

// Define the structure of the custom input data
interface ExampleCustomInterface {
  example: string;
}

// Create a class for the Inputs plugin
export class ExampleInput implements InputInterface<ExampleCustomInterface> {
  public async init(props: InputInitPropsInterface): Promise<void> {
    // Initialization tasks can be performed here
    // You can use props.seed for deterministic behavior if needed
  }

  public async load(): Promise<ExampleCustomInterface> {
    // Simulate loading input data, replace with actual data retrieval logic
    // This could load from files, APIs, databases, etc.
    return { example: "Hello World" };
  }
}
```

## Implementation Steps

1. **Import Required Interfaces**:
   ```typescript
   import InputInterface, {
     InputInitPropsInterface,
   } from "@hashlips-lab/art-engine/dist/common/inputs/input.interface";
   ```

2. **Define Your Data Type**:
   Create an interface that represents the structure of data your input plugin will provide.

3. **Implement the Interface**:
   - Create a class that implements `InputInterface<YourDataType>`
   - Implement the `init()` method for any setup tasks
   - Implement the `load()` method to retrieve and return your data

4. **Place in Custom Directory**:
   Save your plugin in `custom/inputs/your-input.ts`

5. **Use in Configuration**:
   ```typescript
   const { ExampleInput } = require("./custom/inputs/example-input");
   
   const ae = new ArtEngine({
     inputs: {
       myCustomInput: new ExampleInput(),
     },
     // ... rest of config
   });
   ```

## Use Cases

Custom input plugins can be used to:
- Load data from external APIs
- Read from databases
- Parse custom file formats
- Load data from cloud storage
- Transform existing data formats
- Any other data source that doesn't fit the core ImageLayersInput

## Interface Capabilities

The `InputInterface<InputDataType>` interface is **completely flexible**. The `InputDataType` generic parameter can be **any TypeScript type or interface**, allowing you to:

- **Load Any Data Structure**: Define your own interface for the data you need (arrays, objects, nested structures, etc.)
- **Use Any Data Source**: The `load()` method can fetch from files, APIs, databases, cloud storage, AI services, or any other source
- **Perform Any Operations**: Since `load()` is async, you can perform file I/O, HTTP requests, database queries, image processing, video analysis, etc.
- **Return Any Format**: Return simple values, complex objects, arrays, or any data structure your generators need

### Examples of What's Possible

The interface supports loading:
- **Media Files**: Images, videos, audio files, 3D models, animations
- **External APIs**: REST APIs, GraphQL, AI services (OpenAI, Stable Diffusion, etc.)
- **Databases**: SQL databases, NoSQL databases, in-memory data
- **Cloud Storage**: AWS S3, IPFS, Google Cloud Storage, Azure Blob Storage
- **File Formats**: PSD files, SVG files, JSON, CSV, XML, custom formats
- **Generated Data**: AI-generated content, procedurally generated data, transformed data

### Using External Libraries

You can use **any npm package** in your input plugin. For example:
- `axios` or `node-fetch` for API calls
- `pg`, `mysql2`, `mongodb` for database access
- `aws-sdk` or `@aws-sdk/client-s3` for cloud storage
- `openai`, `@anthropic-ai/sdk` for AI services
- `sharp`, `jimp` for image processing
- `fluent-ffmpeg` for video/audio processing
- Any other package you need

Simply install the package and import it in your plugin file.

## Important Notes

- The `load()` method should return data in a format that generators can consume
- Use the `seed` from `init()` if you need deterministic behavior
- The data type you define (`InputDataType`) can be **any TypeScript type** - define it to match your needs
- Input plugins are executed first in the Art Engine execution flow
- Multiple input plugins can be used simultaneously with different keys
- The `load()` method is async, so you can perform any asynchronous operations (API calls, file I/O, database queries, etc.)
- You can use any npm package - there are no restrictions on dependencies