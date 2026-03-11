# SVG structure

How to set up the SVG document and coordinate system for generated artwork.

## Root: `svg`

- The root element of an SVG document is `<svg>`.
- For standalone images, use a single root `<svg>` with no outer HTML.
- For inline use (e.g. in HTML), one `<svg>` is one graphic.

**Attributes that define the canvas:**

- **`width` and `height`** — Optional. Nominal size in CSS pixels (e.g. `width="400" height="300"`). Omit for scalable “no intrinsic size” SVGs when you want CSS to control size.
- **`viewBox`** — Defines the coordinate system and aspect ratio (see below).

**Minimal standalone SVG:**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <!-- content -->
</svg>
```

Always include `xmlns="http://www.w3.org/2000/svg"` for standalone SVGs so they parse correctly everywhere.

## `viewBox`

`viewBox` defines the coordinate system used by the content. Format: `viewBox="minX minY width height"`.

- **minX, minY** — Origin of the coordinate system (often `0 0`).
- **width, height** — Width and height of that coordinate space. Content is drawn in this space; the SVG then scales to fit the element’s display size.

**Why it matters for artwork:**

- Use one consistent coordinate system (e.g. `0 0 100 100` or `0 0 400 300`) and design in that space.
- Aspect ratio of the graphic comes from `viewBox` (and optionally `width`/`height`). Matching `width`/`height` ratio to `viewBox` avoids unexpected stretching.
- To “zoom” into a region, use a smaller viewBox over the same area (e.g. `viewBox="25 25 50 50"` to zoom into the center half).

**Examples:**

- Square, 100×100 units: `viewBox="0 0 100 100"`
- Wide artboard, 300×100: `viewBox="0 0 300 100"`
- Centered origin (e.g. -50 to 50): `viewBox="-50 -50 100 100"`

## Document structure for readability

- Put reusable content in `<defs>` (see [composition.md](composition.md)).
- Group related elements in `<g>` (see [grouping.md](grouping.md)).
- Use clear indentation so nesting is obvious when generating or editing by hand.

## When generating

1. Choose a `viewBox` that matches the intended aspect ratio and “logical” size.
2. Add `xmlns` on the root `<svg>` for standalone output.
3. Add `width`/`height` only when a specific pixel size is required; otherwise omit for flexibility.
