# 💬 Quincy's Tips for Getting a Developer Job

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-30%20Sep%202026-lightgrey?style=flat-square)

> Advice worth quoting, so I learned how to quote it *properly*. 📖

A freeCodeCamp workshop page built around quotations and citations, with advice from Quincy Larson's book on learning to code and getting a developer job.

📄 **File:** [`30-09-2026-FREE-Code-Camp-Workshop-Job-Tips-page.html`](./30-09-2026-FREE-Code-Camp-Workshop-Job-Tips-page.html)

---

## 🧱 What's inside

| Piece | Tag | What it does |
|-------|-----|--------------|
| Short quote | `<q cite="...">` | An **inline** quote; the browser adds the quotation marks for you |
| Long quote | `<blockquote cite="...">` | A **block** quote, shown indented |
| Source title | `<cite>` | Marks the title of the work being quoted (shown in italics) |
| Dash | `&mdash;` | An HTML entity for the long dash before the author's name |
| Sections | `<main>` + 3 × `<section>` | *Envisioning Success*, *Importance of Networking*, *Importance of Building a Reputation* |

**The difference:** the `cite="..."` **attribute** holds the source URL (invisible to readers), while the `<cite>` **element** shows the title on the page.

---

## 🚀 How to run it

Open the `.html` file in a browser. Hover and inspect the quotes with DevTools to see the `cite` URLs, since they don't appear on screen.

---

## 🧠 What I practiced

- Choosing `<q>` vs `<blockquote>` by quote length
- Putting several `<p>` tags inside a `<blockquote>`
- Using the `cite` attribute and the `<cite>` element for sources
- Writing special characters as HTML entities

---

## 💥 Honest corner

- ✅ *Fixed on 3 Oct:* the third `<blockquote>` had a **stray extra `"`** after its `cite` URL (`cite="...""`). Browsers forgive it, but it's invalid HTML and an easy bug to miss. I also tidied that section's indentation.
- ✅ *Fixed on 3 Oct:* the folder and file name had a typo ("Jop" instead of "Job").
- The first quote puts text straight inside `<blockquote>`, while the others wrap it in `<p>`. It's valid, but consistency would be nicer.
- No CSS yet, so the blockquotes are just indented.
---

## 🔮 Mark II ideas

- Run the page through the W3C validator ✅
- Add a visible link to the source book
- Style the blockquotes with a colored left border 🎨
- Wrap the page in `<header>` and `<footer>` for full semantic structure

---

↩️ [Back to examples](../README.md)

*"You can become a developer." Working on it. 🦾*
