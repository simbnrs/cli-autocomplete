#!/usr/bin/env python3
"""
A CLI app with autocomplete functionality.
Type !q to quit. Press Enter to copy the autocomplete suggestion to clipboard.
"""

import pyperclip
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


# Target list of words for autocomplete
WORDS = [
    "Python",
    "JavaScript",
    "TypeScript",
    "Rust",
    "Go",
    "Java",
    "Ruby",
    "Swift",
    "Kotlin",
    "Haskell",
]


def main():
    """Main function to run the autocomplete CLI."""
    print("=" * 50)
    print("Autocomplete CLI")
    print("=" * 50)
    print("Type to see autocomplete suggestions")
    print("Press ENTER to copy the suggestion to clipboard")
    print("Type '!q' to quit")
    print("=" * 50)
    print()

    # Create a word completer with case-insensitive matching
    word_completer = WordCompleter(
        WORDS,
        ignore_case=True,
        sentence=False,  # Don't complete in middle of sentences
    )

    while True:
        try:
            # Get user input with autocomplete
            user_input = prompt(
                "Type here: ",
                completer=word_completer,
                complete_while_typing=True,  # Show suggestions as you type
            )

            # Check if user wants to quit
            if user_input.strip() == "!q":
                print("Goodbye!")
                break

            # Copy to clipboard if something was entered
            if user_input.strip():
                pyperclip.copy(user_input)
                print(f"✓ Copied to clipboard: '{user_input}'")
                print()

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nGoodbye!")
            break
        except EOFError:
            # Handle Ctrl+D gracefully
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
