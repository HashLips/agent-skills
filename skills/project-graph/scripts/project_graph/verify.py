"""Output verification and result emission."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .constants import KNOWLEDGE_FILE


def knowledge_entry_total(know: Dict[str, object]) -> int:
    flows = know.get("flows") or {}
    flow_count = sum(
        1 for v in flows.values()
        if isinstance(v, dict) and (v.get("insight") or v.get("diagram"))
    )
    return (
        (1 if know.get("overview") else 0)
        + len(know.get("technologies") or [])
        + len(know.get("services") or [])
        + len(know.get("files") or {})
        + len(know.get("notes") or [])
        + flow_count
    )


def verify_knowledge_merge(root: Path, know: Dict[str, object], html: str) -> List[str]:
    """Ensure an on-disk knowledge file was actually merged into the HTML payload."""
    problems: List[str] = []
    know_path = root / KNOWLEDGE_FILE
    if not know_path.is_file():
        return problems
    if not know.get("present"):
        problems.append(
            f"{KNOWLEDGE_FILE} exists on disk but could not be merged "
            "(invalid JSON or wrong shape); fix the file and regenerate"
        )
        return problems
    if '"present":true' not in html.replace(" ", ""):
        problems.append("knowledge payload missing from generated HTML")
    return problems


def emit_result(status: Dict[str, object]) -> None:
    """Print one machine-readable line the skill can check without reading the HTML."""
    print("PROJECT_GRAPH_RESULT " + json.dumps(status, ensure_ascii=True))


def verify_html(html: str, output: Path, node_count: int) -> List[str]:
    problems: List[str] = []
    for placeholder in ("__DATA__", "__BRAND__", "__PAGE_TITLE__"):
        if placeholder in html:
            problems.append(f"unreplaced template placeholder {placeholder}")
    if "</html>" not in html:
        problems.append("HTML output is truncated")
    if node_count == 0:
        problems.append("no files discovered (empty folder, everything ignored, or symlink-only folder)")
    try:
        written = output.stat().st_size
    except OSError:
        problems.append("output file was not written")
    else:
        if written != len(html.encode("utf-8")):
            problems.append("output file size does not match rendered HTML")
    return problems
