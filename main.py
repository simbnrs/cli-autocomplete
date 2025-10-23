#!/usr/bin/env python3
"""
A CLI app with autocomplete functionality.
Type !q to quit. Press Enter to copy the autocomplete suggestion to clipboard.
Words are delimited by ';' and '|' instead of whitespace.
Autocomplete is powered by Meilisearch.
"""

import re
import sys
import pyperclip
import meilisearch
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

# Meilisearch configuration
MEILISEARCH_URL = "http://127.0.0.1:7700"
MEILISEARCH_MASTER_KEY = None  # Set to None for local development
INDEX_NAME = "words"


def setup_meilisearch():
    """
    Initialize Meilisearch client and index the words.

    Returns:
        tuple: (client, index) - Meilisearch client and index objects
    """
    try:
        # Create Meilisearch client
        client = meilisearch.Client(MEILISEARCH_URL, MEILISEARCH_MASTER_KEY)

        # Check if Meilisearch is running
        client.health()

        # Get or create the index
        try:
            index = client.get_index(INDEX_NAME)
            # Delete existing index to refresh data
            client.delete_index(INDEX_NAME)
        except Exception:
            pass

        # Create new index
        client.create_index(INDEX_NAME, {'primaryKey': 'id'})
        index = client.get_index(INDEX_NAME)

        # Prepare documents for indexing
        documents = [
            {"id": i, "word": word}
            for i, word in enumerate(WORDS)
        ]

        # Index the documents
        index.add_documents(documents)

        # Wait for indexing to complete
        index.wait_for_task(index.get_tasks().results[0].uid)

        print(f"✓ Meilisearch initialized with {len(WORDS)} words")
        return client, index

    except Exception as e:
        print(f"Error connecting to Meilisearch: {e}")
        print(f"Make sure Meilisearch is running at {MEILISEARCH_URL}")
        print("Run: docker run -d -p 7700:7700 getmeili/meilisearch:latest")
        sys.exit(1)


class CustomDelimiterCompleter(Completer):
    """A completer that uses custom delimiters and Meilisearch for suggestions."""

    def __init__(self, meilisearch_index, delimiters):
        """
        Initialize the completer.

        Args:
            meilisearch_index: Meilisearch index object to query
            delimiters: List of delimiter characters
        """
        self.index = meilisearch_index
        self.delimiters = delimiters

    def get_completions(self, document, complete_event):
        """Generate completions based on custom delimiters using Meilisearch."""
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

        # Don't search if the query is empty
        if not current_word:
            return

        try:
            # Query Meilisearch for matches
            # Use prefix search and limit to 5 results
            results = self.index.search(
                current_word,
                {
                    'limit': 5,
                    'attributesToRetrieve': ['word'],
                }
            )

            # Generate completions from Meilisearch results
            for hit in results['hits']:
                word = hit['word']
                yield Completion(
                    word,
                    start_position=-len(current_word),
                    display=word,
                )

        except Exception as e:
            # If Meilisearch query fails, silently continue
            # (could log this in production)
            pass


def main():
    """Main function to run the autocomplete CLI."""
    print("=" * 50)
    print("Autocomplete CLI (Powered by Meilisearch)")
    print("=" * 50)

    # Initialize Meilisearch
    client, index = setup_meilisearch()

    print("Type to see autocomplete suggestions")
    print("Use ';' or '|' as delimiters between words")
    print("Press ENTER to copy the suggestion to clipboard")
    print("Type '!q' to quit")
    print("=" * 50)
    print()

    # Create a custom delimiter completer with Meilisearch
    word_completer = CustomDelimiterCompleter(
        index,
        DELIMITERS,
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
