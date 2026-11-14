# 🧩 Functions — Building Reusable Suit Parts

![Topic](https://img.shields.io/badge/topic-functions-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20I-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Tony doesn't rebuild the repulsor from scratch every time. He builds it once and bolts it on. 🔧
> That's a function: **write once, use anywhere.**

---

## 🗺️ Overview

| 🧩 Idea | 💬 Meaning |
|---|---|
| Function | A named block of code that does one job |
| Parameter | An input the function receives |
| Return value | The output the function hands back |
| `void` | "I return nothing" |
| Overloading | Same name, different parameters |
| Pass by value / reference | Copy of the data vs the real thing |
| Default arguments | A parameter that fills itself in if skipped |

---

## 1️⃣ Anatomy of a Function

```cpp
#include <iostream>

// returnType  name   (parameters)
int add(int a, int b) {   // takes two ints, gives back one int
    return a + b;         // "return" sends the result back and ENDS the function
}

int main() {
    int result = add(3, 4);   // CALL the function: 3 and 4 are the "arguments"
    std::cout << result << std::endl;   // prints 7
    return 0;
}
```

**Vocabulary that trips me up:**
- **Parameter** = the variable in the definition (`a`, `b`).
- **Argument** = the actual value you pass in (`3`, `4`).

---

## 2️⃣ `void` Functions

```cpp
#include <iostream>
#include <string>

// void = this function does something but returns NO value
void greet(const std::string& name) {
    std::cout << "Hello, " << name << "! 👋" << std::endl;
}

int main() {
    greet("Fadlelmula");   // no variable needed to catch a result
    return 0;
}
```

---

## 3️⃣ Declaration vs Definition (Prototypes)

C++ reads top to bottom. A function must be **known** before it is used.

```cpp
#include <iostream>

int square(int x);   // DECLARATION (prototype): "this function exists, details later"

int main() {
    std::cout << square(5) << std::endl;   // OK because the compiler has seen the prototype
    return 0;
}

int square(int x) {  // DEFINITION: the real body
    return x * x;
}
```

> In bigger projects, prototypes go into **header files** (`.h`) and bodies into `.cpp` files. 🔜 Later Mark.

---

## 4️⃣ Pass by Value vs Pass by Reference

This is where C++ differs from many languages. 🧠

```cpp
#include <iostream>

// BY VALUE: the function gets a COPY. The original is untouched.
void addOneCopy(int x) {
    x = x + 1;   // changes only the local copy
}

// BY REFERENCE: & means "give me the REAL variable, not a copy"
void addOneReal(int& x) {
    x = x + 1;   // changes the original
}

int main() {
    int n = 5;

    addOneCopy(n);
    std::cout << n << std::endl;   // still 5

    addOneReal(n);
    std::cout << n << std::endl;   // now 6

    return 0;
}
```

| 📦 Style | ✍️ Syntax | 🔄 Changes Original? | 🏎️ Cost |
|---|---|---|---|
| By value | `int x` | No | Copies the data |
| By reference | `int& x` | **Yes** | No copy |
| By const reference | `const int& x` | No (read-only) | No copy ✅ |

**Rule of thumb I'm using:**
- Small things (`int`, `double`, `char`, `bool`) → by value.
- Big things (`std::string`, `std::vector`) you only *read* → `const T&`.
- Want the function to *modify* the original → `T&`.

---

## 5️⃣ Default Arguments

```cpp
#include <iostream>
#include <string>

// If the caller skips "punctuation", it becomes "!"
// Default values must be at the END of the parameter list
void shout(const std::string& text, const std::string& punctuation = "!") {
    std::cout << text << punctuation << std::endl;
}

int main() {
    shout("Mark I online");        // uses the default → "Mark I online!"
    shout("Are you sure", "?");    // overrides it    → "Are you sure?"
    return 0;
}
```

---

## 6️⃣ Function Overloading

Same name, **different parameter lists**. The compiler picks the right one.

```cpp
#include <iostream>

int multiply(int a, int b) {              // version for ints
    return a * b;
}

double multiply(double a, double b) {     // version for doubles
    return a * b;
}

int multiply(int a, int b, int c) {       // version with three arguments
    return a * b * c;
}

int main() {
    std::cout << multiply(2, 3) << std::endl;        // calls the int version → 6
    std::cout << multiply(2.5, 2.0) << std::endl;    // calls the double version → 5
    std::cout << multiply(2, 3, 4) << std::endl;     // calls the 3-arg version → 24
    return 0;
}
```

> ⚠️ You **cannot** overload by return type alone. The parameters must differ.

---

## 7️⃣ Scope: Where Variables Live

```cpp
#include <iostream>

int globalCount = 0;   // GLOBAL: visible everywhere (use sparingly!)

void demo() {
    int local = 10;    // LOCAL: exists only inside demo(), dies when it ends
    globalCount++;
}

int main() {
    demo();
    // std::cout << local;   // ❌ error: "local" doesn't exist out here
    std::cout << globalCount << std::endl;   // ✅ prints 1
    return 0;
}
```

---

## 8️⃣ Recursion (a function calling itself)

```cpp
#include <iostream>

// factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
int factorial(int n) {
    if (n <= 1) {                 // BASE CASE: the stopping point (never forget this!)
        return 1;
    }
    return n * factorial(n - 1);  // RECURSIVE CASE: a smaller version of the same problem
}

int main() {
    std::cout << factorial(5) << std::endl;   // 120
    return 0;
}
```

Without a base case → infinite calls → **stack overflow** 💥

---

## 🧪 Mini Challenges

1. Write `isEven(int n)` returning `bool`.
2. Write `swapValues(int& a, int& b)` that swaps two numbers (reference practice!).
3. Overload `area(...)` for a square (1 arg) and a rectangle (2 args).
4. Write a recursive `sumTo(n)` that adds 1 + 2 + ... + n.

---

## 🐛 Gremlins to Remember

- [ ] Forgetting `&` and wondering why the original didn't change
- [ ] Missing base case in recursion
- [ ] Using a function before declaring it
- [ ] Non-`void` function that forgets to `return` on some path

---

<p align="center">
  ⬅️ <a href="./control-flow.md">Control Flow</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./arrays-and-strings.md">Next: Arrays & Strings</a>
</p>
