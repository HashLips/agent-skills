# Project Bootstrap

Use this file to bootstrap a new Next.js repository with secure defaults before feature work starts.

**First read** [dependency-and-version-security.md](dependency-and-version-security.md) for Create Next App, supported `next` / `react` / `react-dom` pairing, and mandatory audit checks.

## Bootstrap Sequence

1. Initialize a new app with **Create Next App** (`npx` / `pnpm` / `bunx` per that reference), **TypeScript** enabled, and the **App Router** unless a legacy project requires otherwise.
2. Run a **dependency audit** and address high/critical (and policy-defined major) issues in runtime dependencies before continuing; see [dependency-and-version-security.md](dependency-and-version-security.md).
3. Create baseline folders under `src/`: `app/`, `modules/`, and `shared/`.
4. Add environment files and secret handling conventions.
5. Configure `.gitignore` for generated output and sensitive files.
6. Configure linting (ESLint) with rules that align with capability boundaries and server/client separation.
7. Configure a test runner (e.g. Jest or equivalent) for unit and integration tests.
8. Confirm capability ownership and routing boundaries before building features.

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
