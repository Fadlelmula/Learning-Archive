# 🏛️ Semantic HTML

> A `div` is not a personality.
> Mark II of the armor: same skeleton, but now every bone has a name.

![Topic](https://img.shields.io/badge/topic-semantic%20HTML-E34F26?logo=html5&logoColor=white)
![Level](https://img.shields.io/badge/level-fundamentals%20%2B-brightgreen)
![Status](https://img.shields.io/badge/status-growing-yellow)
![Tags](https://img.shields.io/badge/%3Cdiv%3E-last%20resort-red)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-blue)

---

## 🗂️ Table of Contents

1. [What "semantic" means](#-what-semantic-means)
2. [Why it matters](#-why-it-matters)
3. [The page layout elements](#-the-page-layout-elements)
4. [section vs article vs div](#-section-vs-article-vs-div)
5. [Landmarks and screen readers](#-landmarks-and-screen-readers)
6. [Headings are the outline](#-headings-are-the-outline)
7. [Semantic elements inside content](#-semantic-elements-inside-content)
8. [Use the right interactive element](#-use-the-right-interactive-element)
9. [Div soup makeover](#-div-soup-makeover)
10. [ARIA: the backup plan](#-aria-the-backup-plan)
11. [Mistakes I actually made](#-mistakes-i-actually-made)
12. [Cheat sheet](#-cheat-sheet)
13. [Practice ideas](#-practice-ideas)
14. [Tools](#-tools)
15. [Related](#-related)

---

## 🧠 What "Semantic" Means

**Semantic HTML = choosing elements for what the content *means*, not how it looks.**

```html
<!-- Non-semantic: tells the browser nothing -->
<div class="top">
  <div class="menu">...</div>
</div>

<!-- Semantic: tells the browser exactly what this is -->
<header>
  <nav>...</nav>
</header>
```

Both can look identical after CSS. The difference is what **browsers, screen readers, search engines, and future me** can understand without guessing.

| Element type | Examples | Carries meaning? |
|---|---|---|
| 🟦 **Non-semantic** | `div`, `span` | ❌ None. Pure containers. |
| 🟩 **Semantic** | `header`, `nav`, `main`, `article`, `button`, `table`, `ul` | ✅ Yes. The name *is* the meaning. |

> 💡 The test: if I removed all CSS, would the page structure still make sense? Semantic HTML survives that test. Div soup doesn't.

---

## 🎯 Why It Matters

| Benefit | What it means in practice |
|---|---|
| ♿ **Accessibility** | Screen reader users can jump between landmarks (nav, main, footer) and headings instead of listening to everything |
| ⌨️ **Free behavior** | A `<button>` is keyboard-focusable and works with Enter/Space *for free*. A clickable `<div>` needs extra code to do the same. |
| 🔍 **Search engines** | Clear structure helps crawlers understand what's important |
| 🧹 **Maintainability** | `<footer>` is easier to find than the fifth nested `<div class="bottom-wrap">` |
| 📖 **Reader modes and tools** | Browsers can extract the `<article>` and strip the clutter |
| 🧩 **Better CSS and JS hooks** | Style `nav a` instead of inventing a class for everything |

---

## 🧱 The Page Layout Elements

The big structural elements, in a typical page:

```
┌────────────────────────────────────┐
│ <header>   logo, title, <nav>      │
├────────────────────────────────────┤
│ <main>                             │
│ ┌──────────────────┐ ┌───────────┐ │
│ │ <article>        │ │ <aside>   │ │
│ │  <section>…      │ │ sidebar,  │ │
│ │  <section>…      │ │ related   │ │
│ └──────────────────┘ └───────────┘ │
├────────────────────────────────────┤
│ <footer>   contact, copyright      │
└────────────────────────────────────┘
```

### The cast

| Element | Purpose | Rules and tips |
|---|---|---|
| `<header>` | Intro content or navigation aids for a page *or* a section | Can appear multiple times. Often holds logo, `h1`, and `nav`. |
| `<nav>` | **Major** navigation links | Not every group of links is a `nav`. Use it for main menus, tables of contents, and pagination. |
| `<main>` | The main, unique content of the page | **Only one visible `main` per page.** Don't put it inside `header`, `nav`, `footer`, `article`, or `aside`. |
| `<section>` | A themed group of content | Should have a heading. See [the section/article/div table](#-section-vs-article-vs-div). |
| `<article>` | Self-contained, reusable content | Blog post, news story, product card, forum comment |
| `<aside>` | Content related to, but separate from, the main flow | Sidebars, pull quotes, ads, "related posts" |
| `<footer>` | Closing info for a page *or* a section | Author, copyright, links, contact. Can also close an `article`. |
| `<address>` | Contact info for the nearest article or the page | Not for just any postal address |

### A clean page skeleton

```html
<body>
  <header>
    <h1>Whisker Weekly</h1>
    <nav aria-label="Main">
      <ul>
        <li><a href="#posts">Posts</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article id="posts">
      <h2>Why Cats Knock Things Off Tables</h2>
      <p>...</p>
    </article>

    <aside>
      <h2>Related reading</h2>
      <ul>...</ul>
    </aside>
  </main>

  <footer id="contact">
    <address>
      Email: <a href="mailto:hello@example.com">hello@example.com</a>
    </address>
    <p>&copy; 2026 Whisker Weekly</p>
  </footer>
</body>
```

---

## ⚖️ section vs article vs div

The trio I confused the most. Here's the decision table:

| | `<article>` | `<section>` | `<div>` |
|---|---|---|---|
| **Meaning** | A complete, standalone piece | A themed chunk of a larger whole | None |
| **Makes sense alone?** | ✅ Yes (could be syndicated or shared) | ❌ Not really, depends on its parent | n/a |
| **Needs a heading?** | Almost always | **Yes** (otherwise it's probably a `div`) | No |
| **Examples** | Blog post, comment, product card, news item | "Features," "Pricing," "FAQ" parts of a page | Wrapper for CSS grid, styling hook |

### The decision flow

```
Is it a self-contained piece that makes sense on its own?
├── YES → <article>
└── NO
    Is it a themed group that deserves a heading?
    ├── YES → <section>
    └── NO
        Is it just a wrapper for styling or layout?
        ├── YES → <div>
        └── NO → there's probably a more specific element (nav, aside, figure, ul…)
```

### Nesting is allowed both ways

```html
<!-- An article containing sections -->
<article>
  <h2>How to Train a Dragon</h2>
  <section>
    <h3>Step 1: Befriend it</h3>
    <p>...</p>
  </section>
  <section>
    <h3>Step 2: Don't get eaten</h3>
    <p>...</p>
  </section>
</article>

<!-- A section containing articles -->
<section>
  <h2>Latest posts</h2>
  <article>...</article>
  <article>...</article>
</section>
```

> ⚠️ **`div` is still allowed!** The goal isn't "never use `div`," it's "use it when nothing more meaningful fits." Layout wrappers for CSS are a perfectly good job for it.

---

## 🗺️ Landmarks and Screen Readers

Screen reader users can pull up a list of **landmarks** and jump straight to one. Semantic elements create them automatically.

| Element | Landmark role | Notes |
|---|---|---|
| `<header>` | `banner` | Only when it's the page-level header (not nested inside `article`/`section`) |
| `<nav>` | `navigation` | |
| `<main>` | `main` | |
| `<aside>` | `complementary` | |
| `<footer>` | `contentinfo` | Only when it's the page-level footer |
| `<section>` | `region` | **Only if it has an accessible name** (e.g. `aria-labelledby`) |
| `<form>` | `form` | Only if it has an accessible name |
| `<search>` | `search` | Newer element for search UI |

### Label repeated landmarks

If there's more than one `nav` on a page, tell them apart:

```html
<nav aria-label="Main">...</nav>
<nav aria-label="Footer">...</nav>
```

### Make a `section` a named region

```html
<section aria-labelledby="pricing-title">
  <h2 id="pricing-title">Pricing</h2>
  ...
</section>
```

---

## 🪜 Headings Are the Outline

Headings are not "big text." They are the **table of contents** of the page.

```html
<h1>Cat Care Guide</h1>
  <h2>Feeding</h2>
    <h3>Wet food</h3>
    <h3>Dry food</h3>
  <h2>Grooming</h2>
    <h3>Brushing</h3>
```

| Do ✅ | Don't ❌ |
|---|---|
| One `<h1>` describing the page | Multiple `<h1>`s for visual size |
| Go down one level at a time (`h2` → `h3`) | Skip from `h2` to `h4` |
| Choose heading level by **structure** | Choose heading level by **size** |
| Use CSS to change how a heading looks | Use `<h4>` because it's smaller |

> 🧠 The old HTML5 "document outline" idea (where `<h1>` resets inside every `<section>`) was **never implemented by browsers.** So don't rely on it. Keep heading levels consistent across the whole page.

**Quick self-test:** read only the headings out loud. If the page still makes sense, the structure is good.

---

## 🧩 Semantic Elements Inside Content

Semantics isn't just page layout. These smaller elements carry meaning too:

| Element | Use it for | Instead of |
|---|---|---|
| `<figure>` + `<figcaption>` | An image/diagram/code block with a caption | `<div>` + `<p>` |
| `<time datetime="2026-10-03">` | A date or time in machine-readable form | Plain text |
| `<mark>` | Highlighted/relevant text | `<span class="yellow">` |
| `<strong>` / `<em>` | Importance / stress | `<b>` / `<i>` for meaning |
| `<blockquote>` + `<cite>` | Quotes with sources | Indented `<p>` |
| `<abbr title="...">` | Abbreviations | Plain text |
| `<ul>` / `<ol>` | Lists of items (including menus) | A pile of `<div>`s or `<br>`s |
| `<dl>` / `<dt>` / `<dd>` | Term + description pairs | Bold text followed by a `<p>` |
| `<table>` + `<caption>`, `<th scope>` | **Tabular data** | A grid of `div`s |
| `<details>` + `<summary>` | Expand/collapse widget | A JS-powered `div` |
| `<dialog>` | Modal or popup | A `div` with `z-index` |
| `<address>` | Contact info for the page/article | `<p>` |
| `<code>`, `<kbd>`, `<samp>` | Code, keystrokes, output | `<span class="mono">` |

### Free interactivity with `<details>`

```html
<details>
  <summary>What does semantic mean?</summary>
  <p>Choosing elements by meaning, not by looks.</p>
</details>
```

No JavaScript, keyboard-accessible, and screen-reader friendly. All for free.

### `<table>` is for data, not layout

```html
<table>
  <caption>Exam results</caption>
  <thead>
    <tr><th scope="col">Student</th><th scope="col">Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Alex</td><td>54</td></tr>
  </tbody>
</table>
```

Tables for *data* are great. Tables for *page layout* are a 1999 habit. Use CSS (flexbox/grid) for layout.

---

## 👆 Use the Right Interactive Element

One of the most important semantic rules:

> **If it goes somewhere → `<a>`. If it does something → `<button>`.**

| Need | Use | Why |
|---|---|---|
| Navigate to another page or section | `<a href="...">` | Works with middle-click, "open in new tab," and shows the URL on hover |
| Trigger an action (submit, open menu, buy) | `<button type="button">` | Built-in keyboard support and focus |
| Submit a form | `<button type="submit">` or `<input type="submit">` | |
| A text field | `<input>` + `<label>` | |

### Why a clickable `div` is a trap

```html
<!-- ❌ Looks like a button, acts like nothing -->
<div class="btn" onclick="buy()">Buy Now</div>

<!-- ✅ Actually a button -->
<button type="button" class="btn">Buy Now</button>
```

The `div` version is missing: keyboard focus, Enter/Space activation, a screen reader announcing "button," and disabled-state support. The real button gives me all of that without writing a single extra line.

### Forms: labels are semantic too

```html
<label for="email">Email</label>
<input type="email" id="email" name="email" required>
```

Group related controls with `fieldset` + `legend`:

```html
<fieldset>
  <legend>How was your stay?</legend>
  <label><input type="radio" name="rating" value="good" required> Good</label>
  <label><input type="radio" name="rating" value="bad"> Bad</label>
</fieldset>
```

---

## 🧽 Div Soup Makeover

A before-and-after based on my own XYZ Bookstore mistake.

### ❌ Before (div soup)

```html
<div class="header">
  <h1>XYZ Bookstore</h1>
  <div class="cart"><button>View Cart</button></div>
</div>

<div class="card-container">
  <div class="card">
    <h2>Sally's SciFi Adventure</h2>
    <p>$9.99</p>
    <button>Buy Now</button>
  </div>
  <div class="card">
    <h2>Mystery of the Missing Sock</h2>
    <p>$7.99</p>
    <button>Buy Now</button>
  </div>
</div>
```

### ✅ After (semantic)

```html
<header>
  <h1>XYZ Bookstore</h1>
  <button type="button">View Cart</button>
</header>

<main>
  <h2>Featured books</h2>
  <div class="card-container">
    <article class="card">
      <h3>Sally's SciFi Adventure</h3>
      <p>$9.99</p>
      <button type="button" aria-label="Buy Sally's SciFi Adventure">Buy Now</button>
    </article>
    <article class="card">
      <h3>Mystery of the Missing Sock</h3>
      <p>$7.99</p>
      <button type="button" aria-label="Buy Mystery of the Missing Sock">Buy Now</button>
    </article>
  </div>
</main>
```

### What changed and why

| Change | Reason |
|---|---|
| `div.header` → `<header>` | Becomes the page `banner` landmark |
| Added `<main>` | Gives screen reader users a "skip to content" target |
| Cards → `<article>` | Each book is self-contained |
| Heading levels fixed (`h1` → `h2` → `h3`) | No skipped levels, a real outline |
| `type="button"` | Prevents accidental form submission |
| `aria-label` on "Buy Now" | Identical buttons now have unique names |
| Kept one `div.card-container` | It's *only* a layout wrapper, and that is a valid use of `div` |

---

## 🆘 ARIA: The Backup Plan

**ARIA** (Accessible Rich Internet Applications) adds extra accessibility info through attributes like `role`, `aria-label`, and `aria-expanded`.

### The First Rule of ARIA

> **Don't use ARIA if a native HTML element already does the job.**

| ❌ ARIA workaround | ✅ Native element |
|---|---|
| `<div role="button" tabindex="0">` | `<button>` |
| `<div role="navigation">` | `<nav>` |
| `<div role="main">` | `<main>` |
| `<span role="link">` | `<a href>` |
| `<div role="list">` | `<ul>` |

### When ARIA *is* the right tool

| Attribute | Use |
|---|---|
| `aria-label="..."` | Give an element a name when there's no visible text (icon buttons, repeated nav) |
| `aria-labelledby="id"` | Name an element using another element's text |
| `aria-describedby="id"` | Attach extra descriptive text (like form hints) |
| `aria-expanded="true/false"` | State of a collapsible control |
| `aria-current="page"` | Marks the current page link in a nav |
| `aria-hidden="true"` | Hide purely decorative things from screen readers |

> ⚠️ **Bad ARIA is worse than no ARIA.** It overrides the browser's built-in meaning. Use it carefully and only to fill real gaps.

---

## 💥 Mistakes I Actually Made

| # | Mistake | Why it hurts | The fix |
|---|---|---|---|
| 1 | Built the whole Bookstore from `div`s | No landmarks, no meaning | `header`, `main`, `article` |
| 2 | Left out `<main>` on several pages | Screen reader users can't skip to content | Wrap the unique content in one `<main>` |
| 3 | Mixed up `<head>` and `<header>` | Totally different jobs | `head` = invisible metadata, `header` = visible intro |
| 4 | Treated `<section>` as a fancy `div` | Section without a heading is an empty promise | Add a heading, or use `div` |
| 5 | Identical "Buy Now" buttons | Can't tell which book | Unique `aria-label` |
| 6 | Picked heading levels by size | Broken outline | Use CSS for size |
| 7 | Forgot `type` on buttons | Default `submit` can trigger a form | Always set `type` |
| 8 | Didn't think about `alt` on linked images | Link purpose unclear | Alt describes destination |

> 🧪 Each of these is now on my pre-flight checklist below.

---

## 🧾 Cheat Sheet

### Which element do I need?

| I'm building... | Use |
|---|---|
| Site logo + title + menu area | `<header>` |
| Main menu | `<nav>` > `<ul>` > `<li>` > `<a>` |
| The unique content of this page | `<main>` |
| A blog post, product card, comment | `<article>` |
| A themed block with a heading | `<section>` |
| A sidebar or "related" box | `<aside>` |
| Copyright, contact, links at the bottom | `<footer>` |
| An image with a caption | `<figure>` + `<figcaption>` |
| A date | `<time datetime="">` |
| A collapsible FAQ | `<details>` + `<summary>` |
| A modal popup | `<dialog>` |
| Data in rows and columns | `<table>` |
| An action | `<button>` |
| A destination | `<a>` |
| Just a wrapper for CSS | `<div>` |
| Just a hook inside a line of text | `<span>` |

### Pre-flight checklist ✅

- [ ] Exactly one `<main>`
- [ ] A page-level `<header>` and `<footer>` where it makes sense
- [ ] Menus are `<nav>` with a `<ul>` of links; multiple `nav`s are labelled
- [ ] Every `<section>` has a heading
- [ ] Each `<article>` would still make sense on its own
- [ ] Heading levels are in order, with no skips
- [ ] Links go places, buttons do things
- [ ] Every button has `type` and a clear (and unique) name
- [ ] Lists are real lists; tables are only for data
- [ ] Every form input has a `<label>`
- [ ] No ARIA where a native element would work
- [ ] The page still reads logically with CSS turned off

---

## 🎮 Practice Ideas

1. 🌱 **Label the wireframe.** Sketch a page on paper, then write the semantic element each box should be.
2. 🌱 **Div detox.** Take any old page of mine and replace every `div` that has a better option.
3. 🔧 **Rebuild the Bookstore.** Do the makeover above from scratch without peeking.
4. 🔧 **CSS off test.** Delete the stylesheet (or disable it in DevTools) and see whether the page still makes sense.
5. 🔧 **Heading audit.** Use a headings-outline extension on three real websites. Which ones are well structured?
6. 🚀 **Screen reader run.** Turn on NVDA (Windows), VoiceOver (Mac/iOS) or TalkBack (Android) and try navigating my own page by landmarks only.
7. 🚀 **Keyboard-only run.** Unplug the mouse. Can I reach and use everything with `Tab`, `Enter`, and `Space`?

---

## 🛠️ Tools

| Tool | What it's for |
|---|---|
| 🔍 **DevTools → Accessibility tab** | Shows the accessibility tree: what assistive tech actually "sees" |
| ♿ **Lighthouse** (in DevTools) | Quick accessibility and SEO score |
| 🧪 [axe DevTools](https://www.deque.com/axe/) | Finds accessibility issues automatically |
| 👁️ [WAVE](https://wave.webaim.org/) | Visual overlay of structure and errors |
| ✅ [W3C Validator](https://validator.w3.org/) | Catches invalid nesting and syntax |
| 📖 [MDN: HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) | The definitive list of every element |
| 📖 [MDN: ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) | When and how to use ARIA |

---

## 🔗 Related

- 📄 [`basics.md`](./basics.md): the skeleton this builds on
- 📝 [`forms.md`](./forms.md): labels, inputs, and validation
- ♿ [`accessibility.md`](./accessibility.md): the bigger accessibility picture
- 🖼️ [`media-and-links.md`](./media-and-links.md): images, audio, video, and paths
- 🧪 [`examples/`](./examples): the Cat Blog is my best semantic page so far; the Bookstore is the cautionary tale
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>Mark I gave the suit a frame. Mark II gives every part a purpose. 🦾</i></p>
