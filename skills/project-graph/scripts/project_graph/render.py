"""Render the self-contained HTML dashboard."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

_TEMPLATE_PATH = Path(__file__).with_name("template.html")


def render_html(payload: Dict[str, object]) -> str:
    template = _TEMPLATE_PATH.read_text(encoding="utf-8")
    data_json = json.dumps(payload, ensure_ascii=True, separators=(",", ":")).replace("</", "<\\/")
    brand = str(payload["project"]).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        template
        .replace("__PAGE_TITLE__", f"{brand} - Project Graph")
        .replace("__BRAND__", brand)
        .replace("__DATA__", data_json)
    )
