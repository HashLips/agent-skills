"""CLI entry point for project graph generation."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List

from .build import build_payload
from .constants import OUTPUT_NAME
from .render import render_html
from .verify import emit_result, verify_html

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an interactive project graph dashboard.")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory (default: current directory).")
    parser.add_argument("-o", "--output", default=None, help=f"Output HTML path (default: <root>/{OUTPUT_NAME}).")
    parser.add_argument("--exclude", action="append", default=[], help="Extra glob pattern to exclude (repeatable).")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        emit_result({"ok": False, "stage": "arguments", "error": f"{root} is not a directory"})
        return 1

    try:
        payload, warnings = build_payload(root, args.exclude)
        output = Path(args.output).resolve() if args.output else root / OUTPUT_NAME
        output.parent.mkdir(parents=True, exist_ok=True)
        html = render_html(payload)
        output.write_text(html, encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 - report instead of stack-tracing
        emit_result({
            "ok": False,
            "stage": "generation",
            "error": f"{type(exc).__name__}: {exc}",
            "hint": "Re-run with --exclude for the offending path, or fix the reported function.",
        })
        return 2

    nodes = payload["nodes"]
    problems = verify_html(html, output, len(nodes))  # type: ignore[arg-type]
    know = payload.get("knowledge", {}) or {}
    status: Dict[str, object] = {
        "ok": not problems,
        "stage": "verified" if not problems else "verification",
        "output": str(output),
        "files": len(nodes),  # type: ignore[arg-type]
        "connections": len(payload["edges"]),  # type: ignore[arg-type]
        "flows": len(payload["flows"]),  # type: ignore[arg-type]
        "external_packages": len(payload["external"]),  # type: ignore[arg-type]
        "html_kb": round(len(html) / 1024),
        "knowledge": {
            "present": bool(know.get("present")),
            "technologies": len(know.get("technologies") or []),
            "services": len(know.get("services") or []),
            "flow_insights": sum(1 for v in (know.get("flows") or {}).values() if v.get("insight")),
            "flow_diagrams": sum(1 for v in (know.get("flows") or {}).values() if v.get("diagram")),
            "file_notes": len(know.get("files") or {}),
            "notes": len(know.get("notes") or []),
        },
        "warning_count": len(warnings),
        "warnings": warnings[:8],
    }
    if problems:
        status["problems"] = problems
    emit_result(status)
    return 0 if not problems else 3
