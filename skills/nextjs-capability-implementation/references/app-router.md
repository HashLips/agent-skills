# App Router

The `app/` directory controls routing and composition.

Responsibilities:

- route segments
- layouts
- page entry points
- metadata
- loading states
- error boundaries

---

## Best Practice

Route files should remain thin and primarily assemble features.

Example pattern:

page.tsx  
imports feature component  
renders composed UI
