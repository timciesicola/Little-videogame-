# Little-videogame- 🎮

A simple **Hangman** game you can run straight from your terminal / Windows CMD.

---

## Requirements

* **Python 3** – already installed on most systems.  
  Check with: `python --version` (Windows) or `python3 --version` (Mac/Linux).

---

## How to play

### Option A – run the file you cloned

```
python game.py
```

*(On Mac / Linux use `python3 game.py`)*

### Option B – copy & paste into CMD

1. Open `game.py` in any text editor.
2. Select all the text and copy it.
3. Open a CMD / terminal window.
4. Start a Python session:
   ```
   python
   ```
5. Paste the code and press **Enter** (or **Ctrl+D** on Mac/Linux to send EOF).

---

## Rules

| | |
|---|---|
| 🔤 | Guess the hidden word one **letter at a time**. |
| ❌ | You get **6 wrong guesses** before the man is hanged. |
| ✅ | Reveal every letter to win! |
| 🚪 | Type `quit` at any time to exit. |

---

## Preview

```
============================================
          H  A  N  G  M  A  N
============================================

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

  Word:  e _ e p h _ n t

  Wrong guesses (3/6): A  B  Z

  Enter a letter (or 'quit'):
```