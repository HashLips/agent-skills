# SVG shapes

Basic shape elements for simple geometry. Use when the design is rectangles, circles, ellipses, or lines; otherwise prefer `path` for full control.

## Rectangle: `rect`

- **`x`, `y`** — Top-left corner (default 0).
- **`width`, `height`** — Size.
- **`rx`, `ry`** — Corner radii (rounded rectangle). Use one value for both.

```xml
<rect x="10" y="20" width="80" height="60" rx="8"/>
```

## Circle: `circle`

- **`cx`, `cy`** — Center.
- **`r`** — Radius.

```xml
<circle cx="50" cy="50" r="40"/>
```

## Ellipse: `ellipse`

- **`cx`, `cy`** — Center.
- **`rx`, `ry`** — Horizontal and vertical radii.

```xml
<ellipse cx="50" cy="50" rx="40" ry="25"/>
```

## Line: `line`

- **`x1`, `y1`** — Start point.
- **`x2`, `y2`** — End point.
- Typically styled with `stroke`; `fill` has no effect.

```xml
<line x1="0" y1="0" x2="100" y2="50" stroke="black"/>
```

## Polyline and polygon: `polyline`, `polygon`

- **`points`** — Space- or comma-separated list of x,y pairs (e.g. `points="0,0 50,50 100,0"`).
- **`polyline`** — Open sequence of points (stroke only, unless you close it manually).
- **`polygon`** — Closed shape (implicit line from last point to first).

```xml
<polygon points="50,0 100,50 50,100 0,50" fill="none" stroke="black"/>
```

## When to use shapes vs path

- **Use shapes** when the design is clearly a rect, circle, ellipse, or line/polygon; they are short and readable.
- **Use `path`** when you need curves, complex outlines, or a single element that’s easier to generate programmatically. For most AI-generated artwork, `path` is the main building block; shapes are conveniences.
