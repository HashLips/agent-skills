# SVG clipping and masking

Ways to show only part of content: **clipPath** gives hard edges; **mask** can soften edges or use luminance/alpha for transparency.

## clipPath — hard-edged visibility

- **Purpose:** Content is visible only inside the clip path; edges are sharp.
- **Usage:** Define a `<clipPath>` in `<defs>`; reference it with `clip-path="url(#id)"` on the element (or group) to clip.

**Structure:**

```xml
<defs>
  <clipPath id="circleClip">
    <circle cx="50" cy="50" r="40"/>
  </clipPath>
</defs>
<g clip-path="url(#circleClip)">
  <!-- content is visible only inside the circle -->
  <rect x="0" y="0" width="100" height="100" fill="blue"/>
</g>
```

- The **geometry** of the clipPath (path, circle, etc.) defines the visible region. Fill/stroke of the clip path don’t paint; only the shape matters. Default fill is `fill="black"` and “black” = visible; `fill="none"` = invisible (no visibility).
- **clipPathUnits:** `userSpaceOnUse` (default) uses the current user coordinate system; `objectBoundingBox` uses the bounding box of the clipped element (0–1).

**When generating:** Use clipPath for hard-edged visibility regions, circular or rounded frames, or any sharp-boundary window into content.

## mask — soft or gradient visibility

- **Purpose:** Control visibility using luminance or alpha. White = fully visible, black = fully hidden, gray = partial. Allows soft edges and gradient fades.
- **Usage:** Define a `<mask>` in `<defs>`; reference it with `mask="url(#id)"`.

**Structure:**

```xml
<defs>
  <mask id="fadeMask">
    <linearGradient id="fadeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="white"/>
      <stop offset="100%" stop-color="black"/>
    </linearGradient>
    <rect x="0" y="0" width="100" height="100" fill="url(#fadeGrad)"/>
  </mask>
</defs>
<g mask="url(#fadeMask)">
  <rect x="0" y="0" width="100" height="100" fill="blue"/>
</g>
```

- Mask content is not painted on the canvas; it only defines visibility. White (or high luminance) = show; black = hide.
- **maskUnits** / **maskContentUnits** control how mask coordinates are interpreted (similar to clipPath).

**When generating:** Use mask for fades, vignettes, soft edges, or any visibility that varies by gradient or grayscale.

## Summary

| Feature   | clipPath        | mask                 |
|----------|------------------|----------------------|
| Edge     | Hard             | Can be soft/gradient |
| Reference| `clip-path="url(#id)"` | `mask="url(#id)"` |
| Content  | Shape only       | Luminance/alpha      |

Both are defined in `<defs>` and referenced by URL. Prefer clipPath for hard-edged visibility; use mask when you need smooth transitions or alpha-based visibility.
