# SVG styling (fill and stroke)

## Summary

- Defines canonical guidance for this SVG topic.
- Use this file to keep vector output consistent and readable.


How to paint the interior and outline of shapes. The core attributes are **fill** and **stroke**; most vector art only needs these plus stroke width and join/cap.

## Fill

- **`fill`** — Paints the interior of shapes (path, rect, circle, etc.).
- **Values:** color name, hex (`#fff`, `#ff0000`), rgb/rgba, or reference to a gradient/pattern (e.g. `url(#myGradient)`).
- **Default:** `fill="black"` for most shapes.
- **`fill="none"`** — No fill; only stroke is visible (common for outlines and lines).

## Stroke

- **`stroke`** — Paints the outline. Same value types as `fill`.
- **Default:** no stroke unless you set `stroke`.
- **`stroke="none"`** — No outline.

**Stroke width and appearance:**

- **`stroke-width`** — Thickness in user units (e.g. `stroke-width="2"`). Affected by transforms.
- **`stroke-linecap`** — End of open paths: `butt` (default), `round`, `square`.
- **`stroke-linejoin`** — Corners: `miter` (default), `round`, `bevel`.
- **`stroke-dasharray`** — Dash pattern (e.g. `5 3` for dash 5, gap 3).
- **`stroke-dashoffset`** — Offset for the dash pattern (useful for animations).

## Inheritance and grouping

- Fill and stroke can be set on a `<g>`; children inherit unless they set their own. Use this to define a default style for a group.
- Setting `fill` or `stroke` on a child overrides the inherited value.

## Presentation attributes vs CSS

- The attributes above are presentation attributes: you can write `fill="red"` or `stroke-width="2"` directly on elements.
- Same properties can be set via CSS (e.g. `style="fill: red; stroke: blue;"` or in a `<style>` block). When generating SVG, either approach is valid; keep it consistent within one file.

## Negative space (holes in a shape)

To show the background through a shape (e.g. facial features as “cut-outs” in a silhouette), use one path with multiple subpaths and **`fill-rule="evenodd"`**. The outer subpath is the main shape; inner subpaths become holes so the background shows through. No extra elements needed.

## When generating artwork

1. Decide fill vs outline: use `fill="none"` for line-only art; set both for solid shapes with borders.
2. Use a consistent unit for `stroke-width` (e.g. 1–2 in viewBox units).
3. For dashed outlines, set `stroke-dasharray`; for rounded caps/joints use `stroke-linecap="round"` and `stroke-linejoin="round"`.
4. For “negative space” features (holes inside a shape), use a single path with one outer subpath and inner subpaths and `fill-rule="evenodd"`.
