---
name: vector-drawing
description: Creates SVG images and vector-based artworks. Use whenever you need to create SVG images, vector graphics, or vector-based artworks instead of raster or bitmap images.
---

# VectorDrawing

This skill guides creation of **vector-based artworks** using SVG—scalable, resolution-independent graphics. Apply it when the user asks for SVG output, vector graphics, logos, icons, illustrations, or any artwork that must scale cleanly.

## Disclaimer (for the user)

This is an experimental skill; outcomes are not guaranteed. Use at your own risk. For the full disclaimer, see the repository README.

## Canonical specification

The official standard is **SVG 2** (W3C). Use it as the authority for syntax and behavior; do not copy the spec verbatim into outputs. Build understanding from it and express it as instructions.

- Specification: https://www.w3.org/TR/SVG2/
- Key sections: Structure, Basic Shapes, Paths, Painting, Coordinate Systems and Transforms, Clipping and Masking, Gradients and Patterns, Text, Reuse (defs/use).

## Core subset for AI-generated artwork

For most vector art, this subset is enough:

| Element/attribute | Role |
|-------------------|------|
| `svg` | Root and canvas |
| `viewBox` | Coordinate system and aspect ratio |
| `path` | Arbitrary shapes and outlines |
| `g` | Grouping and inheritance |
| `fill` | Interior color/pattern |
| `stroke` | Outline color/width |
| `transform` | Move, scale, rotate, skew |
| `clipPath` | Hard-edged visibility |
| `mask` | Soft or gradient visibility |
| `defs` | Define reusable content |
| `use` | Reuse content by reference |

Master these before reaching for shapes, text, or filters.

## Skill flow (reference order)

When generating or editing SVG artwork, apply concepts in this order. Read the referenced file when you need that topic.

1. **SVG structure** → [reference/structure.md](reference/structure.md) — `svg`, `viewBox`, document structure
2. **SVG shapes** → [reference/shapes.md](reference/shapes.md) — rectangles, circles, lines, etc.
3. **SVG paths** → [reference/paths.md](reference/paths.md) — `path` and path commands
4. **SVG styling** → [reference/styling.md](reference/styling.md) — `fill`, `stroke`, painting
5. **SVG grouping** → [reference/grouping.md](reference/grouping.md) — `g`, hierarchy, inheritance
6. **SVG transforms** → [reference/transforms.md](reference/transforms.md) — `transform`
7. **SVG clipping and masking** → [reference/clipping-masking.md](reference/clipping-masking.md) — `clipPath`, `mask`
8. **SVG gradients** → [reference/gradients.md](reference/gradients.md) — gradients (and patterns)
9. **SVG composition** → [reference/composition.md](reference/composition.md) — `defs`, `use`, reuse

## When to use

- User asks for SVG, vector graphics, or scalable artwork
- Task is logos, icons, illustrations, diagrams, or print-ready art
- Output must stay sharp at any size or resolution

## Quick principles

- **Structure first**: use `path`, `g`, `defs` clearly; keep markup readable.
- **Prefer the core subset** unless the design needs text, filters, or advanced features.
- **Accessibility**: add `<title>` and `aria-*` where meaning is conveyed by the graphic.
