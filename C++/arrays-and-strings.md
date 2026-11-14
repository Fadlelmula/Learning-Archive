# 🗃️ Arrays & Strings — Storing Lots of Stuff

![Topic](https://img.shields.io/badge/topic-arrays%20%26%20strings-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20II-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> One variable = one box. But the workshop needs a whole *shelf* of boxes. 📦📦📦

---

## 🗺️ Overview

| 🧩 Tool | 💬 What It Is | 🎯 Use It When |
|---|---|---|
| C-style array `int a[5]` | Fixed-size row of values | Size is known and never changes |
| `std::array` | Safer fixed-size array | Fixed size, but want modern features |
| `std::vector` | **Resizable** array | Default choice for lists ⭐ |
| `std::string` | Text with helpful tools | Any text |

---

## 1️⃣ C-Style Arrays

```cpp
#include <iostream>

int main() {
    int scores[5] = {90, 85, 70, 100, 60};   // 5 ints stored side by side in memory

    // Indexes start at 0! The first item is scores[0], the last is scores[4].
    std::cout << scores[0] << std::endl;     // 90
    std::cout << scores[4] << std::endl;     // 60

    scores[1] = 88;                          // change one element

    // Loop through with a normal for loop
    for (int i = 0; i < 5; i++) {            // i < 5, NOT i <= 5
        std::cout << scores[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

> 💥 **Gremlin:** C++ does **not** stop you from reading `scores[10]`. It happily reads garbage memory (undefined behavior). Arrays have no built-in bounds checking.

**Other limits of C-style arrays:**
- The size is fixed forever.
- When passed to a function, they lose their size information.
- That's why I'll mostly use `std::vector` instead.

---

## 2️⃣ `std::vector` — The Star ⭐

```cpp
#include <iostream>
#include <vector>      // needed to use std::vector

int main() {
    std::vector<int> nums = {10, 20, 30};   // <int> = what type the vector holds

    nums.push_back(40);   // add to the END → {10, 20, 30, 40}
    nums.pop_back();      // remove the LAST item → {10, 20, 30}

    std::cout << "Size: " << nums.size() << std::endl;   // how many items: 3
    std::cout << "First: " << nums.front() << std::endl; // 10
    std::cout << "Last: " << nums.back() << std::endl;   // 30

    // at() checks bounds and throws an error if the index is bad (safer than [])
    std::cout << nums.at(1) << std::endl;                // 20

    // Range-based for: "for each n in nums"
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // Empty? Clear?
    std::cout << std::boolalpha << nums.empty() << std::endl;  // false (boolalpha prints true/false)
    nums.clear();                                              // remove everything

    return 0;
}
```

### Useful vector methods

| 🔧 Method | 💬 Does |
|---|---|
| `push_back(x)` | Add `x` at the end |
| `pop_back()` | Remove the last item |
| `size()` | Number of items |
| `empty()` | `true` if no items |
| `clear()` | Remove all items |
| `at(i)` | Item at index `i` (bounds-checked) |
| `insert(pos, x)` | Insert `x` before position `pos` |
| `erase(pos)` | Remove the item at position `pos` |

### Modifying inside a loop
```cpp
std::vector<int> nums = {1, 2, 3};

for (int& n : nums) {   // the & means n is the REAL element, not a copy
    n = n * 2;          // so this changes the vector → {2, 4, 6}
}
```

### 2D vectors (a grid)
```cpp
// 3 rows, 4 columns, all filled with 0
std::vector<std::vector<int>> grid(3, std::vector<int>(4, 0));

grid[1][2] = 7;   // row 1, column 2
```

---

## 3️⃣ `std::array` (Fixed Size, Modern)

```cpp
#include <array>
#include <iostream>

int main() {
    std::array<int, 3> a = {1, 2, 3};   // <type, size>: the size is part of the type
    std::cout << a.size() << std::endl; // knows its own size (unlike a C-style array)
    return 0;
}
```

---

## 4️⃣ `std::string`

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name = "Tony";        // text lives in DOUBLE quotes
    std::string last = "Stark";

    std::string full = name + " " + last;   // + joins (concatenates) strings
    std::cout << full << std::endl;         // Tony Stark

    std::cout << full.length() << std::endl;  // 10  (size() does the same)
    std::cout << full[0] << std::endl;        // 'T' (first character)

    full[0] = 't';                            // strings can be changed → "tony Stark"

    // Searching: find() returns the position, or std::string::npos if NOT found
    size_t pos = full.find("Stark");          // size_t = an unsigned whole number type
    if (pos != std::string::npos) {
        std::cout << "Found at index " << pos << std::endl;   // 5
    }

    // Slicing: substr(start, length)
    std::cout << full.substr(5, 5) << std::endl;   // Stark

    // Appending
    full += "!";                              // → "tony Stark!"

    return 0;
}
```

### Useful string methods

| 🔧 Method | 💬 Does |
|---|---|
| `length()` / `size()` | Number of characters |
| `empty()` | `true` if `""` |
| `substr(start, len)` | A piece of the string |
| `find(text)` | Position of `text` or `npos` |
| `append(x)` or `+=` | Add to the end |
| `insert(pos, text)` | Insert text at `pos` |
| `erase(pos, len)` | Remove `len` characters from `pos` |
| `compare(other)` | 0 if equal (or just use `==`) |

### Comparing strings
```cpp
std::string a = "apple";
std::string b = "apple";
if (a == b) {            // == works on std::string (compares the CONTENT) ✅
    // equal
}
```

### Converting between numbers and strings
```cpp
int n = std::stoi("42");          // string → int
double d = std::stod("3.14");     // string → double
std::string s = std::to_string(99);   // number → string
```
> ⚠️ `stoi` throws an error if the text isn't a number (e.g., `"abc"`). I'll handle errors in a later Mark.

---

## 5️⃣ Looping Over Characters

```cpp
#include <iostream>
#include <string>
#include <cctype>   // for toupper, isdigit, etc.

int main() {
    std::string word = "hello";

    for (char& c : word) {          // & so we can modify each character in place
        c = std::toupper(c);        // convert a single char to uppercase
    }

    std::cout << word << std::endl; // HELLO
    return 0;
}
```

---

## 6️⃣ Mini Project: Count the Vowels

```cpp
#include <iostream>
#include <string>
#include <cctype>

int countVowels(const std::string& text) {   // const& = read-only, no copy
    int count = 0;
    for (char c : text) {
        char lower = std::tolower(c);        // make it lowercase so 'A' and 'a' both count
        if (lower == 'a' || lower == 'e' || lower == 'i' ||
            lower == 'o' || lower == 'u') {
            count++;
        }
    }
    return count;
}

int main() {
    std::cout << countVowels("Iron Man") << std::endl;   // prints 3 (the vowels are I, o, a)
    return 0;
}
```

---

## 🧪 Mini Challenges

1. Find the largest number in a `std::vector<int>`.
2. Reverse a string without using any built-in reverse function.
3. Check whether a word is a palindrome (`racecar`).
4. Count how many times each letter appears in a sentence.

---

## 🐛 Gremlins to Remember

- [ ] Index starts at **0**; the last valid index is `size() - 1`
- [ ] `[]` doesn't check bounds, `at()` does
- [ ] `'a'` (char) vs `"a"` (string)
- [ ] Copying large vectors/strings by accident (use `const&`)
- [ ] Erasing from a vector while looping over it

---

<p align="center">
  ⬅️ <a href="./functions.md">Functions</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./pointers-and-memory.md">Next: Pointers & Memory 👹</a>
</p>
