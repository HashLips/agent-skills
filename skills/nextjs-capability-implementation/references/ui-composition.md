# UI Composition

Pages should compose feature components.

Example structure:

Page → Feature Component → UI Components

---

## Shared UI

Shared UI primitives should remain presentation-focused.

Examples:

Button  
Card  
Input  
Modal

---

## Client-only patterns

When a feature subtree needs hooks or Context, isolate it in Client Components and keep pages/layouts as composition shells. See [react-hooks-and-context.md](react-hooks-and-context.md).
