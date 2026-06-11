#!/usr/bin/env python3
"""
Generate an interactive project graph dashboard for any codebase.

Scans every file in a project (respecting .gitignore via git, with a manual
fallback), extracts import/include/link relationships between files, detects
entry-point "flows" (routes, APIs, CLI entries, custom flows from a manifest),
and renders a self-contained HTML dashboard with Explorer, Flows, Folders,
Graph and Insights views.

Usage:
  python3 generate-graph.py [project_root] [-o output.html] [--exclude GLOB]

Optional flow manifest at <root>/project-graph.flows.json:
  { "flows": [ { "name": "Send OTP", "description": "...",
                 "entries": ["src/api/otp/send.ts"] } ] }

Optional living knowledge file at <root>/project-graph.knowledge.json:
AI-authored, grows incrementally as the project is explored. Holds an
overview, technologies, services, per-flow insights and diagrams, per-file
notes, and free-form topic notes; all merged into the dashboard on every run.

Implementation lives in the `project_graph` package beside this script.
"""

from __future__ import annotations

import sys

from project_graph.cli import main


if __name__ == "__main__":
    sys.exit(main())
