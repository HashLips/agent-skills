# SVG composition (defs and use)

## Summary

- Defines canonical guidance for this SVG topic.
- Use this file to keep vector output consistent and readable.


Reuse the same graphic multiple times without duplicating markup. **defs** holds definitions; **use** instantiates them. This keeps files small and edits in one place.

## defs — definitions

- **`<defs>`** — Container for content that is not drawn directly. Gradients, patterns, clipPaths, masks, and reusable graphics go here.
- Nothing inside `<defs>` is rendered until referenced (e.g. by `<use>` or by `url(#id)` for paint or clip/mask).

**Place defs once, typically near the top of the SVG:**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
  <defs>
    <linearGradient id="g1">...</linearGradient>
    <g id="symbol-shape">
      <path d="M50,0 L61,35 L98,35 L68,57 L79,92 L50,70 L21,92 L32,57 Z"/>
    </g>
  </defs>
  <use href="#symbol-shape" x="0" y="0"/>
  <use href="#symbol-shape" x="100" y="0" fill="url(#g1)"/>
</svg>
```

## use — reuse by reference

- **`<use href="#id">`** (or legacy `xlink:href="#id"`) — Draws a copy of the element with that `id`. The referenced element can be a shape, `<g>`, `<symbol>`, or other graphics element.
- **Position/size:** `x`, `y`, `width`, `height` on `<use>` apply to the instance. Behavior depends on what is referenced: for a `<symbol>`, they set the viewport; for other elements, they act as an extra transform (e.g. translate).

**Important:** The cloned content is a live reference. Changing the definition updates all instances. Instances can override some presentation (e.g. `fill` on `<use>` can override fill of the referenced content in many implementations).

## symbol vs g for reuse

- **`<g id="...">`** — Reusable group. When referenced by `<use>`, `x` and `y` typically offset the group.
- **`<symbol>`** — Designed for reuse. Supports `viewBox` so the symbol has its own coordinate system; `<use width="..." height="...">` then defines the size of that viewport. Prefer **symbol** when you want a self-contained graphic that scales to the `width`/`height` you give on `<use>`.

**Example with symbol:**

```xml
<defs>
  <symbol id="reusable" viewBox="0 0 20 20">
    <rect x="0" y="0" width="20" height="20" fill="none" stroke="black"/>
    <circle cx="10" cy="10" r="5" fill="red"/>
  </symbol>
</defs>
<use href="#reusable" x="0" y="0" width="20" height="20"/>
<use href="#reusable" x="25" y="0" width="20" height="20"/>
```

## When generating artwork

1. Put all reusable graphics, gradients, patterns, clipPaths, and masks in `<defs>`.
2. Use **`<use href="#id">`** to place the same graphic multiple times; set `x`, `y` (and optionally `width`, `height` for `<symbol>`) and override `fill`/`stroke` if needed.
3. Use **`<symbol>`** with a `viewBox` when the graphic has a fixed logical size and should scale to the size given on `<use>`.
4. Combine with **transform** on `<use>` or a wrapping `<g>` to rotate or scale instances (e.g. repeated shapes or icons).
