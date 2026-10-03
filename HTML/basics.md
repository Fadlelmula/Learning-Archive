# 📄 HTML Basics

> Every suit starts as a blueprint. This is the blueprint for every web page.
> Mark I notes: written while rebuilding the rust, so expect honesty and a few scars.

![Topic](https://img.shields.io/badge/topic-HTML5-E34F26?logo=html5&logoColor=white)
![Level](https://img.shields.io/badge/level-fundamentals-brightgreen)
![Status](https://img.shields.io/badge/status-growing-yellow)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-blue)

---

## 🗂️ Table of Contents

1. [What HTML actually is](#-what-html-actually-is)
2. [Anatomy of an element](#-anatomy-of-an-element)
3. [The page skeleton](#-the-page-skeleton)
4. [Attributes](#-attributes)
5. [Text basics](#-text-basics)
6. [Lists](#-lists)
7. [Links](#-links)
8. [Images](#-images)
9. [Block vs inline](#-block-vs-inline)
10. [Nesting rules](#-nesting-rules)
11. [Comments, entities and whitespace](#-comments-entities-and-whitespace)
12. [Mistakes I actually made](#-mistakes-i-actually-made)
13. [Cheat sheet](#-cheat-sheet)
14. [Practice ideas](#-practice-ideas)
15. [Tools](#-tools)
16. [Related](#-related)

---

## 🧠 What HTML Actually Is

**HTML = HyperText Markup Language.**

- **HyperText:** text that links to other text (the "web" part).
- **Markup:** you wrap content in tags that describe *what it is*.
- **Language:** a set of rules the browser understands.

The important bit: **HTML describes meaning and structure, not looks.** "This is a heading," "this is a list," "this is a navigation menu." Colors, fonts, and layout are CSS's job. Behavior is JavaScript's job.

| Layer | Job | Body analogy |
|---|---|---|
| 🦴 HTML | Structure and meaning | Skeleton |
| 🎨 CSS | Looks and layout | Skin and clothes |
| ⚡ JavaScript | Behavior and interaction | Muscles and nerves |

When a browser loads an HTML file, it reads it top to bottom and builds a tree of objects called the **DOM** (Document Object Model). CSS and JavaScript later grab pieces of that tree to style or change them. Good HTML makes everything after it easier.

---

## 🧬 Anatomy of an Element

An **element** is the whole thing: opening tag, content, and closing tag.

```html
<p class="intro">Hello, <strong>world</strong>!</p>
```

```
 opening tag        content                closing tag
┌────────────────┐ ┌──────────────────────┐ ┌────┐
<p class="intro">  Hello, <strong>…</strong>!  </p>
   │    └── attribute value
   └─ attribute name
```

| Part | Example | Notes |
|---|---|---|
| **Tag name** | `p` | Lowercase by convention |
| **Opening tag** | `<p class="intro">` | Can carry attributes |
| **Content** | `Hello, ...` | Text and/or other elements |
| **Closing tag** | `</p>` | Same name with a `/` |
| **Element** | the whole line | Tag + content + tag |

### Void (empty) elements

Some elements have no content, so they have no closing tag:

```html
<br>
<hr>
<img src="cat.jpg" alt="A sleeping cat">
<input type="text" name="username">
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
```

Common void elements: `br`, `hr`, `img`, `input`, `meta`, `link`, `source`, `track`.
Writing `<br />` (with a slash) is allowed in HTML5, but it's optional.

> 💡 **Tag vs element:** a *tag* is just `<p>` or `</p>`. The *element* is the full package. People mix these up constantly, and so did I.

---

## 🏗️ The Page Skeleton

Every HTML page I write starts from this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Page Title</title>
  </head>
  <body>
    <h1>Hello, world</h1>
  </body>
</html>
```

### Line by line

| Line | What it does | Why it matters |
|---|---|---|
| `<!DOCTYPE html>` | Tells the browser "this is modern HTML5" | Without it, browsers may use *quirks mode* and render things weirdly. It's not a tag, just a declaration. |
| `<html lang="en">` | The root element that wraps everything | `lang` helps screen readers pronounce text, helps translation tools, and helps search engines |
| `<head>` | Info *about* the page (invisible content) | Holds metadata, title, links to CSS |
| `<meta charset="UTF-8">` | Character encoding | Prevents garbled text like `Ã©`. Keep it near the top of `<head>`. |
| `<meta name="viewport" ...>` | Tells phones to use the real screen width | **Without it, phones show a zoomed-out desktop layout.** I forgot this in 5 of my 8 first examples. |
| `<title>` | Text shown in the browser tab, bookmarks, and search results | Every page needs a unique, descriptive one |
| `<body>` | Everything the user actually sees | All visible content goes here |

### `<head>` vs `<header>` vs `<h1>`

The three I mixed up for far too long:

| Element | What it is |
|---|---|
| `<head>` | Invisible metadata container for the *document* |
| `<header>` | Visible intro/navigation area for a page or section (lives in `<body>`) |
| `<h1>`-`<h6>` | Headings: the titles of content |

### The standard document order

```
<!DOCTYPE>
└── <html>
    ├── <head>   → metadata (title, charset, viewport, CSS links)
    └── <body>   → visible content
        ├── <header>
        ├── <nav>
        ├── <main>
        └── <footer>
```

---

## 🏷️ Attributes

Attributes add extra info to an element. They always go in the **opening tag**.

```html
<a href="https://example.com" target="_blank" rel="noopener">Visit</a>
```

**Syntax:** `name="value"`, with a space between multiple attributes.

### Rules I'm following

- ✅ Always use **double quotes** around values.
- ✅ Lowercase attribute names.
- ❌ Never double up quotes. `cite="url""` is a bug (yes, I did this).
- ✅ Values with spaces *must* be quoted: `class="card big"`.

### Boolean attributes

Some attributes are on/off. If they're present, they're **true**. No value needed.

```html
<input type="checkbox" checked>
<input type="text" required disabled>
<video controls loop muted></video>
```

> ⚠️ `disabled="false"` is still **disabled**. Presence means true. To turn it off, remove the attribute entirely.

### Global attributes (work on almost any element)

| Attribute | Purpose | Example |
|---|---|---|
| `id` | Unique identifier (one per page) | `id="main-menu"` |
| `class` | Group label, reusable, can hold several | `class="card featured"` |
| `lang` | Language of this element's content | `lang="ar"` |
| `title` | Tooltip text on hover | `title="More info"` |
| `hidden` | Hides the element | `<p hidden>`... |
| `style` | Inline CSS (avoid; use a stylesheet) | `style="color: red"` |
| `tabindex` | Keyboard focus order | `tabindex="0"` |
| `data-*` | Custom data for JavaScript | `data-book-id="42"` |

### `id` vs `class`

| | `id` | `class` |
|---|---|---|
| Uniqueness | **Must be unique** on the page | Reusable on many elements |
| How many per element | 1 | Many, space-separated |
| Used for | Anchor links, labels (`for`), one-off targets | Styling groups of things |
| CSS selector | `#sally-adventure-book` | `.card` |

### Attributes I use most

| Element | Key attributes |
|---|---|
| `<a>` | `href`, `target`, `rel` |
| `<img>` | `src`, `alt`, `width`, `height`, `loading` |
| `<input>` | `type`, `name`, `id`, `placeholder`, `required`, `value` |
| `<label>` | `for` (must match the input's `id`) |
| `<button>` | `type` (`button`, `submit`, `reset`) |
| `<audio>` / `<video>` | `src`, `controls`, `loop`, `muted`, `poster`, `preload` |
| `<meta>` | `charset`, `name`, `content` |

---

## 🔤 Text Basics

### Headings

```html
<h1>Page title</h1>
<h2>Major section</h2>
<h3>Subsection</h3>
```

- `<h1>` to `<h6>`: six levels, from most to least important.
- **One `<h1>` per page** is the common best practice.
- **Don't skip levels** (no jumping from `<h2>` straight to `<h4>`).
- Never pick a heading because it *looks* bigger. That's CSS's job. Pick it for **structure**.
- Screen reader users often navigate by headings alone, so the outline matters.

### Paragraphs and breaks

```html
<p>This is a paragraph.</p>
<p>Line one<br>line two (same paragraph).</p>
<hr> <!-- a thematic break between topics -->
```

- Use `<p>` for paragraphs. Don't stack `<br><br>` to fake spacing; use CSS margins.
- `<br>` is for line breaks that are *part of the content* (addresses, poems).

### Emphasis and meaning

| Tag | Meaning | Looks like (default) |
|---|---|---|
| `<strong>` | Strong **importance** | Bold |
| `<em>` | Stress **emphasis** (changes how a sentence reads) | Italic |
| `<b>` | Bold for style only, no extra importance | Bold |
| `<i>` | Alternate voice (technical terms, thoughts) | Italic |
| `<mark>` | Highlighted / relevant text | Yellow highlight |
| `<small>` | Side comments, fine print | Smaller text |
| `<del>` / `<ins>` | Removed / inserted text | Strikethrough / underline |
| `<sub>` / `<sup>` | Subscript / superscript | H<sub>2</sub>O, x<sup>2</sup> |

> 🧠 **Rule of thumb:** `<strong>` and `<em>` carry *meaning* (a screen reader can change its voice). `<b>` and `<i>` are just looks. When in doubt, use `strong` and `em`.

### Quotes and citations

```html
<p>As Quincy says, <q cite="https://example.com">You can become a developer.</q></p>

<blockquote cite="https://example.com">
  <p>So much of getting a job is who you know.</p>
</blockquote>
<p>Quincy Larson, <cite>How to Learn to Code</cite></p>
```

| Tag | Use for |
|---|---|
| `<q>` | Short, inline quote (browser adds quotation marks) |
| `<blockquote>` | Long, block-level quote |
| `<cite>` | The **title of a work** (not the person's name) |
| `cite` attribute | URL of the source (not displayed, just machine-readable) |

### Code and technical text

```html
<p>Use the <code>&lt;p&gt;</code> tag for paragraphs.</p>
<pre><code>line one
    line two keeps its spaces
</code></pre>
```

- `<code>` is for inline code, `<pre>` preserves whitespace and line breaks.
- `<kbd>` is for keyboard keys and `<samp>` is for program output.

### Other handy inline tags

```html
<abbr title="HyperText Markup Language">HTML</abbr>
<time datetime="2026-10-03">3 October 2026</time>
<address>Contact info for the page or article author</address>
```

---

## 📋 Lists

```html
<!-- Unordered: order doesn't matter -->
<ul>
  <li>catnip</li>
  <li>laser pointers</li>
</ul>

<!-- Ordered: order matters -->
<ol>
  <li>flea treatment</li>
  <li>thunder</li>
</ol>

<!-- Description list: term + definition -->
<dl>
  <dt>HTML</dt>
  <dd>The structure of a web page.</dd>
  <dt>CSS</dt>
  <dd>The style of a web page.</dd>
</dl>
```

| Tag | Role |
|---|---|
| `<ul>` | Unordered list (bullets) |
| `<ol>` | Ordered list (numbers) |
| `<li>` | A list item |
| `<dl>` / `<dt>` / `<dd>` | Description list / term / definition |

### Useful `<ol>` attributes

| Attribute | Effect |
|---|---|
| `start="5"` | Begin counting at 5 |
| `reversed` | Count down |
| `type="a"` | Letters instead of numbers (`1`, `a`, `A`, `i`, `I`) |

### Nested lists

A nested list goes **inside an `<li>`**, never directly inside the `<ul>`:

```html
<ul>
  <li>Fruits
    <ul>
      <li>Apple</li>
      <li>Mango</li>
    </ul>
  </li>
  <li>Vegetables</li>
</ul>
```

> 📌 A `<ul>` or `<ol>` should only contain `<li>` as direct children. Navigation menus are *also* just lists of links.

---

## 🔗 Links

The `<a>` (anchor) element is what makes it *hyper*text.

```html
<a href="https://example.com">Visit Example</a>
```

### Types of `href`

| Type | Example | Goes to |
|---|---|---|
| Absolute URL | `href="https://example.com/page"` | Another website |
| Relative path | `href="about.html"` | A file in the same folder |
| Parent folder | `href="../index.html"` | One folder up |
| Subfolder | `href="pages/contact.html"` | A folder below |
| Root-relative | `href="/images/logo.png"` | From the site root |
| In-page anchor | `href="#contact"` | The element with `id="contact"` |
| Email | `href="mailto:me@example.com"` | Opens the email app |
| Phone | `href="tel:+15555555555"` | Dials on phones |

### Useful link attributes

| Attribute | Purpose |
|---|---|
| `target="_blank"` | Opens in a new tab |
| `rel="noopener noreferrer"` | Add it with `_blank` as a safety habit (modern browsers imply `noopener`, but it's good manners) |
| `download` | Downloads the file instead of navigating |
| `title` | Extra hint (don't rely on it for important info) |

### In-page navigation (what my Cat Blog does)

```html
<nav>
  <ul>
    <li><a href="#about">About</a></li>
    <li><a href="#posts">Posts</a></li>
  </ul>
</nav>

<section id="about">...</section>
<section id="posts">...</section>
```

### Link text rules

- ✅ Make link text **describe the destination**: "Read the HTML guide."
- ❌ Avoid "click here" and "read more" on their own. Screen reader users often browse a list of links out of context.
- ✅ Keep spaces *outside* the `<a>` tag, so the underline doesn't start with a blank gap.

### File paths cheat sheet

```
project/
├── index.html
├── about.html
├── images/
│   └── cat.jpg
└── pages/
    └── contact.html
```

| From | To | Path |
|---|---|---|
| `index.html` | `about.html` | `about.html` |
| `index.html` | `cat.jpg` | `images/cat.jpg` |
| `pages/contact.html` | `index.html` | `../index.html` |
| `pages/contact.html` | `cat.jpg` | `../images/cat.jpg` |

---

## 🖼️ Images

```html
<img src="images/cat.jpg" alt="An orange cat lying on its back" width="600" height="400">
```

| Attribute | Required? | Purpose |
|---|---|---|
| `src` | ✅ | Where the image lives |
| `alt` | ✅ | Text alternative if the image can't be seen |
| `width` / `height` | Recommended | Reserves space so the page doesn't jump while loading |
| `loading="lazy"` | Optional | Load only when scrolled near |

### Writing good alt text

| Situation | What to write |
|---|---|
| Informative photo | Describe what matters: `alt="Two tabby kittens sleeping on a couch"` |
| Decorative image | Empty alt: `alt=""` (screen readers skip it) |
| Image **inside a link** | Describe the **destination**: `alt="View more cat photos"` |
| Image of text | Write the same text |

- ❌ Don't start with "Image of..." or "Picture of..."; screen readers already announce it's an image.
- ❌ Never leave `alt` off entirely. `alt=""` (deliberately empty) and *missing* `alt` are not the same thing.

### Figures and captions

```html
<figure>
  <img src="lasagna.jpg" alt="A slice of lasagna on a plate">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
```

Use `<figure>` when the image (or code, chart, quote) is a self-contained unit with a caption.

---

## 📦 Block vs Inline

Elements behave in one of two basic ways by default:

| | Block | Inline |
|---|---|---|
| Line behavior | Starts on a **new line**, takes the **full width** | Sits **within** a line, only as wide as its content |
| Can hold | Other blocks and inline | Text and other inline elements |
| Examples | `div`, `p`, `h1`-`h6`, `ul`, `ol`, `li`, `section`, `header`, `footer`, `form`, `table` | `a`, `span`, `strong`, `em`, `img`, `code`, `button`, `input` |

```html
<p>This is a block. <strong>This is inline</strong> inside it.</p>
```

### `div` and `span`: the generic containers

| | `<div>` | `<span>` |
|---|---|---|
| Type | Block | Inline |
| Meaning | **None** | **None** |
| Use when | No semantic element fits, and you need a styling hook | Same, but within a line of text |

> ⚠️ **"Div soup":** a page made of nothing but `<div>`s. It works visually but tells browsers, search engines and screen readers nothing. Try the semantic element first (`header`, `nav`, `main`, `section`, `article`, `footer`) and use `div` as the *last* resort.

**Fun fact:** block vs inline is really a *CSS display* idea (`display: block` / `inline`). HTML5 officially groups elements into "content categories" (flow, phrasing, and so on), but block/inline is still the easiest mental model for now.

---

## 🪆 Nesting Rules

Elements go **inside** other elements. They must close in reverse order, like Russian dolls.

```html
<!-- ✅ Correct -->
<p>I <em>really <strong>love</strong></em> HTML.</p>

<!-- ❌ Overlapping -->
<p>I <em>really <strong>love</em></strong> HTML.</p>
```

### Things that can't go together

| ❌ Don't | Why |
|---|---|
| `<p>` inside `<p>` | The browser auto-closes the first one |
| `<div>` or `<ul>` inside `<p>` | `<p>` only allows inline content |
| `<a>` inside `<a>` | Links can't contain links |
| `<button>` inside `<a>` | Interactive element inside interactive element |
| Anything but `<li>` directly in `<ul>`/`<ol>` | Lists want list items |
| `<h2>` inside `<h1>` | Headings aren't containers |
| Block elements inside `<span>` | Inline containers shouldn't hold blocks |

### Good indentation = readable nesting

- Indent **2 spaces** (or 4, but pick one and stick to it).
- Every child is indented one level deeper than its parent.
- Closing tag lines up with its opening tag.
- Let a formatter (Prettier, VS Code "Format Document") do the work.

---

## 💬 Comments, Entities and Whitespace

### Comments

```html
<!-- This is a comment. Browsers ignore it, but anyone can read it in View Source. -->
```

Great for notes-to-self and temporarily disabling code. **Never put secrets in comments.**

### Character entities

Some characters have special meaning in HTML (`<` starts a tag), so you write them as entities:

| Character | Entity | Notes |
|---|---|---|
| `<` | `&lt;` | Less than |
| `>` | `&gt;` | Greater than |
| `&` | `&amp;` | Ampersand |
| `"` | `&quot;` | Double quote |
| ` ` | `&nbsp;` | Non-breaking space (use sparingly) |
| `©` | `&copy;` | Copyright |
| `—` | `&mdash;` | Em dash |

### Whitespace gets collapsed

HTML squashes any run of spaces, tabs and line breaks into **one single space**:

```html
<p>Hello          world
and     goodbye</p>
<!-- Renders as: Hello world and goodbye -->
```

So extra spaces and blank lines in source code won't create spacing on the page. For that, use CSS (or `<pre>` for preformatted text).

---

## 💥 Mistakes I Actually Made

Honesty section. These came out of reviewing my own first batch of examples:

| # | Mistake | What it does | The fix |
|---|---|---|---|
| 1 | Doubled quote: `cite="url""` | Parser error, browser guesses its way out | One closing quote only |
| 2 | Forgot the viewport `<meta>` in most pages | Phones show a tiny desktop layout | Add it to my starter template |
| 3 | Used `<div>` for everything (Bookstore) | No meaning for screen readers or search | `main`, `article`, `header` |
| 4 | `<button>` with no `type` | Defaults to `submit` inside forms, which can send the form by accident | Always `type="button"` or `type="submit"` |
| 5 | Identical "Buy Now" buttons | A screen reader can't tell which book | `aria-label="Buy Sally's SciFi Adventure"` |
| 6 | Linked image with alt describing the picture | Link purpose unclear | Alt describes where the link goes |
| 7 | Space inside the link: `Email:<a> fake@…</a>` | Underline starts with a gap | Space goes outside the `<a>` |
| 8 | Missing `scope` on table headers | Cell/header association unclear | `<th scope="col">` |
| 9 | Inconsistent indentation and attribute wrapping | Hard to read my own code | Format on save |
| 10 | Media with no captions or fallback text | Inaccessible to some users | `<track kind="captions">` and fallback text |

> 🧪 Mistakes aren't failures. They're the damage report that makes Mark II better.

---

## 🧾 Cheat Sheet

### Starter template (copy me)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Descriptive Title Here</title>
  </head>
  <body>
    <header>
      <h1>Page Title</h1>
      <nav>
        <ul>
          <li><a href="#section-one">Section One</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="section-one">
        <h2>Section One</h2>
        <p>Content goes here.</p>
      </section>
    </main>

    <footer>
      <p>&copy; 2026 Me</p>
    </footer>
  </body>
</html>
```

### Quick reference

| I want to... | Use |
|---|---|
| Add a main title | `<h1>` |
| Write a paragraph | `<p>` |
| Make something important | `<strong>` |
| Stress a word | `<em>` |
| Make a bulleted list | `<ul>` + `<li>` |
| Make a numbered list | `<ol>` + `<li>` |
| Link somewhere | `<a href="...">` |
| Show a picture | `<img src alt>` |
| Caption a picture | `<figure>` + `<figcaption>` |
| Quote someone | `<q>` or `<blockquote>` |
| Group things with no better tag | `<div>` or `<span>` |
| Add a line break | `<br>` |
| Add a thematic divider | `<hr>` |
| Leave a note in the code | `<!-- comment -->` |

### Pre-flight checklist ✅

Before I call a page "done":

- [ ] `<!DOCTYPE html>` is first
- [ ] `<html lang="...">` is set
- [ ] `charset` and `viewport` meta tags are present
- [ ] `<title>` is unique and descriptive
- [ ] Exactly one `<h1>`, and no skipped heading levels
- [ ] Every `<img>` has thought-out `alt`
- [ ] Every link text makes sense out of context
- [ ] Nothing is nested illegally; all tags are closed
- [ ] Every form input has a `<label>`
- [ ] `div` is used only when no semantic tag fits
- [ ] The page passes the [W3C validator](https://validator.w3.org/)
- [ ] Code is indented and formatted consistently

---

## 🎮 Practice Ideas

Level up from Mark I:

1. 🌱 **Rebuild from memory.** Write the page skeleton with no peeking. Repeat until it's muscle memory.
2. 🌱 **About-me page.** Headings, paragraphs, a list of hobbies, one image with real alt text.
3. 🔧 **Recipe page.** `ol` for steps, `ul` for ingredients, `figure` for the photo.
4. 🔧 **Link maze.** Make 3 pages that link to each other with relative paths. Break a path on purpose and watch what happens.
5. 🔧 **Break the validator.** Intentionally write invalid HTML (overlapping tags, doubled quotes), run it through the validator, and read every error.
6. 🚀 **Semantic rewrite.** Take my Bookstore `div` page and rewrite it with proper semantic tags.
7. 🚀 **Document outline.** Write a long article using only `h1`-`h4` correctly, then check the outline in DevTools.

---

## 🛠️ Tools

| Tool | What it's for |
|---|---|
| 🔍 **Browser DevTools** (`F12`) | Inspect the DOM, see the real structure the browser built |
| 👁️ **View Source** (`Ctrl+U`) | See the raw HTML the server sent |
| ✅ [W3C Validator](https://validator.w3.org/) | Catch syntax errors |
| 📖 [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML) | The best HTML reference out there |
| 🎓 [freeCodeCamp](https://www.freecodecamp.org/) | Where my workshop practice came from |
| 💅 **Prettier** (VS Code extension) | Auto-formats and indents on save |
| ♿ **Lighthouse** (in DevTools) | Quick accessibility and best-practice audit |

---

## 🔗 Related

- 🏛️ [`semantic-html.md`](./semantic-html.md): picking the right element for the job
- 📝 [`forms.md`](./forms.md): inputs, labels, and validation
- ♿ [`accessibility.md`](./accessibility.md): building for everyone
- 🖼️ [`media-and-links.md`](./media-and-links.md): images, audio, video, and paths in depth
- 🧪 [`examples/`](./examples): where every concept above got built (and broken)
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>Every great suit starts with a solid frame. Mark I is done. On to Mark II. 🦾</i></p>
