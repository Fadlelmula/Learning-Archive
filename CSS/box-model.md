# 📦 The CSS Box Model: Everything Is Secretly a Box

![Topic](https://img.shields.io/badge/topic-box%20model-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Difficulty](https://img.shields.io/badge/difficulty-Mark%20II-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Every element on a page, even a circle, even a single letter, is a rectangle to the browser. Understand the box and 80% of "why is this 10px off?!" mysteries disappear. 🕵️

⬅️ Previous: [basics.md](./basics.md) | ➡️ Next: [colors-and-typography.md](./colors-and-typography.md)

---

## 📍 Table of Contents

1. [The four layers](#-the-four-layers)
2. [Width and height math](#-the-math-that-trips-everyone-up)
3. [box-sizing](#-box-sizing-the-fix-everyone-uses)
4. [Margin, padding and border](#-margin-padding-border-in-detail)
5. [Shorthand cheat](#-shorthand-the-clockwise-trick)
6. [Margin collapsing](#-margin-collapsing-the-weird-one)
7. [Display types](#-display-block-inline-and-inline-block)
8. [Overflow](#-overflow-when-content-doesnt-fit)
9. [Borders, radius and shadows](#-making-boxes-look-good)
10. [DevTools](#-inspect-the-box-in-devtools)
11. [Practice](#-practice-challenges)

---

## 🧅 The Four Layers

Think of a framed picture hanging on a wall:

```
┌──────────────────────────────────────────┐
│                 MARGIN                   │   ← space OUTSIDE (the wall)
│   ┌──────────────────────────────────┐   │
│   │             BORDER               │   │   ← the frame
│   │   ┌──────────────────────────┐   │   │
│   │   │         PADDING          │   │   │   ← space INSIDE (the matting)
│   │   │   ┌──────────────────┐   │   │   │
│   │   │   │     CONTENT      │   │   │   │   ← the picture itself
│   │   │   │  width × height  │   │   │   │
│   │   │   └──────────────────┘   │   │   │
│   │   └──────────────────────────┘   │   │
│   └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

| Layer | Property | Job | Has background color? |
|---|---|---|---|
| 🖼️ **Content** | `width`, `height` | The actual text, image, etc. | ✅ |
| 🧶 **Padding** | `padding` | Breathing room *inside* the border | ✅ (background extends under it) |
| 🪵 **Border** | `border` | The edge of the box | ✅ (can be styled) |
| 🌌 **Margin** | `margin` | Space *between* this box and others | ❌ always transparent |

> 🧠 **Memory trick:** **P**adding is **P**ersonal space (inside). **M**argin is the **M**oat (outside).

---

## 🧮 The Math That Trips Everyone Up

Given:

```css
.box {
  width: 300px;
  padding: 20px;
  border: 5px solid black;
  margin: 10px;
}
```

### With the default `box-sizing: content-box`

```
total visible width = width + padding-left + padding-right + border-left + border-right
                    = 300   +     20       +      20        +     5      +      5
                    = 350px     (margin adds 10px outside on each side)
```

😱 You asked for 300px but got 350px. That's the surprise.

### With `box-sizing: border-box`

```
total visible width = 300px   (padding and border are carved out of the width)
content area       = 300 - 20 - 20 - 5 - 5 = 250px
```

| | `content-box` (default) | `border-box` ✅ |
|---|---|---|
| `width` means | Content only | Content + padding + border |
| Surprise factor | High 😬 | Low 😌 |
| Easier to plan layouts? | No | Yes |

---

## 🔧 box-sizing: The Fix Everyone Uses

Put this at the top of nearly every stylesheet:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

Now `width: 50%` plus padding doesn't overflow its parent anymore. 🎉

---

## 🔍 Margin, Padding, Border in Detail

### Padding

```css
.button {
  padding: 12px 24px;   /* vertical | horizontal */
}
```

- Can't be negative
- Percentage padding is relative to the **width** of the containing block

### Border

```css
.card {
  border: 2px solid crimson;
  /* shorthand for: border-width  border-style  border-color */
}
```

| Common border styles | Look |
|---|---|
| `solid` | ───── |
| `dashed` | ─ ─ ─ ─ |
| `dotted` | · · · · · |
| `double` | ═════ |
| `none` | no border |

> ⚠️ If you set `border-width` and `border-color` but no `border-style`, **nothing shows**. The default style is `none`.

### Margin

```css
.section { margin-bottom: 2rem; }
.center-me { margin: 0 auto; }   /* centers a block with a set width ✨ */
```

- Can be **negative** (pulls things closer or overlaps them)
- `margin: auto` on left/right centers a block-level element with a defined `width`

---

## 🔄 Shorthand: The Clockwise Trick

Properties like `margin` and `padding` go **clockwise from the top**: **T**op → **R**ight → **B**ottom → **L**eft. Remember **"TRouBLe"** 😅

| You write | Means | Visual |
|---|---|---|
| `margin: 10px` | All four sides = 10px | ⬆️➡️⬇️⬅️ all 10 |
| `margin: 10px 20px` | top & bottom = 10, left & right = 20 | ↕️ 10, ↔️ 20 |
| `margin: 10px 20px 30px` | top = 10, left & right = 20, bottom = 30 | |
| `margin: 10px 20px 30px 40px` | top, right, bottom, left | clockwise 🕐 |

Single-side versions: `margin-top`, `margin-right`, `margin-bottom`, `margin-left` (same for `padding` and `border`).

---

## 🫠 Margin Collapsing (The Weird One)

Vertical margins between **adjacent block elements** collapse into the **larger one**. They do not add up.

```css
.a { margin-bottom: 40px; }
.b { margin-top: 20px; }
```

```
┌─────────┐
│   .a    │
└─────────┘
     ↕  40px   ← NOT 60px. The bigger margin wins.
┌─────────┐
│   .b    │
└─────────┘
```

| Collapses? | Situation |
|---|---|
| ✅ Yes | Vertical margins of adjacent block siblings |
| ✅ Yes | Parent and first/last child margins (when nothing separates them) |
| ❌ No | Horizontal margins |
| ❌ No | Flexbox and Grid items |

> 💡 Avoiding the confusion: many developers only use `margin-bottom` for vertical spacing, or use `gap` in Flexbox/Grid.

---

## 🧱 Display: Block, Inline and Inline-Block

| `display` | Starts on a new line? | Respects `width`/`height`? | Vertical margin/padding pushes others? | Examples |
|---|---|---|---|---|
| `block` | ✅ Yes, and takes full width | ✅ | ✅ | `div`, `p`, `h1`, `section` |
| `inline` | ❌ Flows with text | ❌ Ignored | ❌ Mostly not | `span`, `a`, `strong`, `em` |
| `inline-block` | ❌ Flows with text | ✅ | ✅ | buttons, images (by default) |
| `none` | Removed from the page entirely | n/a | n/a | hidden stuff |

```
block:         [██████████████████████████]
               [██████████████████████████]

inline:        text [span] text [span] text...

inline-block:  [box] [box] [box]   ← sit side by side, but have real sizes
```

> 🧪 `display: none` removes the element from layout and from screen readers. `visibility: hidden` hides it but **keeps its space**.

---

## 🌊 Overflow: When Content Doesn't Fit

```css
.box { width: 200px; height: 100px; overflow: auto; }
```

| Value | Behavior |
|---|---|
| `visible` (default) | Content spills out of the box |
| `hidden` | Extra content is clipped |
| `scroll` | Always shows scrollbars |
| `auto` | Scrollbars only if needed ✅ |

Related: `overflow-x`, `overflow-y`, and `text-overflow: ellipsis` (with `white-space: nowrap; overflow: hidden;`) for the "long text..." effect.

---

## 💅 Making Boxes Look Good

```css
.card {
  border: 1px solid #ddd;
  border-radius: 12px;                       /* rounded corners */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* x, y, blur, color */
  padding: 1.5rem;
}
```

| Property | What it does | Quick example |
|---|---|---|
| `border-radius` | Rounds corners | `50%` on a square makes a circle ⭕ |
| `box-shadow` | Adds shadow around the box | `0 2px 6px rgba(0,0,0,0.2)` |
| `outline` | Like a border, but takes **no space** (used for focus rings) | `outline: 2px solid blue;` |
| `background` | Color/image behind content + padding | `background: #fafafa;` |

> ♿ **Accessibility note:** never remove focus outlines without replacing them. Keyboard users need to see where they are.

---

## 🔬 Inspect the Box in DevTools

1. Right-click an element → **Inspect**
2. In the **Styles** or **Computed** tab, find the **box model diagram**
3. Hover over each colored layer to see it highlighted on the page:
   - 🟦 content
   - 🟩 padding
   - 🟨 border
   - 🟧 margin

This is the single best tool for solving "why is there a gap here?" 🕵️

---

## 🏋️ Practice Challenges

- [ ] **Level 1:** Make a `div` 300px wide with padding and a border. Measure it in DevTools.
- [ ] **Level 2:** Add `box-sizing: border-box` and watch the size change
- [ ] **Level 3:** Create two stacked boxes and prove margin collapsing with DevTools
- [ ] **Level 4:** Center a box horizontally with `margin: 0 auto`
- [ ] **Level 5:** Build a rounded card with a soft shadow and a circle avatar (`border-radius: 50%`)
- [ ] **Boss:** Recreate a business card using only the box model

---

## ✅ Checklist: "Did It Click?"

- [ ] I can draw the four layers from memory
- [ ] I can explain why my 300px box became 350px
- [ ] I know the TRBL clockwise rule
- [ ] I know when margins collapse
- [ ] I can pick `block`, `inline` or `inline-block` on purpose

⬅️ Previous: [basics.md](./basics.md) | ➡️ Next: [colors-and-typography.md](./colors-and-typography.md)
