# 🏁 FreeCodeCamp exam prep: HTML

> Final systems check before the prep exam.
> Every topic from the freeCodeCamp HTML review page, rewritten in my own words with my own examples.

![Topic](https://img.shields.io/badge/topic-HTML%20review-E34F26?logo=html5&logoColor=white)
![Source](https://img.shields.io/badge/source-freeCodeCamp%20v9-0a0a23)
![Type](https://img.shields.io/badge/type-exam%20prep-purple)
![Status](https://img.shields.io/badge/status-final%20check-brightgreen)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-lightgrey)

> 📌 **Source:** [freeCodeCamp: Review HTML](https://www.freecodecamp.org/learn/responsive-web-design-v9/review-html/review-html) (Responsive Web Design v9).
> This file follows the same topic order as that page. The wording and examples are mine. 
---

## 🗂️ Table of Contents

1. [HTML basics](#-html-basics)
2. [Identifiers and grouping](#-identifiers-and-grouping)
3. [Special characters and linking files](#-special-characters-and-linking-files)
4. [Boilerplate and encoding](#-boilerplate-and-encoding)
5. [SEO and social sharing](#-seo-and-social-sharing)
6. [Media elements and optimization](#-media-elements-and-optimization)
7. [Multimedia integration](#-multimedia-integration)
8. [Paths and link behavior](#-paths-and-link-behavior)
9. [Why semantic HTML matters](#-why-semantic-html-matters)
10. [Semantic text elements](#-semantic-text-elements)
11. [Forms](#-forms)
12. [Tables](#-tables)
13. [HTML tools](#-html-tools)
14. [Accessibility: the big picture](#-accessibility-the-big-picture)
15. [Assistive technology](#-assistive-technology)
16. [Accessibility auditing tools](#-accessibility-auditing-tools)
17. [Accessibility best practices](#-accessibility-best-practices)
18. [WAI-ARIA](#-wai-aria)
19. [Self-test: question bank](#-self-test-question-bank)
20. [Exam traps](#-exam-traps)
21. [Gap report](#-gap-report)
22. [Final checklist](#-final-checklist)

---

## 🧱 HTML Basics

| Concept | What I need to know |
|---|---|
| **Role of HTML** | It defines the **structure and meaning** of a web page. CSS styles it, JavaScript animates it. |
| **Elements** | Content wrapped in tags. Most have an opening and a closing tag: `<h1>Title</h1>`. |
| **Document shape** | Two main parts: `<head>` (info about the page) and `<body>` (what people see). |
| **Everyday elements** | Headings `<h1>`-`<h6>`, paragraphs `<p>`, containers `<div>`. |
| **`div`** | A generic box with **no meaning**. Use it to group things when no semantic tag fits. |
| **Void elements** | Elements with no content, so no closing tag: `<img>`, `<br>`, `<hr>`, `<input>`, `<meta>`, `<link>`. |
| **Attributes** | Extra settings inside the opening tag: `name="value"`. |

```html
<h1>My first page</h1>
<p>A paragraph with an <img src="dot.png" alt="small dot"> void element inside it.</p>
<div>
  <p>A div only groups things. It says nothing about what they are.</p>
</div>
```

---

## 🏷️ Identifiers and Grouping

| Attribute | Rule | Typical use |
|---|---|---|
| `id` | **Unique** on the page | Anchor targets, label links, one-off JS/CSS targets |
| `class` | **Reusable**, can list several (space-separated) | Styling or scripting a whole group |

```html
<h2 id="pricing">Pricing</h2>

<p class="note">First note</p>
<p class="note important">Second note, with two classes</p>
```

```css
#pricing   { color: crimson; }   /* the one element with this id */
.note      { font-style: italic; }
.important { font-weight: bold; }
```

---

## 🔣 Special Characters and Linking Files

### Entities

Some characters would confuse the browser, so I write a code for them: it starts with `&` and ends with `;`.

| Want | Write | Why |
|---|---|---|
| `<` | `&lt;` | Otherwise it looks like the start of a tag |
| `>` | `&gt;` | |
| `&` | `&amp;` | `&` starts every entity |
| `"` | `&quot;` | Safe inside attribute values |
| non-breaking space | `&nbsp;` | Keeps two words together on one line |
| `©` | `&copy;` | |

```html
<p>To show a tag on the page, write &lt;p&gt; instead of &lt;p&gt;.</p>
```

### Connecting other files

```html
<head>
  <link rel="stylesheet" href="css/style.css">   <!-- external CSS -->
</head>
<body>
  …
  <script src="js/app.js"></script>               <!-- external JavaScript -->
</body>
```

| Element | Job | Goes in |
|---|---|---|
| `<link>` | Connects an external resource (usually a stylesheet) | `<head>` |
| `<script src>` | Loads an external JavaScript file | `<head>` (with `defer`) or end of `<body>` |

---

## 🏗️ Boilerplate and Encoding

The standard starting point for every page:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Page title</title>
  </head>
  <body>
    <!-- visible content -->
  </body>
</html>
```

| Piece | Purpose |
|---|---|
| `<!DOCTYPE html>` | Says "this is modern HTML," so the browser uses standards mode |
| `<html lang="en">` | Root element; `lang` declares the language |
| `<head>` | Metadata container |
| `<body>` | The visible page |
| `<meta charset="UTF-8">` | **UTF-8** is the character encoding that covers practically every writing system and emoji, so text doesn't turn into garbage like `Ã©` |

> 💡 Add `<meta name="viewport" content="width=device-width, initial-scale=1.0">` too. It's not in the review list, but responsive pages need it.

---

## 🔍 SEO and Social Sharing

### The `description` meta tag

```html
<meta name="description" content="Notes and examples from my HTML learning journey.">
```

- It's a short summary of the page that search engines often show under the title in results.
- Keep it to roughly one or two sentences and make it specific to *that* page.

### Open Graph tags

**Open Graph (OG)** tags control how a page looks when shared on social media or chat apps (the preview card with a title, image, and blurb).

```html
<meta property="og:title" content="HTML Final Review">
<meta property="og:description" content="Every HTML concept in one study page.">
<meta property="og:image" content="https://example.com/images/preview.png">
<meta property="og:url" content="https://example.com/html-review">
<meta property="og:type" content="website">
```

| Tag | Controls |
|---|---|
| `og:title` | Headline in the preview |
| `og:description` | Blurb in the preview |
| `og:image` | Preview picture (use a full absolute URL) |
| `og:url` | The page's canonical address |
| `og:type` | Kind of content (`website`, `article`, …) |

Note the attribute is **`property`**, not `name`, for Open Graph.

---

## 🖼️ Media Elements and Optimization

### Replaced elements

A **replaced element** is one whose content comes from **outside** the HTML file, so the browser *replaces* the tag with that external thing. Examples: `<img>`, `<iframe>`, `<video>`, `<embed>`. Their natural size comes from the resource itself, so I should give them `width`/`height` to avoid layout jumps.

### Optimizing media

| Technique | Why |
|---|---|
| Resize to the size actually displayed | Don't ship huge files |
| Compress | Smaller downloads, same-looking result |
| Modern formats (WebP, AVIF) with a fallback | Smaller files |
| `loading="lazy"` for below-the-fold images | Faster first load |
| `width` and `height` attributes | Prevent layout shift |
| Prefer video over animated GIFs | Much lighter |
| Responsive images (`srcset`, `<picture>`) | Right size per device |

### Image formats at a glance

| Format | Best for |
|---|---|
| JPEG | Photos |
| PNG | Graphics, screenshots, transparency |
| WebP / AVIF | Photos and graphics at smaller sizes |
| GIF | Tiny animations (usually better as video) |
| SVG | Logos, icons, diagrams |

### Licenses

Not everything online is free to use. Before using an image, check its **license**: some require credit (attribution), some forbid commercial use, some are free for anything. Reliable sources: your own work, public-domain and Creative Commons collections, free-stock sites that publish clear terms.

### SVG

**Scalable Vector Graphics** are drawn from math/code, not pixels. They stay sharp at any size, are usually tiny, and can be styled with CSS.

```html
<img src="logo.svg" alt="XYZ Bookstore logo">

<svg width="60" height="60" viewBox="0 0 60 60" role="img" aria-labelledby="dot-title">
  <title id="dot-title">Red dot</title>
  <circle cx="30" cy="30" r="25" fill="crimson"/>
</svg>
```

---

## 🎬 Multimedia Integration

```html
<audio controls src="audio/theme.mp3">
  Your browser doesn't support audio.
</audio>

<video controls width="480" poster="images/poster.jpg">
  <source src="video/intro.mp4" type="video/mp4">
  <track kind="captions" src="video/captions.vtt" srclang="en" label="English">
  Your browser doesn't support video.
</video>

<iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
        title="Describe the video here" width="480" height="270" allowfullscreen></iframe>
```

| Element | Notes |
|---|---|
| `<audio>` | Needs `controls` to be usable; fallback text goes inside |
| `<video>` | `controls`, `poster`, `width`/`height`; multiple `<source>` formats |
| `<track>` | Captions/subtitles for video |
| `<iframe>` | Embeds another page (like a hosted video); always add a `title` |

---

## 🧭 Paths and Link Behavior

### The `target` attribute

| Value | Where the link opens |
|---|---|
| `_self` | Same tab (default) |
| `_blank` | New tab/window |
| `_parent` | The parent frame |
| `_top` | The top-level window, breaking out of all frames |

### Absolute vs relative paths

| | Absolute | Relative |
|---|---|---|
| Looks like | `https://example.com/img/cat.jpg` | `img/cat.jpg` |
| Depends on where the current file is? | No | Yes |
| Best for | Other websites | Files in my own project |

### Path syntax

| Symbol | Meaning |
|---|---|
| `/` | Start from the site root (or separates folders) |
| `./` | Start from the current folder |
| `../` | Go **up one** folder |

```html
<img src="./images/cat.jpg" alt="Cat">          <!-- from this folder -->
<a href="../index.html">Back to the home page</a> <!-- one folder up -->
```

### Link states

| State | When | CSS |
|---|---|---|
| Unvisited | Never clicked | `a:link` |
| Visited | Already clicked | `a:visited` |
| Hover | Mouse over it | `a:hover` |
| Focus | Reached by keyboard | `a:focus` / `a:focus-visible` |
| Active | Being pressed | `a:active` |

Write them in this order, **LVHFA**, so later rules don't get overridden.

### Internal links (jumping within a page)

```html
<a href="#contact">Go to contact</a>
…
<h2 id="contact">Contact</h2>
```

The `href` starts with `#`, followed by the **same text as the target's `id`**.

---

## 🏛️ Why Semantic HTML Matters

### Heading hierarchy

- `<h1>` = the most important heading, `<h6>` = the least.
- Use them to show **structure**, never to get bigger text.
- One `<h1>`, then go down one level at a time.

### Presentational vs semantic

| Presentational (old) | Semantic (modern) |
|---|---|
| `<center>`, `<big>`, `<font>` | Deprecated: tags that only describe **looks**; use CSS instead |
| `<div>` for everything | `header`, `nav`, `article`, `aside`, `section`, `footer` |

### The structural elements

| Element | Represents |
|---|---|
| `<header>` | Introductory content |
| `<nav>` | Navigation links |
| `<article>` | Self-contained content (a post, a card) |
| `<aside>` | Sidebar or related content |
| `<section>` | A themed group of related content |
| `<footer>` | The closing part of a page or section |

---

## ✍️ Semantic Text Elements

| Element | Meaning | Quick example |
|---|---|---|
| `<em>` | Stress emphasis (changes how a sentence reads) | `I <em>did</em> finish.` |
| `<strong>` | Strong **importance** | `<strong>Warning:</strong> hot` |
| `<i>` | Alternate voice or mood, foreign or technical terms, thoughts | `the word <i lang="fr">bonjour</i>` |
| `<b>` | Draws attention without adding importance | `<b>Sally's SciFi</b> is on sale` |
| `<dl>` | Description list (term + details pairs) | wrapper |
| `<dt>` | The term | `<dt>HTML</dt>` |
| `<dd>` | The description | `<dd>Page structure</dd>` |
| `<blockquote>` | A longer quote from another source | block quote |
| `<q>` | A short quote inside a sentence | `She said <q>hello</q>.` |
| `<abbr>` | Abbreviation/acronym (use `title` for the long form) | `<abbr title="World Health Organization">WHO</abbr>` |
| `<address>` | Contact information | author or company contact |
| `<time>` | A date/time | `<time datetime="2026-10-10">Oct 10</time>` |
| `<sup>` / `<sub>` | Superscript / subscript | `x<sup>2</sup>`, `H<sub>2</sub>O` |
| `<code>` | A piece of computer code | `<code>console.log()</code>` |
| `<u>` | Text with an unarticulated (non-text) annotation, such as marking a misspelling | Use rarely; it looks like a link |
| `<ruby>` | Pronunciation annotation, mostly for East Asian text | `<ruby>漢<rt>han</rt></ruby>` |
| `<s>` | Content that is **no longer accurate or relevant** | `<s>$20</s> $15` |

```html
<dl>
  <dt>Void element</dt>
  <dd>An element with no content and no closing tag.</dd>

  <dt>Entity</dt>
  <dd>A code like &amp;lt; that stands for a special character.</dd>
</dl>
```

### Quick contrasts

| Pair | Difference |
|---|---|
| `em` vs `i` | `em` = stress that changes meaning · `i` = different voice/term, no stress |
| `strong` vs `b` | `strong` = important · `b` = attention only |
| `s` vs `del` | `s` = no longer relevant · `del` = deleted from the document |

---

## 📝 Forms

### The form element

```html
<form action="/signup" method="post">
  <!-- controls go here -->
</form>
```

| Attribute | Meaning |
|---|---|
| `action` | The URL that receives the data |
| `method` | How the data is sent. Usually `get` or `post` |

### Input basics

| Attribute | Purpose |
|---|---|
| `type` | Kind of field: `text`, `email`, `password`, `radio`, `checkbox`, `number`, `date`, … |
| `placeholder` | Hint text inside the empty field |
| `value` | The field's value (for button types, it's the button's text) |
| `name` | The **key** under which the data is sent. Radios with the same `name` form one group (only one can be chosen) |
| `size` | How many characters wide the field looks (CSS is preferred in real projects) |
| `min` / `max` | Smallest/largest allowed number (or date) |
| `minlength` / `maxlength` | Fewest/most characters allowed |
| `required` | Must be filled in before submitting |
| `disabled` | Can't be used or changed, and isn't submitted |
| `readonly` | Can't be changed, but **is** submitted |

```html
<input type="text" name="username" placeholder="e.g. tony_s"
       size="20" minlength="3" maxlength="20" required>

<input type="number" name="guests" min="1" max="8">
```

### Labels

```html
<!-- Explicit: for matches id -->
<label for="email">Email</label>
<input type="email" id="email" name="email">

<!-- Implicit: the input is wrapped by the label -->
<label>
  Nickname
  <input type="text" name="nickname">
</label>
```

| Method | How the link is made |
|---|---|
| **Explicit** | `for` on the label = `id` on the input |
| **Implicit** | The input sits inside the `<label>` |

### Buttons

```html
<button type="submit">Send</button>
<button type="reset">Clear</button>
<button type="button">Do something else</button>

<input type="button" value="Old-style button">
```

| `type` | Result |
|---|---|
| `submit` | Sends the form |
| `reset` | Restores the default values |
| `button` | Nothing by itself (JavaScript gives it a job) |

### Grouping with `fieldset` and `legend`

```html
<fieldset>
  <legend>Preferred contact method</legend>

  <input type="radio" id="by-email" name="contact" value="email">
  <label for="by-email">Email</label>

  <input type="radio" id="by-phone" name="contact" value="phone">
  <label for="by-phone">Phone</label>
</fieldset>
```

### Focus

The **focused state** is how an input looks when it's the one currently selected, via a click or the Tab key. It must stay visible.

---

## 📊 Tables

```html
<table>
  <caption>Quiz scores</caption>
  <thead>
    <tr><th>Student</th><th>Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Rami</td><td>80</td></tr>
    <tr><td>Lina</td><td>90</td></tr>
  </tbody>
  <tfoot>
    <tr><td>Average</td><td>85</td></tr>
  </tfoot>
</table>
```

| Element | Role |
|---|---|
| `<table>` | The whole table |
| `<caption>` | The table's title |
| `<thead>` | Header row group |
| `<tbody>` | Main rows group |
| `<tfoot>` | Footer row group (totals, averages) |
| `<tr>` | A row |
| `<th>` | A **header** cell |
| `<td>` | A **data** cell |
| `colspan="n"` | Makes a cell stretch across *n* columns |

```html
<tfoot>
  <tr>
    <td colspan="2">Total (spans two columns)</td>
    <td>250</td>
  </tr>
</tfoot>
```

---

## 🛠️ HTML Tools

| Tool | What it does |
|---|---|
| **HTML validator** | Checks that my code follows the rules and flags mistakes ([validator.w3.org](https://validator.w3.org/)) |
| **DOM inspector** | Lets me look at (and tweak) the live structure of a page |
| **DevTools** | The browser's built-in toolbox for debugging, analyzing and profiling a page (`F12`) |

---

## ♿ Accessibility: The Big Picture

**WCAG** (Web Content Accessibility Guidelines) is the standard for making content usable by people with disabilities. Its four principles spell **POUR**:

| Letter | Principle | Plain meaning |
|---|---|---|
| **P** | Perceivable | People can take the content in (see, hear, or read it some way) |
| **O** | Operable | People can use the interface (keyboard, voice, pointing devices) |
| **U** | Understandable | Content and behavior are clear and predictable |
| **R** | Robust | Works across browsers and assistive technology |

---

## 🧑‍🦯 Assistive Technology

| Technology | Who it helps and how |
|---|---|
| **Screen readers** | Read the screen aloud, for blind or visually impaired users |
| **Large-text or braille keyboards** | Make typing easier for people with visual impairments |
| **Screen magnifiers** | Enlarge the screen for people with low vision |
| **Alternative pointing devices** | Joysticks, trackballs, touchpads, for people with motor impairments |
| **Voice recognition** | Controls the computer by speaking |

---

## 🔬 Accessibility Auditing Tools

| Tool | Notes |
|---|---|
| **Google Lighthouse** | Built into Chrome DevTools |
| **WAVE** | Visual overlay of issues |
| **IBM Equal Access Accessibility Checker** | Extension for scanning pages |
| **axe DevTools** | Detailed issue explanations |

Automated tools find **some** problems. Real keyboard and screen-reader testing finds the rest.

---

## ✅ Accessibility Best Practices

| Practice | Why |
|---|---|
| **Proper heading levels** | Gives assistive tech a logical outline |
| **`th` for header cells, `td` for data cells** | Lets screen readers connect data to headers |
| **Every input has a `<label>`** | Names the field for everyone |
| **Good `alt` text** | Describes images to people who can't see them |
| **Descriptive link text** | The purpose is clear out of context |
| **Captions, transcripts, audio descriptions** | Captions/transcripts for people who can't hear; audio descriptions for people who can't see the visuals |
| **`tabindex`** | Controls keyboard focus. **Only use `0` or `-1`**, never a number above 0 |
| **`accesskey`** | Defines a keyboard shortcut for an element |

```html
<!-- tabindex values -->
<div tabindex="0">Joins the normal Tab order</div>
<div tabindex="-1">Can be focused by script, skipped by Tab</div>
<!-- ❌ tabindex="3" breaks the natural order -->
```

> ⚠️ **Honest note on `accesskey`:** it's on the review list, but in real projects it can clash with browser and screen-reader shortcuts and is inconsistent between browsers, so use it carefully, if at all.

---

## 🆘 WAI-ARIA

**WAI-ARIA** = Web Accessibility Initiative: Accessible Rich Internet Applications. It's a set of extra attributes that tell assistive technology what things are and what they're doing.

| Item | Purpose | Example |
|---|---|---|
| **Roles** | Declare what an element *is* | `role="alert"`, `role="tab"`, `role="menu"` |
| `aria-label` | Gives an accessible name **directly in the attribute** | `<button aria-label="Close">✕</button>` |
| `aria-labelledby` | Names an element by **pointing at another element's `id`** | `<section aria-labelledby="t1">` |
| `aria-describedby` | Points to extra descriptive text | `<input aria-describedby="hint">` |
| `aria-hidden="true"` | Hides an element from assistive tech (good for decoration) | `<span aria-hidden="true">★</span>` |

```html
<button type="button" aria-label="Close dialog">✕</button>

<h2 id="faq-title">FAQ</h2>
<section aria-labelledby="faq-title">…</section>

<label for="pw">Password</label>
<input type="password" id="pw" aria-describedby="pw-hint">
<p id="pw-hint">At least 8 characters.</p>
```

> 🧠 **First rule of ARIA:** if a native HTML element can do the job, use it instead. ARIA fills gaps, it doesn't replace real elements.

---

## 🎯 Self-Test: Question Bank

Cover the answers and quiz myself.

<details>
<summary><b>Basics and structure</b></summary>

1. **What's a void element? Name three.** → An element with no closing tag and no content: `img`, `br`, `input`, `hr`, `meta`, `link`.
2. **`id` or `class` for something used on many elements?** → `class`. IDs must be unique.
3. **What does `<!DOCTYPE html>` do?** → Tells the browser to use modern standards mode.
4. **Why `<meta charset="UTF-8">`?** → So characters from any language display correctly.
5. **How do I show `<` as text?** → `&lt;`
6. **Where do `<link>` and `<script src>` go?** → `<link>` in `<head>`; `<script>` in `<head>` with `defer` or at the end of `<body>`.

</details>

<details>
<summary><b>SEO, media and paths</b></summary>

7. **What does the `description` meta tag influence?** → The snippet shown in search results.
8. **What are Open Graph tags for?** → Controlling the preview card when a link is shared.
9. **What's a replaced element?** → One whose content comes from an external resource (`img`, `iframe`, `video`).
10. **Which format for a logo?** → SVG.
11. **What does `../` mean?** → Go up one folder.
12. **Which `target` opens a new tab?** → `_blank`.
13. **How do I link to `<h2 id="faq">` on the same page?** → `<a href="#faq">`.
14. **Link state order in CSS?** → link, visited, hover, focus, active (LVHFA).

</details>

<details>
<summary><b>Semantics</b></summary>

15. **Name the six structural elements.** → `header`, `nav`, `article`, `aside`, `section`, `footer`.
16. **Why not `<center>` or `<font>`?** → They're deprecated presentational tags; CSS handles looks.
17. **`strong` vs `b`?** → `strong` = importance; `b` = attention only.
18. **`em` vs `i`?** → `em` = stress emphasis; `i` = alternate voice or term.
19. **Which elements build a glossary?** → `dl`, `dt`, `dd`.
20. **`q` vs `blockquote`?** → Inline short quote vs block-level longer quote.
21. **What is `<s>` for?** → Content that's no longer accurate or relevant.

</details>

<details>
<summary><b>Forms and tables</b></summary>

22. **What does `name` do on an input?** → It's the key sent with the value; radios sharing a name form one group.
23. **`disabled` vs `readonly`?** → Disabled: not usable and not submitted. Readonly: not editable but submitted.
24. **Two ways to link a label to an input?** → Explicit (`for` = `id`) and implicit (wrap the input).
25. **What are the three button types?** → `submit`, `reset`, `button`.
26. **What do `fieldset` and `legend` do?** → Group related inputs and caption the group.
27. **How do I make a cell span two columns?** → `colspan="2"`.
28. **Which element titles a table?** → `<caption>`.
29. **`th` vs `td`?** → Header cell vs data cell.

</details>

<details>
<summary><b>Accessibility</b></summary>

30. **What does POUR stand for?** → Perceivable, Operable, Understandable, Robust.
31. **Which `tabindex` values are okay?** → `0` and `-1`. Never above `0`.
32. **`aria-label` vs `aria-labelledby`?** → Direct text vs pointing at another element's `id`.
33. **What does `aria-hidden="true"` do?** → Hides the element from assistive tech.
34. **What do captions, transcripts, and audio descriptions help with?** → Captions/transcripts: hearing. Audio descriptions: vision.
35. **Name three auditing tools.** → Lighthouse, WAVE, axe DevTools (or IBM Equal Access).

</details>

---

## ⚠️ Exam Traps

| Trap | Reality |
|---|---|
| "`id`s can repeat" | ❌ Must be unique |
| "Radios need different `name`s" | ❌ Same `name` makes the group |
| "`disabled` fields are submitted" | ❌ Only `readonly` ones are |
| "Use `tabindex="5"` to control order" | ❌ Never above 0 |
| "`<b>` and `<strong>` are identical" | ❌ Different meaning |
| "Pick `h3` because it looks smaller" | ❌ Headings are for structure |
| "Void elements need a closing tag" | ❌ They don't |
| "`aria-label` always beats a visible `<label>`" | ❌ Native visible labels come first |
| "Open Graph uses `name=`" | ❌ It uses `property=` |
| "`./` and `../` are the same" | ❌ Here vs up one level |
| "Alt text can be `image of ...`" | ❌ Describe the content or purpose |
| "`tfoot` goes before `tbody` in source" | ⚠️ Keep the logical order: `thead`, `tbody`, `tfoot` |

---

## 🧪 Gap Report

How the review page compares to my earlier notes. Items that weren't covered in depth, now filled in:

| Topic from the review | Where I covered it | Status |
|---|---|---|
| Open Graph tags | This file | ✅ Added |
| Replaced elements | This file | ✅ Added |
| `<u>`, `<s>`, `<ruby>` | This file | ✅ Added |
| Deprecated `center`, `big`, `font` | This file | ✅ Added |
| Image licenses | This file and [`media-and-links.md`](./media-and-links.md) | ✅ Covered |
| `accesskey` | This file (with caveats) | ✅ Added |
| Large-text / braille keyboards, pointing devices | This file | ✅ Added |
| `size` attribute | This file | ✅ Added (CSS preferred in practice) |
| Link states | This file and [`media-and-links.md`](./media-and-links.md) | ✅ Covered |
| `input type="button"` | This file | ✅ Added |

Extra things my notes cover that the review page doesn't list: viewport meta, `<picture>`/`srcset`, `<track>` captions in depth, skip links, live regions, security notes for forms, and the debugging guide.

---

## ✅ Final Checklist

Before the prep exam, I can do all of these from memory:

**Structure**
- [ ] Write the full boilerplate without looking
- [ ] Explain `id` vs `class` and when to use each
- [ ] List the void elements and why they're different
- [ ] Write entities for `<`, `>`, `&`, and `"`

**Head and sharing**
- [ ] Add charset, title, description, and Open Graph tags
- [ ] Connect a stylesheet and a script

**Media and links**
- [ ] Choose the right image format for photos, logos, and screenshots
- [ ] Write `audio`, `video`, and `iframe` with the right attributes
- [ ] Write relative paths with `./` and `../`
- [ ] List the four `target` values and the five link states
- [ ] Make an internal link with `#id`

**Semantics**
- [ ] Name the six structural elements and what each is for
- [ ] Explain `em`/`i`, `strong`/`b`, and `s`
- [ ] Build a `dl`, a `blockquote`, a `q`, an `abbr`, and a `time`

**Forms and tables**
- [ ] Build a labelled form with every attribute from the table above
- [ ] Do both label-association methods
- [ ] Build a table with `caption`, `thead`, `tbody`, `tfoot`, and `colspan`

**Accessibility**
- [ ] Recite POUR and name the assistive technologies
- [ ] Explain `tabindex` rules and the ARIA attributes
- [ ] Name three audit tools and run Lighthouse on my own page

> 🟢 Everything checked? Time for the exam, and then on to Mark VI: CSS. 🦾

---

<p align="center"><i>Final systems check complete. Every bolt tightened, every weld tested. Ready for the exam. 🦾</i></p>
