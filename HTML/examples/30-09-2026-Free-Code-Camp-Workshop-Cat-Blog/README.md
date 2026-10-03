# 😺 Mr. Whiskers' Blog

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-30%20Sep%202026-lightgrey?style=flat-square)
![Semantic](https://img.shields.io/badge/semantic-HTML-success?style=flat-square)

> A blog by Jane Doe about her beloved cat. The suit gets a skeleton: header, nav, main, articles, footer. 🐾

A freeCodeCamp workshop page that practices **semantic page structure**, where each part of the page uses the tag that describes what it actually is.

📄 **File:** [`30-09-2026-Free-Code-Camp-Workshop-Cat-Blog.html`](./30-09-2026-Free-Code-Camp-Workshop-Cat-Blog.html)

---

## 🗺️ Page anatomy

| Section | Tags | Contents |
|---------|------|----------|
| 🎩 Header | `<header>`, `<h1>`, `<figure>`, `<nav>` | Title, a photo of Mr. Whiskers with a caption, and a menu |
| 🧭 Navigation | `<nav>` + `<ul>` + `<a href="#...">` | Jump links to **About**, **Posts**, and **Contact** |
| 📝 About | `<section id="about">` | A short intro to Jane and her cat |
| 📰 Posts | `<section id="posts">` + 3 × `<article>` | *First Day Home*, *First Bath*, *First Birthday Party* |
| 📞 Contact | `<footer>`, `<address>` | A `tel:` link and a `mailto:` link |

---

## 🧠 What I practiced

- **Semantic landmarks:** `header`, `nav`, `main`, `section`, `article`, `footer`
- **In-page navigation:** `href="#about"` jumps to the element with `id="about"`
- Special links: `tel:` (tap to call) and `mailto:` (opens your email app)
- Wrapping contact details in `<address>`
- Using `<figure>` and `<figcaption>` for an image with a caption

---

## 🚀 How to run it

Open the `.html` file in a browser, then click the menu links and watch the page jump to each section. The photo loads from freeCodeCamp's servers, so you'll need an internet connection.

---

## 💥 Honest corner

- The post text is **Lorem ipsum** placeholder filler, and the phone number and email are fake.
- No `viewport` meta tag, and no CSS, so the "menu" is just a bullet list.
- The **Contact** section lives inside `<footer>`. That's valid, but it's worth remembering it's a choice.

---

## 🔮 Mark II ideas

- Turn the bullet list into a horizontal navigation bar 🎨
- Add smooth scrolling between sections
- Write real posts about Mr. Whiskers (or a real cat)
- Add dates to the articles with `<time>`

---

↩️ [Back to examples](../README.md)

*Content is king. The cat is the emperor. 👑*
