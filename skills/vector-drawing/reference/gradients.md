# SVG gradients

## Summary

- Defines canonical guidance for this SVG topic.
- Use this file to keep vector output consistent and readable.


Gradients define smooth color transitions for **fill** or **stroke**. Define them in `<defs>`, give an `id`, and reference with `fill="url(#id)"` or `stroke="url(#id)"`.

## Linear gradient: linearGradient

- **Attributes:** `x1`, `y1`, `x2`, `y2` define the gradient vector (default 0%,0% to 100%,0% = left to right).
- **Units:** Percent (e.g. `x1="0%"`) or user space. `gradientUnits="objectBoundingBox"` (default for percent) uses the bounding box of the painted element; `gradientUnits="userSpaceOnUse"` uses viewBox-style coordinates.
- **Children:** `<stop offset="…" stop-color="…"/>`. `offset` is 0–1 or 0%–100%; order by offset.

**Example:**

```xml
<defs>
  <linearGradient id="linear1" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="lightblue"/>
    <stop offset="100%" stop-color="navy"/>
  </linearGradient>
</defs>
<rect x="0" y="0" width="100" height="100" fill="url(#linear1)"/>
```

- `x1="0%" y1="0%" x2="0%" y2="100%"` = top to bottom. Change to `x2="100%"` for left–right.

## Radial gradient: radialGradient

- **Attributes:** `cx`, `cy`, `r` (center and radius). Optional `fx`, `fy` for focal point. Percent or user units; `gradientUnits` as above.
- **Children:** Same `<stop>` elements as linear.

**Example:**

```xml
<defs>
  <radialGradient id="radial1" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="white"/>
    <stop offset="100%" stop-color="transparent"/>
  </radialGradient>
</defs>
<circle cx="50" cy="50" r="40" fill="url(#radial1)"/>
```

## Gradient reuse and scope

- Each gradient has a unique `id`. Reference from any element in the document with `fill="url(#id)"`.
- Gradients are defined in `<defs>` so they don’t draw on the canvas; they only define a paint server.

## When generating artwork

1. Put all gradients in `<defs>` and reference by `url(#id)`.
2. Use **linearGradient** for directional color transitions or flat fades.
3. Use **radialGradient** for center-out or focal-point fades.
4. Add extra `<stop>` elements for multi-stop transitions; keep offsets in order.
5. For patterns (tiled shapes), use `<pattern>` in `<defs>` and `fill="url(#patternId)"`; structure is similar (pattern definition + reference).
