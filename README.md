# CLI Autocomplete

A Python CLI application that provides autocomplete suggestions powered by Meilisearch. Type words with custom delimiters and get intelligent, fast autocomplete suggestions.

## Features

- **Meilisearch-powered autocomplete**: Lightning-fast search with typo tolerance
- **Top 5 results**: Get the 5 most relevant suggestions for your query
- **Real-time autocomplete**: See suggestions as you type
- **Custom delimiters**: Use `;` and `|` as word separators instead of whitespace
- **Clipboard integration**: Press Enter to copy your selection to the clipboard
- **Easy exit**: Type `!q` to quit the application

## Word List

The application autocompletes the following programming languages:
- Python
- JavaScript
- TypeScript
- Rust
- Go
- Java
- Ruby
- Swift
- Kotlin
- Haskell

## Installation

This project uses `uv` as the package manager. First, ensure you have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install the dependencies:

```bash
uv sync
```

## Meilisearch Setup

This application requires Meilisearch to be running. Meilisearch is a powerful, fast, open-source search engine.

### Option 1: Using Docker (Recommended)

```bash
# Run Meilisearch in a Docker container
docker run -d -p 7700:7700 getmeili/meilisearch:latest

# Verify it's running
curl http://127.0.0.1:7700/health
```

### Option 2: Local Installation

Download and install Meilisearch from [meilisearch.com](https://www.meilisearch.com/docs/learn/getting_started/quick_start):

```bash
# macOS
brew install meilisearch

# Linux (using curl)
curl -L https://install.meilisearch.com | sh

# Start Meilisearch
meilisearch
```

The application will automatically:
1. Connect to Meilisearch at `http://127.0.0.1:7700`
2. Create an index called "words"
3. Index all the programming language names
4. Use prefix search with a limit of 5 results

## Usage

Run the application:

```bash
uv run python main.py
```

### Instructions

1. Start typing a programming language name
2. Use `;` or `|` as delimiters to separate multiple words
3. Autocomplete works after each delimiter
4. Use arrow keys to navigate suggestions (if multiple matches)
5. Press Tab or Right Arrow to accept the current suggestion
6. Press Enter to copy the entire line to your clipboard
7. Type `!q` to exit the application
8. Or press Ctrl+C or Ctrl+D to exit

## Example

```
==================================================
Autocomplete CLI (Powered by Meilisearch)
==================================================
✓ Meilisearch initialized with 10 words
Type to see autocomplete suggestions
Use ';' or '|' as delimiters between words
Press ENTER to copy the suggestion to clipboard
Type '!q' to quit
==================================================

Type here: pyt  # Meilisearch returns top 5 matches, "Python" appears
Type here: Python;java  # After ';', typing "java" suggests "JavaScript", "Java"
Type here: Python;JavaScript|rus  # After '|', suggests "Rust"
```

When you press Enter, the entire line will be copied to your clipboard.

**Note**: Meilisearch provides intelligent search with typo tolerance, so even if you mistype, you'll still get relevant suggestions!

## Custom Delimiters

This app uses custom delimiters (`;` and `|`) instead of whitespace. This means:
- You can include spaces in your input without triggering a new completion
- Only `;` and `|` characters will start a new autocomplete context
- Example: `Python ; Java | TypeScript` will autocomplete three separate words

## Requirements

### Software
- Python 3.11+
- Meilisearch (running locally or via Docker)

### Python Packages
- meilisearch
- prompt-toolkit
- pyperclip

All Python dependencies are automatically installed via `uv sync`.

## License

MIT
