# Flows

## Summary

- A flow is a named entry point plus every project file reachable from it through imports.
- Flows answer "what code is involved when X happens" (for example sending an OTP).
- Flows come from two sources: auto-detection and an optional manifest.

## Auto-detection

The generator scans file paths and names for common entry-point shapes:

- **Next.js app router** — `app/**/page.*` and `app/**/route.*` (named by route, for example `/studio`, `/api/send-otp`).
- **Next.js pages router** — `pages/**/*` excluding `_app`, `_document` (API routes under `pages/api/` become `api` flows).
- **SvelteKit** — `src/routes/**/+page.*` and `+server.*`.
- **Handler directories** — files under `api/`, `routes/`, `controllers/`, `handlers/`, `jobs/`, `workers/`, `functions/`, and similar.
- **Generic entries** — root or `src/` files named `main.*`, `index.*`, `app.*`, `server.*`, `cli.*`.
- **Python entries** — `main.py`, `app.py`, `manage.py`, `wsgi.py`, `cli.py`, or any file containing `__main__`.

Membership is computed by breadth-first search over outgoing imports; each member records its depth (entry = step 0, direct imports = step 1, and so on).

## Manifest schema

Define custom flows in `project-graph.flows.json` at the project root:

```json
{
  "flows": [
    {
      "name": "Send OTP",
      "description": "User requests a one-time password via the auth API.",
      "entries": ["src/api/auth/send-otp.ts"]
    }
  ]
}
```

- **name** — required; shown in the flow list, search, and file chips.
- **description** — optional; shown at the top of the flow detail view.
- **entries** — one or more file paths (relative to the root); fuzzy resolution tolerates missing extensions.

Custom flows always sort to the top of the flow list.

## Authoring guidance

1. Prefer the file where the flow starts (route handler, controller, command) as the entry, not a deep helper.
2. Use business names users recognize ("Send OTP", "Checkout", "Export collection"), not file names.
3. Multiple entries are fine when a flow spans a client page plus an API handler.
4. Skip flows the auto-detection already covers unless a better name or description adds value.
5. After editing the manifest, re-run the generator to refresh the dashboard.
