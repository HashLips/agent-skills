"""File category classification."""
from .constants import (
    ASSET_EXTS,
    CODE_EXTS,
    COMPONENT_EXTS,
    CONFIG_EXTS,
    CONFIG_NAME_RE,
    DATA_EXTS,
    DOC_EXTS,
    SHELL_EXTS,
    STYLE_EXTS,
    TEST_NAME_RE,
    TEST_PATH_RE,
)

def categorize(rel: str, name: str, ext: str) -> str:
    lower_name = name.lower()
    if TEST_PATH_RE.search(rel) or TEST_NAME_RE.search(lower_name):
        return "test"
    if ext in ASSET_EXTS and ext != ".svg":
        return "asset"
    if ext == ".svg" and "/src/" not in f"/{rel}":
        return "asset"
    if ext in STYLE_EXTS:
        return "style"
    if ext in DOC_EXTS:
        return "docs"
    if CONFIG_NAME_RE.search(lower_name) or ext in CONFIG_EXTS:
        return "config"
    if ext in {".yml", ".yaml"}:
        return "config"
    if rel.startswith(("scripts/", "bin/", "tools/")) or ext in SHELL_EXTS:
        return "script"
    if ext in COMPONENT_EXTS:
        return "component"
    if ext in CODE_EXTS:
        return "source"
    if ext in DATA_EXTS:
        return "data"
    return "other"

