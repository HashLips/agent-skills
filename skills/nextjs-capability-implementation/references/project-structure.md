# Project Structure

Use this file to define ownership boundaries between routing code and capability modules.

## Baseline Layout

```text
src/
  app/
  modules/
  shared/
```

---

## app/

Controls routing and composition only.

Contains:

- route segments
- layouts
- page entry points
- metadata
- loading states
- error boundaries

Avoid placing domain or application business logic in `app/`.

---

## modules/

Capability modules.

Examples:

`modules/auth`  
`modules/profile`  
`modules/checkout`

Each module owns:

- domain logic
- application orchestration
- infrastructure adapters
- capability-specific UI/components

---

## shared/

Reusable code used across modules.

Examples:

`shared/ui`  
`shared/lib`  
`shared/types`
