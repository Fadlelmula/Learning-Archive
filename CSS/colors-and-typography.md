# 🌈 Colors & Typography: Making Things Look Intentional

![Topic](https://img.shields.io/badge/topic-colors%20%26%20typography-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Difficulty](https://img.shields.io/badge/difficulty-Mark%20I-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Good color and type are the difference between "student project" and "Stark Industries demo." 🎩

⬅️ Previous: [box-model.md](./box-model.md) | ➡️ Next: [layout.md](./layout.md)

---

## 📍 Table of Contents

1. [Ways to write a color](#-ways-to-write-a-color)
2. [Transparency](#-transparency-alpha)
3. [Backgrounds and gradients](#-backgrounds-and-gradients)
4. [Contrast and accessibility](#-contrast-and-accessibility)
5. [CSS units](#-css-units-px-em-rem-and-friends)
6. [Custom properties (variables)](#-custom-properties-css-variables)
7. [Fonts](#-fonts)
8. [Text properties](#-text-properties)
9. [Fluid type](#-fluid-type-with-clamp)
10. [Practice](#-practice-challenges)

---

## 🎨 Ways to Write a Color

| Format | Example | Best for |
|---|---|---|
| **Named** | `crimson`, `ivory`, `tomato` | Quick tests (about 140 names exist) |
| **Hex** | `#dc143c`, `#fff` | The most common format |
| **RGB** | `rgb(220, 20, 60)` | When thinking in red/green/blue amounts |
| **HSL** | `hsl(348, 83%, 47%)` | Making variations. Easy to tweak. |

```
Hex:   #  DC  14  3C
          │   │   │
          R   G   B      (each is 00–FF, i.e. 0–255)
```

### HSL: the "human-friendly" one

```
hsl( HUE , SATURATION , LIGHTNESS )
      │         │            │
      │         │            └─ 0% black → 50% pure color → 100% white
      │         └────────────── 0% gray → 100% vivid
      └──────────────────────── 0–360° around the color wheel
```

| Hue | Color |
|---|---|
| 0° | 🔴 Red |
| 60° | 🟡 Yellow |
| 120° | 🟢 Green |
| 180° | 🔵 Cyan |
| 240° | 🔵 Blue |
| 300° | 🟣 Magenta |

> 💡 Want a darker shade of the same color? Keep hue and saturation, lower the lightness. That's why HSL is lovely for palettes.

---

## 👻 Transparency (Alpha)

```css
.overlay {
  background: rgb(0 0 0 / 50%);        /* modern syntax */
  background: rgba(0, 0, 0, 0.5);      /* older syntax, still works everywhere */
}
```

| Property | What gets transparent? |
|---|---|
| `rgba()` / alpha in the color | Only that color |
| `opacity: 0.5` | The **whole element**, text and children too |

---

## 🖼️ Backgrounds and Gradients

```css
.hero {
  background-color: #111;
  background-image: linear-gradient(135deg, #111 0%, #8b0000 100%);
}
```

| Property | Purpose |
|---|---|
| `background-color` | Solid fill |
| `background-image` | `url(...)` or a gradient |
| `background-size` | `cover` (fill, may crop) or `contain` (fit, may leave gaps) |
| `background-position` | `center`, `top left`, etc. |
| `background-repeat` | `no-repeat` stops tiling |

```css
.banner {
  background: url("hero.jpg") center / cover no-repeat;
}
```

---

## ♿ Contrast and Accessibility

Color alone isn't enough. Text must be readable against its background.

| WCAG level | Normal text | Large text (about 24px, or 19px bold) |
|---|---|---|
| **AA** (the common target) ✅ | 4.5 : 1 | 3 : 1 |
| **AAA** (stricter) | 7 : 1 | 4.5 : 1 |

Rules to live by:

- ✅ Check contrast with a tool (browser DevTools shows the ratio in the color picker)
- ✅ Don't rely on color **alone** to communicate (add icons or text for errors)
- ✅ Test dark text on light *and* light text on dark

---

## 📏 CSS Units: px, em, rem and Friends

| Unit | Relative to | Good for |
|---|---|---|
| `px` | Fixed pixels | Borders, shadows, fine details |
| `rem` ✅ | Root (`html`) font size | Font sizes, spacing (respects user settings) |
| `em` | The element's font size (or the parent's, when used for `font-size`) | Component-relative spacing |
| `%` | The parent's value | Widths, fluid layouts |
| `vw` / `vh` | 1% of viewport width / height | Full-screen sections |
| `dvh` | Dynamic viewport height | Mobile browsers with moving address bars |
| `ch` | Width of the "0" character | Readable line lengths, e.g. `max-width: 65ch` |
| `fr` | A fraction of free space | CSS Grid |

```
Browser default: 1rem = 16px

  1rem   = 16px
  1.5rem = 24px
  0.5rem = 8px
```

> 🧠 **Default plan:** `rem` for text and spacing, `px` for borders, `%`/`fr` for layout widths.

### em vs rem trap

```css
.parent { font-size: 2em; }   /* 2 × its parent */
.child  { font-size: 2em; }   /* 2 × .parent → compounds! */
```

`rem` always points at the root, so it never compounds. 🎯

---

## 🗂️ Custom Properties (CSS Variables)

Define once, reuse everywhere. Change one line to re-theme the whole site.

```css
:root {
  --obsidian: #0b0b0d;   /* placeholder values: swap in your real palette */
  --crimson:  #b3122f;
  --ash:      #c9ccd1;
  --ivory:    #f6f1e7;

  --font-body: "IBM Plex Sans", system-ui, sans-serif;
  --space: 1rem;
}

body {
  background: var(--obsidian);
  color: var(--ivory);
  font-family: var(--font-body);
}

a { color: var(--crimson); }
a:hover { color: var(--ivory); }
```

| Piece | Meaning |
|---|---|
| `:root` | The top of the document (like `html`, but higher specificity) |
| `--name` | Variable names **must** start with two dashes |
| `var(--name)` | Use the variable |
| `var(--name, fallback)` | Use `fallback` if the variable isn't defined |

### Bonus: automatic dark mode 🌙

```css
:root { --bg: #ffffff; --text: #111111; }

@media (prefers-color-scheme: dark) {
  :root { --bg: #0b0b0d; --text: #f6f1e7; }
}

body { background: var(--bg); color: var(--text); }
```

---

## 🔤 Fonts

### `font-family` and fallbacks

```css
body {
  font-family: "IBM Plex Sans", Arial, sans-serif;
  /*           ↑ first choice    ↑ backup  ↑ generic family (always end with one) */
}
```

| Generic family | Vibe | Example font |
|---|---|---|
| `serif` | Formal, bookish | Georgia |
| `sans-serif` | Clean, modern | Arial |
| `monospace` | Code | Courier New |
| `system-ui` | Looks native to the user's OS | (varies) |

> 💡 Multi-word font names need quotes: `"Open Sans"`.

### Loading a web font (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
```

```css
body { font-family: "IBM Plex Sans", sans-serif; }
```

> ⚠️ Always keep fallback fonts. If the font fails to load, the page should still look decent.

---

## 📝 Text Properties

| Property | Common values | What it does |
|---|---|---|
| `font-size` | `1rem`, `1.25rem` | Text size |
| `font-weight` | `400` normal, `700` bold (100–900) | Thickness |
| `font-style` | `italic` | Slanted |
| `line-height` | `1.5` (no unit!) ✅ | Space between lines |
| `letter-spacing` | `0.05em` | Space between letters |
| `word-spacing` | `0.1em` | Space between words |
| `text-align` | `left`, `center`, `right`, `justify` | Horizontal alignment |
| `text-transform` | `uppercase`, `capitalize` | Changes case visually |
| `text-decoration` | `none`, `underline` | Remove or add underlines |
| `white-space` | `nowrap` | Stops wrapping |
| `max-width` | `65ch` | Keeps lines readable |

```
Line height visual:

line-height: 1.0      line-height: 1.5      line-height: 2.0
 Cramped text...       Comfortable text      Very airy text
 Cramped text...                             
                       Comfortable text      Very airy text
```

### Readability rules of thumb

- 📖 Body text: about 16px (`1rem`) or larger
- 📐 `line-height` of about 1.4 to 1.6 for paragraphs
- 📏 Line length of about 45 to 75 characters (`max-width: 65ch`)
- 🎭 Stick to 2 font families, maybe 3 at the very most

---

## 🪄 Fluid Type with `clamp()`

```css
h1 {
  font-size: clamp(1.75rem, 5vw, 3.5rem);
  /*         clamp( minimum , preferred , maximum ) */
}
```

```
Small screen:  grows from 1.75rem ─────────┐
Medium screen: scales smoothly with 5vw    ├─ never smaller than min,
Large screen:  stops growing at 3.5rem ────┘   never bigger than max
```

---

## 🏋️ Practice Challenges

- [ ] **Level 1:** Style a page using only named colors, then redo it in hex
- [ ] **Level 2:** Pick one hue and build 5 shades using HSL lightness
- [ ] **Level 3:** Move every color into `:root` variables
- [ ] **Level 4:** Add a Google Font with proper fallbacks
- [ ] **Level 5:** Check your text contrast in DevTools and fix anything below 4.5 : 1
- [ ] **Boss:** Build a dark/light theme switch using `prefers-color-scheme`

---

## ✅ Checklist: "Did It Click?"

- [ ] I can write the same color in hex, RGB and HSL
- [ ] I know the difference between `rem`, `em` and `px`
- [ ] I can define and use a CSS variable
- [ ] I know what contrast ratio to aim for
- [ ] I always add a fallback font stack

⬅️ Previous: [box-model.md](./box-model.md) | ➡️ Next: [layout.md](./layout.md)
