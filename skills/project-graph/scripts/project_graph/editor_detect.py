"""Detect host IDE for Go-to-file URI scheme (generation-time)."""
from __future__ import annotations

import os
from typing import Tuple

from .constants import EDITOR_SCHEME

# (substring in env value, scheme) — order matters; Cursor before generic Code paths.
_PATH_HINTS = (
    ("cursor", "cursor"),
    ("vscodium", "vscodium"),
    ("windsurf", "windsurf"),
    ("/code/", "vscode"),
    ("\\code\\", "vscode"),
)

_CURSOR_ENV_KEYS = (
    "CURSOR_TRACE_ID",
    "CURSOR_AGENT",
    "CURSOR_SESSION_ID",
    "CURSOR_CHANNEL",
    "CURSOR_WORKSPACE_LABEL",
    "CURSOR_LAYOUT",
)


def detect_editor_scheme() -> Tuple[str, str]:
    """Return (scheme, source) where source explains how the scheme was chosen."""
    env = os.environ

    if any(env.get(k) for k in _CURSOR_ENV_KEYS):
        return "cursor", "cursor_env"

    hook = str(env.get("VSCODE_IPC_HOOK", ""))
    hook_l = hook.lower()
    for hint, scheme in _PATH_HINTS:
        if hint in hook_l:
            return scheme, "host_path"

    for key, val in env.items():
        if not key.startswith("VSCODE_") or not isinstance(val, str):
            continue
        vl = val.lower()
        for hint, scheme in _PATH_HINTS:
            if hint in vl:
                return scheme, "host_path"

    if env.get("VSCODE_IPC_HOOK") or env.get("VSCODE_PID"):
        return "vscode", "vscode_env"

    return EDITOR_SCHEME, "default"
