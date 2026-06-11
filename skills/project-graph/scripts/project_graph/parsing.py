"""File content parsing helpers."""
from __future__ import annotations

import re

def is_binary(blob: bytes) -> bool:
    return b"\0" in blob[:8192]


SUMMARY_PATTERNS = [
    re.compile(r'^\s*(?:#![^\n]*\n)?\s*(?:"""|\'\'\')(.+?)(?:"""|\'\'\')', re.S),  # python docstring
    re.compile(r"^\s*/\*\*?(.+?)\*/", re.S),  # block comment
]
LINE_COMMENT_RE = re.compile(r"^(?:#!\S+\n)?((?:\s*(?://|#)[^\n]*\n)+)")


def extract_summary(ext: str, text: str) -> str:
    snippet = ""
    if ext in {".md", ".mdx", ".rst", ".txt"}:
        for block in re.split(r"\n\s*\n", text.strip()):
            block = block.strip()
            if not block or block.startswith(("#", "---", "<", "![", "|", ">", "```")):
                continue
            snippet = block
            break
        if not snippet:
            m = re.search(r"^#\s+(.+)$", text, re.M)
            snippet = m.group(1) if m else ""
    else:
        for pat in SUMMARY_PATTERNS:
            m = pat.match(text)
            if m:
                snippet = m.group(1)
                break
        if not snippet:
            m = LINE_COMMENT_RE.match(text)
            if m:
                lines = [re.sub(r"^\s*(?://|#)\s?", "", ln) for ln in m.group(1).splitlines()]
                snippet = " ".join(ln for ln in lines if ln.strip() and not ln.strip().startswith(("-*-", "eslint", "@ts-", "type:", "coding")))
    snippet = re.sub(r"^\s*\*\s?", "", snippet, flags=re.M)
    snippet = re.sub(r"\s+", " ", snippet).strip()
    if len(snippet) > 240:
        snippet = snippet[:237].rstrip() + "..."
    return snippet
