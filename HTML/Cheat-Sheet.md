# 🦾 HTML Cheat Sheet

> The whole Mark I to Mark V armor, folded into one reference.
> Open it, copy the snippet, ship the page, and be ready to bolt on CSS and JavaScript.

![Topic](https://img.shields.io/badge/topic-HTML5-E34F26?logo=html5&logoColor=white)
![Type](https://img.shields.io/badge/type-cheat%20sheet-purple)
![Covers](https://img.shields.io/badge/covers-basics%20%7C%20semantics%20%7C%20forms%20%7C%20a11y%20%7C%20media-blue)
![Next](https://img.shields.io/badge/next-CSS%20%2B%20JavaScript-yellow)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-lightgrey)

> 📚 This sheet condenses [`basics.md`](./basics.md), [`semantic-html.md`](./semantic-html.md), [`forms.md`](./forms.md), [`accessibility.md`](./accessibility.md) and [`media-and-links.md`](./media-and-links.md). For the "why" behind anything here, jump to the matching file.

---

## 🗂️ Table of Contents

1. [Starter template](#-starter-template)
2. [Element anatomy and syntax rules](#-element-anatomy-and-syntax-rules)
3. [Tag reference by category](#-tag-reference-by-category)
4. [Attributes reference](#-attributes-reference)
5. [Paths, links and URLs](#-paths-links-and-urls)
6. [Images and media](#-images-and-media)
7. [Forms](#-forms)
8. [Tables](#-tables)
9. [Semantic layout](#-semantic-layout)
10. [Accessibility essentials](#-accessibility-essentials)
11. [Snippet library](#-snippet-library)
12. [Entities and special characters](#-entities-and-special-characters)
13. [Debugging guide](#-debugging-guide)
14. [Top mistakes I made](#-top-mistakes-i-made)
15. [Master checklists](#-master-checklists)
16. [The next-step kit](#-the-next-step-kit)
17. [Readiness self-test](#-readiness-self-test)
18. [Roadmap](#-roadmap)
19. [Tools and references](#-tools-and-references)

---

## 🚀 Starter Template

Copy me into every new project.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Descriptive Page Title</title>
    <meta name="description" content="One sentence about this page." />
    <link rel="icon" href="favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to main content</a>

    <header>
      <h1>Site Title</h1>
      <nav aria-label="Main">
        <ul>
          <li><a href="index.html" aria-current="page">Home</a></li>
          <li><a href="about.html">About</a></li>
        </ul>
      </nav>
    </header>

    <main id="main">
      <h2>Page Heading</h2>
      <p>Content goes here.</p>
    </main>

    <footer>
      <p>&copy; 2026 My Name</p>
    </footer>

    <script src="js/app.js" defer></script>
  </body>
</html>
```

| Line | Why it's there |
|---|---|
| `<!DOCTYPE html>` | Standards mode |
| `lang="en"` | Screen reader pronunciation, translation |
| `charset="UTF-8"` | No garbled text; keep it near the top of `<head>` |
| `viewport` | Correct layout on phones (and works with zoom) |
| `<title>` | Tab label, bookmarks, search results |
| `rel="stylesheet"` | Hook for CSS (next step) |
| `defer` on script | Runs after the HTML is parsed (next step) |
| Skip link | Keyboard users can skip the menu |

---

## 🧬 Element Anatomy and Syntax Rules

```html
<p class="intro" id="top">Hello, <strong>world</strong>!</p>
<!-- tag  attributes        content            closing tag -->
```

| Rule | Detail |
|---|---|
| Tags are lowercase | `<p>`, not `<P>` |
| Close in reverse order | `<p><em>text</em></p>` ✅ / `<p><em>text</p></em>` ❌ |
| Quote attribute values | Double quotes: `class="card"` |
| Never double up quotes | `cite="url""` is a bug |
| Void elements have no closing tag | `br` `hr` `img` `input` `meta` `link` `source` `track` |
| Boolean attributes: presence = true | `disabled="false"` is **still** disabled |
| `id` is unique, `class` is reusable | One `id` per page; many elements can share a class |
| Whitespace collapses | Many spaces/newlines render as one space |
| Comments | `<!-- not shown, but visible in View Source -->` |
| Indent consistently | Format on save (Prettier) |

---

## 📚 Tag Reference by Category

### 🏗️ Document structure

| Tag | Purpose |
|---|---|
| `<html>` | Root element (`lang` goes here) |
| `<head>` | Invisible metadata |
| `<body>` | Everything visible |
| `<title>` | Page title |
| `<meta>` | Charset, viewport, description |
| `<link>` | Link to CSS, favicon |
| `<script>` | JavaScript |
| `<style>` | Embedded CSS |
| `<noscript>` | Fallback if JS is off |

### 🏛️ Page sections (semantic)

| Tag | Use for |
|---|---|
| `<header>` | Intro/branding for page or section |
| `<nav>` | Major navigation |
| `<main>` | The page's unique content (**one per page**) |
| `<section>` | Themed group **with a heading** |
| `<article>` | Self-contained piece (post, card, comment) |
| `<aside>` | Related side content |
| `<footer>` | Closing info for page or section |
| `<address>` | Contact info |
| `<div>` | Generic block wrapper (last resort) |
| `<span>` | Generic inline wrapper (last resort) |

### 🔤 Text

| Tag | Use for |
|---|---|
| `<h1>`-`<h6>` | Headings (one `h1`, no skipped levels) |
| `<p>` | Paragraph |
| `<br>` | Line break (inside content) |
| `<hr>` | Thematic break |
| `<strong>` | Important text |
| `<em>` | Stressed emphasis |
| `<b>` / `<i>` | Style-only bold/italic |
| `<mark>` | Highlight |
| `<small>` | Fine print |
| `<del>` / `<ins>` | Removed / added text |
| `<sub>` / `<sup>` | Subscript / superscript |
| `<abbr title="">` | Abbreviation |
| `<time datetime="">` | Date/time |
| `<q>` | Inline quote |
| `<blockquote cite="">` | Block quote |
| `<cite>` | Title of a work |
| `<code>` | Inline code |
| `<pre>` | Preserve whitespace |
| `<kbd>` / `<samp>` | Keys / program output |

### 📋 Lists

| Tag | Use for |
|---|---|
| `<ul>` + `<li>` | Unordered list |
| `<ol>` + `<li>` | Ordered list (`start`, `reversed`, `type`) |
| `<dl>` `<dt>` `<dd>` | Term + definition |

### 🔗 Links and media

| Tag | Use for |
|---|---|
| `<a href>` | Links |
| `<img>` | Image (needs `alt`) |
| `<figure>` + `<figcaption>` | Captioned media |
| `<picture>` + `<source>` | Format/crop choices |
| `<svg>` | Vector graphics |
| `<audio>` | Sound (`controls`) |
| `<video>` | Video (`controls`, `poster`) |
| `<track>` | Captions/subtitles |
| `<iframe title>` | Embedded page |
| `<canvas>` | Drawing surface for JS |

### 📝 Forms

| Tag | Use for |
|---|---|
| `<form>` | Form wrapper (`action`, `method`) |
| `<label for>` | Names a control |
| `<input type>` | Most controls |
| `<textarea>` | Multi-line text |
| `<select>` + `<option>` / `<optgroup>` | Dropdowns |
| `<datalist>` | Suggestions for an input |
| `<button type>` | Buttons |
| `<fieldset>` + `<legend>` | Group related controls |
| `<output>` | Result of a calculation |
| `<progress>` / `<meter>` | Progress / measurement |

### 📊 Tables

| Tag | Use for |
|---|---|
| `<table>` | Table |
| `<caption>` | Table title |
| `<thead>` `<tbody>` `<tfoot>` | Row groups |
| `<tr>` | Row |
| `<th scope>` | Header cell |
| `<td>` | Data cell |
| `<colgroup>` / `<col>` | Column styling hooks |

### 🧩 Interactive

| Tag | Use for |
|---|---|
| `<details>` + `<summary>` | Expand/collapse, no JS needed |
| `<dialog>` | Modal or popup |
| `<template>` | Hidden markup for JS to clone |
| `<slot>` | Web components (later) |

---

## 🏷️ Attributes Reference

### 🌍 Global attributes (any element)

| Attribute | Purpose | Example |
|---|---|---|
| `id` | Unique ID | `id="menu"` |
| `class` | Reusable label(s) | `class="card featured"` |
| `lang` | Language of content | `lang="ar"` |
| `dir` | Text direction | `dir="rtl"` |
| `title` | Tooltip | `title="Info"` |
| `hidden` | Hide element | `<p hidden>` |
| `style` | Inline CSS (avoid) | `style="color:red"` |
| `tabindex` | Focus order | `0` or `-1` only |
| `data-*` | Custom data for JS | `data-book-id="42"` |
| `aria-*` / `role` | Accessibility extras | `aria-label="Close"` |
| `contenteditable` | User-editable | `contenteditable="true"` |
| `draggable` | Draggable | `draggable="true"` |
| `translate` | Allow/deny translation | `translate="no"` |

### 🔗 Link attributes

| Attribute | Purpose |
|---|---|
| `href` | Destination |
| `target` | `_self` (default) / `_blank` |
| `rel` | `noopener noreferrer`, `nofollow`, `sponsored`, `ugc` |
| `download` | Download instead of navigate |
| `hreflang` | Target language |

### 🖼️ Image attributes

| Attribute | Purpose |
|---|---|
| `src` | File (required) |
| `alt` | Text alternative (required) |
| `width` / `height` | Reserve space |
| `loading` | `lazy` / `eager` |
| `decoding` | `async` |
| `fetchpriority` | `high` for the hero image |
| `srcset` / `sizes` | Responsive sizes |

### 🎬 Media attributes

| Attribute | Applies to | Purpose |
|---|---|---|
| `controls` | audio, video | Show player UI |
| `autoplay` | audio, video | Start automatically (avoid) |
| `muted` | audio, video | Start silent |
| `loop` | audio, video | Repeat |
| `preload` | audio, video | `none` / `metadata` / `auto` |
| `poster` | video | Preview image |
| `playsinline` | video | iPhone inline playback |

### 📝 Form attributes

| Attribute | Purpose |
|---|---|
| `name` | **Key sent to the server** (no name = not sent) |
| `id` | Link for `<label for>` |
| `value` | Default value / value sent |
| `placeholder` | Format hint (not a label) |
| `required` | Must be filled |
| `disabled` | Not editable, **not submitted** |
| `readonly` | Not editable, **is submitted** |
| `min` `max` `step` | Number/date limits |
| `minlength` `maxlength` | Text length limits |
| `pattern` | Regex (must match whole value) |
| `autocomplete` | Autofill hint |
| `autofocus` | Focus on load (use sparingly) |
| `multiple` | Several values (email, file, select) |
| `accept` | Allowed file types |
| `list` | Link to a `<datalist>` |
| `inputmode` | Mobile keyboard hint |
| `checked` / `selected` | Pre-select |
| `novalidate` / `formnovalidate` | Turn off built-in validation |

### 🪪 `<input type>` values

| Group | Types |
|---|---|
| Text | `text` `email` `password` `tel` `url` `search` |
| Numbers | `number` `range` |
| Date/time | `date` `time` `datetime-local` `month` `week` |
| Choices | `checkbox` `radio` `color` `file` |
| Hidden | `hidden` |
| Buttons | `submit` `reset` `button` |

---

## 🧭 Paths, Links and URLs

```
https://www.example.com:443/blog/post.html?id=7&sort=new#comments
└scheme┘ └────host─────┘└port┘└────path────┘└──query──┘└fragment┘
```

| `href` type | Example |
|---|---|
| Absolute | `https://example.com/page` |
| Relative (same folder) | `about.html` |
| Subfolder | `pages/contact.html` |
| Parent folder | `../index.html` |
| Root-relative | `/images/logo.png` |
| In-page | `#contact` |
| Other page + spot | `faq.html#shipping` |
| Email | `mailto:me@example.com?subject=Hello%20there` |
| Phone | `tel:+15555555555` |

**Mnemonic:** `./` here · `../` up one · `/` site root.

**File names:** lowercase, hyphens, no spaces, no apostrophes (`can-t-stay-down.mp3`, not `can't-stay-down.mp3`). Many servers are case-sensitive.

```html
<!-- External link, done right -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  Example (opens in a new tab)
</a>

<!-- Download -->
<a href="report.pdf" download>Download the report (PDF, 2 MB)</a>

<!-- Link wrapping an image: alt describes the destination -->
<a href="/gallery.html"><img src="cats.jpg" alt="View the cat photo gallery"></a>
```

**Link text:** ✅ "Read the 2026 report" · ❌ "Click here". Keep spaces *outside* the `<a>`.

---

## 🖼️ Images and Media

```html
<!-- Basic image -->
<img src="images/cat.jpg" alt="An orange cat asleep on a windowsill"
     width="800" height="533" loading="lazy">

<!-- Decorative image -->
<img src="divider.png" alt="" width="600" height="20">

<!-- Captioned figure -->
<figure>
  <img src="lasagna.jpg" alt="A slice of lasagna on a plate" width="600" height="400">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>

<!-- Responsive sizes -->
<img src="cat-800.jpg"
     srcset="cat-400.jpg 400w, cat-800.jpg 800w, cat-1600.jpg 1600w"
     sizes="(max-width: 600px) 100vw, 800px"
     alt="An orange cat on a windowsill" width="800" height="533">

<!-- Modern formats with fallback -->
<picture>
  <source srcset="cat.avif" type="image/avif">
  <source srcset="cat.webp" type="image/webp">
  <img src="cat.jpg" alt="An orange cat on a windowsill" width="800" height="533">
</picture>
```

```html
<!-- Audio -->
<audio controls preload="metadata">
  <source src="audio/song.mp3" type="audio/mpeg">
  <source src="audio/song.ogg" type="audio/ogg">
  <a href="audio/song.mp3">Download the track</a>
</audio>

<!-- Video with poster and captions -->
<video controls width="640" height="360" poster="images/poster.jpg"
       preload="metadata" playsinline>
  <source src="video/demo.mp4"  type="video/mp4">
  <source src="video/demo.webm" type="video/webm">
  <track kind="captions" src="video/captions-en.vtt" srclang="en" label="English" default>
  <a href="video/demo.mp4">Download the video</a>
</video>

<!-- Safe embed -->
<iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
        title="Intro to HTML tutorial" width="560" height="315"
        loading="lazy" allowfullscreen></iframe>
```

### Alt text decision table

| Image is... | Alt |
|---|---|
| Informative | Describe what matters |
| Decorative | `alt=""` |
| Inside a link | Describe the destination |
| A logo | Company name |
| Text in an image | Same words |
| Chart | Takeaway + longer description nearby |

### Format picker

| Content | Format |
|---|---|
| Photo | WebP / AVIF (JPEG fallback) |
| Logo / icon | SVG |
| Screenshot | PNG / WebP |
| Short animation | Video or animated WebP (not GIF) |
| Audio | MP3 / AAC |
| Video | MP4 (H.264) + optional WebM |

---

## 📝 Forms

### The skeleton

```html
<form action="/submit" method="post">
  <fieldset>
    <legend>About you</legend>

    <p>
      <label for="name">Name</label><br>
      <input type="text" id="name" name="name" autocomplete="name" required>
    </p>

    <p>
      <label for="email">Email</label><br>
      <input type="email" id="email" name="email" autocomplete="email" required>
    </p>
  </fieldset>

  <button type="submit">Send</button>
</form>
```

### Control snippets

```html
<!-- Radio group (one choice) -->
<fieldset>
  <legend>Would you recommend us?</legend>
  <label><input type="radio" name="recommend" value="yes" required> Yes</label>
  <label><input type="radio" name="recommend" value="no"> No</label>
</fieldset>

<!-- Checkbox group (many choices) -->
<fieldset>
  <legend>What did you like?</legend>
  <label><input type="checkbox" name="liked" value="food"> Food</label>
  <label><input type="checkbox" name="liked" value="staff"> Staff</label>
</fieldset>

<!-- Dropdown with a blank first option (no default bias) -->
<label for="rating">Rating</label>
<select id="rating" name="rating" required>
  <option value="">Choose one…</option>
  <option value="5">Excellent</option>
  <option value="4">Good</option>
</select>

<!-- Textarea -->
<label for="msg">Message</label>
<textarea id="msg" name="msg" rows="5" cols="40" maxlength="500"></textarea>

<!-- Suggestions + free typing -->
<input list="cities" name="city" id="city">
<datalist id="cities"><option value="Riyadh"><option value="Jeddah"></datalist>

<!-- ZIP code with a pattern -->
<input type="text" name="zip" pattern="[0-9]{5}" inputmode="numeric"
       title="Five digits, like 90210">

<!-- Number with limits -->
<input type="number" name="age" min="3" max="120">

<!-- File upload (form needs method="post" enctype="multipart/form-data") -->
<input type="file" name="photo" accept="image/*">
```

### Forms quick facts

| Fact | Detail |
|---|---|
| Only `name` is sent | `id` is not submitted |
| Not submitted | Unchecked boxes/radios, `disabled` controls, controls without `name` |
| Radios group by | Same `name` |
| `<button>` default type | `submit`. Always write the `type`. |
| GET | Data in URL; for searches |
| POST | Data in body; for logins, signups, changes |
| Placeholder | A hint, **never** a label |
| `number` type | For quantities only, not phone/ZIP/card numbers |
| Validation | Browser checks are UX, **not security**; the server must validate again |
| Autofill tokens | `name` `email` `tel` `street-address` `postal-code` `username` `current-password` `new-password` `one-time-code` |

### Validation CSS hooks

| Selector | Matches |
|---|---|
| `:required` / `:optional` | By requirement |
| `:valid` / `:invalid` | Current validity |
| `:user-invalid` | Invalid after the user interacted |
| `:focus-visible` | Keyboard focus |
| `:disabled` | Disabled controls |

---

## 📊 Tables

```html
<table>
  <caption>Exam results, Term 1</caption>
  <thead>
    <tr><th scope="col">Student</th><th scope="col">Score</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Alex</th><td>54</td></tr>
    <tr><th scope="row">Sam</th><td>92</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Average</th><td>73</td></tr>
  </tfoot>
</table>
```

| Rule | Why |
|---|---|
| Tables are for **data**, not layout | Use CSS flexbox/grid for layout |
| `caption` + `scope` | Screen readers link headers to cells |
| `colspan` / `rowspan` | Merge cells (use sparingly) |
| Wide tables | Wrap in a scrolling container on mobile |

---

## 🏛️ Semantic Layout

```
┌────────────────────────────────────┐
│ <header>   logo, h1, <nav>         │
├────────────────────────────────────┤
│ <main>                             │
│ ┌──────────────────┐ ┌───────────┐ │
│ │ <article>        │ │ <aside>   │ │
│ │  <section>…      │ │ related   │ │
│ └──────────────────┘ └───────────┘ │
├────────────────────────────────────┤
│ <footer>   contact, copyright      │
└────────────────────────────────────┘
```

### Which container?

```
Self-contained and reusable on its own?   → <article>
Themed group with a heading?              → <section>
Related side content?                     → <aside>
Major links?                              → <nav>
Just a wrapper for styling?               → <div>
```

### Landmark map

| Element | Landmark |
|---|---|
| `header` (page-level) | banner |
| `nav` | navigation |
| `main` | main |
| `aside` | complementary |
| `footer` (page-level) | contentinfo |
| `section` with a name | region |
| `form` with a name | form |

### Links vs buttons

> **Goes somewhere → `<a>`. Does something → `<button type="button">`.**

### Headings

- One `<h1>`. Go down one level at a time. Pick by **structure**, never by size.
- Test: read only the headings. Does the page still make sense?

---

## ♿ Accessibility Essentials

### 🟢 Quick wins

| Effort | Action |
|---|---|
| 5 seconds | `lang`, descriptive `<title>`, viewport |
| 1 minute | `alt` on every image, `type` on every button |
| 5 minutes | Landmarks (`header` `nav` `main` `footer`) |
| 10 minutes | Heading order, label on every input |
| 30 minutes | Skip link, visible focus, table `scope` |
| 1 hour+ | Captions/transcripts, screen reader pass |

### Key rules

| Rule | Detail |
|---|---|
| Contrast | Text 4.5:1 · large text and UI 3:1 |
| Never color alone | Add text/icons |
| Keyboard | Everything reachable and usable; never remove focus outlines without a replacement |
| `tabindex` | Only `0` or `-1`; never positive |
| Zoom | Allow it; works at 200% and 320px width |
| Motion | Respect `prefers-reduced-motion` |
| Media | Captions for video, transcripts for audio, no autoplay with sound |
| Touch targets | At least 24×24 CSS px (about 44px comfortable) |

### ARIA in 30 seconds

> **First rule: don't use ARIA if a native element does the job.**

| Need | Use |
|---|---|
| Name with no visible text | `aria-label="Close"` |
| Name from other text | `aria-labelledby="id"` |
| Extra hint | `aria-describedby="id"` |
| Toggle state | `aria-expanded="true/false"` |
| Current page link | `aria-current="page"` |
| Hide decoration | `aria-hidden="true"` (never on focusable items) |
| Polite message | `role="status"` |
| Urgent message | `role="alert"` |

### Hiding techniques

| Technique | Visible | Screen reader | Focusable |
|---|---|---|---|
| `display:none` / `hidden` | ❌ | ❌ | ❌ |
| `aria-hidden="true"` | ✅ | ❌ | ✅ (careful) |
| `.sr-only` class | ❌ | ✅ | depends |

---

## 🧰 Snippet Library

Copy-paste building blocks.

### Skip link

```html
<a class="skip-link" href="#main">Skip to main content</a>
```
```css
.skip-link { position: absolute; left: -9999px; }
.skip-link:focus { left: 1rem; top: 1rem; background: #fff; padding: .5rem 1rem; z-index: 1000; }
```

### Screen-reader-only text

```css
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
```

### Card

```html
<article class="card">
  <img src="book.jpg" alt="Cover of Sally's SciFi Adventure" width="300" height="400" loading="lazy">
  <h3>Sally's SciFi Adventure</h3>
  <p class="price">$9.99</p>
  <button type="button" aria-label="Buy Sally's SciFi Adventure">Buy Now</button>
</article>
```

### Navigation with current page

```html
<nav aria-label="Main">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

### Accordion (no JavaScript)

```html
<details>
  <summary>What is semantic HTML?</summary>
  <p>Choosing elements by meaning, not by looks.</p>
</details>
```

### Modal dialog

```html
<button type="button" id="open">Open</button>

<dialog id="modal">
  <h2>Hello</h2>
  <p>This is a modal.</p>
  <button type="button" id="close">Close</button>
</dialog>
```
```js
document.querySelector("#open").addEventListener("click", () => modal.showModal());
document.querySelector("#close").addEventListener("click", () => modal.close());
```

### Contact block

```html
<address>
  Email: <a href="mailto:hello@example.com">hello@example.com</a><br>
  Phone: <a href="tel:+15555555555">+1 555 555 5555</a>
</address>
```

### Quote with attribution

```html
<figure>
  <blockquote cite="https://example.com/source">
    <p>Quote text here.</p>
  </blockquote>
  <figcaption>— Author Name, <cite>Title of the Work</cite></figcaption>
</figure>
```

### Form error message

```html
<label for="email">Email</label>
<input type="email" id="email" name="email" aria-invalid="true" aria-describedby="email-err">
<p id="email-err" role="alert">Enter an email like name@example.com.</p>
```

### Live status message

```html
<p role="status" id="cart-msg"></p>
```

### Responsive 16:9 embed

```css
.video-wrapper iframe { width: 100%; height: auto; aspect-ratio: 16 / 9; border: 0; }
```

### Basic responsive reset (CSS preview)

```css
*, *::before, *::after { box-sizing: border-box; }
img, video { max-width: 100%; height: auto; }
```

---

## 🔣 Entities and Special Characters

| Character | Entity | Notes |
|---|---|---|
| `<` | `&lt;` | Always escape in text |
| `>` | `&gt;` | |
| `&` | `&amp;` | |
| `"` | `&quot;` | Inside attribute values |
| (space) | `&nbsp;` | Non-breaking space, sparingly |
| `©` | `&copy;` | |
| `®` | `&reg;` | |
| `™` | `&trade;` | |
| `—` | `&mdash;` | |
| `–` | `&ndash;` | |
| `…` | `&hellip;` | |
| `€` | `&euro;` | |

With `charset="UTF-8"` you can usually type most characters directly.

---

## 🐞 Debugging Guide

| Symptom | Likely cause | Fix |
|---|---|---|
| Page looks tiny on a phone | No viewport meta | Add `<meta name="viewport" ...>` |
| Image doesn't show | Wrong path or case; file not saved in that folder | Check the path with `./` `../`; match case exactly |
| Link goes to the wrong place | Relative path from the wrong file | Count folder levels |
| Link jumps to top of page | `href="#"` placeholder | Real URL, or use `<button>` |
| `#section` link does nothing | `id` missing or misspelled | `id` must match exactly |
| Form data doesn't arrive | Missing `name` attributes | Add `name` to every control |
| Label click doesn't focus input | `for` ≠ `id` | Make them match |
| Radios both selectable | Different `name` values | Same `name` for the group |
| Form submits unexpectedly | `<button>` with no `type` | `type="button"` |
| Layout is broken after an edit | Unclosed or misnested tag | Validator + indent |
| Strange text characters (Ã©) | Missing charset or file not UTF-8 | `charset="UTF-8"` + save as UTF-8 |
| Audio/video won't play | Unsupported format or missing `type` | MP3/MP4 + correct `type` |
| Nothing changes after editing | Browser cache or wrong file open | Hard refresh `Ctrl+Shift+R` |
| Spaces/line breaks ignored | HTML collapses whitespace | Use CSS or `<pre>` |
| Everything runs together unstyled | Inputs are inline by default | Wrap in `<p>`/`<div>` (CSS later) |

### DevTools survival kit

| Shortcut | Does |
|---|---|
| `F12` / `Ctrl+Shift+I` | Open DevTools |
| `Ctrl+Shift+C` | Inspect an element |
| `Ctrl+U` | View raw source |
| **Elements tab** | See the live DOM, edit HTML/CSS in place |
| **Network tab** | Which files loaded, failed, or were slow; what forms send |
| **Console tab** | JavaScript errors |
| **Accessibility pane** | See name/role/state the screen reader gets |
| **Lighthouse** | Accessibility and performance audit |

---

## 💥 Top Mistakes I Made

| # | Mistake | Fix |
|---|---|---|
| 1 | Doubled quote: `cite="url""` | One closing quote; run the validator |
| 2 | No viewport meta tag | Put it in my starter template |
| 3 | `<div>` for everything | `header` `nav` `main` `article` `footer` |
| 4 | `<button>` without `type` | Always `type="button"` or `"submit"` |
| 5 | Identical "Buy Now" buttons | Unique `aria-label` |
| 6 | Linked image alt described the picture | Describe the destination |
| 7 | Space inside link text | Move the space outside `<a>` |
| 8 | Skipped captions on video | `<track kind="captions">` |
| 9 | Pre-selected "Excellent" in dropdowns | Blank first `<option value="">` |
| 10 | Radios not `required` | Add `required` to the group |
| 11 | Forgot `scope` on table headers | `scope="col"` / `scope="row"` |
| 12 | Messy file names (apostrophes, caps) | lowercase-with-hyphens |
| 13 | `.mov` as the only video | MP4 (+ WebM) |
| 14 | Inconsistent indentation | Prettier, format on save |
| 15 | Treated ARIA as magic | Native element first |

> 🧪 Mistakes aren't failures. They're the damage report that makes the next suit better.

---

## ✅ Master Checklists

### Before I call a page done

**Document**
- [ ] `<!DOCTYPE html>`, `lang`, `charset`, `viewport`, unique `<title>`
- [ ] No parser errors in the [W3C validator](https://validator.w3.org/)
- [ ] Consistent indentation

**Structure**
- [ ] One `<main>`; `header`, `nav`, `footer` where they make sense
- [ ] One `<h1>`; no skipped heading levels
- [ ] Every `<section>` has a heading
- [ ] `div`/`span` only where nothing better fits
- [ ] Lists are real lists; tables only for data

**Content**
- [ ] Every `<img>` has `alt` (empty if decorative), `width`, `height`
- [ ] Link text works out of context; `_blank` links have `rel` and a warning
- [ ] No `href="#"` placeholders
- [ ] File names lowercase-hyphenated; paths verified

**Forms**
- [ ] Every control has `name` and a connected `<label>`
- [ ] Right `type`; `required`/`min`/`max`/`pattern` where useful
- [ ] Radios/checkboxes in `fieldset` + `legend`
- [ ] No misleading defaults; `autocomplete` on personal fields
- [ ] Every `<button>` has `type` and a clear name

**Media**
- [ ] `controls` on audio/video; fallback content inside
- [ ] Captions or transcripts; no autoplay with sound
- [ ] `<iframe>` has a `title`
- [ ] I have the right to use every asset

**Accessibility**
- [ ] Keyboard-only run passes; focus is visible
- [ ] Contrast checked; color is never the only signal
- [ ] Zoom to 200% works
- [ ] Lighthouse / axe has no serious issues

---

## 🧰 The Next-Step Kit

Everything HTML gives me so CSS and JavaScript (or another language) have something solid to build on.

### 🎨 Ready for CSS

**1. Connect the stylesheet**

```html
<link rel="stylesheet" href="css/style.css">
```

Put it in `<head>`. Multiple stylesheets are fine; later ones win ties.

**2. Make the HTML "selectable"**

CSS finds elements through selectors, so my HTML is the targeting system:

| HTML I wrote | CSS selector | Example |
|---|---|---|
| `<p>` | Element | `p { line-height: 1.6; }` |
| `class="card"` | Class | `.card { padding: 1rem; }` |
| `id="main"` | ID | `#main { max-width: 60rem; }` |
| `<nav> … <a>` | Descendant | `nav a { text-decoration: none; }` |
| `type="email"` | Attribute | `input[type="email"] { … }` |
| `:focus-visible` | Pseudo-class | `a:focus-visible { outline: 3px solid; }` |
| `:user-invalid` | Pseudo-class | `input:user-invalid { border-color: #c00; }` |
| `li:first-child` | Structural | `li:first-child { font-weight: 700; }` |

**3. Concepts to learn first**

| Concept | One-liner |
|---|---|
| 📦 **Box model** | Every element is a box: content + padding + border + margin. Set `box-sizing: border-box`. |
| 🧱 **Block vs inline** | Becomes `display: block / inline / inline-block / flex / grid / none` |
| 🎚️ **Cascade and specificity** | Later rules win ties; `#id` beats `.class` beats `element` |
| 🧬 **Inheritance** | Some properties (color, font) pass to children |
| 📏 **Units** | `rem` for type, `%`/`fr`/`vw` for layout, `px` for borders |
| 🧲 **Flexbox** | One-dimensional layout (nav bars, card rows) |
| 🧮 **Grid** | Two-dimensional layout (page layouts, galleries) |
| 📱 **Media queries** | `@media (min-width: 40rem) { … }` for responsive design |
| 🎨 **Custom properties** | `--brand: #e34f26; color: var(--brand);` |
| 🌓 **User preferences** | `prefers-color-scheme`, `prefers-reduced-motion` |

**4. HTML habits that make CSS easier**

- Use **semantic elements** as hooks: `header nav`, `main article`, `footer p`.
- Name classes by **purpose**, not looks: `.card`, `.price`, not `.red-big`.
- Keep the DOM order logical; CSS can rearrange visually, but screen readers and keyboards follow the HTML.
- Wrap label/input pairs in a `<div>`/`<p>` so each can be laid out as a unit.
- Avoid inline `style`; use classes.
- Keep `width`/`height` on images, plus `max-width: 100%; height: auto;`.

**5. First CSS files to write**

```css
/* css/style.css */
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
  --brand: #e34f26;
}

*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
  color: var(--text);
  background: var(--bg);
}

img, video { max-width: 100%; height: auto; }

a:focus-visible, button:focus-visible, input:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}
```

---

### ⚡ Ready for JavaScript

**1. Connect the script**

```html
<script src="js/app.js" defer></script>
```

| Option | Behavior | Use |
|---|---|---|
| `defer` | Downloads in parallel, runs **after** HTML is parsed, in order | ✅ Default choice (put in `<head>` or end of `<body>`) |
| `async` | Runs as soon as downloaded, any order | Independent scripts (analytics) |
| `type="module"` | Modern ES modules; deferred by default | Larger projects |
| None | Blocks parsing | Avoid |

**2. The DOM: my HTML as a tree**

The browser turns my HTML into objects (the **DOM**). JavaScript reads and changes it:

```js
const title = document.querySelector("h1");        // find one element
const cards = document.querySelectorAll(".card");  // find many
title.textContent = "New title";                   // change text
cards[0].classList.add("featured");                // change classes
```

**3. HTML hooks JavaScript uses**

| Hook | HTML | JS |
|---|---|---|
| `id` | `<button id="open">` | `document.getElementById("open")` |
| `class` | `<li class="item">` | `querySelectorAll(".item")` |
| `data-*` | `<button data-book-id="42">` | `button.dataset.bookId` |
| `name` | `<input name="email">` | `form.elements.email.value` |
| `aria-*` state | `aria-expanded="false"` | `setAttribute("aria-expanded", "true")` |
| `hidden` | `<ul id="menu" hidden>` | `menu.hidden = false` |
| `<template>` | `<template id="row">…</template>` | `row.content.cloneNode(true)` |

**4. Events: reacting to the user**

```html
<button type="button" id="buy" data-book-id="42">Buy Now</button>
<p role="status" id="msg"></p>
```

```js
const buy = document.querySelector("#buy");
const msg = document.querySelector("#msg");

buy.addEventListener("click", () => {
  msg.textContent = `Added book ${buy.dataset.bookId} to your cart`;
});
```

| Event | Fires when |
|---|---|
| `click` | Mouse click, tap, Enter/Space on a button |
| `submit` | A form is submitted |
| `input` | A field's value changes as the user types |
| `change` | A field is committed (blur, select change) |
| `keydown` | A key is pressed |
| `DOMContentLoaded` | HTML is parsed (not needed with `defer`) |

**5. Forms and JS together**

```js
const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();                 // stop the page reload
  const data = new FormData(form);        // collects every control with a name
  console.log(Object.fromEntries(data));  // { name: "...", email: "..." }
});
```

This is why `name` attributes matter: `FormData` only sees controls that have one.

**6. JavaScript must keep my HTML accessible**

| Do ✅ | Why |
|---|---|
| Use real `<button>`s for actions | Keyboard support for free |
| Update `aria-expanded` / `aria-current` when state changes | Screen readers hear the change |
| Announce updates in a `role="status"` region | Dynamic changes get read out |
| Manage focus after opening/closing a dialog | Keyboard users don't get lost |
| Prefer `textContent` over `innerHTML` | Avoids injecting unsafe HTML (XSS) |
| Don't remove native behavior without replacing it | Don't break links or forms |

**7. JS concepts to learn first**

| Concept | Why |
|---|---|
| Variables (`const`, `let`) | Storing values |
| Types and operators | Numbers, strings, booleans, arrays, objects |
| Functions and arrow functions | Reusable behavior |
| Conditionals and loops | Decisions and repetition |
| DOM selection and manipulation | Connects to my HTML |
| Events | Makes the page interactive |
| Arrays and objects (methods like `map`, `filter`) | Working with data |
| `fetch` and JSON | Talking to servers and APIs |
| Debugging with Console and breakpoints | Fixing my own mistakes |

---

### 🐍 Ready for Python, SQL, or another language

HTML is the **universal output format** of the web. Whatever the backend language, it ends up sending HTML (or JSON that JavaScript turns into HTML).

| Bridge | What HTML already taught me |
|---|---|
| 📮 **Forms → server** | `name="email"` becomes the **key** the backend reads. `method` and `action` decide how and where data travels. |
| 🧩 **Templates** | Backends fill HTML with data, e.g. Python (Flask/Jinja): `<h1>{{ title }}</h1>` |
| 🗃️ **SQL** | Form fields map to table columns: `name`, `email` → `INSERT INTO users (name, email) …` |
| 🔗 **URLs and routes** | Query strings (`?id=7`) and paths (`/blog/post`) become backend routes and parameters |
| 🔐 **Security** | Never trust form data; validate and escape on the server |
| 📦 **APIs and JSON** | Servers can send data instead of pages, and JS renders it into HTML |

A tiny taste of the backend half (Python/Flask):

```html
<!-- templates/subscribe.html -->
<form action="/subscribe" method="post">
  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>
  <button type="submit">Subscribe</button>
</form>
```

```python
# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("subscribe.html")

@app.post("/subscribe")
def subscribe():
    email = request.form["email"]   # the "name" attribute is the key
    # validate again here, then save to a database
    return f"Thanks, {email}!"
```

| HTML habit | Pays off in any language |
|---|---|
| Clean, consistent structure | Easier templating |
| Meaningful `name`/`id`/`class` values | Easier data handling |
| Accessible markup | Less rework later |
| Valid HTML | Fewer weird bugs |

---

## 🎯 Readiness Self-Test

Can I do all of these **from memory**? If yes → on to the next suit. If not → revisit the linked file.

### Before CSS

- [ ] Write the starter template without peeking → [`basics.md`](./basics.md)
- [ ] Explain `head` vs `header` vs `h1` → [`basics.md`](./basics.md)
- [ ] Choose between `section`, `article`, and `div` → [`semantic-html.md`](./semantic-html.md)
- [ ] Build a page with `header`, `nav`, `main`, `footer` → [`semantic-html.md`](./semantic-html.md)
- [ ] Explain block vs inline → [`basics.md`](./basics.md)
- [ ] Write correct relative paths (`./`, `../`) → [`media-and-links.md`](./media-and-links.md)
- [ ] Add responsive images with width, height, alt → [`media-and-links.md`](./media-and-links.md)
- [ ] Name classes by purpose, not looks

### Before JavaScript

- [ ] Build a labelled, validated form → [`forms.md`](./forms.md)
- [ ] Explain why `name` matters for submitted data → [`forms.md`](./forms.md)
- [ ] Tell a link from a button, and when to use each → [`semantic-html.md`](./semantic-html.md)
- [ ] Use `id`, `class`, and `data-*` attributes on purpose → [`basics.md`](./basics.md)
- [ ] Build an accessible nav, dialog, and accordion → [snippet library](#-snippet-library)
- [ ] Do a keyboard-only run of my page → [`accessibility.md`](./accessibility.md)
- [ ] Read DevTools: Elements, Network, Console → [debugging guide](#-debugging-guide)

### Before a backend language

- [ ] Explain GET vs POST → [`forms.md`](./forms.md)
- [ ] Explain why client-side validation isn't enough → [`forms.md`](./forms.md)
- [ ] Describe the parts of a URL → [`media-and-links.md`](./media-and-links.md)
- [ ] Build a form that posts several kinds of fields (radio, checkbox, select, textarea) → [`forms.md`](./forms.md)

### Scoring myself

| Checked | Verdict |
|---|---|
| 80%+ | 🟢 Ready. Start CSS now. |
| 50-80% | 🟡 Almost. Patch the gaps while starting CSS. |
| Under 50% | 🔴 Spend one more week rebuilding the pages above from scratch. |

---

## 🗺️ Roadmap

```
  ✅ Mark I     basics.md           skeleton, tags, attributes
  ✅ Mark II    semantic-html.md    right element for the job
  ✅ Mark III   forms.md            collecting input
  ✅ Mark IV    accessibility.md    suit fits everyone
  ✅ Mark V     media-and-links.md  connect and show
  🔜 Mark VI    CSS                 style, layout, responsive design
  🔜 Mark VII   JavaScript          behavior, DOM, events, fetch
  🔜 Mark VIII  Python / SQL        server side and data
  🔮 Mark 85    everything together: build anything, iterate, ship
```

### Suggested path

1. 🔁 Rebuild every example page from memory using this sheet.
2. 🧪 Fix the issues found in the earlier code review (viewport, captions, button names, `main`, table `scope`).
3. 🎨 Move to CSS: style one of my own pages (the Cat Blog is a great start).
4. ⚡ Add JavaScript to the Bookstore (cart counter) and the Feedback Form (live validation).
5. 🐍 Receive that form on a tiny Python backend.
6. 🚀 Put it all online and write about what broke in [`../notes/things-i-broke.md`](../notes/things-i-broke.md).

---

## 🛠️ Tools and References

| Tool | Use |
|---|---|
| 📖 [MDN HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML) | The best element and attribute docs |
| 📖 [MDN: Learn web development](https://developer.mozilla.org/en-US/docs/Learn) | Structured beginner path (HTML → CSS → JS) |
| ✅ [W3C Validator](https://validator.w3.org/) | Catch syntax errors |
| 🔍 **DevTools** (`F12`) | Inspect, edit, debug |
| ♿ **Lighthouse / axe / WAVE** | Accessibility audits |
| 🎨 [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Check color contrast |
| 🗜️ [Squoosh](https://squoosh.app/) | Compress and convert images |
| 💅 **Prettier** | Auto-format code |
| 🔗 [W3C Link Checker](https://validator.w3.org/checklink) | Find broken links |
| 🎓 [freeCodeCamp](https://www.freecodecamp.org/) | Workshops and practice |
| 📚 [CSS-Tricks](https://css-tricks.com/) / [web.dev](https://web.dev/learn) | Next-step learning |

---

## 🔗 Related

- 📄 [`basics.md`](./basics.md) · 🏛️ [`semantic-html.md`](./semantic-html.md) · 📝 [`forms.md`](./forms.md) · ♿ [`accessibility.md`](./accessibility.md) · 🖼️ [`media-and-links.md`](./media-and-links.md)
- 🧪 [`examples/`](./examples): every concept above, built and broken
- 🎨 [`../CSS`](../CSS) · ⚡ [`../JavaScript`](../JavaScript) · 🐍 [`../Python`](../Python) · 🗃️ [`../SQL`](../SQL): where the armor gets its next upgrades
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>Five suits built, one blueprint folded. Time to give the armor color and a pulse. Mark VI loading… 🦾</i></p>
