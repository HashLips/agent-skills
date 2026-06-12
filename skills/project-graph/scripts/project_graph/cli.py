"""CLI entry point for project graph generation."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Dict, List

from .build import build_payload
from .constants import EDITOR_SCHEMES, OUTPUT_NAME
from .render import render_html
from .constants import KNOWLEDGE_FILE
from .verify import emit_result, knowledge_entry_total, verify_html, verify_knowledge_merge

_PACKAGE_DIR = Path(__file__).resolve().parent
_GENERATOR_SCRIPT = _PACKAGE_DIR.parent / "generate-graph.py"


def _remove_package_pycache() -> None:
    cache = _PACKAGE_DIR / "__pycache__"
    if cache.is_dir():
        shutil.rmtree(cache, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an interactive project graph dashboard.")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory (default: current directory).")
    parser.add_argument("-o", "--output", default=None, help=f"Output HTML path (default: <root>/{OUTPUT_NAME}).")
    parser.add_argument("--exclude", action="append", default=[], help="Extra glob pattern to exclude (repeatable).")
    parser.add_argument(
        "--editor-scheme",
        choices=list(EDITOR_SCHEMES),
        default=None,
        help="URI scheme for Go to file (default: auto-detect host IDE at generation time).",
    )
    args = parser.parse_args()

    exit_code = 1
    try:
        root = Path(args.root).resolve()
        if not root.is_dir():
            emit_result({"ok": False, "stage": "arguments", "error": f"{root} is not a directory"})
            exit_code = 1
        else:
            try:
                payload, warnings = build_payload(root, args.exclude, editor_scheme=args.editor_scheme)
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
                exit_code = 2
            else:
                nodes = payload["nodes"]
                know = payload.get("knowledge", {}) or {}
                problems = verify_html(html, output, len(nodes))  # type: ignore[arg-type]
                problems.extend(verify_knowledge_merge(root, know, html))  # type: ignore[arg-type]
                status: Dict[str, object] = {
                    "ok": not problems,
                    "stage": "verified" if not problems else "verification",
                    "generator_script": str(_GENERATOR_SCRIPT) if _GENERATOR_SCRIPT.is_file() else "",
                    "output": str(output),
                    "files": len(nodes),  # type: ignore[arg-type]
                    "connections": len(payload["edges"]),  # type: ignore[arg-type]
                    "flows": len(payload["flows"]),  # type: ignore[arg-type]
                    "external_packages": len(payload["external"]),  # type: ignore[arg-type]
                    "html_kb": round(len(html) / 1024),
                    "knowledge": {
                        "present": bool(know.get("present")),
                        "file_on_disk": (root / KNOWLEDGE_FILE).is_file(),
                        "total_entries": knowledge_entry_total(know),  # type: ignore[arg-type]
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
                exit_code = 0 if not problems else 3
    finally:
        _remove_package_pycache()

    return exit_code
