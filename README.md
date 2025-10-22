# CLI Autocomplete

A simple Python CLI application that provides autocomplete suggestions while you type, based on a predefined list of programming language names.

## Features

- **Real-time autocomplete**: See suggestions as you type
- **Case-insensitive matching**: Type in any case and get suggestions
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

## Usage

Run the application:

```bash
uv run python main.py
```

### Instructions

1. Start typing a programming language name
2. Use arrow keys to navigate suggestions (if multiple matches)
3. Press Tab or Right Arrow to accept the current suggestion
4. Press Enter to copy the completed word to your clipboard
5. Type `!q` to exit the application
6. Or press Ctrl+C or Ctrl+D to exit

## Example

```
==================================================
Autocomplete CLI
==================================================
Type to see autocomplete suggestions
Press ENTER to copy the suggestion to clipboard
Type '!q' to quit
==================================================

Type here: pyt  # As you type "pyt", "Python" appears as suggestion
```

When you press Enter, the word will be copied to your clipboard.

## Requirements

- Python 3.11+
- prompt-toolkit
- pyperclip

## License

MIT
