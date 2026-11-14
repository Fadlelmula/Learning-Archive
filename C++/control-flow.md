# 🔀 Control Flow — Teaching the Suit to Decide

![Topic](https://img.shields.io/badge/topic-control%20flow-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20I-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> A suit that can't make decisions is just expensive armor. 🛡️
> Control flow is how a program chooses *what to do* and *how many times to do it*.

---

## 🗺️ Overview

| 🧩 Tool | 🎯 Use It When |
|---|---|
| `if / else if / else` | Choosing between a few conditions |
| `switch` | Matching one value against many exact options |
| ternary `?:` | A tiny if/else that returns a value |
| `for` | You know how many times to repeat |
| `while` | Repeat until something changes |
| `do...while` | Run at least once, then check |
| `break` / `continue` | Escape or skip inside a loop |

---

## 1️⃣ `if`, `else if`, `else`

```cpp
#include <iostream>

int main() {
    int score = 85;   // pretend this came from a test

    if (score >= 90) {                 // checked first. If true, the rest is SKIPPED
        std::cout << "Grade: A" << std::endl;
    } else if (score >= 80) {          // only checked if the first one was false
        std::cout << "Grade: B" << std::endl;
    } else if (score >= 70) {
        std::cout << "Grade: C" << std::endl;
    } else {                           // runs when NOTHING above was true
        std::cout << "Keep going, Mark I 💪" << std::endl;
    }
    return 0;
}
```

**How it works:** C++ reads top to bottom and runs the *first* block whose condition is true, then jumps past the rest. So order matters. Putting `score >= 70` first would make an 85 print "C".

### Combining conditions
```cpp
int age = 20;
bool hasTicket = true;

if (age >= 18 && hasTicket) {   // && = AND: BOTH must be true
    // enter
}
if (age < 13 || age > 65) {     // || = OR: at least ONE must be true
    // discount
}
if (!hasTicket) {               // !  = NOT: flips true/false
    // go buy one
}
```

---

## 2️⃣ `switch`

Best when comparing **one variable** to **specific values**.

```cpp
#include <iostream>

int main() {
    int day = 3;   // 1 = Monday ... 7 = Sunday

    switch (day) {                 // look at the value of "day"
        case 1:                    // if day == 1, start running here
            std::cout << "Monday" << std::endl;
            break;                 // break = STOP and leave the switch
        case 2:
            std::cout << "Tuesday" << std::endl;
            break;
        case 3:
            std::cout << "Wednesday" << std::endl;
            break;
        default:                   // like "else": runs if no case matched
            std::cout << "Some other day" << std::endl;
            break;
    }
    return 0;
}
```

> 🐛 **Gremlin: fall-through.** Forget a `break` and C++ keeps running into the *next* case. Sometimes useful, usually a bug.
> `switch` works with integers and characters, **not** strings.

---

## 3️⃣ The Ternary Operator

```cpp
int age = 17;
// Format: condition ? value_if_true : value_if_false
std::string status = (age >= 18) ? "adult" : "minor";
```
Great for tiny choices. If it gets hard to read, use a normal `if`.

---

## 4️⃣ `for` Loop

```cpp
#include <iostream>

int main() {
    // for (start; keep-going-while; after-each-round)
    for (int i = 1; i <= 5; i++) {
        // int i = 1  → runs ONCE at the start: make a counter
        // i <= 5     → checked BEFORE every round: if false, the loop ends
        // i++        → runs AFTER every round: add 1 to the counter
        std::cout << "Round " << i << std::endl;
    }
    return 0;
}
```

### Range-based `for` (a nicer way to walk a collection)
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {10, 20, 30};   // a list of numbers

    for (int n : nums) {                    // read as: "for each n in nums"
        std::cout << n << std::endl;        // n is a COPY of each element
    }
    return 0;
}
```

---

## 5️⃣ `while` and `do...while`

```cpp
#include <iostream>

int main() {
    int fuel = 3;

    while (fuel > 0) {                      // check FIRST, then run
        std::cout << "Fuel left: " << fuel << std::endl;
        fuel--;                             // IMPORTANT: change something, or it loops forever
    }

    int tries = 0;
    do {                                    // run FIRST, then check
        std::cout << "Attempt " << tries + 1 << std::endl;
        tries++;
    } while (tries < 2);                    // note the semicolon after the condition

    return 0;
}
```

| 🔁 Loop | 🕵️ Checks Condition | 🏃 Runs At Least Once? |
|---|---|---|
| `while` | Before each round | No |
| `do...while` | After each round | **Yes** |

---

## 6️⃣ `break` and `continue`

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 3) {
            continue;   // SKIP the rest of this round, jump to the next i
        }
        if (i == 6) {
            break;      // STOP the whole loop right now
        }
        std::cout << i << " ";   // prints: 1 2 4 5
    }
    std::cout << std::endl;
    return 0;
}
```

---

## 7️⃣ Nested Loops (a multiplication table)

```cpp
#include <iostream>

int main() {
    for (int row = 1; row <= 3; row++) {          // OUTER loop: picks the row
        for (int col = 1; col <= 3; col++) {      // INNER loop: runs fully for EACH row
            std::cout << row * col << "\t";       // \t = a tab, to line up columns
        }
        std::cout << std::endl;                   // new line after each row
    }
    return 0;
}
```

---

## 🧪 Mini Challenges

1. FizzBuzz: print 1 to 30; multiples of 3 → `Fizz`, of 5 → `Buzz`, of both → `FizzBuzz`.
2. Number guessing game with `while` (use a fixed secret number first, random later).
3. Print a right triangle of `*` using nested loops.

---

## 🐛 Gremlins to Remember

- [ ] Forgetting `break` in `switch`
- [ ] Infinite loops (forgetting to change the loop variable)
- [ ] Off-by-one: `<` vs `<=`
- [ ] A stray `;` after `if (...)` or `for (...)` makes the block run unconditionally

---

<p align="center">
  ⬅️ <a href="./basics.md">Basics</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./functions.md">Next: Functions</a>
</p>
