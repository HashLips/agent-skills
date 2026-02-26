# Custom Generator Plugins

This document describes how to create custom generator plugins for the Art Engine.

## Interface

All generator plugins in the Art Engine implement the `GeneratorInterface<GeneratorDataType>` interface:

```typescript
interface GeneratorInterface<GeneratorDataType> {
  init: (props: GeneratorInitPropsInterface) => Promise<void>;
  generate: () => Promise<ItemsAttributes<GeneratorDataType>>;
}
```

- `GeneratorInterface<GeneratorDataType>`: This is a generic interface. `GeneratorDataType` specifies the type of data that the generator will produce, which corresponds to the type of data that the `ItemsAttributes` interface is parameterized with.
- `init(props: GeneratorInitPropsInterface) => Promise<void>`: This method is used to initialize the generator. It takes an object of type `GeneratorInitPropsInterface` as an argument, containing the seed and inputs manager. It returns a promise that resolves when the initialization is complete.
- `generate() => Promise<ItemsAttributes<GeneratorDataType>>`: This method is responsible for generating the attributes for items. It returns a promise that resolves to an object conforming to the structure defined by `ItemsAttributes<GeneratorDataType>`. This object maps item UIDs to arrays of attributes.

### ItemsAttributes

```typescript
interface ItemsAttributes<AttributeDataType> {
  [itemUid: string]: ItemPropertiesInterface<AttributeDataType>[];
}
```

This structure maps item unique identifiers (item UIDs) to arrays of attribute data. Each item UID serves as a key, and its corresponding value is an array of attributes, where each attribute has a specific format defined by the `ItemPropertiesInterface`.

### GeneratorInitPropsInterface

```typescript
interface GeneratorInitPropsInterface {
  seed: string;
  inputsManager: InputsManager;
}
```

- `seed`: This is a string value that serves as a seed for deterministic generation. Deterministic generation ensures that the same input will always produce the same output, which can be useful for testing and reproducibility.
- `inputsManager`: This is an instance of the `InputsManager` class. The `InputsManager` is used to manage and access the data produced by input plugins. It allows the generator to retrieve data from various input sources, such as images or text, and use it in the generation process.

### ItemPropertiesInterface

Each attribute in the array must have a `kind` and `data` property:

```typescript
{
  kind: "YourUniqueIdentifier@v1",
  data: {
    // Your custom data structure
  }
}
```

- `kind`: A unique string identifier for this type of attribute (e.g., `"MyCustomAttribute@v1"`)
- `data`: The actual attribute data matching your `GeneratorDataType`

## Example Implementation

```typescript
import GeneratorInterface, {
  GeneratorInitPropsInterface,
  ItemsAttributes,
} from "@hashlips-lab/art-engine/dist/common/generators/generator.interface";
import InputsManager from "@hashlips-lab/art-engine/dist/utils/managers/inputs/inputs.manager";

// Define the structure of the custom generator data
interface ExampleCustomInterface {
  example: string;
}

// Create a class for the Generator plugin
export class ExampleGenerator
  implements GeneratorInterface<ExampleCustomInterface>
{
  inputsManager!: InputsManager;

  public async init(props: GeneratorInitPropsInterface): Promise<void> {
    this.inputsManager = props.inputsManager;
    // Initialization tasks can be performed here
    // You can use props.seed for deterministic behavior if needed
  }

  public async generate(): Promise<ItemsAttributes<ExampleCustomInterface>> {
    // Simulate fetching input data, replace with actual data retrieval logic
    const inputData = this.inputsManager.get("any_existing_input_key");

    // Generate and structure the custom data for each item
    const items: ItemsAttributes<ExampleCustomInterface> = {
      1: [
        {
          kind: "AnyUniqueGeneratorDataIdentifier@v1",
          data: {
            example: inputData.example,
          },
        },
      ],
      2: [
        {
          kind: "AnyUniqueGeneratorDataIdentifier@v1",
          data: {
            example: "Another example",
          },
        },
      ],
      // Add more items as needed
    };

    return items;
  }
}
```

## Implementation Steps

1. **Import Required Interfaces**:
   ```typescript
   import GeneratorInterface, {
     GeneratorInitPropsInterface,
     ItemsAttributes,
   } from "@hashlips-lab/art-engine/dist/common/generators/generator.interface";
   import InputsManager from "@hashlips-lab/art-engine/dist/utils/managers/inputs/inputs.manager";
   ```

2. **Define Your Data Type**:
   Create an interface that represents the structure of data your generator will produce.

3. **Implement the Interface**:
   - Create a class that implements `GeneratorInterface<YourDataType>`
   - Store `inputsManager` from `init()` for accessing input data
   - Implement the `init()` method for any setup tasks
   - Implement the `generate()` method to create attributes for each item
   - Return an object mapping item UIDs to arrays of attributes with `kind` and `data`

4. **Use Unique Kind Identifiers**:
   Each attribute must have a unique `kind` identifier (e.g., `"MyCustomGenerator@v1"`)

5. **Place in Custom Directory**:
   Save your plugin in `custom/generators/your-generator.ts`

6. **Use in Configuration**:
   ```typescript
   const { ExampleGenerator } = require("./custom/generators/example-generator");
   
   const ae = new ArtEngine({
     generators: [
       new ExampleGenerator(),
     ],
     // ... rest of config
   });
   ```

## Accessing Input Data

Use the `inputsManager` to access data from input plugins:

```typescript
// Get data from an input plugin by its key
const inputData = this.inputsManager.get("inputKey");

// Use the input data in your generation logic
```

## Use Cases

Custom generator plugins can be used to:
- Generate attributes based on custom algorithms
- Create variations from input data
- Apply randomization with specific rules
- Generate metadata for non-image assets
- Create complex attribute combinations
- Any other attribute generation logic

## Interface Capabilities

The `GeneratorInterface<GeneratorDataType>` interface is **completely flexible**. The `GeneratorDataType` generic parameter can be **any TypeScript type or interface**, allowing you to:

- **Generate Any Attributes**: Define your own interface for the attributes you generate (simple values, complex objects, nested structures, etc.)
- **Use Any Generation Logic**: The `generate()` method can use algorithms, AI, randomization, weighted probabilities, external APIs, or any other logic
- **Access Any Input Data**: Use `inputsManager.get()` to access data from any input plugin
- **Return Any Structure**: Return attributes with any data structure - as long as each attribute has `kind` and `data` properties

### Examples of What's Possible

The interface supports generating:
- **Media Attributes**: Image paths, video sequences, audio compositions, 3D model configurations
- **AI-Generated Content**: AI-generated names, descriptions, traits, prompts, or any text/image attributes
- **Probabilistic Attributes**: Weighted random selection, rarity systems, trait combinations
- **Deterministic Attributes**: Hash-based generation, seed-based selection, reproducible randomness
- **Complex Attributes**: Nested objects, arrays, multi-dimensional data, relationships between traits
- **External Data**: Attributes fetched from APIs, databases, or computed from external services

### Using External Libraries

You can use **any npm package** in your generator plugin. For example:
- `openai`, `@anthropic-ai/sdk` for AI generation
- `seedrandom` for deterministic randomization
- `lodash` for data manipulation
- `axios` for API calls
- `crypto` (built-in) for hashing and deterministic generation
- Any other package you need

Simply install the package and import it in your plugin file.

### Accessing Multiple Inputs

You can access data from multiple input plugins:

```typescript
const imageInput = this.inputsManager.get("images");
const apiInput = this.inputsManager.get("apiData");
const videoInput = this.inputsManager.get("videos");
// Combine or use any input data in your generation logic
```

## Important Notes

- The `kind` identifier must be unique and consistent (use versioning like `@v1`)
- Each item UID should map to an array of attributes
- Each attribute must have `kind` (string) and `data` (your `GeneratorDataType`) properties
- Generators run after inputs and before renderers
- Multiple generators can be used, and their outputs are combined
- Use the `seed` from `init()` for deterministic generation if needed
- The `kind` identifier is used by renderers to identify which attributes to process
- The `GeneratorDataType` can be **any TypeScript type** - define it to match your needs
- You can use any npm package - there are no restrictions on dependencies
- The `generate()` method is async, so you can perform any asynchronous operations