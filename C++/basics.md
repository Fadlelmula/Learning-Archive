# 🧱 C++ Basics — Mark I Boots Up

![Topic](https://img.shields.io/badge/topic-basics-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20I-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Every suit starts as a pile of scrap in a cave. This file is my pile of scrap. 🔩

---

## 🎯 What I'm Learning Here

| 🧠 Topic | 💬 In Plain Words |
|---|---|
| Program structure | What every C++ program must contain |
| Variables | Named boxes that hold data |
| Data types | What *kind* of data a box holds |
| Input / Output | Talking to the user with `cin` and `cout` |
| Operators | Math, comparison, and logic symbols |
| Constants and `auto` | Values that never change, and letting the compiler guess the type |

---

## 1️⃣ Anatomy of a C++ Program

```cpp
// A line starting with // is a comment. The compiler ignores it.
// Comments are notes for humans (including future me).

#include <iostream>   // #include pastes in a library. <iostream> gives us cin and cout.

int main() {          // main() is the starting point. The OS calls it when the program runs.
                      // "int" means main hands back an integer when it finishes.

    std::cout << "Mark I online 🤖" << std::endl;
    // std::     = the "standard" namespace (a labeled drawer where cout lives)
    // cout      = "console output", the screen
    // <<        = the "stream insertion" operator: pushes data INTO the stream
    // std::endl = ends the line and flushes the output

    return 0;     // 0 = "all good". Any other number usually means an error.
}
```

**Compile and run:**

```bash
# -std=c++17  : use the C++17 language rules
# -Wall -Wextra : show extra warnings (my compiler coach)
# -o app      : name the finished program "app"
g++ -std=c++17 -Wall -Wextra main.cpp -o app
./app
```

### 🧐 Why `std::`?
C++ keeps its built-in names inside a namespace called `std`. Writing `std::cout` means "the `cout` from the `std` drawer."
You can write `using namespace std;` to skip the prefix, but in bigger projects that causes name clashes, so I'm practicing the explicit way.

---

## 2️⃣ Variables

A variable is a **named box in memory**. You pick the type, the name, and (ideally) the starting value.

```cpp
#include <iostream>

int main() {
    int age = 25;              // int    : whole numbers (no decimals)
    double price = 19.99;      // double : numbers with decimals (more precise than float)
    char grade = 'A';          // char   : ONE character, in SINGLE quotes
    bool isLearning = true;    // bool   : true or false only

    std::cout << "Age: " << age << std::endl;        // print the int
    std::cout << "Price: " << price << std::endl;    // print the double
    std::cout << "Grade: " << grade << std::endl;    // print the char
    std::cout << "Learning? " << isLearning << std::endl;  // prints 1 (true) or 0 (false)

    age = 26;   // variables can change. "=" means ASSIGN, not "equals".
    std::cout << "Next year: " << age << std::endl;

    return 0;
}
```

### 📏 Naming rules
| ✅ Allowed | ❌ Not allowed |
|---|---|
| Letters, digits, underscores | Spaces or symbols like `-`, `!` |
| Starting with a letter or `_` | Starting with a digit (`2fast`) |
| `camelCase` or `snake_case` | Reserved words (`int`, `return`, `class`...) |

C++ is **case-sensitive**: `Age` and `age` are two different variables.

---

## 3️⃣ Data Types Cheat Table

| 🏷️ Type | 📦 Holds | 🧪 Example | 📐 Typical Size |
|---|---|---|---|
| `int` | Whole numbers | `42` | 4 bytes |
| `long long` | Very big whole numbers | `9000000000LL` | 8 bytes |
| `float` | Decimals (less precise) | `3.14f` | 4 bytes |
| `double` | Decimals (more precise) | `3.14159` | 8 bytes |
| `char` | One character | `'x'` | 1 byte |
| `bool` | `true` / `false` | `true` | 1 byte |
| `std::string` | Text | `"hello"` | varies |

> ⚠️ Sizes depend on the machine and compiler. Use `sizeof(type)` to check yours.

```cpp
#include <iostream>

int main() {
    // sizeof(x) tells us how many bytes a type or variable uses
    std::cout << "int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "double: " << sizeof(double) << " bytes" << std::endl;
    std::cout << "char: " << sizeof(char) << " byte" << std::endl;
    return 0;
}
```

### 💥 Gremlin: integer division
```cpp
int a = 7 / 2;        // both are ints, so the result is 3 (decimals are CHOPPED OFF)
double b = 7 / 2;     // still 3! The division happens in int BEFORE it is stored
double c = 7.0 / 2;   // 3.5 ✅ one side is a double, so the math is done in double
```

---

## 4️⃣ Input and Output

```cpp
#include <iostream>
#include <string>      // needed for std::string

int main() {
    std::string name;  // an empty text box
    int age;           // a number box (no starting value yet)

    std::cout << "What's your name? ";
    std::cin >> name;  // cin = "console input". >> pulls data OUT of the stream into the variable.
                       // WARNING: cin >> stops reading at the first space.

    std::cout << "How old are you? ";
    std::cin >> age;

    std::cout << "Hello, " << name << "! Next year you'll be " << age + 1 << "." << std::endl;
    return 0;
}
```

### Reading a whole line (with spaces)
```cpp
#include <iostream>
#include <string>

int main() {
    std::string fullName;
    std::cout << "Full name: ";
    std::getline(std::cin, fullName);   // reads everything until Enter, spaces included
    std::cout << "Welcome, " << fullName << "!" << std::endl;
    return 0;
}
```

> 🐛 **Classic bug:** mixing `cin >> number` and then `getline(...)` skips the line, because `cin >>` leaves the Enter key (`\n`) in the buffer. Fix: call `std::cin.ignore();` after `cin >>` and before `getline`.

---

## 5️⃣ Operators

| ➕ Type | 🔣 Operators | 🧪 Example |
|---|---|---|
| Arithmetic | `+ - * / %` | `10 % 3` → `1` (remainder) |
| Assignment | `= += -= *= /=` | `x += 5;` same as `x = x + 5;` |
| Increment | `++ --` | `i++;` adds 1 |
| Comparison | `== != < > <= >=` | `age >= 18` |
| Logical | `&& \|\| !` | `a > 0 && b > 0` (AND), `\|\|` (OR), `!` (NOT) |

> ⚠️ `=` assigns, `==` compares. Writing `if (x = 5)` is a famous bug: it assigns 5 and is always true.

---

## 6️⃣ Constants and `auto`

```cpp
#include <iostream>

int main() {
    const double PI = 3.14159;   // const = this value can NEVER change after this line
    // PI = 3;                   // ❌ compiler error. That's the point: it protects me.

    auto count = 10;             // auto = "compiler, figure out the type": here, int
    auto ratio = 2.5;            // here, double

    std::cout << PI << " " << count << " " << ratio << std::endl;
    return 0;
}
```

---

## 🧪 Mini Challenges

1. Ask for two numbers and print their sum, difference, product, and quotient (use `double`!).
2. Ask for a temperature in Celsius and print Fahrenheit (`F = C * 9 / 5 + 32`, watch the integer division trap).
3. Print the `sizeof` of five different types and compare with a friend's machine.

---

## 🐛 Gremlins to Remember

- [ ] `=` vs `==`
- [ ] Integer division chops decimals
- [ ] `cin >>` stops at spaces
- [ ] Uninitialized variables hold garbage values

---

<p align="center">
  ⬅️ <a href="./README.md">C++ Home</a> · ➡️ <a href="./control-flow.md">Next: Control Flow</a>
</p>
