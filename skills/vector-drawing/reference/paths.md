# SVG paths

## Summary

- Defines canonical guidance for this SVG topic.
- Use this file to keep vector output consistent and readable.


The `path` element is the main tool for arbitrary vector shapes. Paths are defined by a `d` (path data) attribute: a string of commands that draw geometry.

## Path element

```xml
<path d="M 10 10 L 90 10 L 50 90 Z" fill="navy"/>
```

- **`d`** — Path data. Sequence of commands; each command is a letter followed by numeric arguments. Uppercase = absolute coordinates, lowercase = relative.

## Core commands (enough for most artwork)

| Command | Meaning | Example |
|--------|--------|--------|
| `M x y` | Move pen to (x, y). Start of subpath. | `M 0 0` |
| `L x y` | Line to (x, y). | `L 100 50` |
| `H x` | Horizontal line to x. | `H 80` |
| `V y` | Vertical line to y. | `V 40` |
| `Z` (or `z`) | Close path (line to start of current subpath). | `Z` |
| `C x1 y1 x2 y2 x y` | Cubic Bézier to (x,y); (x1,y1) control start, (x2,y2) control end. | `C 20 80 80 20 100 50` |
| `Q x1 y1 x y` | Quadratic Bézier to (x,y); (x1,y1) control. | `Q 50 0 100 50` |
| `A rx ry x-axis-rotation large-arc sweep x y` | Arc to (x,y). Ellipse radii rx, ry; rotation; large-arc and sweep flags (0 or 1). | `A 20 20 0 0 1 80 80` |

**Relative forms:** `m`, `l`, `h`, `v`, `c`, `q`, `a` use offsets from the current point. Useful when generating paths from deltas.

## Rules when generating path data

1. **Start with M** — Every subpath begins with a move (`M` or `m`).
2. **Numbers** — Can be comma- or space-separated; avoid commas between command letter and first number for clarity.
3. **Multiple subpaths** — One `d` can have multiple `M…` segments; each is a separate subpath. Fill uses even-odd or nonzero rule across all subpaths.
4. **Z** — Closes the current subpath from the current point to the last `M`; no coordinates.

## Bézier tips for curves

- **C (cubic):** Two control points. Good for smooth curves and symmetric shapes (symmetric or organic shapes). Control points “pull” the curve.
- **Q (quadratic):** One control point. Simpler; good when one bend is enough.
- **A (arc):** Use for circle/ellipse segments when you know start, end, and radii. Large-arc and sweep disambiguate the four possible arcs.

## When generating artwork

- Prefer one coherent `d` per logical shape when possible; use multiple subpaths (multiple `M`) for holes or separate regions in one path.
- Keep commands readable: space between commands, one command per line if the path is long.
- For complex outlines, build `d` programmatically (e.g. from a list of points and curve parameters) rather than hand-authoring long strings.
