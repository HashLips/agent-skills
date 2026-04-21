# Canonical Markdown Syntax

## Summary

- Use one syntax style across repositories.
- Favor diff-friendly, parser-friendly forms.
- This file is the single source for syntax shape and inline examples.
- If a syntax case is not explicitly defined here, use fallback rules below.

## Lists

- **Unordered** — `- item`
- **Ordered** — `1. item`
- **Nested** — two-space indentation
- **Named item canonical form** — `- **name** — value`

```markdown
- Item
  - Nested item
1. Step one
2. Step two
- **apiKey** — string, required
```

## Task lists

```markdown
- [ ] Open item
- [x] Done item
```

## Headings

```markdown
# Title
## Section
### Subsection
#### Detail
```

## Emphasis

- Use strong emphasis sparingly.
- Prefer headings and lists over heavy inline styling.

```markdown
Use `inline code` for identifiers and **strong** only for key labels.
```

## Code

- Inline code uses backticks.
- Blocks use triple fences and language tags when practical.
- Keep examples short and runnable.

````markdown
```ts
const enabled = true;
```
````

## Links and images

- Links use `[label](url)`.
- Images use `![alt](src)`.

```markdown
[Project docs](https://example.com/docs)
![Architecture diagram](./diagram.png)
```

## Variables and interfaces

- Variables use named items only.
- Interfaces use `### <Name>` and fixed bullets.

```markdown
## Variables
- **timeoutMs** — number, default 5000

## Interfaces
### PaymentGateway
- **Purpose** — Process payment authorization
- **Inputs** — amount, currency, token
- **Outputs** — authId, status
- **Constraints** — idempotent key required
```

## Steps and workflows

```markdown
## Workflow
1. Load configuration.
2. Validate inputs.
3. Execute main action.
4. Return output.
```

## Horizontal rules and quotes

- Use `---` sparingly.
- Use `>` for quotations or one highlighted excerpt only.

```markdown
> Important note.
---
```

## Fallback rules (when syntax is undefined)

- **Unknown block type** — render as plain text under a clear heading; do not invent custom wrappers.
- **Unknown structured field** — use named item format: `- **name** — value`.
- **Unknown sequence/process** — use ordered list (`1.`) if order matters, else bullet list (`-`).
- **Unknown code-like content** — use fenced code block with best-guess language tag, or plain fenced block if unknown.
- **Unknown inline token** — prefer plain text unless it is an identifier/path/key, then use inline code.
- **Unknown visual/decorative construct** — drop decoration and keep semantic text only.
