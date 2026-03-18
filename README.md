# Little-videogame- 🎮

A simple **Hangman** game that runs directly in your Windows CMD or terminal.

---

## ✅ Step 1 — Make sure Python is installed

Open CMD (Windows) or Terminal (Mac/Linux) and type:

```
python --version
```

You should see something like `Python 3.x.x`.  
If you get an error, download Python for free at **https://www.python.org/downloads/** and install it.

---

## ✅ Step 2 — Save the game file

**What to copy:** the file [`game.py`](game.py) in this repository.

Here is exactly what to do:

1. Click on **`game.py`** at the top of this page (or [click here](game.py)).
2. Click the **Raw** button (top-right of the file view) — you will see plain text code.
3. Press **Ctrl + A** (select all), then **Ctrl + C** (copy).
4. Open **Notepad** (Windows) or any plain text editor.
5. Press **Ctrl + V** to paste.
6. Save the file as **`game.py`** — for example, save it on your Desktop.

> ⚠️ Make sure Notepad saves it as `game.py` and **not** `game.py.txt`.  
> In Notepad → "Save As" → change "Save as type" to **All Files (\*.\*)** → type `game.py` → Save.

---

## ✅ Step 3 — Open CMD in the same folder

**On Windows:**

1. Open the folder where you saved `game.py` (e.g. the Desktop).
2. Click the address bar at the top of the folder window.
3. Type `cmd` and press **Enter** — a black CMD window opens in that folder.

**On Mac / Linux:**

Open Terminal, then type `cd` followed by the path to the folder, for example:
```
cd ~/Desktop
```

---

## ✅ Step 4 — Run the game

Type this **exactly** into CMD and press **Enter**:

```
python game.py
```

> On Mac or Linux, use `python3 game.py` if `python` does not work.

The game will start immediately! 🎮

---

## 🎮 How to play

| | |
|---|---|
| 🔤 | A secret word is hidden. Guess it **one letter at a time**. |
| ❌ | You get **6 wrong guesses** before the man is hanged. |
| ✅ | Reveal every letter in the word to win! |
| 🚪 | Type `quit` and press Enter at any time to exit. |

---

## 📺 What it looks like

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