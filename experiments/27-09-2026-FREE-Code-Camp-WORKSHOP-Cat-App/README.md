# 🐾 CatPhotoApp — Free Code Camp Workshop

> *"Everyone loves cute cats online"* — and this repo has receipts. 🌺

A tiny, no-nonsense HTML page built during the FreeCodeCamp workshop. No frameworks, no build step, no drama — just markup, doing what markup does best: showing off cats.

---

## 🌸 What lives here

One glorious `.html` file that:

- Greets the world with an **h1** worthy of a cat-themed royal decree
- Shows off a gallery-worthy cat photo (with a link, because the internet demands options)
- Ranks cat opinions with brutal honesty — a `<ul>` of things cats *love*, an `<ol>` of things cats *hate*
- Wraps up with a proper `<footer>` giving credit where it's due

Semantic HTML doing semantic HTML things: `<main>`, `<section>`, `<figure>`, `<figcaption>` — all present, all behaving.

---

## 🔴 Petal-by-petal breakdown

```
📄 index.html
 ├── <head>            — charset + title, minimal and correct
 └── <body>
      ├── <h1>          — the app announces itself
      ├── Cat Photos    — section: image + gallery link
      ├── Cat Lists     — section: loves (ul) vs. hates (ol)
      └── <footer>      — no copyright, all love
```

---

## 🕯️ Code review — a few things I'd tend to before this blooms further

Nothing's on fire, but here's what I noticed while poking around:

1. **`target="_blank"` without a chaperone** — the gallery link opens a new tab but skips `rel="noopener noreferrer"`. Small thing, real thing: it's a minor security/performance leak (the new tab can reach back and mess with `window.opener`).
2. **No `<meta name="viewport">`** — on mobile this page won't scale properly; it'll just render at desktop width and shrink. One line fixes it.
3. **Images have no `width`/`height` attributes** — without them, the browser can't reserve space before the image loads, which causes layout shift (the page jumps around as images pop in).

None of these break anything — they're the difference between "works" and "polished."

---



---

<p align="center">🌺 no copyright, only cats 🌺</p>
