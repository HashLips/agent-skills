"""Project graph generator — modular package."""
from .build import build_payload
from .cli import main
from .render import render_html

__all__ = ["build_payload", "main", "render_html"]
