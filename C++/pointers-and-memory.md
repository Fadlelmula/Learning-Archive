# 👹 Pointers & Memory — The Boss Fight

![Topic](https://img.shields.io/badge/topic-pointers%20%26%20memory-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20III-red?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/difficulty-boss%20fight-black?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> This is the part of C++ that scares everyone.
> It's also the part that makes C++ *C++*. If I beat this, I understand how computers actually work. 🧠💥

---

## 🗺️ Overview

| 🧩 Idea | 💬 In Plain Words |
|---|---|
| Memory address | Every variable lives at a numbered spot in memory |
| Pointer | A variable that stores **an address** |
| `&` (address-of) | "Where does this variable live?" |
| `*` (dereference) | "Go to that address and give me the value" |
| Reference | A permanent nickname for an existing variable |
| Stack vs heap | Automatic memory vs memory I manage |
| `new` / `delete` | Ask for / give back heap memory |
| Smart pointers | Pointers that clean up after themselves ✅ |

---

## 1️⃣ The Mental Model 🏠

Think of memory as a **street of houses**, each with an address.

- A **variable** is a house with something inside.
- A **pointer** is a *piece of paper with a house address written on it*.
- To see what's inside the house, you **follow the address**. That's dereferencing.

```
 variable  x          pointer  p
┌────────┐          ┌──────────────┐
│   42   │ ◄──────── │ address of x │
└────────┘          └──────────────┘
 at 0x1000            at 0x2000
```

---

## 2️⃣ Pointer Basics

```cpp
#include <iostream>

int main() {
    int x = 42;          // a normal int variable

    int* p = &x;         // int*  = "pointer to an int"
                         // &x    = "the address of x"
                         // so p now STORES the address of x

    std::cout << x << std::endl;    // 42       → the value
    std::cout << &x << std::endl;   // 0x7ffe...→ the address of x (will differ every run)
    std::cout << p << std::endl;    // same address as &x, because p holds it
    std::cout << *p << std::endl;   // 42       → * follows the address and reads the value

    *p = 100;                       // follow the address and CHANGE the value there
    std::cout << x << std::endl;    // 100!  x changed because p points at x

    return 0;
}
```

### 🔑 The two meanings of `*` (this confuses everyone)

| 📍 Where | ✍️ Example | 💬 Meaning |
|---|---|---|
| In a **declaration** | `int* p;` | "p is a pointer to an int" |
| In an **expression** | `*p = 5;` | "follow p and use the value there" |

And `&` also has two meanings: in a declaration (`int& r`) it means *reference*; in an expression (`&x`) it means *address-of*.

---

## 3️⃣ `nullptr` — The Pointer to Nothing

```cpp
int* p = nullptr;      // "I point at nothing yet" (always initialize pointers!)

if (p != nullptr) {    // ALWAYS check before dereferencing
    std::cout << *p << std::endl;
}
// *p when p is nullptr → crash (segmentation fault) 💥
```

> Use `nullptr`, not `NULL` or `0`. It's the modern, type-safe way.

---

## 4️⃣ References

A reference is **another name for an existing variable**.

```cpp
#include <iostream>

int main() {
    int x = 10;
    int& ref = x;      // ref IS x (same box, two names). Must be initialized right away.

    ref = 20;          // changes x
    std::cout << x << std::endl;   // 20

    return 0;
}
```

### Pointer vs Reference

| ⚔️ Feature | 📍 Pointer | 🔗 Reference |
|---|---|---|
| Can be `nullptr` | Yes | No |
| Can be re-pointed later | Yes | No (bound for life) |
| Must be initialized | Not required (but should be) | **Yes** |
| Syntax to use value | `*p` | just `ref` |
| Typical use | Optional things, dynamic memory | Function parameters |

**My current rule:** use a reference when I can, a pointer when I must.

---

## 5️⃣ Pointers and Arrays

```cpp
#include <iostream>

int main() {
    int nums[3] = {10, 20, 30};

    int* p = nums;            // an array name "decays" into a pointer to its first element

    std::cout << *p << std::endl;        // 10
    std::cout << *(p + 1) << std::endl;  // 20 → p + 1 moves ONE int forward (not one byte)
    std::cout << *(p + 2) << std::endl;  // 30

    std::cout << p[1] << std::endl;      // 20 → p[1] is just shorthand for *(p + 1)
    return 0;
}
```

This is **pointer arithmetic**: adding 1 to an `int*` moves by `sizeof(int)` bytes automatically. It's also why `array[i]` works the way it does under the hood.

---

## 6️⃣ Pointers in Functions

```cpp
#include <iostream>

// Takes a POINTER, so we can change the caller's variable
void doubleIt(int* p) {
    if (p == nullptr) return;   // safety check first
    *p = *p * 2;                // follow the pointer and double the value
}

int main() {
    int n = 8;
    doubleIt(&n);               // pass the ADDRESS of n
    std::cout << n << std::endl;   // 16
    return 0;
}
```

---

## 7️⃣ Stack vs Heap 🥞

| 🥞 Stack | 🏔️ Heap |
|---|---|
| Automatic: created and destroyed with the scope | Manual: I create it, I must destroy it |
| Very fast | Slower |
| Small, fixed limit | Large, flexible |
| Normal variables: `int x = 5;` | Made with `new` (or smart pointers) |
| Freed when the function ends | Lives until freed |

---

## 8️⃣ `new` and `delete` (Manual Heap Memory)

```cpp
#include <iostream>

int main() {
    int* p = new int(5);       // new: ask the heap for space for ONE int, set it to 5
                               // it returns the ADDRESS, which we keep in p

    std::cout << *p << std::endl;   // 5

    delete p;                  // give the memory back (REQUIRED, or we "leak" it)
    p = nullptr;               // good habit: don't leave a "dangling" pointer around

    // Arrays use new[] and delete[]
    int* arr = new int[3]{1, 2, 3};   // heap array of 3 ints
    std::cout << arr[2] << std::endl; // 3
    delete[] arr;                     // MUST use delete[] (not delete) for new[]
    arr = nullptr;

    return 0;
}
```

### 💀 The Classic Memory Bugs

| 🐞 Bug | 💬 What Happens |
|---|---|
| **Memory leak** | `new` without `delete`: memory is lost until the program ends |
| **Dangling pointer** | Using a pointer after `delete`: undefined behavior |
| **Double delete** | `delete`-ing the same pointer twice: crash |
| **Wrong delete** | `delete` on `new[]` (or vice versa) |
| **Null dereference** | Using `*p` when `p` is `nullptr`: crash |

---

## 9️⃣ Smart Pointers (The Modern Way ✅)

Manual `new`/`delete` is error-prone. Modern C++ uses **smart pointers** that free memory automatically.

```cpp
#include <iostream>
#include <memory>   // needed for smart pointers

int main() {
    // unique_ptr: ONE owner. Memory is freed automatically when it goes out of scope.
    std::unique_ptr<int> a = std::make_unique<int>(10);
    std::cout << *a << std::endl;   // use it like a normal pointer → 10

    // shared_ptr: MANY owners. Freed when the LAST owner is gone.
    std::shared_ptr<int> b = std::make_shared<int>(20);
    std::shared_ptr<int> c = b;     // b and c share ownership
    std::cout << b.use_count() << std::endl;   // 2 owners

    return 0;   // no delete needed. Everything is cleaned up automatically 🎉
}
```

| 🧠 Type | 👥 Owners | 🎯 Use When |
|---|---|---|
| `unique_ptr` | Exactly 1 | Default choice ⭐ |
| `shared_ptr` | Many | Truly shared ownership |
| raw pointer `T*` | None (just observes) | Looking at something someone else owns |

> This idea is called **RAII**: resources are tied to an object's lifetime, so cleanup happens automatically.

---

## 🔟 Returning Things Safely

```cpp
// ❌ BAD: returns the address of a local variable that dies when the function ends
int* broken() {
    int x = 5;
    return &x;      // x is destroyed after this line → dangling pointer 💀
}

// ✅ GOOD: return by value (simple things are cheap to copy)
int fine() {
    int x = 5;
    return x;
}
```

---

## 🧪 Mini Challenges

1. Write `swap(int* a, int* b)` using pointers, then again with references. Compare.
2. Create a heap `int` with `new`, change it, print it, and free it correctly.
3. Rewrite challenge 2 using `std::unique_ptr` and notice how much less you have to remember.
4. Draw (on paper!) the memory boxes for `int x = 5; int* p = &x; int** pp = &p;`.

---

## 🐛 Gremlins to Remember

- [ ] `*` has two meanings (declaration vs dereference)
- [ ] Always initialize pointers (to something valid or `nullptr`)
- [ ] Every `new` needs one `delete` (every `new[]` needs `delete[]`)
- [ ] Never return the address of a local variable
- [ ] Prefer smart pointers and `std::vector` over raw `new`/`delete`

---

<p align="center">
  ⬅️ <a href="./arrays-and-strings.md">Arrays & Strings</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./oop.md">Next: OOP</a>
</p>
