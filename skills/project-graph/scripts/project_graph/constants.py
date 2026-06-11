"""Shared constants for project graph generation."""
import re
OUTPUT_NAME = "project-graph.html"
FLOWS_MANIFEST = "project-graph.flows.json"
KNOWLEDGE_FILE = "project-graph.knowledge.json"
MAX_PARSE_BYTES = 1_500_000
MAX_AUTO_FLOWS = 200

# ---------------------------------------------------------------- languages

LANG_BY_EXT = {
    ".ts": "TypeScript", ".tsx": "TypeScript", ".mts": "TypeScript", ".cts": "TypeScript",
    ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
    ".vue": "Vue", ".svelte": "Svelte", ".astro": "Astro",
    ".py": "Python", ".rb": "Ruby", ".go": "Go", ".rs": "Rust",
    ".java": "Java", ".kt": "Kotlin", ".kts": "Kotlin", ".swift": "Swift",
    ".c": "C", ".h": "C", ".cpp": "C++", ".cc": "C++", ".hpp": "C++",
    ".cs": "C#", ".php": "PHP", ".lua": "Lua", ".dart": "Dart", ".ex": "Elixir", ".exs": "Elixir",
    ".css": "CSS", ".scss": "SCSS", ".sass": "Sass", ".less": "Less", ".styl": "Stylus",
    ".html": "HTML", ".htm": "HTML", ".xml": "XML", ".svg": "SVG",
    ".md": "Markdown", ".mdx": "MDX", ".rst": "reST", ".txt": "Text",
    ".json": "JSON", ".jsonc": "JSON", ".yml": "YAML", ".yaml": "YAML",
    ".toml": "TOML", ".ini": "INI", ".cfg": "INI", ".env": "Env",
    ".sql": "SQL", ".graphql": "GraphQL", ".gql": "GraphQL", ".prisma": "Prisma", ".proto": "Protobuf",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell", ".ps1": "PowerShell", ".bat": "Batch",
    ".r": "R", ".scala": "Scala", ".clj": "Clojure", ".hs": "Haskell", ".zig": "Zig",
}

CODE_EXTS = {
    ".ts", ".tsx", ".mts", ".cts", ".js", ".jsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro",
    ".py", ".rb", ".go", ".rs", ".java", ".kt", ".kts", ".swift", ".c", ".h", ".cpp", ".cc",
    ".hpp", ".cs", ".php", ".lua", ".dart", ".ex", ".exs", ".r", ".scala", ".clj", ".hs", ".zig",
}
COMPONENT_EXTS = {".tsx", ".jsx", ".vue", ".svelte", ".astro"}
STYLE_EXTS = {".css", ".scss", ".sass", ".less", ".styl"}
DOC_EXTS = {".md", ".mdx", ".rst", ".txt"}
DATA_EXTS = {".json", ".jsonc", ".csv", ".tsv", ".sql", ".graphql", ".gql", ".prisma", ".proto", ".xml"}
ASSET_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".ico", ".bmp", ".svg",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
    ".mp3", ".mp4", ".wav", ".ogg", ".webm", ".mov", ".pdf", ".zip", ".gz", ".glb", ".gltf",
}
CONFIG_EXTS = {".toml", ".ini", ".cfg", ".env", ".properties", ".editorconfig"}
SHELL_EXTS = {".sh", ".bash", ".zsh", ".ps1", ".bat"}

CONFIG_NAME_RE = re.compile(
    r"(^\.|config|conf$|rc$|rc\.|^dockerfile|^makefile|^procfile|\.lock$|^docker-compose"
    r"|^package\.json$|^tsconfig|^pyproject|^setup\.(py|cfg)$|^cargo\.toml$|^go\.(mod|sum)$"
    r"|^gemfile|^requirements.*\.txt$|^\.env)",
    re.IGNORECASE,
)
TEST_PATH_RE = re.compile(r"(^|/)(tests?|__tests__|spec|e2e|cypress)(/|$)", re.IGNORECASE)
TEST_NAME_RE = re.compile(r"\.(test|spec)\.[^.]+$|(_|^)test_", re.IGNORECASE)

EXT_PRIORITY = [
    ".ts", ".tsx", ".mts", ".js", ".jsx", ".mjs", ".cjs", ".vue", ".svelte", ".astro",
    ".py", ".rb", ".go", ".rs", ".java", ".kt", ".php", ".cs", ".c", ".cpp",
    ".css", ".scss", ".json", ".md", ".html",
]

DEFAULT_IGNORE_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "bower_components", "vendor",
    ".venv", "venv", "env", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    "dist", "build", "out", ".next", ".nuxt", ".svelte-kit", ".astro", ".turbo",
    ".cache", ".parcel-cache", "coverage", ".idea", ".vscode", ".DS_Store",
    "target", "Pods", "DerivedData", ".gradle", ".terraform", ".serverless",
}

