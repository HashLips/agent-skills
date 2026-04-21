# Data Directory Structure

Create a README.md file in the `data/` directory to guide users on organizing their image layers.

### File
`data/README.md`

### Content

```markdown
# Data Directory

This directory contains your image layers organized by trait categories. The Art Engine uses a specific naming convention to control layer ordering (z-index), rarity weights, and conditional variations (edge cases).

## Structure

Organize your image layers in subdirectories, one for each trait category. Each folder and file can use special naming parameters to control behavior:

```
data/
  ├── Background__z10/
  │   ├── Blue__w5.png
  │   ├── Navy Blue__w10.png
  │   └── Orange__w10.png
  ├── Body__z20/
  │   ├── Green__w10.png
  │   ├── Grey__w10.png
  │   └── Robot__w5.png
  ├── Face__z40/
  │   ├── Old Face__w10.png
  │   ├── Old Face__z-15.png
  │   └── Robot Face__w20.png
  └── Prop__z50/
      ├── Backpack__w10.png
      └── edge-cases/
          └── Backpack__z-35__tClothing__vSanta.png
```

## Naming Conventions

### Folder Names (Layer Categories)

- **Basic**: `Background`, `Body`, `Face` - Simple folder names
- **With Z-Index**: `Background__z10`, `Body__z20` - Control layer rendering order
  - Use `__z{number}` to specify z-index (rendering depth)
  - Lower z-index values render behind higher ones
  - Example: `Background__z10` renders behind `Body__z20`

### File Names (Trait Variations)

- **Basic**: `Blue.png`, `Red.png` - Simple file names
- **With Weight**: `Blue__w5.png`, `Navy Blue__w10.png` - Control rarity
  - Use `__w{number}` to specify rarity weight
  - Higher weights = more likely to be selected
  - Example: `Navy Blue__w10` is twice as likely as `Blue__w5`
- **With Z-Index**: `Old Face__z-15.png` - Override layer z-index for specific files
  - Use `__z{number}` in filename to override folder z-index
  - Can be positive or negative
  - Example: `Old Face__z-15` renders at z-index -15 instead of the folder's z-index

### Edge Cases (Conditional Variations)

Edge cases allow you to create variations that appear only when specific conditions are met. Create an `edge-cases` folder inside any layer folder.

**Edge Case Parameters:**
- `__z{number}` - Z-index for the edge case
- `__t{TraitName}` - Trait name to match (e.g., `__tClothing`)
- `__v{Value}` - Trait value to match (e.g., `__vSanta`)

**Example**: `Backpack__z-35__tClothing__vSanta.png`
- This backpack variant appears when:
  - The `Clothing` trait has the value `Santa`
  - It renders at z-index -35

**Multiple Conditions**: You can combine multiple trait/value pairs:
- `Backpack__z20__tClothing__vSanta__tFace__vRobot.png` - Matches when Clothing=Santa AND Face=Robot

## Important Notes

- **Each subdirectory represents a trait category** (e.g., Background, Body, Face)
- **Image files within each subdirectory are the different variations** of that trait
- **Z-Index**: Controls rendering order (lower numbers render behind higher numbers)
- **Weight**: Controls rarity/probability of selection (higher numbers = more common)
- **Edge Cases**: Create conditional variations based on other trait combinations
- **Supported formats**: PNG, JPG, JPEG
- **Image dimensions**: Should be the same for best results
- **Layer order**: Automatically determined by z-index values, not folder order

## Examples

### Basic Structure
```
data/
  ├── Background/
  │   ├── Blue.png
  │   └── Red.png
```

### With Z-Index and Weights
```
data/
  ├── Background__z10/
  │   ├── Blue__w5.png      (rare - weight 5)
  │   └── Red__w10.png      (common - weight 10)
  └── Body__z20/
      ├── Normal__w10.png
      └── Robot__w5.png     (rare - weight 5)
```

### With Edge Cases
```
data/
  └── Prop__z50/
      ├── Backpack__w10.png
      └── edge-cases/
          ├── Backpack__z-35__tClothing__vSanta.png
          └── Backpack__z20__tClothing__vSanta.png
```

## Next Steps

1. Add your image layers to the appropriate subdirectories
2. Use `__z{number}` in folder names to control layer order
3. Use `__w{number}` in file names to control rarity
4. Create `edge-cases` folders for conditional variations
5. Update the `dataSet` in `index.ts` generator to match your input key (default is 'apes')
6. Adjust `startIndex` and `endIndex` in the generator to set how many NFTs to generate
7. Run `npm run start` to create your NFTs
```

### Important Notes

- The README helps users understand how to organize their artwork layers
- Layer order is automatically determined by z-index values (`__z{number}`) in folder and file names
- Users should create subdirectories in `data/` for each trait category
- The naming conventions (`__z`, `__w`, `__t`, `__v`) enable fine-grained control over rendering order, rarity, and conditional variations
