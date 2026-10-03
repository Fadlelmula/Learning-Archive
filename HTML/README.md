# 🌐 HTML

> The skeleton of every website. No bones, no body.
> Mark I of the armor: simple, a bit rough, and absolutely essential.

![Topic](https://img.shields.io/badge/topic-HTML5-E34F26?logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/status-rebuilding%20the%20rust-yellow)
![Difficulty](https://img.shields.io/badge/difficulty-friendly-brightgreen)
![Tags](https://img.shields.io/badge/<div>-overused-red)

---

## 🎯 Why This Folder Exists

Before I can build the fancy suit (CSS, JavaScript, whatever comes next), I need a solid frame underneath. HTML is that frame. This folder is me re-learning it properly: the real structure, the semantics, and the accessibility habits that I skipped the first time around.

**Goal:** write HTML I'd be proud to show someone, not just HTML that "works on my machine."

---

## 🗺️ Folder Map

| Item | What's inside | Status |
|---|---|---|
| 📄 [`basics.md`](./basics.md) | Document structure, tags, attributes, nesting | 🌱 Growing |
| 🏛️ [`semantic-html.md`](./semantic-html.md) | `header`, `nav`, `main`, `section`, `article`, `footer` and why `div` isn't everything | 🌱 Growing |
| 📝 [`forms.md`](./forms.md) | Inputs, labels, validation, buttons | 🌱 Growing |
| ♿ [`accessibility.md`](./accessibility.md) | Alt text, ARIA basics, keyboard navigation | 📖 Reading |
| 🖼️ [`media-and-links.md`](./media-and-links.md) | Images, audio, video, links, and paths | 🌱 Growing |
| 🧪 [`examples/`](./examples) | Small practice pages and mini projects | 🔬 Experimenting |

*Legend: 🌱 growing · 🔬 experimenting · 📖 reading · ✅ comfortable*

```
HTML/
├── README.md
├── basics.md
├── semantic-html.md
├── forms.md
├── accessibility.md
├── media-and-links.md
└── examples/
```

---

## 🧰 The Cheat Sheet (a.k.a. things I keep forgetting)

| Tag | What it does | Pro tip |
|---|---|---|
| `<header>` | Intro content or navigation for a page or section | Not the same as `<head>`. Ask me how I know. |
| `<nav>` | Major navigation links | Wrap the main menu, not every link |
| `<main>` | The main content of the page | Use it once per page |
| `<section>` | A themed group of content | Give it a heading |
| `<article>` | Self-contained content | Would it make sense on its own? Then yes. |
| `<button>` | A clickable action | Use it instead of a clickable `div` |
| `<label>` | Text tied to a form input | Makes forms usable for everyone |

---

## 🧭 Learning Path

1. **Basics:** structure of a page, tags, attributes
2. **Semantics:** use elements for what they mean
3. **Forms:** collect input without crying
4. **Accessibility:** build for everyone, not just my screen
5. **Practice:** break things in `examples/`, then write down what happened

---

## 🧱 Principles I'm Following

- Use the right element for the job. A `div` is not a personality.
- If it's clickable, it's a link or a button.
- Every image gets thought-out alt text.
- Validate early, validate often.
- Build the Mark I first, then make it pretty with CSS.

---

## 🔗 Related

- 🎨 [`../CSS`](../CSS): giving this skeleton some style
- ⚡ [`../JavaScript`](../JavaScript): making it move
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): where my HTML disasters live

---

<p align="center"><i>Every great suit starts with a solid frame. 🦾</i></p>
