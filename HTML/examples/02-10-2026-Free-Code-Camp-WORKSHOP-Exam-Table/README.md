# 🌺 Calculus Final Exam Grades

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-2%20Oct%202026-lightgrey?style=flat-square)
![Topic](https://img.shields.io/badge/topic-tables-informational?style=flat-square)

> Five students, one exam, and the cold, honest truth of a 54. 🥀

A tidy HTML table from a freeCodeCamp workshop. It's all about structure: a caption, a header, a body, and a footer.

📄 **File:** [`02-10-2026-Free-Code-Camp-WORKSHOP-Exam-Table.html`](./02-10-2026-Free-Code-Camp-WORKSHOP-Exam-Table.html)

---

## 🧱 What's inside

| Part | Tag | What it does |
|------|-----|--------------|
| Title | `<caption>` | Describes the table before anyone reads a cell |
| Header | `<thead>` + `<th>` | Names the columns: **Last Name**, **First Name**, **Grade** |
| Body | `<tbody>` + `<td>` | The five students and their grades |
| Footer | `<tfoot>` | Holds the **Average Grade** |
| Stretchy cell | `colspan="2"` | Lets "Average Grade" span two columns |

---

## 📊 The data

| Last Name | First Name | Grade |
|-----------|------------|-------|
| Davis | Alex | 54 |
| Doe | Samantha | 92 |
| Rodriguez | Marcus | 88 |
| Thompson | Jane | 77 |
| Williams | Natalie | 83 |
| **Average Grade** | | **78.8** |

✔️ Math check: (54 + 92 + 88 + 77 + 83) ÷ 5 = **78.8**. The average is correct.

---

## 🚀 How to run it

Open the `.html` file in a browser. You'll see a plain little table, no installs, no build step. ✨

---

## 🧠 What I practiced

- Giving a table a `<caption>`
- Splitting it into `<thead>`, `<tbody>`, and `<tfoot>`
- `<th>` for headers vs. `<td>` for data
- Merging cells with `colspan`

---

## 💥 Honest corner

- The average (78.8) is **typed by hand**, so if a grade changes, it won't update. Tables don't do math!
- No `scope` attributes on the headers, so screen readers get less help.
- No CSS (the table has no borders) and no `viewport` meta tag.

---

## 🔮 Mark II ideas

- Add `scope="col"` to each `<th>` ♿
- Style it: borders, zebra stripes, and a deep red header 🌺
- Calculate the average with JavaScript instead of typing it
- Add a `rowspan` example to practice merging vertically

---

↩️ [Back to examples](../README.md)

*Made with curiosity, a few typos, and a lot of `<td>`s. 🌺*
