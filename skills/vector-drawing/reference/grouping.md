# SVG grouping

The **`g`** element groups children without drawing anything itself. Use it to structure artwork, apply shared transforms or styles, and keep markup readable.

## Purpose of `g`

- **Hierarchy** — Group logically related elements (e.g. one symbol, one icon, one layer).
- **Inheritance** — Attributes set on `<g>` apply to all descendants unless overridden. Common uses: `fill`, `stroke`, `transform`, `opacity`.
- **Transforms** — Apply `transform` to a `<g>` to move, scale, or rotate an entire group.
- **Clarity** — Indentation and nested `<g>` make the structure of the art obvious when generating or editing.

## Syntax

```xml
<g fill="blue" stroke="black" stroke-width="1">
  <path d="M 0 0 L 50 50 L 100 0 Z"/>
  <circle cx="50" cy="30" r="10"/>
</g>
```

No `x`, `y`, `width`, or `height` on `g`; position and size come from its children and from `transform`.

## Naming and accessibility

- **`id`** — Give a group an `id` if you reference it (e.g. in `<use>`) or for scripting/accessibility.
- **`aria-label`** — For accessibility, describe the group’s meaning when the graphic conveys information.

## When generating artwork

1. Group by logical part: one `<g>` per symbol, layer, or repeated unit.
2. Set shared fill/stroke/opacity on the group when all children share the same style.
3. Use nested `<g>` for sub-parts (e.g. group “arm” inside group “figure”).
4. Apply transforms on the group when the whole group should move, scale, or rotate together.
