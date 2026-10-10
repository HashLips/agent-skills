# Repository Structure

## Summary

- One flat folder per category.
- Places nest through fields, not subfolders.
- `agent/` holds instructions. Lore stays in category folders.

Use a flat, minimal folder structure.

World entries must live in these folders unless `agent/categories.md` registers more:

- world/
- regions/
- rules/
- inhabitants/
- artifacts/
- phenomena/
- cultures/
- symbols/
- myths/
- stories/
- artworks/

Also place files in any folder registered in `agent/categories.md`.

`agent/` is for instructions, plans, and maps. It is not a lore category.

Do not create category subfolders by default.
Place files directly in their category folder (for example `artifacts/trade-coin.md`).

## Region Hierarchy

Places can exist within other places.

Use:

- `place_type`
- `parent_region`

Example:

Outer Sea
└ Northern Coast
  └ Port City
    └ Market Hall

Place types may include:

- realm
- region
- state
- city
- district
- building
- shop
- landmark

The `parent_region` must always be the immediate containing location.
