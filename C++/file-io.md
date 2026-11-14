# 💾 File I/O — Giving the Suit a Memory

![Topic](https://img.shields.io/badge/topic-file%20I%2FO-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20V-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Variables vanish the moment a program ends. Files are how J.A.R.V.I.S. *remembers*. 🧠💽

---

## 🗺️ Overview

| 🧩 Class | 💬 Use | 🏷️ Header |
|---|---|---|
| `std::ofstream` | **Write** to a file (output) | `<fstream>` |
| `std::ifstream` | **Read** from a file (input) | `<fstream>` |
| `std::fstream` | Read **and** write | `<fstream>` |

The good news: files work just like `cout` and `cin`. Same `<<` and `>>`, different destination. 🎉

---

## 1️⃣ Writing to a File

```cpp
#include <fstream>    // file streams
#include <iostream>

int main() {
    std::ofstream out("notes.txt");    // opens (or CREATES) notes.txt. Existing content is ERASED.

    if (!out.is_open()) {              // ALWAYS check that the file really opened
        std::cerr << "Could not open file!" << std::endl;   // cerr = error output
        return 1;                      // non-zero return = "something went wrong"
    }

    out << "Mark I online" << std::endl;   // used exactly like cout
    out << "Power level: " << 85 << std::endl;

    out.close();                       // close it (also happens automatically at end of scope)
    return 0;
}
```

### Appending instead of overwriting
```cpp
// std::ios::app = APPEND mode: new text is added to the END, old text is kept
std::ofstream out("notes.txt", std::ios::app);
out << "One more line" << std::endl;
```

---

## 2️⃣ Reading from a File

### Line by line (most common)
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream in("notes.txt");     // open for reading

    if (!in.is_open()) {
        std::cerr << "File not found!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(in, line)) {   // reads one line each round; stops at the end of the file
        std::cout << line << std::endl;
    }

    return 0;                          // "in" closes automatically here (RAII 🎉)
}
```

### Word by word
```cpp
std::string word;
while (in >> word) {        // >> skips whitespace and reads one word at a time
    std::cout << word << std::endl;
}
```

### Reading numbers
```cpp
// numbers.txt contains:  10 20 30 40
std::ifstream in("numbers.txt");
int n;
int sum = 0;
while (in >> n) {           // keeps going while a number was read successfully
    sum += n;
}
std::cout << "Sum: " << sum << std::endl;   // 100
```

> 🐛 **Don't write** `while (!in.eof())`. It's a famous bug that processes the last line twice. Use `while (std::getline(...))` or `while (in >> x)`.

---

## 3️⃣ File Modes

| 🚩 Flag | 💬 Meaning |
|---|---|
| `std::ios::in` | Open for reading |
| `std::ios::out` | Open for writing (erases old content) |
| `std::ios::app` | Append to the end |
| `std::ios::trunc` | Erase existing content (default for `out`) |
| `std::ios::binary` | Binary mode (not text) |

Combine with `|`:
```cpp
std::fstream f("data.txt", std::ios::in | std::ios::out);
```

---

## 4️⃣ Where Does My File Live?

A name like `"notes.txt"` is relative to the **current working directory**, which is the folder the program is *run from*, not necessarily where the `.cpp` file is.

- If the file "isn't found", this is the first thing to check.
- Use a full path (`"C:/Users/me/notes.txt"` or `"/home/me/notes.txt"`) to be sure.
- On Windows paths, either use `/` or double backslashes: `"C:\\Users\\me\\notes.txt"`.

---

## 5️⃣ Mini Project: Tiny To-Do Saver ✅

```cpp
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// Load all tasks from the file into a vector
std::vector<std::string> loadTasks(const std::string& filename) {
    std::vector<std::string> tasks;
    std::ifstream in(filename);              // if the file doesn't exist yet, this simply fails quietly
    std::string line;
    while (std::getline(in, line)) {
        if (!line.empty()) {                 // skip blank lines
            tasks.push_back(line);
        }
    }
    return tasks;                            // returned by value (the compiler makes this cheap)
}

// Save all tasks, one per line (overwrites the file)
void saveTasks(const std::string& filename, const std::vector<std::string>& tasks) {
    std::ofstream out(filename);
    for (const std::string& t : tasks) {
        out << t << "\n";
    }
}

int main() {
    const std::string file = "tasks.txt";
    std::vector<std::string> tasks = loadTasks(file);   // 1. load what we saved last time

    std::cout << "New task (or press Enter to just list): ";
    std::string input;
    std::getline(std::cin, input);
    if (!input.empty()) {
        tasks.push_back(input);                          // 2. add the new one
        saveTasks(file, tasks);                          // 3. save everything back
    }

    std::cout << "\nYour tasks:\n";
    for (size_t i = 0; i < tasks.size(); i++) {
        std::cout << i + 1 << ". " << tasks[i] << "\n";
    }
    return 0;
}
```
Run it twice: the tasks from the first run are still there on the second. That's persistence. 🎉

---

## 6️⃣ Mini Project: CSV Reader 📊

```cpp
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main() {
    // scores.csv looks like:
    // Tony,95
    // Pepper,98
    std::ifstream in("scores.csv");
    std::string line;

    while (std::getline(in, line)) {
        std::istringstream row(line);    // treat the line like a mini input stream
        std::string name, scoreText;

        std::getline(row, name, ',');        // read up to the comma (the 3rd argument is the delimiter)
        std::getline(row, scoreText, ',');   // read the rest

        int score = std::stoi(scoreText);    // convert text → number
        std::cout << name << " scored " << score << std::endl;
    }
    return 0;
}
```

---

## 🧪 Mini Challenges

1. Count the lines, words, and characters in a text file (like `wc`).
2. Copy one file to another, line by line.
3. Read a list of numbers and write the sorted list to a new file.
4. Make the To-Do Saver support deleting a task by number.

---

## 🐛 Gremlins to Remember

- [ ] Always check `is_open()`
- [ ] `ofstream` **erases** existing content unless you use `std::ios::app`
- [ ] Wrong working directory = "file not found"
- [ ] Never loop on `eof()`
- [ ] `std::stoi` crashes on non-numeric text (needs error handling)

---

<p align="center">
  ⬅️ <a href="./stl.md">STL</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./cheat-sheet.md">Next: Cheat Sheet</a>
</p>
