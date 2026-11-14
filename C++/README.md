# ⚙️ C++ — Building Things Close to the Metal

![Language](https://img.shields.io/badge/language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Status](https://img.shields.io/badge/status-Mark%20I%20%7C%20just%20started-red?style=for-the-badge)
![Level](https://img.shields.io/badge/level-rusty%20but%20rebuilding-orange?style=for-the-badge)
![Part Of](https://img.shields.io/badge/part%20of-Learning--Archive-black?style=for-the-badge&logo=github)

> *"Sometimes you gotta run before you can walk."* — Tony Stark
> (Me, staring at my first segmentation fault: **"...I should've walked."** 🚶‍♂️💥)

---

## 👋 Welcome to the Engine Room

Python lets me *talk* to the computer. **C++ lets me hold the wrench.** 🔧

This folder is where I learn C++ in public: how memory really works, why the compiler yells at me, and how to build fast things from the ground up. If the HTML and CSS folders are the **suit's paint job**, this is the **arc reactor**. ⚡

I'm **rusty**, I'm **rebuilding**, and I'm going to **break things**. Every mistake lands in [`../notes/things-i-broke.md`](../notes/things-i-broke.md) because honesty beats pretending. 😅

---

## 🎯 Why C++?

| 🤔 Question | 💡 My Answer |
|---|---|
| Why not just stay in Python? | Python hides the machine. I want to *see* the machine. |
| Why is C++ worth the pain? | Speed, control, and it teaches how computers actually think. |
| What do I want to build with it? | Small tools, games, and simulations. Eventually, things that feel like Tony's workshop. |
| Is it scary? | Yes. That's the point. 🦾 |

---

## 🗺️ Folder Map

```
C++/
├── README.md                  ← you are here 📍
├── basics.md                  ← syntax, variables, types, I/O
├── control-flow.md            ← if, switch, loops
├── functions.md               ← parameters, return values, overloading
├── arrays-and-strings.md      ← arrays, std::vector, std::string
├── pointers-and-memory.md     ← pointers, references, new/delete (the boss fight 👹)
├── oop.md                     ← classes, objects, inheritance, polymorphism
├── stl.md                     ← the Standard Template Library toolbox
├── file-io.md                 ← reading and writing files
├── cheat-sheet.md             ← quick reference for future me
├── final-review.md            ← recap of everything above
└── examples/                  ← small programs I wrote (and broke)
    └── README.md              ← index of all examples
```

> 🌱 This folder will keep growing. New topics get added as I level up.

---

## 📚 What's Inside

| 📄 File | 🧠 What It Covers | 🚦 Status |
|---|---|---|
| `basics.md` | Hello World, variables, data types, `cin` / `cout` | 🔜 Planned |
| `control-flow.md` | Decisions and loops | 🔜 Planned |
| `functions.md` | Breaking code into reusable pieces | 🔜 Planned |
| `arrays-and-strings.md` | Storing and handling collections of data | 🔜 Planned |
| `pointers-and-memory.md` | How memory works, addresses, references | 🔜 Planned |
| `oop.md` | Classes and objects | 🔜 Planned |
| `stl.md` | Vectors, maps, algorithms | 🔜 Planned |
| `file-io.md` | Working with files | 🔜 Planned |
| `cheat-sheet.md` | The "I forgot the syntax again" lifesaver | 🔜 Planned |
| `final-review.md` | Wrap-up and self-check | 🔜 Planned |

**Legend:** ✅ Done · 🚧 In progress · 🔜 Planned

---

## 🛠️ My Setup

| 🧰 Tool | 📝 Notes |
|---|---|
| **Compiler** | `g++` (GCC), or `clang++` |
| **Standard** | C++17 (`-std=c++17`) |
| **Editor** | VS Code |
| **Version control** | Git + GitHub (obviously) |

**Compile and run any example:**

```bash
# Compile main.cpp into a program called "app"
# -std=c++17 : use the C++17 version of the language
# -Wall -Wextra : turn on extra warnings (the compiler becomes my coach)
# -o app : name the output file "app"
g++ -std=c++17 -Wall -Wextra main.cpp -o app

# Run the program
./app
```

---

## 🧪 Example: The Classic First Program

```cpp
// Include the input/output library so we can print to the screen
#include <iostream>

// main() is where every C++ program starts running
int main() {
    // std::cout prints text; std::endl ends the line
    std::cout << "Hello, world! Mark I online. 🤖" << std::endl;

    // Returning 0 tells the operating system "everything went fine"
    return 0;
}
```

More programs live in [`examples/`](./examples/).

---

## 🧭 My Learning Roadmap

| 🚀 Mark | 🎯 Goal |
|---|---|
| **Mark I** | Syntax, variables, control flow, functions |
| **Mark II** | Arrays, strings, vectors |
| **Mark III** | Pointers, references, memory 🧠💥 |
| **Mark IV** | Classes and object-oriented design |
| **Mark V** | STL, file I/O, a real small project |
| **Mark ...85** | Build anything. Iterate forever. 🦾 |

---

## 🐛 Known Gremlins

Honest list of what I don't understand yet (updated as I learn):

- [ ] Pointers vs references: when do I use which?
- [ ] Why does the compiler error message look like a novel?
- [ ] Memory management: `new` / `delete` vs smart pointers

> Gremlins that get defeated move to [`../notes/things-i-finally-understood.md`](../notes/things-i-finally-understood.md) 🏆

---

## 🔗 Resources I'm Using

| 📖 Resource | 💬 Why |
|---|---|
| [learncpp.com](https://www.learncpp.com/) | Free, thorough, beginner friendly |
| [cppreference.com](https://en.cppreference.com/) | The official-ish reference |
| [freeCodeCamp](https://www.freecodecamp.org/) | Practice and structure |

More in [`../notes/useful-resources.md`](../notes/useful-resources.md).

---

## 🤝 For Visitors

- **Fellow learners:** take what helps, and tell me if I got something wrong.
- **Future me:** you did this. Keep going. 💪
- **Employers:** this is my learning process, unpolished and real. Mistakes included.

---

<p align="center">
  🔙 <a href="../README.md">Back to Learning-Archive</a> · Built by <a href="https://github.com/Fadlelmula">Fadlelmula</a> ⚙️
</p>
