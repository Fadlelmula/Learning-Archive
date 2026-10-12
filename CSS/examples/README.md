# 🧪 CSS Examples: The Workshop Floor

![Type](https://img.shields.io/badge/type-examples-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Built](https://img.shields.io/badge/built-0%20of%203-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/status-planning-orange?style=for-the-badge)

> Notes teach me the rules. Examples prove I can actually *use* them. Every project in here has its own folder, its own README, and an honest "what went wrong" section. 🔧

⬅️ Back to [CSS README](../README.md)

---

## 📍 Table of Contents

1. [Status legend](#-status-legend)
2. [Example index](#-example-index)
3. [Planned examples in detail](#-planned-examples-in-detail)
4. [Folder structure](#-folder-structure-for-each-example)
5. [README template](#-example-readme-template)
6. [How to add a new example](#-how-to-add-a-new-example)
7. [Quality checklist](#-quality-checklist)

---

## 🚦 Status Legend

| Icon | Meaning |
|:---:|---|
| 💡 | Idea: not started |
| 🚧 | In progress |
| ✅ | Finished and pushed |
| 🔁 | Finished, being improved (new Mark!) |

---

## 📋 Example Index

| # | Example | Skills practiced | Difficulty | Status |
|:---:|---|---|:---:|:---:|
| 1 | 🎧 **Styled audio controller** | Box model, colors, variables, `:hover`/`:focus-visible`, transitions | ⭐⭐ | 💡 |
| 2 | 🖤 **Brand palette with CSS variables** | Custom properties, `:root`, dark theme, typography | ⭐⭐ | 💡 |
| 3 | 📱 **Responsive card layout** | Flexbox, Grid, `auto-fit`/`minmax`, media queries | ⭐⭐⭐ | 💡 |

> 📌 Every row is a plan, not a finished project. Statuses change only when real work is pushed.

---

## 🔍 Planned Examples in Detail

### 1️⃣ 🎧 Styled Audio Controller

Take the accessible audio controller from my HTML examples and give it a proper look.

| | |
|---|---|
| **Starts from** | The HTML audio example in [`../../HTML/examples`](../../HTML/examples) |
| **Goal** | Make it look polished without breaking accessibility |
| **Layout sketch** | |

```
┌──────────────────────────────────────────┐
│  🎵 Track title                          │
│  ▶  ━━━━━━━●━━━━━━━━━━  1:24 / 3:40  🔊  │
└──────────────────────────────────────────┘
```

**Concepts to practice:**
- [ ] Flexbox row with aligned controls
- [ ] Rounded card with soft shadow ([box-model.md](../box-model.md))
- [ ] Color variables ([colors-and-typography.md](../colors-and-typography.md))
- [ ] Visible `:focus-visible` rings for keyboard users
- [ ] Smooth hover transitions ([animations.md](../animations.md))

**Success looks like:** every control is reachable and visible with the keyboard only.

---

### 2️⃣ 🖤 Brand Palette with CSS Variables

A themed page driven entirely by custom properties: obsidian, crimson and ivory.

| | |
|---|---|
| **Goal** | Change one block of variables and watch the whole page re-theme |
| **Key idea** | Zero hard-coded colors outside `:root` |

```
:root
 ├── --obsidian  ██  dark background
 ├── --crimson   ██  accent / links / buttons
 ├── --ash       ██  muted text
 └── --ivory     ██  main text
```

**Concepts to practice:**
- [ ] `:root` variables and `var()` with fallbacks
- [ ] Contrast checks (target 4.5 : 1)
- [ ] A light variant using `prefers-color-scheme`
- [ ] A type scale with `rem` and `clamp()`

**Success looks like:** a "theme swap" demo changing only the variable block.

---

### 3️⃣ 📱 Responsive Card Layout

A gallery of cards that rearranges itself from phone to desktop.

| | |
|---|---|
| **Goal** | One codebase, every screen size |
| **Key idea** | Grid does the heavy lifting, Flexbox arranges inside each card |

```
📱 1 column      💻 2 columns        🖥️ 3+ columns
┌────────┐       ┌──────┐ ┌──────┐   ┌────┐ ┌────┐ ┌────┐
│ card   │       │ card │ │ card │   │card│ │card│ │card│
├────────┤       ├──────┤ ├──────┤   └────┘ └────┘ └────┘
│ card   │       │ card │ │ card │
└────────┘       └──────┘ └──────┘
```

**Concepts to practice:**
- [ ] Viewport meta tag
- [ ] `repeat(auto-fit, minmax(220px, 1fr))`
- [ ] Flexbox inside each card
- [ ] Fluid images (`max-width: 100%`, `object-fit: cover`)
- [ ] A hover effect, only where hover exists (`@media (hover: hover)`)

**Success looks like:** no horizontal scrollbar at any width, including zoomed to 200%.

---

## 🗂️ Folder Structure for Each Example

```
examples/
├── README.md                    ← this index
└── audio-controller/
    ├── README.md                ← what it is, what I learned, what broke
    ├── index.html
    ├── styles.css
    └── screenshot.png           ← visual proof 📸
```

> 💡 Name folders in `lowercase-with-dashes`. Keep each example **self-contained** so it opens by double-clicking `index.html`.

---

## 📝 Example README Template

Copy this into every new example's folder:

```markdown
# 🎧 Example Name

![Status](https://img.shields.io/badge/status-finished-brightgreen)

## 🎯 What This Is
One or two sentences on what I built and why.

## 📸 Preview
![Screenshot](./screenshot.png)

## 🧠 Concepts Practiced
- Concept one
- Concept two

## 🔨 How I Built It
1. Step one (what, and why)
2. Step two

## 💥 What Went Wrong
Honest list of bugs and how I fixed them.

## 💡 What Clicked
The "ohhh" moments.

## 🚀 Next Iteration (Mark II)
What I'd improve next.

## ▶️ How to Run
Open `index.html` in a browser.
```

---

## ➕ How to Add a New Example

1. **Create the folder:** `CSS/examples/your-example-name/`
2. **Add the files:** `index.html`, `styles.css`, and a `README.md` from the template above
3. **Build it** and take a screenshot
4. **Test it:** keyboard only, 200% zoom, narrow and wide screens
5. **Update the index table** in this file (change 💡 to ✅ and update the "Built" badge count)
6. **Commit with a clear message:**

```bash
git add CSS/examples/your-example-name CSS/examples/README.md
git commit -m "Add CSS example: your-example-name"
git push
```

---

## ✅ Quality Checklist

Before an example gets a ✅:

- [ ] Opens and works by double-clicking `index.html`
- [ ] HTML is valid and semantic
- [ ] Viewport meta tag is present
- [ ] Works with keyboard only, and focus is always visible
- [ ] Text contrast is at least 4.5 : 1
- [ ] No horizontal scrollbar on narrow screens
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Example README is complete (including **What Went Wrong**)
- [ ] Screenshot added

⬅️ Back to [CSS README](../README.md)
