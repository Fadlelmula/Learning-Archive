# 🎧 Accessible Audio Controller

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![ARIA](https://img.shields.io/badge/ARIA-accessibility-blueviolet)
![Source](https://img.shields.io/badge/from-freeCodeCamp%20Workshop-0a0a23?logo=freecodecamp&logoColor=white)
![Status](https://img.shields.io/badge/status-Mark%20I-red)

> *Anyone can build a button. Building one that **everyone** can use? That's the real engineering.* 🔧

A tiny audio control panel (Play, Volume, Mute) built to practice **web accessibility**: making sure screen readers and keyboard users get the same experience as everyone else.

📅 Built: **October 9, 2026** · 🏕️ Source: freeCodeCamp workshop · 🦾 Suit version: **Mark I** (rebuilt in public, bugs included)

---

## 🧰 What's inside

| File | What it is |
|------|------------|
| `09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller.html` | The workshop version, exactly as followed along 📝 |
| `09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller-v2.html` | My reviewed version with the fixes below ⚡ |
| `README.md` | You are here 👋 |

## 🧪 The parts

| Part | Element | Why it matters |
|------|---------|----------------|
| ▶️ Play | `<button type="button">` | Native button = keyboard and screen reader support for free |
| 🔊 Volume | `<input type="range">` | Built-in arrow-key control, no JavaScript needed |
| 🔇 Mute | `<button type="button">` | Same as Play: use the right element and don't fight the browser |

## ♿ Accessibility concepts I practiced

- **`aria-labelledby`**: points to another element that gives the control its *name*
- **`aria-describedby`**: points to extra help text (the *description*)
- **`<label for="...">`**: the best way to name a form control; clicking the label focuses the input
- **`aria-pressed`**: tells assistive tech a button is a toggle (on/off)
- **Semantic HTML first**, ARIA second 🥇

## 🐛 Things I found when reviewing my own code

Honest section, because rebuilding skills means admitting what's broken:

| # | Issue | Fix |
|---|-------|-----|
| 1 | Description text was used inside `aria-labelledby`, so the slider's *name* became "Volume Adjust the sound level" | Name = `<label>`, description = `aria-describedby` |
| 2 | Labels were plain `<span>`s, so clicking "Volume" did nothing | Use a real `<label for="volume">` and give the input an `id` |
| 3 | Play and Mute are toggles but never announce their state | Add `aria-pressed` (and update it with JavaScript later) |
| 4 | No `<main>` landmark and no grouping | Wrap in `<main>` and `role="group"` with a label |
| 5 | Missing viewport meta tag | Add `<meta name="viewport" ...>` for mobile |

## 🚧 Still to build (Mark II)

- [ ] Hook up a real `<audio>` element
- [ ] JavaScript to toggle Play/Pause and Mute, and update `aria-pressed`
- [ ] Show the live volume value with `<output>`
- [ ] Test with a real screen reader (NVDA or VoiceOver) 🎙️

## ▶️ Run it

Open `09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller.html` in any browser. No install, no build step, no drama. Then press **Tab** to move between controls and use the **arrow keys** on the slider. ⌨️

---

*Part of my [learning-archive](https://github.com/Fadlelmula/learning-archive): rusty skills, rebuilt in public, one suit upgrade at a time.* 🦾
