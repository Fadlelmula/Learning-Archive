# 🌐 HTML

> The skeleton of every website. No bones, no body.
> **Mark I of the armor: complete.** Notes written, examples built, cheat sheet forged. Mark II ([CSS](../CSS)) is already on the workbench.

![Topic](https://img.shields.io/badge/topic-HTML5-E34F26?logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/status-Mark%20I%20complete-brightgreen)
![Notes](https://img.shields.io/badge/notes-5%20topics%20%2B%20cheat%20sheet-blue)
![Examples](https://img.shields.io/badge/examples-10-orange)
[![Next](https://img.shields.io/badge/next-CSS-yellow)](../CSS)
![Tags](https://img.shields.io/badge/<div>-last%20resort-red)

---

## 🎯 Why This Folder Exists

Before I can build the fancy suit (CSS, JavaScript, whatever comes next), I need a solid frame underneath. HTML is that frame. This folder is me re-learning it properly: the real structure, the semantics, and the accessibility habits that I skipped the first time around.

**Goal:** write HTML I'd be proud to show someone, not just HTML that "works on my machine."

**Where it stands:** the learning part is done. Every topic has notes, every topic has been practiced in an example, and everything is folded into one cheat sheet. What's left is a short, honest list of polish tasks (see [Known Gremlins](#-known-gremlins)), and I'm parking those on purpose so I could move on to CSS (already started).

---

## 🚪 Start Here

New to this folder (including future me)? Read in this order:

| Step | Open | Why |
|---|---|---|
| 1️⃣ | [`basics.md`](./basics.md) | The skeleton: tags, attributes, nesting |
| 2️⃣ | [`semantic-html.md`](./semantic-html.md) | Choosing the right element for the job |
| 3️⃣ | [`forms.md`](./forms.md) | Collecting input without crying |
| 4️⃣ | [`accessibility.md`](./accessibility.md) | Building for everyone |
| 5️⃣ | [`media-and-links.md`](./media-and-links.md) | Links, paths, images, audio, video |
| 6️⃣ | [`Cheat-Sheet.md`](./Cheat-Sheet.md) | Everything above, folded into one reference |
| 7️⃣ | [`FreeCodeCamp-ExamPrep.md`](./FreeCodeCamp-ExamPrep.md) | Final check before the freeCodeCamp exam |
| 🔧 | [`examples/`](./examples) | Where I actually build (and break) things |

> ⚡ **In a hurry?** Skip straight to [`Cheat-Sheet.md`](./Cheat-Sheet.md). It has copy-paste snippets, a debugging guide, and a checklist.

---

## 🗺️ Folder Map

| Item | What's inside | Status |
|---|---|---|
| 📄 [`basics.md`](./basics.md) | Document structure, tags, attributes, nesting, entities | ✅ Done |
| 🏛️ [`semantic-html.md`](./semantic-html.md) | `header`, `nav`, `main`, `section`, `article`, `footer`, and why `div` isn't everything | ✅ Done |
| 📝 [`forms.md`](./forms.md) | Inputs, labels, validation, buttons, form security basics | ✅ Done |
| ♿ [`accessibility.md`](./accessibility.md) | Alt text, keyboard navigation, contrast, ARIA, testing | ✅ Done |
| 🖼️ [`media-and-links.md`](./media-and-links.md) | Links, paths, images, audio, video, embeds | ✅ Done |
| 🦾 [`Cheat-Sheet.md`](./Cheat-Sheet.md) | One-stop reference, snippet library, debugging guide, next-step kit for CSS and JavaScript | 📖 Reference |
| 🏁 [`FreeCodeCamp-ExamPrep.md`](./FreeCodeCamp-ExamPrep.md) | The freeCodeCamp HTML review in my own words, plus a self-test | 📖 Reference |
| 🧪 [`examples/`](./examples) | 10 practice pages, each in its own folder with a README | ✅ Built (polish in Mark II) |

*Legend: ✅ done · 📖 reference · 🔬 experimenting*

```
HTML/
├── README.md
├── basics.md
├── semantic-html.md
├── forms.md
├── accessibility.md
├── media-and-links.md
├── Cheat-Sheet.md
├── FreeCodeCamp-ExamPrep.md
└── examples/
    ├── README.md
    └── (10 dated project folders)
```

---

## 📈 Progress Check

| Milestone | Status |
|---|---|
| Core topic notes (basics, semantics, forms, accessibility, media and links) | ✅ Done |
| One-page cheat sheet with snippets and checklists | ✅ Done |
| freeCodeCamp review rewritten in my own words | ✅ Done |
| 10 practice pages with a README each | ✅ Done |
| Pass the HTML readiness self-test in the cheat sheet | 🎯 Next |
| Start the [`CSS`](../CSS) folder | 🌱 Started |
| Fix the known gremlins in the examples (viewport, captions, `scope`, `&amp;`) | 🔮 Mark II backlog |

> 🎯 The readiness check lives in [`Cheat-Sheet.md`](./Cheat-Sheet.md#-readiness-self-test). When I can tick 80% of it from memory, the armor is ready for paint.

---

## 🧰 Cheat Sheet Teaser (a.k.a. things I keep forgetting)

| Tag | What it does | Pro tip |
|---|---|---|
| `<header>` | Intro content or navigation for a page or section | Not the same as `<head>`. Ask me how I know. |
| `<main>` | The main content of the page | Use it once per page |
| `<button>` | A clickable action | Use it instead of a clickable `div`, and always set its `type` |

The full list lives in [`Cheat-Sheet.md`](./Cheat-Sheet.md).

---

## 🧭 Learning Path

1. ✅ **Basics:** structure of a page, tags, attributes
2. ✅ **Semantics:** use elements for what they mean
3. ✅ **Forms:** collect input without crying
4. ✅ **Accessibility:** build for everyone, not just my screen
5. ✅ **Media and links:** paths, images, audio, video
6. ✅ **Consolidate:** cheat sheet and exam prep, so it sticks
7. ✅ **Practice:** break things in `examples/`, then write down what happened
8. 🌱 **Level up:** [CSS](../CSS) (started), then JavaScript

---

## 🧱 Principles I'm Following

- Use the right element for the job. A `div` is not a personality.
- If it's clickable, it's a link or a button.
- Every image gets thought-out alt text.
- Every page gets a `viewport` meta tag.
- Every media file gets a fallback (and video gets captions).
- Validate early, validate often.
- Build the Mark I first, then make it pretty with CSS.

---

## 💥 Known Gremlins

Mark I shipped, but it didn't ship perfect, and I'd rather say so than hide it. The full table lives in [`examples/README.md`](./examples/README.md#-honest-corner-known-gremlins). Short version:

- 📱 Six pages are missing the `viewport` tag
- 🎬 The Video Player has no `<track>` captions
- 📊 The Exam Table headers need `scope`
- 🗓️ The Schedule Table has raw `&` characters and uneven indentation
- 🎨 No CSS anywhere yet, so everything looks like 1995

**The plan:** these are queued in the Mark II backlog. I know exactly how to fix each one. I'm choosing to move forward and circle back, because shipping a prototype and iterating beats polishing one forever.

---

## 🔗 Related

- 🏠 [Back to the Learning Archive](../README.md)
- 🎨 [`CSS/`](../CSS): giving this skeleton some style *(started)*
- ⚡ `JavaScript/`: making it move *(coming soon)*
- 💥 `notes/things-i-broke.md`: where my HTML disasters will live *(coming soon)*

---

<p align="center"><i>Mark I is built. Time to paint the armor. 🎨🦾</i></p>
