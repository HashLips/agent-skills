"""Living knowledge file loading and flow matching."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from .constants import KNOWLEDGE_FILE
from .flows import flow_slug

def _know_str(value: object, limit: int = 2000) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text[:limit]


def _know_entry_list(raw: object, name_key: str = "name") -> List[Dict[str, str]]:
    """Normalize a list of strings or dicts into [{name, role, detail}, ...]."""
    items: List[Dict[str, str]] = []
    if not isinstance(raw, list):
        return items
    for item in raw[:60]:
        if isinstance(item, str):
            items.append({"name": _know_str(item, 120), "role": "", "detail": ""})
        elif isinstance(item, dict) and item.get(name_key):
            items.append({
                "name": _know_str(item.get(name_key), 120),
                "role": _know_str(item.get("role") or item.get("kind"), 120),
                "detail": _know_str(item.get("detail") or item.get("description"), 600),
            })
    return [i for i in items if i["name"]]


def _know_diagram(raw: object) -> Optional[Dict[str, object]]:
    """Normalize a flow diagram: steps (boxes) and edges (arrows)."""
    if not isinstance(raw, dict):
        return None
    steps_raw = raw.get("steps")
    if not isinstance(steps_raw, list):
        return None
    valid_kinds = {"start", "action", "decision", "io", "external", "end"}
    steps: List[Dict[str, str]] = []
    ids: Set[str] = set()
    for s in steps_raw[:40]:
        if not isinstance(s, dict) or not s.get("id") or not s.get("label"):
            continue
        sid = _know_str(s["id"], 60)
        if sid in ids:
            continue
        ids.add(sid)
        kind = _know_str(s.get("kind"), 20).lower()
        steps.append({
            "id": sid,
            "label": _know_str(s["label"], 140),
            "kind": kind if kind in valid_kinds else "action",
            "file": _know_str(s.get("file"), 240),
        })
    if len(steps) < 2:
        return None
    edges: List[Dict[str, str]] = []
    for e in (raw.get("edges") if isinstance(raw.get("edges"), list) else [])[:80]:
        if not isinstance(e, dict):
            continue
        src, dst = _know_str(e.get("from"), 60), _know_str(e.get("to"), 60)
        if src in ids and dst in ids and src != dst:
            edges.append({"from": src, "to": dst, "label": _know_str(e.get("label"), 60)})
    if not edges:
        # fall back to a simple chain so a steps-only diagram still renders
        edges = [{"from": steps[i]["id"], "to": steps[i + 1]["id"], "label": ""} for i in range(len(steps) - 1)]
    return {"steps": steps, "edges": edges}


def load_knowledge(root: Path) -> Tuple[Dict[str, object], List[str]]:
    """Load and lenient-validate the AI-authored living knowledge file."""
    empty: Dict[str, object] = {
        "present": False, "updated": "", "overview": "",
        "technologies": [], "services": [], "flows": {}, "files": {}, "notes": [],
    }
    path = root / KNOWLEDGE_FILE
    if not path.is_file():
        return empty, []
    warnings: List[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        warnings.append(f"could not parse {KNOWLEDGE_FILE}: {exc}")
        return empty, warnings
    if not isinstance(data, dict):
        warnings.append(f"{KNOWLEDGE_FILE} must be a JSON object; ignoring it")
        return empty, warnings

    flows_know: Dict[str, Dict[str, object]] = {}
    raw_flows = data.get("flows")
    if isinstance(raw_flows, dict):
        for key, val in list(raw_flows.items())[:120]:
            if not isinstance(val, dict):
                continue
            entry: Dict[str, object] = {}
            insight = _know_str(val.get("insight") or val.get("summary"))
            if insight:
                entry["insight"] = insight
            diagram = _know_diagram(val.get("diagram") or val)
            if diagram:
                entry["diagram"] = diagram
            if entry:
                flows_know[str(key)] = entry

    file_notes: Dict[str, str] = {}
    raw_files = data.get("files")
    if isinstance(raw_files, dict):
        for key, val in list(raw_files.items())[:400]:
            if isinstance(val, dict):
                val = val.get("note", "")
            note = _know_str(val if isinstance(val, str) else "")
            if note:
                file_notes[str(key).lstrip("./")] = note

    notes: List[Dict[str, str]] = []
    raw_notes = data.get("notes")
    if isinstance(raw_notes, list):
        for item in raw_notes[:80]:
            if isinstance(item, dict) and item.get("body"):
                notes.append({
                    "topic": _know_str(item.get("topic"), 120) or "Note",
                    "body": _know_str(item.get("body"), 1200),
                })

    return {
        "present": True,
        "updated": _know_str(data.get("updated"), 40),
        "overview": _know_str(data.get("overview")),
        "technologies": _know_entry_list(data.get("technologies")),
        "services": _know_entry_list(data.get("services")),
        "flows": flows_know,
        "files": file_notes,
        "notes": notes,
    }, warnings


def match_flow_knowledge(
    flows_know: Dict[str, Dict[str, object]],
    flows: List[Dict[str, object]],
) -> Tuple[Dict[str, Dict[str, object]], List[str]]:
    """Map knowledge keys (flow names, slugs, or ids) onto expanded flow ids."""
    matched: Dict[str, Dict[str, object]] = {}
    stale: List[str] = []
    by_id = {str(f["id"]) for f in flows}
    by_slug = {str(f["id"])[len("flow:"):]: str(f["id"]) for f in flows}
    by_name = {str(f["name"]).strip().lower(): str(f["id"]) for f in flows}
    for key, val in flows_know.items():
        fid: Optional[str] = None
        if key in by_id:
            fid = key
        elif flow_slug(key) in by_slug:
            fid = by_slug[flow_slug(key)]
        elif key.strip().lower() in by_name:
            fid = by_name[key.strip().lower()]
        if fid:
            matched.setdefault(fid, {}).update(val)
        else:
            stale.append(key)
    return matched, stale

