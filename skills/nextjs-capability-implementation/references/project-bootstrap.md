# Project Bootstrap

Use this file to bootstrap a new Next.js repository with secure defaults before feature work starts.

## Bootstrap Sequence

1. Initialize Next.js with TypeScript enabled.
2. Create baseline folders under `src/`: `app/`, `modules/`, and `shared/`.
3. Add environment files and secret handling conventions.
4. Configure `.gitignore` for generated output and sensitive files.
5. Configure linting (ESLint) with rules that align with capability boundaries and server/client separation.
6. Configure a test runner (e.g. Jest or equivalent) for unit and integration tests.
7. Confirm capability ownership and routing boundaries before building features.

---

## Expected Baseline Layout

```text
src/
  app/
  modules/
  shared/
```

Use this as a starting point only. Capability folders are added under `modules/` as features are defined.

## Read Next

- Folder ownership and boundaries: [project-structure.md](project-structure.md)
- Secret and env variable rules: [environment-variables.md](environment-variables.md)
- Ignore rules for sensitive/generated files: [gitignore.md](gitignore.md)
