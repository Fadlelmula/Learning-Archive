# 🏗️ Object-Oriented Programming — Designing the Suit as a System

![Topic](https://img.shields.io/badge/topic-OOP-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Level](https://img.shields.io/badge/level-Mark%20IV-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> A suit isn't one giant blob of code. It's a helmet, a repulsor, a power core, each with its own job, all working together. 🦾
> OOP lets me build programs the same way: **objects** that bundle data and behavior.

---

## 🗺️ Overview

| 🧩 Idea | 💬 In Plain Words |
|---|---|
| Class | A blueprint |
| Object | A real thing built from the blueprint |
| Member variable | Data stored inside an object |
| Member function (method) | An action an object can do |
| Constructor | Sets up a new object |
| Destructor | Cleans up when an object dies |
| Encapsulation | Hide the insides, expose a safe interface |
| Inheritance | A new class built on an existing one |
| Polymorphism | Same call, different behavior depending on the object |

---

## 1️⃣ Classes and Objects

```cpp
#include <iostream>
#include <string>

// "class" defines a BLUEPRINT. No object exists yet.
class Suit {
public:                               // public = anyone can use these
    std::string name;                 // member variable (data)
    int powerLevel;                   // member variable (data)

    void status() {                   // member function (behavior)
        std::cout << name << " | power: " << powerLevel << std::endl;
    }
};                                    // ← the semicolon after a class is REQUIRED

int main() {
    Suit mark1;                       // create an OBJECT from the blueprint
    mark1.name = "Mark I";            // the dot . accesses a member
    mark1.powerLevel = 10;

    Suit mark2;                       // a second, separate object
    mark2.name = "Mark II";
    mark2.powerLevel = 25;

    mark1.status();                   // Mark I | power: 10
    mark2.status();                   // Mark II | power: 25
    return 0;
}
```

---

## 2️⃣ Encapsulation: `public` vs `private`

```cpp
#include <iostream>
#include <string>

class Reactor {
private:                                  // private = ONLY the class itself can touch these
    int energy;                           // hidden data protects itself from bad values

public:
    // Constructor: same name as the class, no return type. Runs when an object is created.
    Reactor(int startEnergy) {
        if (startEnergy < 0) {
            energy = 0;                   // guard against nonsense values
        } else {
            energy = startEnergy;
        }
    }

    // "Getter": lets the outside READ the value
    int getEnergy() const {               // const = this function promises not to change the object
        return energy;
    }

    // "Setter": lets the outside CHANGE the value, but with rules
    void addEnergy(int amount) {
        if (amount > 0) {
            energy += amount;
        }
    }
};

int main() {
    Reactor core(100);                    // calls the constructor with 100
    core.addEnergy(50);
    std::cout << core.getEnergy() << std::endl;   // 150
    // core.energy = -999;                // ❌ error: energy is private. The class protects itself.
    return 0;
}
```

**Why bother?** The object guarantees its own data stays valid. Nobody can accidentally set energy to `-999`.

> `class` members default to **private**; `struct` members default to **public**. Otherwise they're nearly identical.

---

## 3️⃣ Constructors in Detail

```cpp
#include <iostream>
#include <string>

class Hero {
private:
    std::string name;
    int level;

public:
    // Default constructor: used when no arguments are given
    Hero() : name("Unknown"), level(1) {}
    // The part after the colon is the INITIALIZER LIST.
    // It sets members BEFORE the constructor body runs (faster and the preferred style).

    // Parameterized constructor
    Hero(const std::string& n, int l) : name(n), level(l) {}

    void show() const {
        std::cout << name << " (Lv " << level << ")" << std::endl;
    }
};

int main() {
    Hero a;                       // default constructor → Unknown (Lv 1)
    Hero b("Tony", 85);           // parameterized     → Tony (Lv 85)
    a.show();
    b.show();
    return 0;
}
```

---

## 4️⃣ Destructors

```cpp
#include <iostream>

class Tracker {
public:
    Tracker()  { std::cout << "Built 🔧" << std::endl; }
    ~Tracker() { std::cout << "Destroyed 💥" << std::endl; }
    // ~ClassName() is the destructor. It runs AUTOMATICALLY when the object's scope ends.
};

int main() {
    {
        Tracker t;    // prints "Built"
    }                 // t goes out of scope here → prints "Destroyed"
    return 0;
}
```
Destructors are where a class frees resources (memory, files). This is the heart of **RAII** from the pointers file.

---

## 5️⃣ Splitting Into Header and Source (Preview)

In real projects a class is split into two files:

```cpp
// suit.h : the DECLARATION (what the class looks like)
#pragma once                       // prevents the file being included twice
class Suit {
public:
    void fly();
};

// suit.cpp : the DEFINITION (the real code)
#include "suit.h"
#include <iostream>
void Suit::fly() {                 // Suit:: says "this function belongs to Suit"
    std::cout << "Flying!" << std::endl;
}
```
Compile both: `g++ main.cpp suit.cpp -o app`

---

## 6️⃣ Inheritance

A **child** class reuses everything from a **parent** and adds its own stuff.

```cpp
#include <iostream>
#include <string>

class Vehicle {                          // PARENT (base class)
protected:                               // protected = private to outsiders, but visible to children
    std::string name;

public:
    Vehicle(const std::string& n) : name(n) {}

    void describe() const {
        std::cout << "I am " << name << std::endl;
    }
};

class Jet : public Vehicle {             // CHILD: ": public Vehicle" means "Jet IS-A Vehicle"
private:
    int speed;

public:
    Jet(const std::string& n, int s)
        : Vehicle(n), speed(s) {}        // call the PARENT constructor first

    void boost() const {
        std::cout << name << " boosting at " << speed << " km/h" << std::endl;
    }
};

int main() {
    Jet j("Stark Jet", 900);
    j.describe();   // inherited from Vehicle → "I am Stark Jet"
    j.boost();      // Jet's own method
    return 0;
}
```

| 🔐 Access | 🧍 Same Class | 👶 Child Class | 🌍 Outside |
|---|---|---|---|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

---

## 7️⃣ Polymorphism and `virtual`

Same function name, different behavior depending on the real object type.

```cpp
#include <iostream>
#include <memory>
#include <vector>

class Weapon {
public:
    virtual void fire() const {                       // virtual = "children may override this"
        std::cout << "Generic weapon fires" << std::endl;
    }
    virtual ~Weapon() = default;                      // ALWAYS make the base destructor virtual
};

class Repulsor : public Weapon {
public:
    void fire() const override {                      // override = "I'm replacing the parent's version"
        std::cout << "Repulsor blast ⚡" << std::endl;
    }
};

class Missile : public Weapon {
public:
    void fire() const override {
        std::cout << "Missile launched 🚀" << std::endl;
    }
};

int main() {
    // A list of base-class pointers that actually hold different child objects
    std::vector<std::unique_ptr<Weapon>> arsenal;
    arsenal.push_back(std::make_unique<Repulsor>());
    arsenal.push_back(std::make_unique<Missile>());

    for (const auto& w : arsenal) {
        w->fire();      // -> is shorthand for (*w).fire()
                        // C++ picks the RIGHT fire() at runtime: blast, then missile
    }
    return 0;
}
```

### Abstract classes (pure virtual)
```cpp
class Shape {
public:
    virtual double area() const = 0;   // "= 0" makes it PURE virtual: no body here
    virtual ~Shape() = default;        // children MUST implement area(). You can't create a plain Shape.
};
```

---

## 8️⃣ `static` Members and `this`

```cpp
#include <iostream>

class Counter {
private:
    int value = 0;              // each object has its OWN value
public:
    static int totalCreated;    // ONE shared variable for the whole class

    Counter() { totalCreated++; }

    Counter& increment() {
        value++;
        return *this;           // "this" is a pointer to the CURRENT object. Returning it allows chaining.
    }

    int get() const { return value; }
};

int Counter::totalCreated = 0;  // static members are defined once, outside the class

int main() {
    Counter a, b;
    a.increment().increment();             // chaining thanks to "return *this"
    std::cout << a.get() << std::endl;     // 2
    std::cout << Counter::totalCreated << std::endl;   // 2 (a and b)
    return 0;
}
```

---

## 🧪 Mini Challenges

1. Make a `BankAccount` class with private `balance`, `deposit()`, and `withdraw()` that refuses to overdraw.
2. Create `Animal` → `Dog` and `Cat` that override `speak()`.
3. Build a `Shape` base class with `Circle` and `Rectangle` children computing `area()`, store them in one vector and loop.
4. Add a `static` counter that tracks how many objects were created.

---

## 🐛 Gremlins to Remember

- [ ] Missing `;` after the closing brace of a class
- [ ] Forgetting `virtual` → the parent's version runs instead of the child's
- [ ] Base class without a `virtual` destructor
- [ ] Member initializer list order follows the **declaration order**, not the order I write it
- [ ] Putting everything `public` and losing the whole point of encapsulation

---

<p align="center">
  ⬅️ <a href="./pointers-and-memory.md">Pointers & Memory</a> · 🏠 <a href="./README.md">C++ Home</a> · ➡️ <a href="./stl.md">Next: STL</a>
</p>
