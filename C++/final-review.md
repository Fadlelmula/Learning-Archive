# 🏁 C++ Final Review — Mark I Systems Check

![Topic](https://img.shields.io/badge/topic-final%20review-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Use](https://img.shields.io/badge/use-self--check-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Before Tony flies the suit, he runs diagnostics. 🛫
> This file recaps everything in the C++ folder and tests whether I *really* understood it, not just read it.

---

## 🗺️ The Whole Journey in One Table

| 🚀 Mark | 📄 File | 🧠 The One-Sentence Version |
|---|---|---|
| **I** | [`basics.md`](./basics.md) | Programs start in `main()`; variables are typed boxes; `cin`/`cout` talk to the user |
| **I** | [`control-flow.md`](./control-flow.md) | `if`/`switch` decide, `for`/`while` repeat |
| **I** | [`functions.md`](./functions.md) | Reusable named blocks; `&` passes the real thing, not a copy |
| **II** | [`arrays-and-strings.md`](./arrays-and-strings.md) | `std::vector` and `std::string` are my default containers |
| **III** | [`pointers-and-memory.md`](./pointers-and-memory.md) | Pointers store addresses; prefer smart pointers over `new`/`delete` |
| **IV** | [`oop.md`](./oop.md) | Classes bundle data + behavior; `virtual` enables polymorphism |
| **V** | [`stl.md`](./stl.md) | Ready-made containers and algorithms; don't reinvent the wheel |
| **V** | [`file-io.md`](./file-io.md) | Files behave like `cin`/`cout` through `ifstream`/`ofstream` |
| 📋 | [`cheat-sheet.md`](./cheat-sheet.md) | Fast lookup for syntax |

---

## 🧠 Key Ideas to Never Forget

### 1. Types and values
- C++ is **statically typed**: every variable has a type fixed at compile time.
- `int / int` stays an `int`. Convert at least one side to `double` for decimals.
- `=` assigns, `==` compares.

### 2. Memory is real
- Every variable has an **address**. A pointer stores one.
- **Stack** = automatic and fast. **Heap** = manual (or smart pointer managed).
- Every `new` needs a `delete`, or just use `std::unique_ptr` / `std::vector`.

### 3. Copies are expensive, references are cheap
- By default, passing to a function **copies**.
- Use `const T&` to read big things without copying, `T&` to modify the original.

### 4. Let the library do the work
- Use `std::vector` instead of raw arrays.
- Use `std::string` instead of `char[]`.
- Use `<algorithm>` (`sort`, `find`, `count`) instead of hand-written loops where possible.

### 5. Classes protect their data
- `private` data + `public` methods = an object that can't easily be put into a bad state.
- Base classes get a **virtual destructor**.
- Overriding methods get the `override` keyword so the compiler checks my work.

---

## ✅ Self-Check Quiz

Try to answer **without looking**, then check the answers below.

### Section A: Basics
1. What does `7 / 2` evaluate to when both are `int`?
2. Why does `std::cin >> name` fail to read "Tony Stark" fully, and what reads the whole line?
3. What's the difference between `'a'` and `"a"`?

### Section B: Control flow
4. What happens in a `switch` if you forget `break`?
5. Which loop is guaranteed to run at least once?
6. What does `continue` do compared with `break`?

### Section C: Functions
7. What's the difference between a *parameter* and an *argument*?
8. What does `void f(int& x)` allow that `void f(int x)` doesn't?
9. Why does every recursive function need a base case?

### Section D: Arrays and strings
10. What is the index of the last element in a vector of size `n`?
11. What's the difference between `v[i]` and `v.at(i)`?
12. What does `find()` return on a `std::string` when the text isn't found?

### Section E: Pointers
13. In `int* p = &x;`, what is stored in `p`?
14. What does `*p` mean in an expression?
15. Name two bugs that come from manual `new` / `delete`.
16. Why is `std::unique_ptr` usually better than `new`?

### Section F: OOP
17. What's the difference between a class and an object?
18. What does `override` do?
19. Why must a base class have a `virtual` destructor?

### Section G: STL and files
20. What's the difference between `map` and `unordered_map`?
21. What does `std::sort(v.begin(), v.end())` need as its first two arguments?
22. What happens to a file's old content when you open it with `std::ofstream`?
23. Why is `while (!file.eof())` a bad loop condition?

---

## 🔑 Answers

<details>
<summary>👀 Click to reveal (try first!)</summary>

1. `3`. Integer division chops the decimal.
2. `cin >>` stops at whitespace. Use `std::getline(std::cin, name)`.
3. `'a'` is a single `char`; `"a"` is a string (text).
4. Execution **falls through** into the next case.
5. `do...while`.
6. `continue` skips to the next round; `break` exits the loop entirely.
7. Parameter = variable in the function definition; argument = the actual value passed in.
8. It lets the function modify the caller's original variable (no copy).
9. Without it, the function calls itself forever → stack overflow.
10. `n - 1`.
11. `at(i)` checks bounds and throws an error; `[]` doesn't check (undefined behavior).
12. `std::string::npos`.
13. The **address** of `x`.
14. "Follow the pointer and use the value stored at that address" (dereference).
15. Any two of: memory leak, dangling pointer, double delete, wrong delete form, null dereference.
16. It frees memory automatically when it goes out of scope, so there's nothing to forget.
17. A class is the blueprint; an object is a real instance built from it.
18. It tells the compiler "this replaces a parent's virtual function", and errors if nothing matches.
19. So deleting a child object through a base pointer runs the child's destructor too (otherwise → leaks / undefined behavior).
20. `map` keeps keys sorted; `unordered_map` has no order but is generally faster for lookups.
21. Iterators marking the range: `begin()` and `end()`.
22. It's erased, unless you open with `std::ios::app`.
23. `eof()` only becomes true *after* a failed read, so the loop runs one extra time. Use `while (std::getline(...))` or `while (in >> x)`.

</details>

**My score:** ___ / 23  📊
**Sections I need to revisit:** ______________________

---

## 🏆 Capstone Project Ideas

Pick one and build it using as many topic files as possible:

| 🧪 Project | 🛠️ Uses |
|---|---|
| **Number guessing game** | Control flow, functions, random numbers |
| **Contact book** | Classes, `vector`, `map`, file I/O |
| **Text adventure** | Classes, inheritance, `switch`, `map` |
| **Bank account system** | OOP, encapsulation, file saving |
| **Student grade tracker** | Vectors, algorithms, file I/O |
| **Tic-tac-toe** | 2D arrays/vectors, functions, loops |
| **Mini J.A.R.V.I.S. (text commands)** | Strings, `map` of commands, polymorphism |

Each finished project becomes a folder in [`examples/`](./examples/) with its own README. 📁

---

## 🐛 Backlog: Gremlins Still Alive

Honest list. Move items to [`../notes/things-i-finally-understood.md`](../notes/things-i-finally-understood.md) when defeated. 🏆

- [ ] Pointers vs references: choosing confidently
- [ ] Reading long template error messages
- [ ] Header files and multi-file projects
- [ ] Error handling with `try` / `catch`
- [ ] Templates
- [ ] Move semantics (a future boss fight)

---

## 🚀 What's Next (Mark VI and Beyond)

| 🎯 Goal | 📚 Topic |
|---|---|
| Write safer code | Exceptions, `std::optional`, RAII habits |
| Organize big projects | Headers, namespaces, CMake |
| Write generic code | Templates |
| Go faster | Move semantics, profiling, algorithms and complexity |
| Build something visual | SFML or SDL for 2D games |

> From the first `Hello, world` to Mark 85, one iteration at a time. 🦾

---

<p align="center">
  ⬅️ <a href="./cheat-sheet.md">Cheat Sheet</a> · 🏠 <a href="./README.md">C++ Home</a> · 🔙 <a href="../README.md">Learning-Archive</a>
</p>
