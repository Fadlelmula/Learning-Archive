# 📚 XYZ Bookstore

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-27%20Sep%202026-lightgrey?style=flat-square)
![Tags](https://img.shields.io/badge/%3Cdiv%3E-overused-red?style=flat-square)

> A storefront with no store. The buttons look great and do absolutely nothing, yet. 🛒

A freeCodeCamp workshop page that lays out a bookstore using `div` "cards" and buttons. It's structure only, and every `id` and `class` is a hook waiting for CSS and JavaScript.

📄 **File:** [`27-09-2026-FREE-Code-Camp-WORKSHOP-XYZ-Bookstore.html`](./27-09-2026-FREE-Code-Camp-WORKSHOP-XYZ-Bookstore.html)

---

## 🧱 What's inside

| Piece | Details |
|-------|---------|
| Header | `<h1>XYZ Bookstore</h1>` and a welcome line |
| `.card-container` | A wrapper around the two book cards |
| 📖 Card 1 | `#sally-adventure-book`: *Sally's SciFi Adventure* |
| 🍳 Card 2 | `#dave-cooking-book`: *Dave's Cooking Adventure* |
| `.btn` buttons | "Buy Now" on each card |
| `.btn-container` | Holds **View Cart** (`#view-cart-btn`) and **Checkout** (`#checkout-btn`) |

---

## 🧠 What I practiced

- Grouping content with `<div>` containers
- Giving elements an **`id`** (unique, one per page) vs. a **`class`** (reusable, many per page)
- Naming things so that future CSS and JS can find them
- Writing buttons with `<button>`

---

## 🚀 How to run it

Open the `.html` file in a browser. You'll see a plain list of books and buttons. Click away. Nothing happens, and that's expected. 😄

---

## 💥 Honest corner

- **The buttons are decorative.** There's no JavaScript, and they're not inside a `<form>`, so clicking does nothing.
- It's `div` all the way down. Real semantic tags like `<main>`, `<section>`, and `<article>` would say more about the content.
- No CSS yet, so the "cards" aren't visually cards.
- No `viewport` meta tag.

---

## 🔮 Mark II ideas

- Style the `.card` class into real cards: border, padding, shadow 🎨
- Swap `div.card` for `<article class="card">`
- Make **Buy Now** add the book to a cart with JavaScript
- Add book covers with proper `alt` text

---

↩️ [Back to examples](../README.md)

*Open for business. Sort of. 🏪*
