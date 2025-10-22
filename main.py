#!/usr/bin/env python3
"""
A CLI app with autocomplete functionality.
Type !q to quit. Press Enter to copy the autocomplete suggestion to clipboard.
Words are delimited by ';' and '|' instead of whitespace.
"""

import re
import pyperclip
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document


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

# Custom delimiters
DELIMITERS = [';', '|']


class CustomDelimiterCompleter(Completer):
    """A completer that uses custom delimiters instead of whitespace."""

    def __init__(self, words, delimiters, ignore_case=True):
        self.words = words
        self.delimiters = delimiters
        self.ignore_case = ignore_case

    def get_completions(self, document, complete_event):
        """Generate completions based on custom delimiters."""
        # Get the text before the cursor
        text_before_cursor = document.text_before_cursor

        # Find the last delimiter position
        last_delimiter_pos = -1
        for delimiter in self.delimiters:
            pos = text_before_cursor.rfind(delimiter)
            if pos > last_delimiter_pos:
                last_delimiter_pos = pos

        # Extract the current word (after the last delimiter)
        if last_delimiter_pos >= 0:
            current_word = text_before_cursor[last_delimiter_pos + 1:]
        else:
            current_word = text_before_cursor

        # Strip leading/trailing whitespace from the current word
        current_word = current_word.strip()

        # Generate completions
        for word in self.words:
            if self.ignore_case:
                if word.lower().startswith(current_word.lower()):
                    # Calculate how much of the word to display
                    # We want to complete from the current position
                    yield Completion(
                        word,
                        start_position=-len(current_word),
                        display=word,
                    )
            else:
                if word.startswith(current_word):
                    yield Completion(
                        word,
                        start_position=-len(current_word),
                        display=word,
                    )


def main():
    """Main function to run the autocomplete CLI."""
    print("=" * 50)
    print("Autocomplete CLI")
    print("=" * 50)
    print("Type to see autocomplete suggestions")
    print("Use ';' or '|' as delimiters between words")
    print("Press ENTER to copy the suggestion to clipboard")
    print("Type '!q' to quit")
    print("=" * 50)
    print()

    # Create a custom delimiter completer with case-insensitive matching
    word_completer = CustomDelimiterCompleter(
        WORDS,
        DELIMITERS,
        ignore_case=True,
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
