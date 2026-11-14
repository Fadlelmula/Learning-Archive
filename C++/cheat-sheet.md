# 📋 C++ Cheat Sheet — "I Forgot the Syntax Again"

![Topic](https://img.shields.io/badge/topic-cheat%20sheet-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Use](https://img.shields.io/badge/use-quick%20reference-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-living%20document-orange?style=for-the-badge)

> Even Tony checks the blueprints. This is my blueprint drawer. 📐
> Details live in the topic files; this page is for **fast lookup**.

---

## 🚀 1. Program Skeleton

```cpp
#include <iostream>            // libraries
#include <string>

int main() {                   // entry point
    std::cout << "Hello" << std::endl;
    return 0;                  // 0 = success
}
```

**Compile & run**
```bash
g++ -std=c++17 -Wall -Wextra main.cpp -o app && ./app
```
Multiple files: `g++ -std=c++17 main.cpp other.cpp -o app`

---

## 🧱 2. Types & Variables

| Type | Example |
|---|---|
| `int` | `int a = 5;` |
| `long long` | `long long big = 9000000000LL;` |
| `double` | `double d = 3.14;` |
| `char` | `char c = 'x';` |
| `bool` | `bool ok = true;` |
| `std::string` | `std::string s = "hi";` |
| `auto` | `auto x = 10;` |
| constant | `const int MAX = 100;` |

⚠️ `int / int` = int (`7 / 2` is `3`). Use `7.0 / 2` for `3.5`.

---

## ⌨️ 3. Input / Output

```cpp
std::cout << "text" << var << "\n";     // print
std::cin >> var;                        // read one word / number
std::getline(std::cin, line);           // read a full line
std::cin.ignore();                      // clear leftover Enter after cin >>
std::cerr << "error";                   // error output
```

---

## 🔣 4. Operators

| Kind | Operators |
|---|---|
| Math | `+ - * / %` |
| Assign | `= += -= *= /= %=` |
| Inc/Dec | `++ --` |
| Compare | `== != < > <= >=` |
| Logic | `&&` (and) `\|\|` (or) `!` (not) |
| Ternary | `cond ? a : b` |

---

## 🔀 5. Control Flow

```cpp
if (a > b) { } else if (a == b) { } else { }

switch (x) { case 1: /*...*/ break; default: break; }

for (int i = 0; i < n; i++) { }
for (auto& item : container) { }        // range-based (& to modify)
while (cond) { }
do { } while (cond);

break;      // leave the loop
continue;   // next round
```

---

## 🧩 6. Functions

```cpp
int add(int a, int b) { return a + b; }            // returns a value
void hello() { }                                   // returns nothing
void change(int& x) { x++; }                       // reference: modifies the original
void show(const std::string& s) { }                // const ref: read-only, no copy
void greet(std::string n = "friend") { }           // default argument
int add(int a, int b, int c);                      // overload (different params)
int factorial(int n);                              // prototype (declaration)
```

| Pass by | Syntax | Modifies original? |
|---|---|---|
| Value | `int x` | No |
| Reference | `int& x` | Yes |
| Const reference | `const T& x` | No (no copy) |
| Pointer | `int* x` | Yes (via `*x`) |

---

## 🗃️ 7. Arrays, Vectors, Strings

```cpp
int a[3] = {1, 2, 3};                    // C array (fixed size, no bounds check)
std::vector<int> v = {1, 2, 3};          // ⭐ dynamic array
v.push_back(4);  v.pop_back();
v.size();  v.empty();  v.clear();
v[0];   v.at(0);   v.front();   v.back();

std::string s = "hello";
s.length();  s[0];  s + " world";  s += "!";
s.substr(1, 3);  s.find("ll");           // npos if not found
std::stoi("42");  std::stod("3.5");  std::to_string(7);
```

---

## 👹 8. Pointers & Memory

```cpp
int x = 5;
int* p = &x;         // p stores the ADDRESS of x
*p = 10;             // follow p, change x
int* q = nullptr;    // points at nothing (check before using!)
int& r = x;          // r is another name for x

int* h = new int(5); delete h;           // heap (manual)
int* arr = new int[3]; delete[] arr;     // heap array

auto u = std::make_unique<int>(5);       // ⭐ auto-cleanup (one owner)
auto s = std::make_shared<int>(5);       // auto-cleanup (many owners)
// #include <memory>
```

| Symbol | In a declaration | In an expression |
|---|---|---|
| `*` | pointer type (`int* p`) | dereference (`*p`) |
| `&` | reference type (`int& r`) | address-of (`&x`) |

---

## 🏗️ 9. Classes

```cpp
class Hero {
private:
    std::string name;
    int level;
public:
    Hero(const std::string& n, int l) : name(n), level(l) {}   // constructor + init list
    ~Hero() {}                                                  // destructor
    int getLevel() const { return level; }                      // const method
    static int count;                                           // shared by all objects
};

class Sidekick : public Hero { /* inherits Hero */ };           // inheritance

class Base {
public:
    virtual void act() const { }       // can be overridden
    virtual ~Base() = default;         // ALWAYS virtual in a base class
};
class Child : public Base {
    void act() const override { }      // override = "replacing parent's version"
};
virtual void f() = 0;                  // pure virtual → abstract class
```

| Access | Same class | Child | Outside |
|---|---|---|---|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

---

## 🧰 10. STL Quick Hits

```cpp
#include <vector> <map> <set> <stack> <queue> <algorithm> <numeric>

std::map<std::string, int> m;   m["a"] = 1;   m.find("a") != m.end();   m.erase("a");
std::set<int> s = {3, 1, 3};    s.insert(2);  s.count(2);
std::stack<int> st;  st.push(1); st.top(); st.pop();
std::queue<int> q;   q.push(1);  q.front(); q.pop();

std::sort(v.begin(), v.end());
std::sort(v.begin(), v.end(), std::greater<int>());      // descending
std::reverse(v.begin(), v.end());
std::find(v.begin(), v.end(), x);                        // iterator, or end() if missing
std::count(v.begin(), v.end(), x);
*std::min_element(v.begin(), v.end());
*std::max_element(v.begin(), v.end());
std::accumulate(v.begin(), v.end(), 0);                  // sum

[](int a, int b) { return a > b; }                       // lambda
```

---

## 💾 11. Files

```cpp
#include <fstream>
std::ofstream out("f.txt");                    // write (erases)
std::ofstream out("f.txt", std::ios::app);     // append
std::ifstream in("f.txt");                     // read
if (!in.is_open()) { /* handle error */ }

while (std::getline(in, line)) { }             // read lines
while (in >> word) { }                         // read words
```

---

## 🆘 12. Reading Compiler Errors

| 💬 Message | 🔍 Usually Means |
|---|---|
| `expected ';'` | Missing semicolon (check the **previous** line) |
| `was not declared in this scope` | Typo, missing `#include`, or missing `std::` |
| `undefined reference to ...` | Declared but never defined, or file missing from the compile command |
| `no matching function for call` | Wrong argument types or count |
| `Segmentation fault` | Bad pointer / out-of-bounds access (runtime) |

**Debugging habit:** read the **first** error only, fix it, recompile. Later errors are often side effects.

---

## 🧯 13. Top 10 Gremlins

1. `=` vs `==`
2. Integer division
3. Off-by-one (`<` vs `<=`)
4. Forgetting `break` in `switch`
5. Forgetting `&` (copy instead of reference)
6. Out-of-bounds index
7. Uninitialized variable or pointer
8. `new` without `delete` (use smart pointers!)
9. Dangling pointer / returning a local's address
10. Missing `virtual` destructor in a base class

---

## 🧭 Next-Step Kit

| 🎯 Want To Learn | 🔗 Look Into |
|---|---|
| Better error handling | `try / catch`, `std::optional` |
| Cleaner code organization | Header files, namespaces, `CMake` |
| Reusable generic code | Templates (`template <typename T>`) |
| Performance | `const`, move semantics, profiling |
| Building real stuff | A small game (SFML), a CLI tool, a simulation |

---

<p align="center">
  ⬅️ <a href="./file-io.md">File I/O</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./final-review.md">Next: Final Review</a>
</p>
