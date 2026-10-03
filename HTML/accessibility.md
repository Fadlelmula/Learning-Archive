# ♿ Accessibility

> Build for everyone, not just my screen.
> Mark IV of the armor: a suit that only fits one pilot isn't a suit, it's a costume.

![Topic](https://img.shields.io/badge/topic-accessibility-E34F26?logo=html5&logoColor=white)
![Level](https://img.shields.io/badge/level-must%20know-red)
![Status](https://img.shields.io/badge/status-reading%20%2B%20practicing-yellow)
![Standard](https://img.shields.io/badge/standard-WCAG%202.2%20AA-blue)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-lightgrey)

---

## 🗂️ Table of Contents

1. [What accessibility is](#-what-accessibility-is)
2. [Why it matters](#-why-it-matters)
3. [The four principles](#-the-four-principles)
4. [Start with semantic HTML](#-start-with-semantic-html)
5. [Text alternatives](#-text-alternatives)
6. [Page structure and navigation](#-page-structure-and-navigation)
7. [Keyboard accessibility](#-keyboard-accessibility)
8. [Color, contrast and visual design](#-color-contrast-and-visual-design)
9. [Links and buttons](#-links-and-buttons)
10. [Forms and tables](#-forms-and-tables)
11. [Audio and video](#-audio-and-video)
12. [ARIA in practice](#-aria-in-practice)
13. [Hiding things the right way](#-hiding-things-the-right-way)
14. [Screen readers 101](#-screen-readers-101)
15. [How to test](#-how-to-test)
16. [Audit of my own examples](#-audit-of-my-own-examples)
17. [Mistakes I actually made](#-mistakes-i-actually-made)
18. [Cheat sheet](#-cheat-sheet)
19. [Practice ideas](#-practice-ideas)
20. [Tools](#-tools)
21. [Related](#-related)

---

## 🧠 What Accessibility Is

**Accessibility (a11y)** means making websites usable by as many people as possible, including people who:

| Area | Examples | How they might browse |
|---|---|---|
| 👁️ **Vision** | Blindness, low vision, color blindness | Screen readers, zoom, high contrast, braille displays |
| 👂 **Hearing** | Deafness, hard of hearing | Captions, transcripts |
| 🖐️ **Motor** | Tremors, paralysis, missing limbs, RSI | Keyboard only, switch devices, voice control, eye tracking |
| 🧩 **Cognitive** | Dyslexia, ADHD, memory or attention differences | Clear layout, plain language, no time pressure, reader modes |
| 🌱 **Temporary** | Broken arm, eye surgery, ear infection | Same tools as above |
| 🌍 **Situational** | Bright sunlight, noisy train, holding a baby, slow connection | Captions, keyboard, big tap targets |

> 💡 "a11y" = **a**, then 11 letters, then **y**. It's a numeronym, like i18n for internationalization.

Accessibility isn't a special mode for a small group. Everyone is temporarily or situationally limited at some point. Good accessible design makes the web better for all of us (captions help in noisy cafés, keyboard shortcuts help power users, clear contrast helps in sunlight).

---

## 🎯 Why It Matters

| Reason | Details |
|---|---|
| 🤝 **It's the right thing** | The web is for everyone. According to the WHO, roughly 1 in 6 people worldwide lives with a significant disability. |
| ⚖️ **It's often the law** | Many countries require accessible websites (for example the ADA in the US, the European Accessibility Act, and local regulations elsewhere). Rules vary, so check the ones that apply. |
| 🔍 **It helps SEO** | Semantic structure, descriptive links, and alt text help search engines too |
| 💼 **It's a hiring skill** | Employers increasingly expect front-end developers to know it |
| 🧹 **It makes code better** | Accessible code tends to be cleaner, more semantic, and easier to maintain |
| 💰 **It widens the audience** | More people can use (and buy from) the site |

---

## 🏛️ The Four Principles

The **WCAG** (Web Content Accessibility Guidelines) are organized around four principles, remembered as **POUR**:

| Principle | Meaning | Examples |
|---|---|---|
| 👁️ **P**erceivable | Users can *perceive* the content | Alt text, captions, enough contrast, resizable text |
| 🖱️ **O**perable | Users can *operate* the interface | Keyboard access, enough time, no seizure-causing flashes, clear focus |
| 🧭 **U**nderstandable | Users can *understand* content and how the UI works | Plain language, predictable behavior, clear error messages |
| 🔩 **R**obust | Works with many browsers and assistive technologies | Valid HTML, correct semantics, proper ARIA |

### WCAG levels

| Level | Meaning |
|---|---|
| **A** | Bare minimum. Without it, some people are blocked completely. |
| **AA** | The standard target for most sites and the one laws usually reference |
| **AAA** | Highest level. Great goal, but not always possible for everything. |

The current version is **WCAG 2.2** (published October 2023). It adds things like minimum touch target size, focus that isn't hidden behind other content, and easier authentication. **My target: AA.**

---

## 🧱 Start with Semantic HTML

The biggest accessibility win costs nothing: **use the right element.**

| Instead of... | Use | Free benefit |
|---|---|---|
| `<div onclick>` | `<button>` | Keyboard focus, Enter/Space, correct announcement |
| `<div class="nav">` | `<nav>` | Navigation landmark |
| `<span class="big-bold">` | `<h2>` | Heading navigation |
| `<div>`s in rows | `<table>` with `th` | Cell/header association |
| Line breaks as list | `<ul>` + `<li>` | "List of 5 items" announced |
| Text above an input | `<label for>` | Input is named and clickable |

> 📌 More detail in [`semantic-html.md`](./semantic-html.md). Rule of thumb: **if HTML has a native element for it, use it before reaching for ARIA.**

---

## 🖼️ Text Alternatives

Anything that isn't text needs a text equivalent.

### Images: choosing the alt text

| Situation | Alt text |
|---|---|
| Informative image | Describe what matters in context: `alt="Orange cat asleep on a laptop keyboard"` |
| Decorative image | Empty: `alt=""` so screen readers skip it |
| Image inside a link | Describe the **destination or action**: `alt="Cat photos gallery"` |
| Image of text (like a logo with words) | The same words: `alt="XYZ Bookstore"` |
| Chart or diagram | Short alt + a longer description nearby (or in the text) |
| Icon-only button | Name the button: `aria-label="Close"` or visually hidden text |

Alt text dos and don'ts:

- ✅ Keep it concise (a sentence or two).
- ✅ Think "what would I say if I read this page aloud to someone?"
- ❌ Don't start with "image of" or "picture of."
- ❌ Don't stuff keywords.
- ❌ Never leave `alt` off. A missing `alt` makes some screen readers read out the file name.

### Icons and SVG

```html
<!-- Icon-only button: give it a name -->
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24">…</svg>
</button>

<!-- Meaningful standalone SVG -->
<svg role="img" aria-labelledby="chart-title" viewBox="0 0 200 100">
  <title id="chart-title">Sales rose 20% in 2026</title>
  …
</svg>
```

---

## 🗺️ Page Structure and Navigation

### Basics every page needs

| Item | Why |
|---|---|
| `<html lang="en">` | Screen readers pick the right pronunciation |
| A unique, descriptive `<title>` | It's the first thing a screen reader reads, and it labels the tab |
| One `<h1>`, ordered headings | Headings are the page's table of contents |
| Landmarks: `header`, `nav`, `main`, `footer` | Users jump between them |
| A skip link | Lets keyboard users bypass the menu |

### Marking language changes

```html
<p>The French say <span lang="fr">c'est la vie</span>.</p>
```

### The skip link

```html
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header>…long navigation…</header>
  <main id="main" tabindex="-1">…</main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
  background: #fff;
  padding: 0.5rem 1rem;
  z-index: 1000;
}
```

It's invisible until a keyboard user presses `Tab` the first time. Then it appears and lets them jump past the whole menu.

### Headings and landmarks quick-check

- Can I read just the headings and understand the page?
- Is there exactly one `<main>`?
- Do multiple `<nav>`s have distinct `aria-label`s?

---

## ⌨️ Keyboard Accessibility

Many people never touch a mouse: screen reader users, people with motor disabilities, and power users. **Everything a mouse can do, a keyboard must be able to do.**

### Keys to know

| Key | Action |
|---|---|
| `Tab` / `Shift + Tab` | Move focus forward / back |
| `Enter` | Activate links and buttons |
| `Space` | Activate buttons, toggle checkboxes, scroll |
| `Arrow keys` | Move within radios, selects, menus, tabs |
| `Esc` | Close dialogs, menus, popups |

### Focus rules

| Rule | Details |
|---|---|
| **Natural order** | Tab order follows the order in the HTML. Write the DOM in a logical order. |
| **Visible focus** | The user must always see where they are. **Never** use `outline: none` without a replacement. |
| **No keyboard traps** | If you can Tab in, you must be able to Tab (or Esc) out |
| **Don't hide focused things** | Sticky headers shouldn't cover the focused element |

```css
/* ✅ A clear, custom focus style */
:focus-visible {
  outline: 3px solid #1a73e8;
  outline-offset: 2px;
}
```

### `tabindex` cheat sheet

| Value | Effect | Use? |
|---|---|---|
| `tabindex="0"` | Adds a non-interactive element to the Tab order | Rarely; prefer a native control |
| `tabindex="-1"` | Focusable by script only, not by Tab | ✅ For focus management (like the `<main>` skip target) |
| `tabindex="1"` or higher | Forces a custom order | ❌ **Never.** It breaks the natural order. |

### Native elements are already keyboard friendly

`<a href>`, `<button>`, `<input>`, `<select>`, `<textarea>`, `<summary>`, and `<dialog>` all work with the keyboard out of the box. A `div` with an `onclick` does not.

---

## 🎨 Color, Contrast and Visual Design

### Contrast ratios (WCAG AA)

| Content | Minimum ratio |
|---|---|
| Normal text | **4.5 : 1** |
| Large text (about 24px, or 18.5px bold) | **3 : 1** |
| UI components and graphics (borders, icons, focus ring) | **3 : 1** |
| AAA level for normal text | 7 : 1 |

Light grey text on white is the classic offender. Test colors with a contrast checker before committing to them.

### Never use color alone

```html
<!-- ❌ Only color shows the error -->
<input style="border-color: red">

<!-- ✅ Color + text + icon -->
<input aria-invalid="true" aria-describedby="err">
<p id="err">⚠️ Enter a valid email, like name@example.com</p>
```

Roughly 1 in 12 men has some form of color vision deficiency, so "the red one" isn't a safe instruction.

### Respect user preferences

```css
/* Reduce motion for people who get dizzy from animation */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  :root { --bg: #111; --text: #eee; }
}
```

### Text and zoom

| Do ✅ | Don't ❌ |
|---|---|
| Size text in `rem`/`em` | Lock text in tiny `px` values everywhere |
| Support 200% zoom with no loss of content | Break the layout at larger sizes |
| Reflow to one column at about 320px width | Force sideways scrolling for text |
| Use readable line length and spacing | Cram long lines of tight text |
| Allow pinch-zoom | `user-scalable=no` or `maximum-scale=1` in the viewport tag |

### Touch targets

- WCAG 2.2 AA requires targets of at least **24 × 24 CSS px** (or enough spacing).
- Around **44 × 44 px** is a comfortable size for fingers.

### Motion and flashing

- Nothing may flash more than 3 times per second (seizure risk).
- Moving or auto-updating content lasting more than 5 seconds needs a way to pause, stop, or hide it.

---

## 🔗 Links and Buttons

| Rule | Example |
|---|---|
| Link text makes sense **out of context** | ✅ "Download the 2026 report (PDF)" ❌ "Click here" |
| Links go places, buttons do things | `<a href>` navigates, `<button>` acts |
| Links inside text are visually distinct | Underline them, not just a color change |
| Warn about new tabs/files | `Read more (opens in a new tab)` |
| Same name = same destination | Two "Read more" links to different pages are confusing |
| Buttons have clear unique names | `aria-label="Buy Sally's SciFi Adventure"` |

```html
<a href="report.pdf">Download the 2026 report (PDF, 2 MB)</a>

<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  Example site (opens in a new tab)
</a>
```

> 🧠 Screen reader users often pull up a **list of all links** on the page. If it says "click here, click here, read more, read more," it's useless.

---

## 📝 Forms and Tables

Full details are in [`forms.md`](./forms.md). The accessibility highlights:

### Forms

| Do ✅ | Why |
|---|---|
| Visible `<label for>` on every control | Names the field, enlarges the click area |
| `fieldset` + `legend` for radio and checkbox groups | Gives each option its context |
| Mark required and optional fields in text | Not by color alone |
| Link hints/errors with `aria-describedby` | Read with the field |
| Correct `type` and `autocomplete` | Easier input, especially for motor and cognitive disabilities |
| Specific error messages | "Password needs at least 8 characters" beats "Invalid input" |
| Don't clear the form on error | Don't make people retype everything |

### Announcing errors

```html
<label for="email">Email</label>
<input type="email" id="email" name="email"
       aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Enter an email like name@example.com.</p>
```

### Tables

```html
<table>
  <caption>Exam results, Term 1</caption>
  <thead>
    <tr>
      <th scope="col">Student</th>
      <th scope="col">Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Alex</th>
      <td>54</td>
    </tr>
  </tbody>
</table>
```

- Use tables for **data only**, never for layout.
- `<caption>` names the table, `scope` ties headers to cells.
- Keep tables simple; avoid merged cells where possible.

---

## 🎬 Audio and Video

| Need | Solution |
|---|---|
| Deaf or hard of hearing users | **Captions** for video; **transcripts** for audio |
| Blind users | **Audio description** for important visuals; a text alternative |
| Users who dislike surprises | **No autoplay with sound**; give controls |
| Everyone | Keyboard-operable player, volume control, pause |

### Adding captions with `<track>`

```html
<video controls width="640" poster="poster.jpg">
  <source src="demo.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English" default>
  <p>Your browser doesn't support video. <a href="demo.mp4">Download it here</a>.</p>
</video>
```

A minimal WebVTT caption file (`captions-en.vtt`):

```
WEBVTT

00:00:01.000 --> 00:00:04.000
Welcome to the demo.

00:00:04.500 --> 00:00:08.000
Today we're building an accessible page.
```

### Audio

```html
<audio controls src="song.mp3">
  Your browser doesn't support audio. <a href="song.mp3">Download the track</a>.
</audio>
<p><a href="song-transcript.html">Read the transcript</a></p>
```

Also: if audio plays automatically for more than 3 seconds, the user needs a way to pause or mute it. Better yet, don't autoplay.

---

## 🆘 ARIA in Practice

**ARIA** adds accessibility information that plain HTML can't express. It only changes what assistive tech *hears*, not what the browser *does*, so it never adds keyboard behavior.

### The rules

1. **Use a native element if one exists.** `<button>` beats `<div role="button">`.
2. **Don't change native semantics** unless you really must (no `<h2 role="button">`).
3. **All ARIA controls must work with the keyboard.**
4. **Don't hide focusable elements** with `aria-hidden="true"`.
5. **Every interactive element needs an accessible name.**

### Roles, states and properties

| Kind | Examples | Purpose |
|---|---|---|
| **Role** | `role="alert"`, `role="status"`, `role="dialog"` | What the thing *is* |
| **State** | `aria-expanded`, `aria-checked`, `aria-current`, `aria-invalid` | What it's doing *right now* (changes) |
| **Property** | `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-controls` | Extra info (usually stable) |

### Accessible names: which to use?

| Attribute | When |
|---|---|
| Visible text / `<label>` | **Preferred.** Always first choice. |
| `aria-labelledby="id"` | Name comes from other visible text on the page |
| `aria-label="text"` | No visible text exists (icon buttons, repeated `nav`) |
| `aria-describedby="id"` | Extra description or hints (not the name) |

### Live regions: announcing changes

When content changes without a page load (a form error, a "Added to cart" message), screen readers won't notice unless told.

| Markup | Behavior |
|---|---|
| `role="status"` (or `aria-live="polite"`) | Announced when the user is idle. Good for confirmations. |
| `role="alert"` (or `aria-live="assertive"`) | Interrupts immediately. Only for urgent errors. |

```html
<p role="status" id="cart-msg"></p>
<!-- JS later sets: cart-msg.textContent = "Added to cart" -->
```

The live region should exist in the page **before** the message is inserted.

### State example: a toggle button

```html
<button type="button" aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>…</ul>
```

JavaScript flips `aria-expanded` to `"true"` and removes `hidden`.

### Current page in navigation

```html
<nav aria-label="Main">
  <a href="/" aria-current="page">Home</a>
  <a href="/about">About</a>
</nav>
```

---

## 🙈 Hiding Things the Right Way

Different techniques hide things from different audiences:

| Technique | Hidden from sighted users | Hidden from screen readers | Removed from Tab order |
|---|---|---|---|
| `display: none` / `visibility: hidden` / `hidden` attribute | ✅ | ✅ | ✅ |
| `aria-hidden="true"` | ❌ (still visible) | ✅ | ❌ (**still focusable, so don't use on focusable things**) |
| Visually hidden class (below) | ✅ | ❌ (still read) | ❌ (still focusable if interactive) |
| `opacity: 0` | ✅ | ❌ | ❌ |

### The "screen reader only" class

For text that sighted users don't need but screen reader users do:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

```html
<button type="button">
  <svg aria-hidden="true">…</svg>
  <span class="sr-only">Add to wishlist</span>
</button>
```

---

## 🔊 Screen Readers 101

A screen reader turns the page into speech (or braille). It reads the **accessibility tree**, which the browser builds from the HTML.

| Screen reader | Platform | Cost |
|---|---|---|
| **NVDA** | Windows | Free |
| **JAWS** | Windows | Paid |
| **Narrator** | Windows | Built in |
| **VoiceOver** | macOS / iOS | Built in |
| **TalkBack** | Android | Built in |
| **Orca** | Linux | Free |

### How people actually use them

| They navigate by... | Which only works if I used... |
|---|---|
| Headings (`H` key in NVDA/JAWS) | Real `<h1>`-`<h6>` in order |
| Landmarks | `header`, `nav`, `main`, `footer` |
| List of links | Descriptive link text |
| Form fields | Labels and fieldsets |
| Tables | `th`, `scope`, `caption` |
| Buttons | Real `<button>` elements with clear names |

### What it announces

For `<button type="button" aria-expanded="false">Menu</button>` you might hear: **"Menu, button, collapsed."** Name + role + state. If any of those three is missing or wrong, the user is guessing.

---

## 🧪 How to Test

Automated tools catch only *some* problems (missing alt, low contrast, missing labels). They can't tell if alt text is *good* or the order is *logical*. Use all of these layers:

| Layer | What to do |
|---|---|
| 🤖 **Automated** | Run Lighthouse, axe, or WAVE and fix what they flag |
| ⌨️ **Keyboard-only** | Unplug the mouse. Tab through everything. Can I reach, see, and operate every control? |
| 🔎 **Zoom** | Zoom to 200% and 400%. Does anything overlap or vanish? |
| 🎨 **Contrast** | Check text and UI colors with a contrast checker |
| 🌓 **Preferences** | Turn on dark mode, reduced motion, and high contrast |
| 🔊 **Screen reader** | Navigate by headings, landmarks and forms. Is it understandable? |
| 📴 **CSS off** | Does the reading order still make sense? |
| 👥 **Real users** | The gold standard. Nothing replaces feedback from people with disabilities. |

### My 5-minute test routine

1. Run Lighthouse (DevTools → Lighthouse → Accessibility).
2. Tab through the whole page. Is focus always visible?
3. Zoom to 200%.
4. Check the headings outline.
5. Read the page with a screen reader for one minute.

---

## 🔍 Audit of My Own Examples

A quick accessibility pass over my practice pages (see [`examples/`](./examples)):

| Project | ✅ Good | ⚠️ To fix |
|---|---|---|
| **Cat Blog** | Strong landmarks (`header`, `nav`, `main`, `article`, `footer`), `address`, sensible headings, alt text | Space inside the email link; add viewport meta |
| **Cat Photo App** | `figure`/`figcaption`, `strong`/`em` for meaning | Linked image's alt describes the image, not the destination; add `rel` to `target="_blank"` links |
| **XYZ Bookstore** | Clear text on buttons | Div soup; identical "Buy Now" buttons need unique names; buttons need `type`; no `main` |
| **Music Player** | Native `controls` | No `main`; no fallback text; no transcript |
| **Video Player** | `poster`, `preload`, multiple sources, fallback link | **No `<track>` captions**; no `main` |
| **Job Tips Page** | Real `blockquote`/`q`/`cite` markup | Quote attribution should use `figure`/`figcaption`; fix the stray quote in a `cite` attribute |
| **Hotel Feedback Form** | Every input has a matching label; `fieldset` + `legend` | Radios not required; dropdown pre-selected; no `autocomplete`; no viewport |
| **Exam Table** | `caption`, `thead`, `tbody`, `tfoot` | Add `scope` to headers; no viewport |

> 🧪 Pattern I notice: my biggest gaps are **captions, unique button names, landmarks (`main`), and `scope` on tables.** Easy fixes, big wins.

---

## 💥 Mistakes I Actually Made

| # | Mistake | Impact | The fix |
|---|---|---|---|
| 1 | Thought alt text was just "describe the picture" | Linked images don't explain where the link goes | Describe the **purpose** |
| 2 | Skipped `<track>` captions on the video | Deaf users miss the whole video | Add WebVTT captions |
| 3 | Used identical button text for different items | Screen reader users can't tell them apart | Unique `aria-label` |
| 4 | Left out `<main>` | No landmark to jump to | One `<main>` per page |
| 5 | Forgot `scope` on table headers | Cell/header link is ambiguous | `scope="col"` / `scope="row"` |
| 6 | Used a form default that biased the answer | Everyone's "Excellent" | Blank first option |
| 7 | Treated ARIA as a magic fix | Wrong ARIA is worse than none | Native element first |
| 8 | Thought accessibility was a "final polish" step | Retrofitting is painful | Build it in from the start |
| 9 | Forgot the viewport meta tag | Poor experience on phones and with zoom | Put it in my template |

---

## 🧾 Cheat Sheet

### Quick wins by effort

| Effort | Action |
|---|---|
| 🟢 **5 seconds** | `<html lang="en">`, a descriptive `<title>`, and a viewport meta tag |
| 🟢 **1 minute** | Add `alt` to every image; add `type` to every button |
| 🟡 **5 minutes** | Add `<main>`, `<nav>`, `<header>`, `<footer>` landmarks |
| 🟡 **10 minutes** | Fix heading order; add labels to every input |
| 🟠 **30 minutes** | Add a skip link, visible focus styles, table `scope`s |
| 🔴 **Hour+** | Captions and transcripts for media; full screen reader pass |

### Pre-flight checklist ✅

**Structure**
- [ ] `lang` on `<html>`; unique descriptive `<title>`
- [ ] One `<h1>`; headings in order
- [ ] Landmarks: `header`, `nav`, `main`, `footer`; multiple `nav`s labelled
- [ ] Skip link present

**Content**
- [ ] Every `<img>` has appropriate `alt` (empty if decorative)
- [ ] Link text makes sense out of context
- [ ] Language changes are marked with `lang`
- [ ] Plain, clear language

**Interaction**
- [ ] Everything works with the keyboard
- [ ] Focus is always visible; no keyboard traps
- [ ] No positive `tabindex`
- [ ] Buttons are `<button>`, links are `<a href>`
- [ ] Buttons have explicit `type` and unique, clear names

**Visual**
- [ ] Text contrast ≥ 4.5:1 (large text and UI ≥ 3:1)
- [ ] Color is never the only signal
- [ ] Page works at 200% zoom and 320px width
- [ ] Zoom is not disabled
- [ ] `prefers-reduced-motion` respected

**Forms and data**
- [ ] Every input has a connected `<label>`
- [ ] Radio/checkbox groups use `fieldset` + `legend`
- [ ] Errors are specific and linked to their fields
- [ ] Tables have `caption` and `th scope`

**Media**
- [ ] Video has captions; audio has a transcript
- [ ] No autoplay with sound
- [ ] Media controls are keyboard accessible

**ARIA**
- [ ] No ARIA where a native element works
- [ ] No `aria-hidden` on focusable elements
- [ ] Dynamic messages use `role="status"` / `role="alert"`

---

## 🎮 Practice Ideas

1. 🌱 **Keyboard day.** Browse three websites using only the keyboard. Note what breaks.
2. 🌱 **Alt text workout.** Pick 10 images from news sites and write the alt text each *should* have.
3. 🌱 **Contrast hunt.** Find three real sites with bad contrast and calculate the ratios.
4. 🔧 **Fix the Bookstore.** Rewrite it with landmarks, unique button names, and proper headings.
5. 🔧 **Caption the video.** Write a WebVTT file for the Video Player example and add `<track>`.
6. 🔧 **Table makeover.** Add `scope`, `caption`, and a clear structure to the Exam Table.
7. 🔧 **Build a skip link** and a visible `:focus-visible` style for every project.
8. 🚀 **Screen reader tour.** Install NVDA (free), then navigate my own examples by headings, landmarks, and forms.
9. 🚀 **Zoom torture test.** Zoom to 400% on every example. Fix what breaks.
10. 🚀 **Accessible tabs/accordion.** Build one with `<details>` first, then (later, with JavaScript) as a custom widget using ARIA.
11. 🚀 **Audit a real site** with axe, then explain each issue in my own words.

---

## 🛠️ Tools

| Tool | What it's for |
|---|---|
| ♿ **Lighthouse** (DevTools) | Quick accessibility score and issues list |
| 🧪 [axe DevTools](https://www.deque.com/axe/) | Browser extension; precise issue explanations |
| 👁️ [WAVE](https://wave.webaim.org/) | Visual overlay of errors, landmarks, and structure |
| 🎨 [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Check color pairs against WCAG ratios |
| 🔍 **DevTools → Accessibility panel** | See the accessibility tree and computed names/roles |
| ✅ [W3C Validator](https://validator.w3.org/) | Valid HTML is the foundation for accessibility |
| 🔊 [NVDA](https://www.nvaccess.org/) | Free Windows screen reader |
| 🍎 **VoiceOver** (built into macOS/iOS) | `Cmd + F5` on Mac to start |
| 📖 [MDN: Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) | Excellent explanations |
| 📖 [WCAG Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | Filterable list of all success criteria |
| 📖 [WebAIM](https://webaim.org/) | Practical articles and surveys |
| 📖 [A11y Project Checklist](https://www.a11yproject.com/checklist/) | A friendly, practical checklist |

---

## 🔗 Related

- 📄 [`basics.md`](./basics.md): tags, attributes, nesting, alt text basics
- 🏛️ [`semantic-html.md`](./semantic-html.md): the foundation of accessible markup
- 📝 [`forms.md`](./forms.md): labels, fieldsets, validation, and error handling
- 🖼️ [`media-and-links.md`](./media-and-links.md): images, audio, video, and link text in depth
- 🧪 [`examples/`](./examples): the practice pages audited above
- 🎨 [`../CSS`](../CSS): focus styles, contrast, and responsive design
- ⚡ [`../JavaScript`](../JavaScript): focus management and live updates
- 🧠 [`../UX`](../UX): inclusive design and usability
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>A suit that only one pilot can wear is a costume. Mark IV is built for everyone. 🦾</i></p>
