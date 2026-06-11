"""Assemble the graph payload from discovered project files."""
from __future__ import annotations

import datetime
import json
import posixpath
import re
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Dict, List, Set, Tuple

from .categorize import categorize
from .constants import LANG_BY_EXT, MAX_PARSE_BYTES
from .discovery import discover_files
from .flows import detect_auto_flows, expand_flows, load_manifest_flows
from .knowledge import load_knowledge, match_flow_knowledge
from .parsing import extract_summary, is_binary
from .refs import extract_refs
from .resolver import Resolver, load_ts_aliases

def project_name(root: Path) -> str:
    pkg = root / "package.json"
    if pkg.is_file():
        try:
            name = json.loads(pkg.read_text(encoding="utf-8")).get("name")
            if name:
                return str(name)
        except (ValueError, OSError):
            pass
    pyproject = root / "pyproject.toml"
    if pyproject.is_file():
        m = re.search(r'^name\s*=\s*"([^"]+)"', pyproject.read_text(encoding="utf-8", errors="replace"), re.M)
        if m:
            return m.group(1)
    cargo = root / "Cargo.toml"
    if cargo.is_file():
        m = re.search(r'^name\s*=\s*"([^"]+)"', cargo.read_text(encoding="utf-8", errors="replace"), re.M)
        if m:
            return m.group(1)
    return root.resolve().name


def build_payload(root: Path, excludes: List[str]) -> Tuple[Dict[str, object], List[str]]:
    rel_files = discover_files(root, excludes)
    node_set = set(rel_files)
    aliases = load_ts_aliases(root)
    resolver = Resolver(node_set, aliases)

    nodes: List[Dict[str, object]] = []
    edge_map: Dict[Tuple[str, str], Set[str]] = {}
    out_adj: Dict[str, List[str]] = {}
    externals_total: Counter = Counter()
    py_mains: Set[str] = set()
    warnings: List[str] = []
    skip_parse_names = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml", "composer.lock", "Cargo.lock", "poetry.lock", "uv.lock", "bun.lockb", "Gemfile.lock"}

    for rel in rel_files:
        path = root / rel
        try:
            size = path.stat().st_size
        except OSError as exc:
            warnings.append(f"skipped {rel}: {exc}")
            continue
        name = posixpath.basename(rel)
        ext = PurePosixPath(rel).suffix.lower()
        category = categorize(rel, name, ext)
        lang = LANG_BY_EXT.get(ext, ext.lstrip(".").upper() if ext else "Plain")

        loc = 0
        summary = ""
        node_externals: List[str] = []
        if size <= MAX_PARSE_BYTES and category != "asset" and name not in skip_parse_names:
            # A single unreadable or pathological file must never break the
            # whole generation: degrade to a bare node and record a warning.
            try:
                blob = path.read_bytes()
            except OSError:
                blob = b""
            try:
                if blob and not is_binary(blob):
                    text = blob.decode("utf-8", "replace")
                    loc = sum(1 for ln in text.splitlines() if ln.strip())
                    summary = extract_summary(ext, text)
                    if ext == ".py" and "__main__" in text:
                        py_mains.add(rel)
                    ext_seen: Set[str] = set()
                    for spec, kind, hint in extract_refs(ext, text):
                        target, external = resolver.resolve(rel, spec, hint)
                        if target and target != rel and target in node_set:
                            edge_map.setdefault((rel, target), set()).add(kind)
                            out_adj.setdefault(rel, []).append(target)
                        elif external:
                            externals_total[external] += 1
                            if external not in ext_seen and len(node_externals) < 24:
                                ext_seen.add(external)
                                node_externals.append(external)
            except Exception as exc:  # noqa: BLE001 - resilience by design
                warnings.append(f"could not parse {rel}: {type(exc).__name__}: {exc}")

        nodes.append({
            "id": rel,
            "label": name,
            "dir": posixpath.dirname(rel),
            "category": category,
            "lang": lang,
            "size": size,
            "loc": loc,
            "summary": summary,
            "external": node_externals,
            "flows": [],
        })

    # de-dup adjacency
    for key in out_adj:
        out_adj[key] = sorted(set(out_adj[key]))

    flows_defs = load_manifest_flows(root) + detect_auto_flows(rel_files, py_mains)
    flows = expand_flows(flows_defs, out_adj, node_set, resolver)

    knowledge, know_warnings = load_knowledge(root)
    warnings.extend(know_warnings)
    flow_know, stale_flow_keys = match_flow_knowledge(knowledge["flows"], flows)  # type: ignore[arg-type]
    knowledge["flows"] = flow_know
    live_notes = {p: note for p, note in knowledge["files"].items() if p in node_set}  # type: ignore[union-attr]
    stale_file_keys = [p for p in knowledge["files"] if p not in node_set]  # type: ignore[union-attr]
    knowledge["files"] = live_notes
    if stale_flow_keys:
        warnings.append(f"knowledge: {len(stale_flow_keys)} flow entr{'y' if len(stale_flow_keys) == 1 else 'ies'} matched no flow: {', '.join(stale_flow_keys[:4])}")
    if stale_file_keys:
        warnings.append(f"knowledge: {len(stale_file_keys)} file note(s) point at missing files: {', '.join(stale_file_keys[:4])}")

    node_by_id = {n["id"]: n for n in nodes}
    for flow in flows:
        for member, _depth in flow["members"]:  # type: ignore[union-attr]
            node = node_by_id.get(member)
            if node is not None and len(node["flows"]) < 60:  # type: ignore[arg-type]
                node["flows"].append(flow["id"])  # type: ignore[union-attr]

    edges = [
        {"source": s, "target": t, "kinds": sorted(kinds)}
        for (s, t), kinds in sorted(edge_map.items())
    ]

    return {
        "generated": datetime.date.today().isoformat(),
        "project": project_name(root),
        "nodes": nodes,
        "edges": edges,
        "flows": flows,
        "external": externals_total.most_common(40),
        "knowledge": knowledge,
    }, warnings
