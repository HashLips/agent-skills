# Preserve Regions

Copy sanitizer edits **natural language the author wrote or approved**. Some parts of a paste must stay literal.

## Always preserve unless user says otherwise

- **Proper nouns** — people, brands, places, titles
- **Quotes and dialogue** — exact wording inside quotation marks
- **Numbers, dates, statistics, legal or medical terms** — factual literals
- **URLs, emails, handles, SKUs, code snippets** — do not rephrase
- **User-marked blocks** — anything the user flags as do not edit

## Optional preserve (ask or infer from context)

- **Headlines the user supplied verbatim**
- **Taglines or trademarked phrases**
- **Citations and references** — author, title, year unchanged
- **Lists of specs** — model numbers, ingredients, features (fix prose around them, not the list items)

## What to sanitize

- Sentences and paragraphs meant to be read as the author's voice
- Body copy, intros, conclusions, transitions, descriptions
- Social captions, email bodies, chapter narration, ad paragraphs

## Format agnostic

Copy may arrive as plain text, HTML, markdown, or a paste from a doc. Deliver **readable publishable text**, not markup.

## Strip markdown (book and manuscript copy)

When the source uses markdown (or similar) styling, **remove the symbols** and keep the words. Readers of books and print copy should not see `**`, `#`, or link syntax.

| Markup | Output |
| --- | --- |
| `**bold**` or `__bold__` | bold |
| `*italic*` or `_italic_` | italic |
| `# Heading` | Heading as plain line (no `#`) |
| `` `code` `` in prose | plain word unless it is a real command the user must keep |
| `[label](url)` | label, or label plus url in parentheses if the url matters |
| `---`, `***` | remove rule lines |
| Leading `- ` or `1. ` list markers | plain paragraph or simple line break; no bullet syntax |

Do not leave stray asterisks, hashes, or backticks in final copy unless the user asks to keep markdown.

If the user says output is for the web and must stay markdown, skip this strip for that session.

## User instructions win

If the user says keep a paragraph, tone, or term unchanged, skip it for that session.

When unsure whether something is copy or a literal, **preserve**.
