"""Flow detection, manifest loading, and reachability expansion."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Set

from .constants import CODE_EXTS, FLOWS_MANIFEST, MAX_AUTO_FLOWS
from .resolver import Resolver

ROUTE_APP_RE = re.compile(r"^(?:src/)?app/(.*?)/?(page|route|layout|template)\.[^./]+$")
ROUTE_PAGES_RE = re.compile(r"^(?:src/)?pages/(.+)\.[^./]+$")
ROUTE_DIR_RE = re.compile(r"^(?:src/|app/|lib/)?(api|routes?|controllers?|handlers?|endpoints?|views|commands?|jobs?|workers?|lambdas?|functions)/(.+)\.[^./]+$")
ENTRY_RE = re.compile(r"^(?:src/)?(main|index|app|server|cli|extension|background|worker)\.[^./]+$")
PY_ENTRY_NAMES = {"main.py", "app.py", "manage.py", "wsgi.py", "asgi.py", "cli.py", "run.py", "__main__.py"}
SVELTE_ROUTE_RE = re.compile(r"^(?:src/)?routes/(.*?)/?\+(page|server|layout)(?:\.server)?\.[^./]+$")


def flow_slug(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return value or "flow"


def detect_auto_flows(node_ids: List[str], py_mains: Set[str]) -> List[Dict[str, object]]:
    flows: List[Dict[str, object]] = []
    seen_entries: Set[str] = set()

    def add(name: str, kind: str, entry: str) -> None:
        if entry in seen_entries:
            return
        seen_entries.add(entry)
        flows.append({"name": name, "kind": kind, "desc": "", "entries": [entry]})

    for rel in node_ids:
        ext = PurePosixPath(rel).suffix
        if ext not in CODE_EXTS and ext not in {".html", ".htm"}:
            continue
        m = SVELTE_ROUTE_RE.match(rel)
        if m:
            route = "/" + m.group(1)
            add(route if route != "/" else "/ (home)", "route", rel)
            continue
        m = ROUTE_APP_RE.match(rel)
        if m:
            route = "/" + m.group(1)
            if m.group(2) == "layout":
                continue
            kind = "api" if "/api/" in route + "/" or m.group(2) == "route" else "route"
            add(route if route != "/" else "/ (home)", kind, rel)
            continue
        m = ROUTE_PAGES_RE.match(rel)
        if m:
            route = "/" + m.group(1)
            if PurePosixPath(rel).stem.startswith("_"):
                continue
            route = re.sub(r"/index$", "", route) or "/"
            kind = "api" if route.startswith("/api/") else "route"
            add(route if route != "/" else "/ (home)", kind, rel)
            continue
        m = ROUTE_DIR_RE.match(rel)
        if m:
            group = m.group(1).rstrip("s")
            target = re.sub(r"/(index|route|handler)$", "", m.group(2))
            add(f"{m.group(1)}/{target}", "api" if group in {"api", "route", "endpoint", "handler"} else group, rel)
            continue
        m = ENTRY_RE.match(rel)
        if m:
            add(f"entry: {rel}", "entry", rel)
            continue
        name = PurePosixPath(rel).name
        if name in PY_ENTRY_NAMES or rel in py_mains:
            add(f"entry: {rel}", "entry", rel)
    return flows


def load_manifest_flows(root: Path) -> List[Dict[str, object]]:
    path = root / FLOWS_MANIFEST
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        print(f"Warning: could not parse {FLOWS_MANIFEST}: {exc}", file=sys.stderr)
        return []
    raw_flows = data.get("flows", data) if isinstance(data, dict) else data
    flows: List[Dict[str, object]] = []
    if not isinstance(raw_flows, list):
        return []
    for item in raw_flows:
        if not isinstance(item, dict) or not item.get("name"):
            continue
        entries = item.get("entries") or item.get("entry") or []
        if isinstance(entries, str):
            entries = [entries]
        flows.append({
            "name": str(item["name"]),
            "kind": "custom",
            "desc": str(item.get("description", "") or ""),
            "entries": [str(e).lstrip("./") for e in entries],
        })
    return flows


def expand_flows(
    flows: List[Dict[str, object]],
    out_adj: Dict[str, List[str]],
    node_set: Set[str],
    resolver: Resolver,
) -> List[Dict[str, object]]:
    expanded: List[Dict[str, object]] = []
    used_ids: Set[str] = set()
    for flow in flows:
        entries: List[str] = []
        for e in flow["entries"]:  # type: ignore[union-attr]
            if e in node_set:
                entries.append(e)
            else:
                hit = resolver.lookup(str(e))
                if hit:
                    entries.append(hit)
        if not entries:
            continue
        members: List[List[object]] = []
        seen: Set[str] = set()
        frontier = list(entries)
        for e in frontier:
            seen.add(e)
        depth = 0
        while frontier and depth < 40:
            for node in sorted(frontier):
                members.append([node, depth])
            nxt: List[str] = []
            for node in frontier:
                for target in out_adj.get(node, []):
                    if target not in seen and target in node_set:
                        seen.add(target)
                        nxt.append(target)
            frontier = nxt
            depth += 1
        fid = "flow:" + flow_slug(str(flow["name"]))
        if fid in used_ids:
            fid = fid + "-" + flow_slug(entries[0])
        if fid in used_ids:
            continue
        used_ids.add(fid)
        expanded.append({
            "id": fid,
            "name": flow["name"],
            "kind": flow["kind"],
            "desc": flow["desc"],
            "entries": entries,
            "members": members,
        })
    expanded.sort(key=lambda f: (f["kind"] != "custom", -len(f["members"]), str(f["name"])))  # type: ignore[arg-type]
    return expanded[:MAX_AUTO_FLOWS + 50]
