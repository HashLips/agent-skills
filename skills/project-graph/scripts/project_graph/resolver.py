"""Resolve import specifiers to project-relative paths."""
from __future__ import annotations

import json
import posixpath
import re
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Set, Tuple

from .constants import EXT_PRIORITY

class Resolver:
    def __init__(self, files: Set[str], aliases: List[Tuple[str, List[str]]]):
        self.files = files
        self.aliases = aliases
        self.no_ext: Dict[str, str] = {}
        self.dir_index: Dict[str, str] = {}
        self.suffix_index: Dict[str, str] = {}
        prio = {ext: i for i, ext in enumerate(EXT_PRIORITY)}

        def better(new: str, old: Optional[str]) -> bool:
            if old is None:
                return True
            return prio.get(PurePosixPath(new).suffix, 99) < prio.get(PurePosixPath(old).suffix, 99)

        for f in sorted(files):
            p = PurePosixPath(f)
            if p.suffix:
                key = f[: -len(p.suffix)]
                if better(f, self.no_ext.get(key)):
                    self.no_ext[key] = f
            if p.stem in {"index", "__init__", "mod", "main"}:
                parent = str(p.parent)
                parent = "" if parent == "." else parent
                if better(f, self.dir_index.get(parent)):
                    self.dir_index[parent] = f
            # progressive suffixes for dotted lookups (java/go style)
            no_ext_path = f[: -len(p.suffix)] if p.suffix else f
            parts = no_ext_path.split("/")
            for i in range(max(0, len(parts) - 5), len(parts)):
                self.suffix_index.setdefault("/".join(parts[i:]), f)

    def lookup(self, cand: str) -> Optional[str]:
        cand = posixpath.normpath(cand).lstrip("/")
        if cand in (".", ""):
            return None
        if cand in self.files:
            return cand
        if cand in self.no_ext:
            return self.no_ext[cand]
        if cand in self.dir_index:
            return self.dir_index[cand]
        suffix = PurePosixPath(cand).suffix
        if suffix in {".js", ".jsx", ".mjs", ".cjs"}:
            stem = cand[: -len(suffix)]
            if stem in self.no_ext:
                return self.no_ext[stem]
            if stem in self.dir_index:
                return self.dir_index[stem]
        return None

    def resolve(self, from_rel: str, spec: str, hint: str) -> Tuple[Optional[str], Optional[str]]:
        """Return (resolved_relpath, external_package)."""
        spec = spec.split("?")[0].split("#")[0].strip()
        if not spec or spec.startswith(("http:", "https:", "//", "data:", "mailto:")):
            return None, None
        base_dir = posixpath.dirname(from_rel)

        if hint == "py":
            return self.resolve_python(from_rel, spec)
        if hint == "rust-mod":
            for cand in (
                posixpath.join(base_dir, spec + ".rs"),
                posixpath.join(base_dir, spec, "mod.rs"),
                posixpath.join(base_dir, PurePosixPath(from_rel).stem, spec + ".rs"),
            ):
                hit = self.lookup(cand)
                if hit:
                    return hit, None
            return None, None
        if hint == "rust-crate":
            parts = spec.split("/")
            for i in range(len(parts), 0, -1):
                hit = self.lookup("src/" + "/".join(parts[:i]))
                if hit:
                    return hit, None
            return None, None
        if hint == "dotted":
            path = spec.replace(".", "/")
            parts = path.split("/")
            for i in range(len(parts), max(0, len(parts) - 3), -1):
                tail = "/".join(parts[max(0, i - 5): i])
                if tail in self.suffix_index:
                    return self.suffix_index[tail], None
            return None, spec.split(".")[0]
        if hint == "dotted-path":
            parts = spec.split("/")
            for i in range(len(parts)):
                tail = "/".join(parts[i:])
                hit = self.lookup(tail)
                if hit:
                    return hit, None
                if tail in self.suffix_index:
                    return self.suffix_index[tail], None
            return None, spec.split("/")[0]

        if spec.startswith("."):
            return self.lookup(posixpath.join(base_dir, spec)), None
        if spec.startswith("/"):
            body = spec.lstrip("/")
            for prefix in ("", "public/", "static/", "src/"):
                hit = self.lookup(prefix + body)
                if hit:
                    return hit, None
            return None, None

        for prefix, targets in self.aliases:
            if spec == prefix.rstrip("/") or spec.startswith(prefix):
                rest = spec[len(prefix):] if spec.startswith(prefix) else ""
                for target in targets:
                    hit = self.lookup(posixpath.join(target, rest))
                    if hit:
                        return hit, None

        for alias in ("@/", "~/", "#/"):
            if spec.startswith(alias):
                rest = spec[len(alias):]
                for prefix in ("src/", "", "app/", "lib/"):
                    hit = self.lookup(prefix + rest)
                    if hit:
                        return hit, None
                return None, None

        if hint == "path":
            hit = self.lookup(posixpath.join(base_dir, spec))
            if hit:
                return hit, None
        if hint in {"js", "path"}:
            for prefix in ("", "src/"):
                hit = self.lookup(prefix + spec)
                if hit:
                    return hit, None
        if hint == "js":
            pkg = "/".join(spec.split("/")[:2]) if spec.startswith("@") else spec.split("/")[0]
            return None, pkg
        return None, None

    def resolve_python(self, from_rel: str, spec: str) -> Tuple[Optional[str], Optional[str]]:
        if spec.startswith("."):
            dots = len(spec) - len(spec.lstrip("."))
            rest = spec.lstrip(".")
            base = PurePosixPath(from_rel).parent
            for _ in range(dots - 1):
                base = base.parent
            cand = str(base / rest.replace(".", "/")) if rest else str(base)
            cands = [cand]
        else:
            path = spec.replace(".", "/")
            cands = [path, "src/" + path]
        for cand in cands:
            parts = cand.split("/")
            for i in range(len(parts), 0, -1):
                hit = self.lookup("/".join(parts[:i]))
                if hit and hit.endswith((".py", ".pyi")):
                    return hit, None
        if not spec.startswith("."):
            return None, spec.split(".")[0]
        return None, None


def load_ts_aliases(root: Path) -> List[Tuple[str, List[str]]]:
    aliases: List[Tuple[str, List[str]]] = []
    for name in ("tsconfig.json", "jsconfig.json"):
        cfg_path = root / name
        if not cfg_path.is_file():
            continue
        try:
            raw = cfg_path.read_text(encoding="utf-8", errors="replace")
            raw = re.sub(r"//[^\n]*", "", raw)
            raw = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
            raw = re.sub(r",\s*([}\]])", r"\1", raw)
            cfg = json.loads(raw)
        except (ValueError, OSError):
            continue
        opts = cfg.get("compilerOptions", {}) or {}
        base = str(opts.get("baseUrl", ".") or ".").strip("./") or ""
        for key, targets in (opts.get("paths", {}) or {}).items():
            prefix = key[:-1] if key.endswith("*") else key
            resolved = []
            for t in targets if isinstance(targets, list) else [targets]:
                t = str(t)
                t = t[:-1] if t.endswith("*") else t
                resolved.append(posixpath.normpath(posixpath.join(base, t)))
            if prefix:
                aliases.append((prefix, resolved))
    return aliases
