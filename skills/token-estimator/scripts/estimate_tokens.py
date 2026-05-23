#!/usr/bin/env python3
"""Rough, deterministic token estimates. Not billing-grade."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".md", ".txt", ".mdx"}
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv"}
MAX_FILE_BYTES = 2 * 1024 * 1024


def est_tokens(chars: int) -> int:
    return (chars + 3) // 4


def iter_text_files(root: Path):
    if root.is_file():
        if root.suffix.lower() in TEXT_EXTENSIONS:
            yield root
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIR_NAMES)
        for name in sorted(filenames):
            path = Path(dirpath) / name
            if path.suffix.lower() not in TEXT_EXTENSIONS:
                continue
            try:
                if path.stat().st_size > MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            yield path


def measure_path(root: Path) -> list[tuple[str, int, int]]:
    root = root.resolve()
    rows: list[tuple[str, int, int]] = []
    if root.is_file():
        text = root.read_text(encoding="utf-8")
        c = len(text)
        rows.append((root.name, c, est_tokens(c)))
        return rows
    for path in sorted(iter_text_files(root), key=lambda p: p.relative_to(root).as_posix()):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        c = len(text)
        rows.append((path.relative_to(root).as_posix(), c, est_tokens(c)))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Rough token estimates (chars÷4)")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    for root in args.paths:
        if not root.exists():
            print(f"Error: not found: {root}", file=sys.stderr)
            return 1
        rows = measure_path(root)
        if not rows:
            print(f"{root}: (no text files)")
            continue
        total_chars = sum(r[1] for r in rows)
        total_est = est_tokens(total_chars)
        if args.json:
            print(
                json.dumps(
                    {
                        "path": str(root.resolve()),
                        "total_chars": total_chars,
                        "est_tokens": total_est,
                        "files": [
                            {"path": r[0], "chars": r[1], "est_tokens": r[2]} for r in rows
                        ],
                    },
                    indent=2,
                )
            )
        else:
            print(f"{root.resolve()}")
            print(f"total: {total_chars} chars, ~{total_est} est_tokens")
            if len(rows) > 1:
                for rel, c, t in rows:
                    print(f"  {rel}: {c} chars, ~{t} est_tokens")
            print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
