# 🥀 the_great_exodus.py

*"Higanbana blooms where the dead have passed, and where nothing returns."*

This script is a one-way ferry. Point it at a folder, run it, and every
file inside packs its bags and relocates to `/tmp` — no goodbyes, no
copies left behind. All that remains where they used to live is a single
withered petal: `filelist.txt`, the manifest of who left and when.

## 🕯️ What it actually does

1. Looks around the current directory.
2. Makes a list of every *file* it finds (folders are left alone — this
   isn't that kind of massacre).
3. Writes that list to `filelist.txt`, so you have a record of the dead.
4. Moves each file, one by one, into `/tmp`.
5. Prints a little eulogy for each one as it goes.

## ☠️ The crime it used to be

The original version of this script (RIP) had three separate curses on it:

- `import OS` — capital letters, because Python's `os` module apparently
  needed to be shouted at. This alone made it fail before it even started.
- A `filelist.txt` that got *opened* but never actually written to or
  closed — a grave dug and never filled.
- An `os.chdir('/tmp')` fired *before* the loop even began, so by the
  time it tried to rename files, it was already standing in `/tmp`
  looking for files that were never there. Doomed from the first step.

This version fixes all three, adds a manifest that's actually useful,
and skips over the script itself so it doesn't accidentally exile itself
along with everything else.

## 🌺 How to run it

```bash
python the_great_exodus.py
```

Run it from inside whichever directory you want to... reduce. It reads
that directory, not wherever it happens to be saved.

## ⚠️ A word of warning

This *moves* files, it doesn't copy them. If you run it in the wrong
folder, that folder will be a folder of one file: `filelist.txt`,
mourning everything that used to be there. Point carefully.

---
*Filed under: 2026-09-26, the day the tmp folder grew a little heavier.*
