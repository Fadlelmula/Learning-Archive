# 🧰 The STL — The Standard Toolbox

![Topic](https://img.shields.io/badge/topic-STL-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20V-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Tony doesn't forge his own screws. He grabs a drawer of ready-made, battle-tested parts. 🔩
> The **Standard Template Library (STL)** is that drawer: containers, algorithms, and iterators that already work.

---

## 🗺️ Overview

The STL has three big pieces that work together:

| 🧩 Piece | 💬 What It Is | 🧪 Examples |
|---|---|---|
| **Containers** | Hold data | `vector`, `map`, `set`, `queue`, `stack` |
| **Iterators** | Point at elements inside a container | `begin()`, `end()` |
| **Algorithms** | Do work on containers | `sort`, `find`, `count`, `reverse` |

---

## 1️⃣ Choosing a Container

| 📦 Container | 🏷️ Header | 🎯 Best For | ⏱️ Notes |
|---|---|---|---|
| `vector` | `<vector>` | Default dynamic list ⭐ | Fast access by index |
| `array` | `<array>` | Fixed-size list | Size known at compile time |
| `deque` | `<deque>` | Add/remove at both ends | |
| `list` | `<list>` | Frequent inserts in the middle | Rarely the best choice |
| `set` | `<set>` | Unique values, kept sorted | No duplicates |
| `unordered_set` | `<unordered_set>` | Unique values, fastest lookup | No order |
| `map` | `<map>` | Key → value, sorted by key | |
| `unordered_map` | `<unordered_map>` | Key → value, fastest lookup | No order |
| `stack` | `<stack>` | Last in, first out | |
| `queue` | `<queue>` | First in, first out | |

> 💡 When unsure: start with `vector` (lists) or `unordered_map` (lookups).

---

## 2️⃣ `std::map` — Key → Value

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> ages;      // keys are strings, values are ints

    ages["Tony"] = 53;                    // insert or overwrite using []
    ages["Pepper"] = 50;
    ages.insert({"Rhodey", 52});          // another way to insert

    std::cout << ages["Tony"] << std::endl;   // 53

    // Check if a key exists BEFORE using it
    if (ages.find("Happy") == ages.end()) {   // end() means "not found"
        std::cout << "Happy not in the map" << std::endl;
    }

    // Loop: each element is a pair (key = first, value = second)
    for (const auto& pair : ages) {
        std::cout << pair.first << " -> " << pair.second << std::endl;
    }                                         // prints in sorted key order

    ages.erase("Pepper");                     // remove by key
    std::cout << ages.size() << std::endl;    // 2
    return 0;
}
```

> ⚠️ **Gremlin:** `ages["Nobody"]` on a missing key **creates** it with value `0`. Use `find()` or `count()` to check first.

---

## 3️⃣ `std::set` — Unique Values

```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> s = {5, 1, 3, 3, 1};   // duplicates are dropped automatically

    s.insert(4);                          // add a value

    for (int n : s) {
        std::cout << n << " ";            // 1 3 4 5 (sorted!)
    }
    std::cout << std::endl;

    std::cout << s.count(3) << std::endl; // 1 if present, 0 if not
    return 0;
}
```

---

## 4️⃣ Stack and Queue

```cpp
#include <iostream>
#include <queue>
#include <stack>

int main() {
    std::stack<int> st;        // LIFO: Last In, First Out (like a stack of plates)
    st.push(1);
    st.push(2);
    st.push(3);
    std::cout << st.top() << std::endl;   // 3 (peek at the top)
    st.pop();                             // removes 3 (pop does NOT return the value)

    std::queue<int> q;         // FIFO: First In, First Out (like a line at a shop)
    q.push(1);
    q.push(2);
    q.push(3);
    std::cout << q.front() << std::endl;  // 1 (the one waiting longest)
    q.pop();                              // removes 1

    return 0;
}
```

---

## 5️⃣ Iterators

An iterator is like a **pointer** to an element of a container.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30};

    // begin() = first element, end() = ONE PAST the last element
    for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
        std::cout << *it << " ";      // * reads the value the iterator points at
    }
    std::cout << std::endl;

    // Same thing, but 'auto' saves typing:
    for (auto it = v.begin(); it != v.end(); ++it) {
        *it += 1;                     // modify through the iterator
    }
    return 0;
}
```
`end()` is **one past** the last element, so never dereference it.

---

## 6️⃣ Algorithms (`<algorithm>`)

```cpp
#include <algorithm>   // sort, find, reverse, count, min_element, max_element...
#include <iostream>
#include <numeric>     // accumulate (sum)
#include <vector>

int main() {
    std::vector<int> v = {5, 2, 9, 1, 7};

    // sort: takes a RANGE (begin to end)
    std::sort(v.begin(), v.end());                       // 1 2 5 7 9
    std::sort(v.begin(), v.end(), std::greater<int>());  // 9 7 5 2 1 (descending)

    std::reverse(v.begin(), v.end());                    // flips the order

    // find: returns an iterator to the match, or end() if missing
    auto it = std::find(v.begin(), v.end(), 7);
    if (it != v.end()) {
        std::cout << "Found 7 at index " << (it - v.begin()) << std::endl;
    }

    // count: how many times a value appears
    std::cout << std::count(v.begin(), v.end(), 2) << std::endl;

    // min / max
    std::cout << *std::min_element(v.begin(), v.end()) << std::endl;  // * because it returns an iterator
    std::cout << *std::max_element(v.begin(), v.end()) << std::endl;

    // sum everything: the 0 is the starting value
    int total = std::accumulate(v.begin(), v.end(), 0);
    std::cout << total << std::endl;   // 24
    return 0;
}
```

---

## 7️⃣ Lambdas (Tiny Throwaway Functions)

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {5, 2, 9, 1, 7};

    // Syntax: [capture](parameters) { body }
    // This lambda says: "a comes before b if a is larger"
    std::sort(v.begin(), v.end(), [](int a, int b) {
        return a > b;
    });

    int limit = 4;
    // [limit] "captures" the outside variable so the lambda can use it
    int bigOnes = std::count_if(v.begin(), v.end(), [limit](int x) {
        return x > limit;
    });
    std::cout << bigOnes << std::endl;   // how many are greater than 4 → 3
    return 0;
}
```

---

## 8️⃣ Mini Project: Word Counter 📝

```cpp
#include <iostream>
#include <map>
#include <sstream>   // istringstream: lets us read a string word by word
#include <string>

int main() {
    std::string text = "the suit the arc the reactor";
    std::map<std::string, int> counts;   // word → how many times

    std::istringstream stream(text);     // treat the string like an input stream
    std::string word;
    while (stream >> word) {             // reads one word at a time until the end
        counts[word]++;                  // missing key starts at 0, then becomes 1, 2, ...
    }

    for (const auto& pair : counts) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    return 0;
}
```
Output:
```
arc: 1
reactor: 1
suit: 1
the: 3
```

---

## 🧪 Mini Challenges

1. Sort a vector of names alphabetically, then by length (use a lambda).
2. Remove duplicates from a vector using `std::set`.
3. Check balanced brackets `({[]})` using `std::stack`.
4. Simulate a print queue using `std::queue`.

---

## 🐛 Gremlins to Remember

- [ ] `map[key]` creates missing keys
- [ ] `end()` is one **past** the last element
- [ ] `stack::pop()` / `queue::pop()` don't return the value (use `top()` / `front()` first)
- [ ] Erasing or inserting while iterating can invalidate iterators
- [ ] Forgetting `#include <algorithm>`

---

<p align="center">
  ⬅️ <a href="./oop.md">OOP</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./file-io.md">Next: File I/O</a>
</p>
