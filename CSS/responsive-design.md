# 📱 Responsive Design: One Page, Every Screen

![Topic](https://img.shields.io/badge/topic-responsive%20design-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Difficulty](https://img.shields.io/badge/difficulty-Mark%20IV-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Phones, tablets, laptops, ultrawide monitors, a fridge with a browser... the same HTML has to survive all of them. 📺➡️💻➡️📱

⬅️ Previous: [layout.md](./layout.md) | ➡️ Next: [animations.md](./animations.md)

---

## 📍 Table of Contents

1. [What "responsive" means](#-what-responsive-means)
2. [The viewport meta tag](#-step-zero-the-viewport-meta-tag)
3. [Mobile-first](#-mobile-first-thinking)
4. [Media queries](#-media-queries)
5. [Breakpoints](#-choosing-breakpoints)
6. [Fluid techniques](#-fluid-techniques-responsive-without-media-queries)
7. [Responsive images](#-responsive-images)
8. [Container queries](#-container-queries-the-new-hotness)
9. [User preference queries](#-media-queries-beyond-width)
10. [Testing](#-testing-your-work)
11. [Practice](#-practice-challenges)

---

## 🌊 What "Responsive" Means

A responsive page **adapts its layout to the space available**, instead of having a separate "mobile site."

```
 📱 Phone (≈ 375px)       💻 Laptop (≈ 1280px)

 ┌───────────┐            ┌──────────────────────────────┐
 │  Header   │            │ Header                       │
 ├───────────┤            ├────────┬─────────────────────┤
 │  Content  │            │ Side   │ Content             │
 ├───────────┤            │        │                     │
 │  Sidebar  │            ├────────┴─────────────────────┤
 ├───────────┤            │ Footer                       │
 │  Footer   │            └──────────────────────────────┘
 └───────────┘
   one column               two columns
```

The three ingredients of responsive design:

| Ingredient | What it is |
|---|---|
| 🔧 **Viewport meta tag** | Tells phones to use their real width |
| 💧 **Flexible layouts** | `%`, `fr`, `rem`, Flexbox, Grid |
| 🎚️ **Media queries** | Rules that apply only at certain sizes |

---

## 🚨 Step Zero: The Viewport Meta Tag

This goes in the HTML `<head>`. **Without it, phones pretend to be a ~980px-wide desktop and shrink everything.**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```
WITHOUT the tag:                WITH the tag:
┌───────┐                       ┌───────┐
│ ▪▪▪▪▪ │ ← tiny desktop page   │ Hello │ ← real size text
│ ▪▪▪▪▪ │   zoomed out          │ World │
└───────┘                       └───────┘
```

> 📌 This is one of the open fixes from my HTML folder. I'm putting it here too so I never skip it again.

---

## 🥇 Mobile-First Thinking

**Mobile-first** = write the small-screen styles as your default, then *add* styles as the screen gets bigger using `min-width`.

| | Mobile-first ✅ | Desktop-first |
|---|---|---|
| Base styles | Phone layout | Desktop layout |
| Media query | `min-width` (grows up) | `max-width` (shrinks down) |
| Result | Simpler CSS, lighter on phones | Lots of overriding |

```css
/* 📱 Base: phones. One column. */
.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* 💻 Wider screens: add columns */
@media (min-width: 768px) {
  .cards { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1100px) {
  .cards { grid-template-columns: repeat(3, 1fr); }
}
```

```
screen width ───────────────────────────────────────────────▶
0px          768px                  1100px
│  1 column  │      2 columns       │      3 columns       │
```

---

## 🎚️ Media Queries

```css
@media (condition) {
  /* rules that only apply when the condition is true */
}
```

| Condition | Meaning |
|---|---|
| `(min-width: 768px)` | Viewport is **768px or wider** |
| `(max-width: 767px)` | Viewport is **767px or narrower** |
| `(min-width: 600px) and (max-width: 900px)` | Between the two |
| `(orientation: landscape)` | Wider than tall |

```css
@media (min-width: 768px) and (orientation: landscape) { ... }
```

> 💡 Media queries add **no specificity**. They only turn rules on or off. Put them *after* the base rules so they win by source order.

---

## 📐 Choosing Breakpoints

Common starting points (not laws):

| Name | Width | Typical device |
|---|---|---|
| Small | up to 480px | Phones |
| Medium | 768px and up | Tablets |
| Large | 1024px and up | Laptops |
| X-Large | 1280px and up | Desktops |

> 🧠 **Better approach:** let the *content* choose. Drag your browser narrower. Where the layout breaks or looks ugly, **that's** your breakpoint. Don't chase specific phone models.

---

## 💧 Fluid Techniques (Responsive Without Media Queries)

Many layouts adapt on their own if you write them flexibly.

| Technique | Example | What it gives you |
|---|---|---|
| `max-width` instead of `width` | `max-width: 900px; margin: 0 auto;` | Shrinks on small screens, caps on big ones |
| Percentage widths | `width: 100%` | Fills the parent |
| Flex wrapping | `display: flex; flex-wrap: wrap; gap: 1rem;` | Items drop to the next row |
| Auto-fit grid | `repeat(auto-fit, minmax(220px, 1fr))` | Columns appear/disappear automatically ✨ |
| `clamp()` | `font-size: clamp(1rem, 2.5vw, 2rem);` | Fluid sizes with min/max limits |
| `min()` / `max()` | `width: min(100%, 600px);` | The smaller / larger of the two |
| Relative units | `rem`, `%`, `vw`, `ch` | Scales with context |

```css
.container {
  width: min(100% - 2rem, 1000px);   /* 1rem margin each side on small screens, capped at 1000px */
  margin-inline: auto;
}
```

---

## 🖼️ Responsive Images

The golden rule:

```css
img {
  max-width: 100%;   /* never wider than its container */
  height: auto;      /* keep the proportions */
  display: block;    /* removes the tiny gap under inline images */
}
```

### Cropping to fit

```css
.thumb {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;   /* fill the box, crop the overflow */
}
```

| `object-fit` | Behavior |
|---|---|
| `cover` | Fills the box, crops extra |
| `contain` | Fits whole image, may leave gaps |
| `fill` | Stretches (usually distorts 😬) |

### Different images for different screens (HTML)

```html
<picture>
  <source media="(min-width: 800px)" srcset="hero-large.jpg">
  <img src="hero-small.jpg" alt="Description of the image">
</picture>
```

> ♿ Always keep a meaningful `alt` on `<img>`. Responsive doesn't mean skipping accessibility.

---

## 📦 Container Queries (The New Hotness)

Media queries ask "how wide is the **screen**?" Container queries ask "how wide is the **parent**?" so a component adapts to wherever it's placed.

```css
.card-wrapper {
  container-type: inline-size;
}

.card { display: block; }

@container (min-width: 400px) {
  .card {
    display: flex;      /* side-by-side layout when its container is wide enough */
    gap: 1rem;
  }
}
```

```
Narrow container:          Wide container:
┌──────────┐               ┌──────────────────────────┐
│  [img]   │               │ [img]  Title             │
│  Title   │               │        Description...    │
│  Desc... │               └──────────────────────────┘
└──────────┘
```

> ⚠️ Support is good in modern browsers, but check [caniuse.com](https://caniuse.com) before relying on any newer feature.

---

## 👤 Media Queries Beyond Width

Responsive design also means respecting **user preferences**.

| Query | Detects | Use |
|---|---|---|
| `prefers-color-scheme: dark` | User likes dark mode 🌙 | Swap color variables |
| `prefers-reduced-motion: reduce` | User wants less animation | Turn off or soften animations |
| `hover: hover` | Device can really hover (mouse) | Only add hover effects where they make sense |
| `print` | Printing the page 🖨️ | Hide nav, use black on white |

```css
@media (hover: hover) {
  .card:hover { transform: translateY(-4px); }
}

@media print {
  nav, footer { display: none; }
}
```

---

## 🧪 Testing Your Work

1. Open DevTools (`F12`)
2. Toggle the **device toolbar** (`Ctrl/Cmd + Shift + M`)
3. Pick a preset device **and** drag the handle to resize freely
4. Test: 📱 narrow, 📱↔️ landscape, 💻 wide, and **zoomed to 200%**
5. Look for:
   - [ ] Horizontal scrollbars (almost always a bug 🐛)
   - [ ] Text too small to read
   - [ ] Tap targets too tiny (aim for about 44×44px)
   - [ ] Images overflowing their boxes

> ⚠️ DevTools emulation is great but isn't a real phone. Check on an actual device when you can.

---

## 🏋️ Practice Challenges

- [ ] **Level 1:** Add the viewport tag and watch a page change on a real phone or emulator
- [ ] **Level 2:** Make images responsive with `max-width: 100%`
- [ ] **Level 3:** Turn a 1-column list into 2 then 3 columns with `min-width` queries
- [ ] **Level 4:** Rebuild that same layout with `auto-fit` and `minmax` (zero media queries)
- [ ] **Level 5:** Use `clamp()` for headings
- [ ] **Boss:** Build a navbar that is a stacked menu on mobile and a horizontal bar on desktop

---

## ✅ Checklist: "Did It Click?"

- [ ] I can explain what the viewport meta tag does
- [ ] I can say why mobile-first uses `min-width`
- [ ] I can make an image behave on any screen
- [ ] I can build a layout that adapts with *and* without media queries
- [ ] I know how to test responsiveness in DevTools

⬅️ Previous: [layout.md](./layout.md) | ➡️ Next: [animations.md](./animations.md)
