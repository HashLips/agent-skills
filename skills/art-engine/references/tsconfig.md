# TypeScript Configuration

Create a TypeScript configuration file for the Art Engine project.

### File
`tsconfig.json`

### Configuration

```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "display": "Default",
  "exclude": ["node_modules", "dist", "build", "__test__"],
  "include": ["."],
  "compilerOptions": {
    "target": "ESNext",
    "module": "commonjs",
    "composite": false,
    "declaration": true,
    "declarationMap": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "inlineSources": false,
    "isolatedModules": true,
    "moduleResolution": "node",
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "preserveWatchOutput": true,
    "skipLibCheck": true,
    "strict": true,
    "resolveJsonModule": true,
    "outDir": "./dist"
  }
}
```

### Important Notes

- **CommonJS Module System**: Configured to use CommonJS (`"module": "commonjs"`) to match the template project
- **Strict Mode**: Enabled for better type safety
- **Output Directory**: TypeScript compiles to `./dist` directory
- **Exclusions**: `node_modules`, `dist`, `build`, and `__test__` directories are excluded from compilation
