# SVG transforms

The **`transform`** attribute moves, scales, rotates, skews, or combines these for an element or group. Transformations apply in element order and affect the element’s coordinate system and all its descendants (for `g`).

## Transform functions

Use space-separated functions in one `transform`; they apply right-to-left (last in list is applied first to the geometry).

| Function | Syntax | Effect |
|----------|--------|--------|
| **translate** | `translate(tx [, ty])` | Move. `ty` defaults to 0. |
| **scale** | `scale(sx [, sy])` | Scale. `sy` defaults to `sx`. |
| **rotate** | `rotate(angle [, cx, cy])` | Rotate by `angle` degrees. Optional (cx, cy) = center of rotation (default 0,0). |
| **skewX** | `skewX(angle)` | Skew horizontally. |
| **skewY** | `skewY(angle)` | Skew vertically. |
| **matrix** | `matrix(a b c d e f)` | Full 2×3 transform matrix. |

**Examples:**

```xml
<g transform="translate(50, 20) rotate(-15) scale(1.2)">
  <path d="..."/>
</g>
```

Interpretation: scale by 1.2, then rotate -15° around (0,0), then translate by (50,20). Order matters: changing the sequence changes the result.

## Coordinate system

- Transforms define a new coordinate system for the element and its children.
- **Units** for translate are in the current user coordinate system (viewBox units by default). Scale is unitless multiplier; rotate/skew are in degrees.
- Strokes are transformed too; if you scale up, stroke gets thicker unless you compensate (e.g. thinner stroke or `vector-effect="non-scaling-stroke"` where supported).

## When generating artwork

1. **Positioning** — Use `translate(tx, ty)` to place a group or shape at (tx, ty).
2. **Rotation** — Use `rotate(angle, cx, cy)` to spin around a point (e.g. center of a shape). Omit cx, cy to rotate around (0, 0).
3. **Scaling** — Use `scale(sx)` or `scale(sx, sy)` for size. Apply scale on a group to resize a whole symbol.
4. **Order** — Think “first geometry, then transform”: list from “what I draw” toward “where/how it appears” (e.g. scale then rotate then translate).
5. **Reuse** — Combined with `defs` and `use`, transform lets you place the same graphic many times at different positions/angles/scales.
