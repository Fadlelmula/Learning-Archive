# 🧪 C++ Examples — The Workshop Floor

![Language](https://img.shields.io/badge/language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Examples](https://img.shields.io/badge/examples-0%20so%20far-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-workshop%20just%20opened-orange?style=for-the-badge)
![Part Of](https://img.shields.io/badge/part%20of-Learning--Archive-black?style=for-the-badge&logo=github)

> *"If you're nothing without the suit, then you shouldn't have it."* — Tony Stark
> (Translation: reading about code is not enough. I have to **build** it, break it, and fix it.) 🔧💥

---

## 👋 What Is This Folder?

The topic files in [`../`](../) are my **notes**. This folder is my **proof of work**.

Every program here is something I actually wrote, compiled, and ran. Some will work on the first try. Most won't. The failures go in [`../../notes/things-i-broke.md`](../../notes/things-i-broke.md), because honesty beats pretending. 😅

| 🎯 Purpose | 💬 What It Means |
|---|---|
| Practice | Turning theory from the topic files into muscle memory |
| Proof | Showing (to myself, learners, and employers) that I really built it |
| Iteration | Mark I is ugly. Mark II is better. The history stays visible. |

---

## 🗺️ Folder Layout

Every example lives in its **own folder** with its own README, so the folder stays tidy as it grows.

```
examples/
├── README.md                          ← you are here 📍
├── YYYY-MM-DD-short-name/             ← one folder per example
│   ├── README.md                      ← what it is, how to run it, what I learned
│   ├── main.cpp                       ← the code
│   └── screenshot.png                 ← (optional) the program running
└── ...
```

**Folder naming rule:** `date-` + `source or type` + `-name`, e.g.

```
2026-11-20-LEARN-Hello-World
2026-11-22-PRACTICE-Number-Guessing-Game
2026-12-01-PROJECT-Contact-Book
```

> 💡 Dates at the front keep the folders sorted in the order I built them, so the list reads like a timeline of my progress.

---

## 📚 Example Index

**Legend:** ✅ Done · 🚧 In progress · 🔜 Planned

### 🚀 Mark I: Basics, Control Flow, Functions

| 📅 Date | 📁 Example | 🧠 Practices | 📖 From Topic File | 🚦 |
|---|---|---|---|---|
| — | Hello World + compile it myself | Program structure, `g++` | [`basics.md`](../basics.md) | 🔜 |
| — | Temperature converter (C → F) | Variables, `double`, integer-division trap | [`basics.md`](../basics.md) | 🔜 |
| — | FizzBuzz | `for`, `if`, `%` | [`control-flow.md`](../control-flow.md) | 🔜 |
| — | Number guessing game | `while`, `cin`, functions | [`control-flow.md`](../control-flow.md) | 🔜 |
| — | Factorial (recursive) | Functions, base case | [`functions.md`](../functions.md) | 🔜 |
| — | Swap with references | `&`, pass by reference | [`functions.md`](../functions.md) | 🔜 |

### 🔧 Mark II: Arrays and Strings

| 📅 Date | 📁 Example | 🧠 Practices | 📖 From Topic File | 🚦 |
|---|---|---|---|---|
| — | Vowel counter | `std::string`, loops, `<cctype>` | [`arrays-and-strings.md`](../arrays-and-strings.md) | 🔜 |
| — | Palindrome checker | Strings, two-index loop | [`arrays-and-strings.md`](../arrays-and-strings.md) | 🔜 |
| — | Largest number in a vector | `std::vector`, loops | [`arrays-and-strings.md`](../arrays-and-strings.md) | 🔜 |

### 👹 Mark III: Pointers and Memory

| 📅 Date | 📁 Example | 🧠 Practices | 📖 From Topic File | 🚦 |
|---|---|---|---|---|
| — | Pointer swap (`int*` version) | Pointers, `&`, `*` | [`pointers-and-memory.md`](../pointers-and-memory.md) | 🔜 |
| — | Heap vs smart pointer demo | `new`/`delete` vs `unique_ptr` | [`pointers-and-memory.md`](../pointers-and-memory.md) | 🔜 |

### 🏗️ Mark IV: OOP

| 📅 Date | 📁 Example | 🧠 Practices | 📖 From Topic File | 🚦 |
|---|---|---|---|---|
| — | Bank account class | Encapsulation, constructors | [`oop.md`](../oop.md) | 🔜 |
| — | Shapes with polymorphism | Inheritance, `virtual`, `override` | [`oop.md`](../oop.md) | 🔜 |

### 🧰 Mark V: STL and File I/O

| 📅 Date | 📁 Example | 🧠 Practices | 📖 From Topic File | 🚦 |
|---|---|---|---|---|
| — | Word counter | `std::map`, `istringstream` | [`stl.md`](../stl.md) | 🔜 |
| — | Tiny to-do saver | `vector`, file read and write | [`file-io.md`](../file-io.md) | 🔜 |
| — | CSV reader | `getline` with a delimiter, `stoi` | [`file-io.md`](../file-io.md) | 🔜 |

### 🏆 Capstone Projects

| 📅 Date | 📁 Project | 🧠 Uses | 🚦 |
|---|---|---|---|
| — | Contact book | Classes, `map`, file I/O | 🔜 |
| — | Text adventure | Classes, inheritance, `switch` | 🔜 |
| — | Mini J.A.R.V.I.S. (text commands) | Strings, `map` of commands, polymorphism | 🔜 |

> 🌱 This index grows with every example I finish. The planned ones come from the mini challenges in each topic file, and I'll swap in real dates and links as I build them.

---

## ▶️ How to Run Any Example

```bash
# 1. Go into the example's folder
cd 2026-11-20-LEARN-Hello-World

# 2. Compile main.cpp into a program called "app"
#    -std=c++17    → use the C++17 language rules
#    -Wall -Wextra → turn on extra warnings (the compiler becomes my coach)
#    -o app        → name the finished program "app"
g++ -std=c++17 -Wall -Wextra main.cpp -o app

# 3. Run it
./app            # on Windows: app.exe
```

**Examples with more than one `.cpp` file:**
```bash
# List EVERY .cpp file in the compile command
g++ -std=c++17 -Wall -Wextra main.cpp helper.cpp -o app
```

**Tip:** if something doesn't compile, read only the **first** error, fix it, then recompile. Later errors are often side effects. 🧯

---

## 📝 Template: README for Each Example

Copy this into each new example folder and fill it in:

````markdown
# 🧪 Example Name

![Language](https://img.shields.io/badge/language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Status](https://img.shields.io/badge/status-working-green?style=for-the-badge)

> One playful line about what this program does.

## 🎯 What It Does
A short plain-English description.

## 🧠 Concepts Practiced
| Concept | Where I Learned It |
|---|---|
| e.g. `std::vector` | [arrays-and-strings.md](../../arrays-and-strings.md) |

## ▶️ How to Run
```bash
g++ -std=c++17 -Wall -Wextra main.cpp -o app
./app
```

## 📺 Sample Output
```
paste a real run here
```

## 🐛 What Broke (and How I Fixed It)
- Honest list of bugs I hit.

## 💡 What I Learned
- One or two takeaways.

## 🚀 Next Iteration (Mark II Ideas)
- [ ] Something I could add later.

[⬅️ Back to Examples](../README.md)
````

---

## ✅ My Checklist Before Adding an Example

- [ ] It compiles with **no warnings** under `-Wall -Wextra`
- [ ] Every important line has a comment explaining *why* (future me will thank me)
- [ ] I tested it with bad input (empty, zero, negative, huge)
- [ ] The README has a sample output and a "what broke" section
- [ ] The example is added to the index table above
- [ ] The mistakes I made went into [`things-i-broke.md`](../../notes/things-i-broke.md)

---

## 🤝 For Visitors

- **Fellow learners:** feel free to compile, tweak, and break these. That's how I learn too. If you spot a bug or a better way, tell me!
- **Future me:** look how far the suit has come. 🦾
- **Employers:** these are unpolished, honest learning projects. The git history shows the real process, mistakes included.

---

<p align="center">
  ⬅️ <a href="../README.md">C++ Home</a> · 🔙 <a href="../../README.md">Learning-Archive</a> · Built by <a href="https://github.com/Fadlelmula">Fadlelmula</a> ⚙️
</p>
