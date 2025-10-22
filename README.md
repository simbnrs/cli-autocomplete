# CLI Autocomplete

A simple Python CLI application that provides autocomplete suggestions while you type, based on a predefined list of programming language names.

## Features

- **Real-time autocomplete**: See suggestions as you type
- **Custom delimiters**: Use `;` and `|` as word separators instead of whitespace
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
Autocomplete CLI
==================================================
Type to see autocomplete suggestions
Use ';' or '|' as delimiters between words
Press ENTER to copy the suggestion to clipboard
Type '!q' to quit
==================================================

Type here: pyt  # As you type "pyt", "Python" appears as suggestion
Type here: Python;java  # After delimiter ';', typing "java" suggests "JavaScript"
Type here: Python;JavaScript|rust  # Works with '|' delimiter too, suggesting "Rust"
```

When you press Enter, the entire line will be copied to your clipboard.

## Custom Delimiters

This app uses custom delimiters (`;` and `|`) instead of whitespace. This means:
- You can include spaces in your input without triggering a new completion
- Only `;` and `|` characters will start a new autocomplete context
- Example: `Python ; Java | TypeScript` will autocomplete three separate words

## Requirements

- Python 3.11+
- prompt-toolkit
- pyperclip

## License

MIT
