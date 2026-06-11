"""Project file discovery (git-aware, privacy-safe)."""
from __future__ import annotations

import fnmatch
import os
import posixpath
import subprocess
from pathlib import Path
from typing import List, Optional

from .constants import DEFAULT_IGNORE_DIRS, OUTPUT_NAME

def git_list_files(root: Path) -> Optional[List[str]]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            capture_output=True, timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    return [p for p in proc.stdout.decode("utf-8", "replace").split("\0") if p]


def load_gitignore_patterns(root: Path) -> List[str]:
    patterns: List[str] = []
    gi = root / ".gitignore"
    if gi.is_file():
        for line in gi.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("!"):
                continue
            patterns.append(line.rstrip("/"))
    return patterns


def ignored_by_patterns(rel: str, name: str, patterns: List[str]) -> bool:
    for pat in patterns:
        target = rel if "/" in pat else name
        if fnmatch.fnmatch(target, pat.lstrip("/")) or fnmatch.fnmatch(rel, pat.lstrip("/") + "/*"):
            return True
    return False


def walk_files(root: Path) -> List[str]:
    patterns = load_gitignore_patterns(root)
    found: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root).as_posix()
        rel_dir = "" if rel_dir == "." else rel_dir
        dirnames[:] = [
            d for d in dirnames
            if d not in DEFAULT_IGNORE_DIRS
            and not d.startswith(".")
            and not ignored_by_patterns(f"{rel_dir}/{d}".lstrip("/"), d, patterns)
        ]
        for fname in filenames:
            rel = f"{rel_dir}/{fname}".lstrip("/")
            if fname in DEFAULT_IGNORE_DIRS:
                continue
            if ignored_by_patterns(rel, fname, patterns):
                continue
            found.append(rel)
    return found


def discover_files(root: Path, excludes: List[str]) -> List[str]:
    listed = git_list_files(root)
    if listed is None:
        listed = walk_files(root)
    result: List[str] = []
    for rel in sorted(set(listed)):
        name = posixpath.basename(rel)
        if name == OUTPUT_NAME or rel.endswith("/" + OUTPUT_NAME):
            continue
        # Privacy rule: dotfiles and dot-folders (.env, .git, .github, .vscode,
        # machine-local config) are never opened or included in the graph.
        if any(part.startswith(".") for part in rel.split("/")):
            continue
        if name in {"Thumbs.db", "desktop.ini"}:
            continue
        if any(fnmatch.fnmatch(rel, pat) for pat in excludes):
            continue
        if not (root / rel).is_file():
            continue
        result.append(rel)
    return result
