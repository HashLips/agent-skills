"""Import/reference extraction from source files."""
from __future__ import annotations

import re
from typing import List, Tuple

from .constants import SHELL_EXTS, STYLE_EXTS


RE_JS_IMPORT = re.compile(r"""(?:^|[\s;(])import\s+(?:type\s+)?(?:[\w*\s{},$]+?\s+from\s+)?["']([^"'\n]+)["']""", re.M)
RE_JS_EXPORT = re.compile(r"""(?:^|[\s;])export\s+(?:type\s+)?[\w*\s{},$]*?\s*from\s+["']([^"'\n]+)["']""", re.M)
RE_REQUIRE = re.compile(r"""require\s*\(\s*["']([^"'\n]+)["']\s*\)""")
RE_DYN_IMPORT = re.compile(r"""import\s*\(\s*["']([^"'\n]+)["']\s*\)""")
RE_PY_FROM = re.compile(r"^\s*from\s+([.\w]+)\s+import\s", re.M)
RE_PY_IMPORT = re.compile(r"^\s*import\s+([\w.]+(?:\s*,\s*[\w.]+)*)", re.M)
RE_CSS_IMPORT = re.compile(r"""@import\s+(?:url\(\s*)?["']?([^"'()\s;]+)""")
RE_CSS_USE = re.compile(r"""@(?:use|forward)\s+["']([^"'\n]+)["']""")
RE_HTML_REF = re.compile(r"""(?:src|href)\s*=\s*["']([^"'\n]+)["']""", re.IGNORECASE)
RE_C_INCLUDE = re.compile(r"""^\s*#include\s*"([^"\n]+)\"""", re.M)
RE_GO_BLOCK = re.compile(r"import\s*\(([^)]*)\)", re.S)
RE_GO_SINGLE = re.compile(r"""^\s*import\s+(?:\w+\s+)?"([^"\n]+)\"""", re.M)
RE_GO_PATH = re.compile(r"""(?:^|\n)\s*(?:\w+\s+)?"([^"\n]+)\"""")
RE_RUST_MOD = re.compile(r"^\s*(?:pub\s+)?mod\s+(\w+)\s*;", re.M)
RE_RUST_USE = re.compile(r"^\s*(?:pub\s+)?use\s+crate::([\w:]+)", re.M)
RE_JVM_IMPORT = re.compile(r"^\s*import\s+(?:static\s+)?([\w.]+)", re.M)
RE_RUBY_REQREL = re.compile(r"""require_relative\s+["']([^"'\n]+)["']""")
RE_PHP_INCLUDE = re.compile(r"""(?:require|include)(?:_once)?\s*\(?\s*(?:__DIR__\s*\.\s*)?["']([^"'\n]+)["']""")
RE_SHELL_SOURCE = re.compile(r"""(?:^|\s)(?:source|\.)\s+["']?([\w./~-]+)""", re.M)
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+?)(?:[#?][^)]*)?\)")

JS_LIKE = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".mts", ".cts", ".vue", ".svelte", ".astro"}


def extract_refs(ext: str, text: str) -> List[Tuple[str, str, str]]:
    """Return list of (spec, kind, resolver_hint)."""
    refs: List[Tuple[str, str, str]] = []
    if ext in JS_LIKE or ext in {".html", ".htm"}:
        for m in RE_JS_IMPORT.finditer(text):
            refs.append((m.group(1), "import", "js"))
        for m in RE_JS_EXPORT.finditer(text):
            refs.append((m.group(1), "re-export", "js"))
        for m in RE_REQUIRE.finditer(text):
            refs.append((m.group(1), "require", "js"))
        for m in RE_DYN_IMPORT.finditer(text):
            refs.append((m.group(1), "dynamic import", "js"))
    if ext in {".html", ".htm"}:
        for m in RE_HTML_REF.finditer(text):
            refs.append((m.group(1), "link", "path"))
    if ext == ".py":
        for m in RE_PY_FROM.finditer(text):
            refs.append((m.group(1), "import", "py"))
        for m in RE_PY_IMPORT.finditer(text):
            for part in m.group(1).split(","):
                refs.append((part.strip(), "import", "py"))
    if ext in STYLE_EXTS:
        for m in RE_CSS_IMPORT.finditer(text):
            refs.append((m.group(1), "style import", "path"))
        for m in RE_CSS_USE.finditer(text):
            refs.append((m.group(1), "style use", "path"))
    if ext in {".c", ".h", ".cpp", ".cc", ".hpp"}:
        for m in RE_C_INCLUDE.finditer(text):
            refs.append((m.group(1), "include", "path"))
    if ext == ".go":
        for block in RE_GO_BLOCK.finditer(text):
            for m in RE_GO_PATH.finditer(block.group(1)):
                refs.append((m.group(1), "import", "dotted-path"))
        for m in RE_GO_SINGLE.finditer(text):
            refs.append((m.group(1), "import", "dotted-path"))
    if ext == ".rs":
        for m in RE_RUST_MOD.finditer(text):
            refs.append((m.group(1), "mod", "rust-mod"))
        for m in RE_RUST_USE.finditer(text):
            refs.append((m.group(1).replace("::", "/"), "use", "rust-crate"))
    if ext in {".java", ".kt", ".kts", ".scala", ".cs"}:
        for m in RE_JVM_IMPORT.finditer(text):
            refs.append((m.group(1), "import", "dotted"))
    if ext == ".rb":
        for m in RE_RUBY_REQREL.finditer(text):
            refs.append(("./" + m.group(1), "require", "path"))
    if ext == ".php":
        for m in RE_PHP_INCLUDE.finditer(text):
            spec = m.group(1)
            if not spec.startswith((".", "/")):
                spec = "./" + spec
            refs.append((spec, "include", "path"))
    if ext in SHELL_EXTS:
        for m in RE_SHELL_SOURCE.finditer(text):
            refs.append((m.group(1), "source", "path"))
    if ext in {".md", ".mdx"}:
        for m in RE_MD_LINK.finditer(text):
            spec = m.group(1)
            if spec.startswith(("http:", "https:", "mailto:", "#", "data:")):
                continue
            refs.append((spec, "doc link", "path"))
    return refs
