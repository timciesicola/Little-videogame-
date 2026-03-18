"""
╔══════════════════════════════════════════╗
║         HANGMAN  –  CMD  EDITION         ║
║  Just run:  python game.py               ║
╚══════════════════════════════════════════╝

Rules
-----
  • Guess the hidden word one letter at a time.
  • You have 6 wrong guesses before the man is hanged.
  • Type a single letter and press Enter each turn.
  • Type 'quit' to exit at any time.
"""

import random
import os

# ── word list ────────────────────────────────────────────────────────────────
WORDS = [
    # animals
    "elephant", "giraffe", "penguin", "dolphin", "cheetah",
    "crocodile", "butterfly", "hamster", "kangaroo", "flamingo",
    # fruits
    "strawberry", "pineapple", "watermelon", "blueberry", "tangerine",
    # tech
    "keyboard", "monitor", "software", "internet", "algorithm",
    "database", "password", "download", "bluetooth", "processor",
    # misc
    "adventure", "treasure", "mystery", "champion", "volcano",
    "rainbow", "universe", "dinosaur", "skeleton", "gravity",
]

# ── ASCII art for each stage (0 = fresh gallows, 6 = fully drawn) ────────────
HANGMAN_STAGES = [
    # 0 wrong guesses
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # 1 wrong guess
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # 2 wrong guesses
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # 3 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # 4 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    # 5 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    # 6 wrong guesses – game over
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

MAX_WRONG = len(HANGMAN_STAGES) - 1   # 6


def clear():
    """Clear the terminal screen (works on Windows and Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def display(word, guessed, wrong_letters):
    """Print the current game state."""
    clear()
    print("=" * 44)
    print("          H  A  N  G  M  A  N")
    print("=" * 44)

    # gallows
    print(HANGMAN_STAGES[len(wrong_letters)])

    # masked word  e.g.  _ l _ _ h _ n t
    masked = "  ".join(
        letter if letter in guessed else "_" for letter in word
    )
    print(f"  Word:  {masked}\n")

    # wrong guesses
    if wrong_letters:
        print(f"  Wrong guesses ({len(wrong_letters)}/{MAX_WRONG}): "
              + "  ".join(sorted(wrong_letters)).upper())
    else:
        print(f"  Wrong guesses: none yet  (you have {MAX_WRONG} tries)")

    print()


def get_letter(guessed):
    """Prompt the player for a valid, not-yet-used letter."""
    while True:
        raw = input("  Enter a letter (or 'quit'): ").strip().lower()
        if raw == "quit":
            return None
        if len(raw) != 1 or not raw.isalpha():
            print("  ✗ Please type a single letter.")
            continue
        if raw in guessed:
            print(f"  ✗ You already tried '{raw.upper()}'. Pick another.")
            continue
        return raw


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()

    while True:
        display(word, guessed, wrong)

        # victory check
        if all(letter in guessed for letter in word):
            print(f"  🎉  You won!  The word was: {word.upper()}")
            print("=" * 44)
            break

        # defeat check
        if len(wrong) >= MAX_WRONG:
            print(f"  💀  Game over!  The word was: {word.upper()}")
            print("=" * 44)
            break

        letter = get_letter(guessed)
        if letter is None:          # player typed 'quit'
            print(f"\n  Quitting… the word was: {word.upper()}")
            break

        guessed.add(letter)
        if letter in word:
            count = word.count(letter)
            print(f"  ✓ '{letter.upper()}' is in the word! "
                  f"({count} time{'s' if count > 1 else ''})")
        else:
            wrong.add(letter)
            remaining = MAX_WRONG - len(wrong)
            print(f"  ✗ '{letter.upper()}' is NOT in the word. "
                  f"{remaining} chance{'s' if remaining != 1 else ''} left.")

        input("  (press Enter to continue)")


def main():
    while True:
        play()
        print()
        again = input("  Play again? (y / n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()
