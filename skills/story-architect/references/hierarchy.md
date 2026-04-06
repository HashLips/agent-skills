# Repository Structure

Use a flat, minimal folder structure.

World entries must live in these folders:

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

Do not create category subfolders by default.
Place files directly in their category folder (for example `artifacts/sky-unit-currency.md`).

# Region Hierarchy

Places can exist within other places.

Use:

- `place_type`
- `parent_region`

Example:

Floating Sky
└ Lower Drift State
  └ Ashen Harbor
    └ Quiet Cup

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
