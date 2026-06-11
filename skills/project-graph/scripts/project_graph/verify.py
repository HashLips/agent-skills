"""Output verification and result emission."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

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
