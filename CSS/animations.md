# ✨ Animations: Transitions, Transforms & Keyframes

![Topic](https://img.shields.io/badge/topic-animations-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Difficulty](https://img.shields.io/badge/difficulty-Mark%20V-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)

> Motion is the arc reactor glow of a UI: used well, it guides attention. Used badly, it makes people dizzy. 😵‍💫

⬅️ Previous: [responsive-design.md](./responsive-design.md) | ➡️ Next: [cheat-sheet.md](./cheat-sheet.md)

---

## 📍 Table of Contents

1. [Three tools, three jobs](#-three-tools-three-jobs)
2. [Transitions](#-transitions-smooth-changes)
3. [Transforms](#-transforms-move-rotate-scale)
4. [Easing](#-easing-the-feel-of-motion)
5. [Keyframe animations](#-keyframe-animations)
6. [Performance](#-performance-what-to-animate)
7. [Accessibility](#-accessibility-prefers-reduced-motion)
8. [Recipes](#-recipes)
9. [Practice](#-practice-challenges)

---

## 🧰 Three Tools, Three Jobs

| Tool | Job | Needs a trigger? |
|---|---|---|
| **`transform`** | Moves, rotates, scales, skews an element | No. It's just a style. |
| **`transition`** | Smoothly animates **between two states** (like normal → hover) | Yes (hover, focus, class change...) |
| **`@keyframes` + `animation`** | Multi-step animations that can run on their own | No. Can loop automatically. |

```
transition:   A ───────────▶ B           (two states, triggered)
animation:    A ──▶ B ──▶ C ──▶ A ...    (many steps, can run alone)
```

---

## 🎬 Transitions: Smooth Changes

Without a transition, a hover change is instant. With one, it glides.

```css
.button {
  background: #222;
  transition: background 0.3s ease;
}

.button:hover {
  background: crimson;
}
```

### The shorthand

```
transition: property  duration  timing-function  delay;
            │         │         │                │
            │         │         │                └─ wait before starting (0s)
            │         │         └────────────────── easing curve (ease)
            │         └──────────────────────────── how long (0.3s)
            └────────────────────────────────────── what to animate (background)
```

| Property | Example |
|---|---|
| `transition-property` | `background-color`, `transform`, `all` |
| `transition-duration` | `0.2s`, `300ms` |
| `transition-timing-function` | `ease`, `linear`, `ease-in-out` |
| `transition-delay` | `0.1s` |

Multiple at once:

```css
.card {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
```

> ⚠️ **Put `transition` on the base state**, not only on `:hover`. Otherwise it animates *in* but snaps back *out*.

> ⚠️ You can't transition `display: none` to `block`. Animate `opacity` or `transform` instead.

---

## 🔄 Transforms: Move, Rotate, Scale

| Function | Effect | Example |
|---|---|---|
| `translate(x, y)` | Move | `transform: translate(20px, -10px);` |
| `translateY(-4px)` | Move up/down only | Hover "lift" effect |
| `rotate(deg)` | Spin | `transform: rotate(45deg);` |
| `scale(n)` | Resize | `transform: scale(1.1);` (110%) |
| `skew(deg)` | Slant | `transform: skewX(10deg);` |

Combine them (they apply **right to left** visually, so order matters):

```css
.box { transform: translateX(50px) rotate(10deg) scale(1.2); }
```

```
 original      translateY(-8px)    rotate(10deg)     scale(1.3)
  ┌───┐           ┌───┐               ╱╲                ┌─────┐
  │   │           │   │              ╱  ╲               │     │
  └───┘           └───┘              ╲  ╱               │     │
                  (moved up)          ╲╱                └─────┘
```

### `transform-origin`

The pivot point for rotating and scaling.

```css
.arrow { transform-origin: left center; }   /* default is center */
```

> 💡 Transforms **don't affect the layout of surrounding elements**. The original space stays reserved, which is why transforms are great for effects.

---

## 🎢 Easing: The Feel of Motion

| Keyword | Feel | Good for |
|---|---|---|
| `linear` | Constant speed, robotic 🤖 | Spinners, progress bars |
| `ease` | Default: starts fast, ends slow | General use |
| `ease-in` | Starts slow, ends fast | Things **leaving** the screen |
| `ease-out` | Starts fast, ends slow | Things **arriving** ✅ |
| `ease-in-out` | Slow-fast-slow | Moves between two points |
| `cubic-bezier(...)` | Custom curve | Fine tuning |
| `steps(n)` | Jumps in n steps | Sprite sheets, typewriter effects |

```
linear:        ╱              ease-out:      ╭──────
              ╱                            ╱
             ╱                            ╱
            ╱                           ╱
```

### Duration guide

| Duration | Use for |
|---|---|
| 100–200ms | Tiny feedback (button hover) |
| 200–400ms | Menus, cards, most UI |
| 400–800ms | Big page-level moves |
| 1s+ | Decorative or looping only |

---

## 🎞️ Keyframe Animations

For animations with multiple steps, or ones that run without a trigger.

### Step 1: define the steps

```css
@keyframes pulse {
  0%   { transform: scale(1);   opacity: 1; }
  50%  { transform: scale(1.1); opacity: 0.7; }
  100% { transform: scale(1);   opacity: 1; }
}
```

(`from` and `to` are aliases for `0%` and `100%`.)

### Step 2: attach it to an element

```css
.heart {
  animation: pulse 1.5s ease-in-out infinite;
}
```

### The shorthand

```
animation: name  duration  timing  delay  iteration-count  direction  fill-mode;
           pulse 1.5s      ease    0s     infinite         alternate  forwards
```

| Property | Common values | Meaning |
|---|---|---|
| `animation-name` | `pulse` | Which `@keyframes` to run |
| `animation-duration` | `1.5s` | One cycle length |
| `animation-timing-function` | `ease-in-out` | Easing per keyframe step |
| `animation-delay` | `0.5s` | Wait before starting |
| `animation-iteration-count` | `3`, `infinite` | How many times |
| `animation-direction` | `normal`, `reverse`, `alternate` | Forward, backward, ping-pong |
| `animation-fill-mode` | `forwards`, `backwards`, `both` | Style before/after it runs |
| `animation-play-state` | `running`, `paused` | Pause on hover! |

> 🧠 `animation-fill-mode: forwards` keeps the **final** keyframe's styles after it ends. Without it, the element snaps back to its original look.

---

## ⚡ Performance: What to Animate

Browsers can animate some properties cheaply and others expensively.

| Speed | Properties | Why |
|---|---|---|
| 🟢 **Smooth** | `transform`, `opacity` | Handled by the GPU, no re-layout |
| 🟡 **Okay-ish** | `color`, `background-color`, `box-shadow` | Repaint only |
| 🔴 **Janky** | `width`, `height`, `margin`, `top`, `left` | Forces layout recalculation every frame |

```css
/* ❌ Janky: triggers layout */
.menu { transition: left 0.3s; }
.menu.open { left: 0; }

/* ✅ Smooth: transform only */
.menu { transform: translateX(-100%); transition: transform 0.3s; }
.menu.open { transform: translateX(0); }
```

---

## ♿ Accessibility: `prefers-reduced-motion`

Some people get dizzy, nauseous, or distracted by motion. Operating systems have a "reduce motion" setting, and CSS can listen to it.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Motion checklist:

- ✅ Respect `prefers-reduced-motion`
- ✅ Nothing flashes more than 3 times per second
- ✅ Keep essential info available *without* animation
- ✅ Let users pause anything that loops for a long time

---

## 🍳 Recipes

### 1. Hover lift card

```css
.card {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
}
```

### 2. Loading spinner

```css
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #ddd;
  border-top-color: crimson;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 3. Fade-in on load

```css
.fade-in {
  animation: fadeIn 0.6s ease-out both;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

### 4. Underline that grows on hover

```css
.link {
  position: relative;
  text-decoration: none;
}
.link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}
.link:hover::after {
  transform: scaleX(1);
}
```

---

## 🏋️ Practice Challenges

- [ ] **Level 1:** Make a button change color smoothly on hover
- [ ] **Level 2:** Add a "lift" effect with `translateY` and a shadow
- [ ] **Level 3:** Build a CSS-only loading spinner
- [ ] **Level 4:** Create a fade-in animation that runs when the page loads
- [ ] **Level 5:** Pause an animation on hover with `animation-play-state`
- [ ] **Boss:** Build an animated card set, then add `prefers-reduced-motion` support

---

## ✅ Checklist: "Did It Click?"

- [ ] I can say when to use a transition vs a keyframe animation
- [ ] I know why `transform` and `opacity` are the safest properties to animate
- [ ] I can write a `@keyframes` block and attach it
- [ ] I know why `transition` goes on the *base* state
- [ ] I always add `prefers-reduced-motion` support

⬅️ Previous: [responsive-design.md](./responsive-design.md) | ➡️ Next: [cheat-sheet.md](./cheat-sheet.md)
