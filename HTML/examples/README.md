# 🧪 HTML / examples

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Projects](https://img.shields.io/badge/projects-10-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Mark%20I%20(prototype)-orange?style=for-the-badge)
![No CSS](https://img.shields.io/badge/CSS-not%20yet-lightgrey?style=for-the-badge)

> 🛠️ **The workshop.** Every great suit starts with a garage full of prototypes, some of which explode. This folder is mine.

The notes one level up explain the *theory*. This folder is where I **build it, break it, and fix it**: small, dated, one-idea-per-folder HTML experiments. Most are freeCodeCamp workshops that I rebuilt by hand.

Every project has its own `README.md` that says what it does, how to run it, and (honestly) what's still rough. 💥

---

## 🚀 Quick start

1. Open any project folder.
2. Double-click the `.html` file (or right-click → *Open with* → your browser).
3. Open the same file in a code editor and **change something to see what happens.** That's the whole point. 🔧

No installs, no build tools, no frameworks. Just HTML and a browser. Some pages load images, audio, or video from freeCodeCamp's servers, so keep your internet connection on. 🌐

---

## 🗓️ The lineup (in the order I built them)

| Date | Project | What it's about | Key tags |
|------|---------|-----------------|----------|
| 27 Sep | [Cat Photo App](./27-09-2026-FREE-Code-Camp-WORKSHOP-Cat-App) | The basics: headings, links, images, lists, captions | `a` `img` `ul` `ol` `figure` |
| 27 Sep | [XYZ Bookstore](./27-09-2026-FREE-Code-Camp-WORKSHOP-XYZ-Bookstore) | Card layout with `div`s, ready for CSS later | `div` `id` `class` `button` |
| 29 Sep | [Music Player](./29-09-2026-Free-Code-Camp-Workshop-HTML-MusicPlayer) | Playing audio with no JavaScript | `audio` `controls` `loop` |
| 29 Sep | [Video Player](./29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer) | Video in several formats, with a fallback | `video` `source` `poster` |
| 30 Sep | [Cat Blog](./30-09-2026-Free-Code-Camp-Workshop-Cat-Blog) | Semantic page layout and in-page navigation | `header` `nav` `article` `footer` |
| 30 Sep | [Job Tips Page](./30-09-2026-FREE-Code-Camp-Workshop-Job-Tips-page) | Quotes and citations | `q` `blockquote` `cite` |
| 1 Oct | [Hotel Feedback Form](./01-10-2026-Free-Code-Camp-WORKSHOP-Hotel-Feedback-Form) | A full form with built-in validation | `form` `input` `select` `fieldset` |
| 2 Oct | [Exam Table](./02-10-2026-Free-Code-Camp-WORKSHOP-Exam-Table) | A structured data table | `table` `thead` `tfoot` `colspan` |
| 7 Oct | [Schedule Table](./07-10-2026-FREE-Code-Camp-WORKSHOP-Schedule-Table) | A conference schedule with row and column headers | `caption` `scope` `colspan` |
| 9 Oct | [Accessible Audio Controller](./09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller) | Play, volume, and mute controls that work for everyone | `button` `input type="range"` `label` `aria-*` |

---

## 🧠 Concept map: "where did I practice X?"

| Concept | Practiced in |
|---------|--------------|
| Headings, paragraphs, links, images, lists | [Cat Photo App](./27-09-2026-FREE-Code-Camp-WORKSHOP-Cat-App) |
| Semantic layout (`header`, `nav`, `main`, `footer`) | [Cat Blog](./30-09-2026-Free-Code-Camp-Workshop-Cat-Blog) |
| In-page links, `tel:` and `mailto:` links | [Cat Blog](./30-09-2026-Free-Code-Camp-Workshop-Cat-Blog) |
| Forms, input types, validation | [Hotel Feedback Form](./01-10-2026-Free-Code-Camp-WORKSHOP-Hotel-Feedback-Form) |
| Tables, `thead`, `tfoot`, `colspan` | [Exam Table](./02-10-2026-Free-Code-Camp-WORKSHOP-Exam-Table) |
| Accessible tables (`caption`, `scope`) | [Schedule Table](./07-10-2026-FREE-Code-Camp-WORKSHOP-Schedule-Table) |
| Audio | [Music Player](./29-09-2026-Free-Code-Camp-Workshop-HTML-MusicPlayer) |
| Video and responsive media | [Video Player](./29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer) |
| Quotes and citations | [Job Tips Page](./30-09-2026-FREE-Code-Camp-Workshop-Job-Tips-page) |
| `div`, `id`, and `class` as hooks | [XYZ Bookstore](./27-09-2026-FREE-Code-Camp-WORKSHOP-XYZ-Bookstore) |
| Labels, `aria-labelledby`, `aria-describedby`, `aria-pressed` | [Accessible Audio Controller](./09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller) |
| Range slider and native keyboard control | [Accessible Audio Controller](./09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller) |

---

## 🗺️ Folder map

```
HTML/examples/
├── README.md                                                   ← you are here 📍
├── 01-10-2026-Free-Code-Camp-WORKSHOP-Hotel-Feedback-Form/
├── 02-10-2026-Free-Code-Camp-WORKSHOP-Exam-Table/
├── 07-10-2026-FREE-Code-Camp-WORKSHOP-Schedule-Table/
├── 09-10-2026-FREE-Code-Camp-WORKSHOP-Accessible-Audio-Controller/
├── 27-09-2026-FREE-Code-Camp-WORKSHOP-Cat-App/
├── 27-09-2026-FREE-Code-Camp-WORKSHOP-XYZ-Bookstore/
├── 29-09-2026-Free-Code-Camp-Workshop-HTML-MusicPlayer/
├── 29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer/
├── 30-09-2026-Free-Code-Camp-Workshop-Cat-Blog/
└── 30-09-2026-FREE-Code-Camp-Workshop-Job-Tips-page/
```

*(Folders are listed the way GitHub sorts them: alphabetically. Use the lineup table above for the real timeline.)*

**Naming convention:** `DD-MM-YYYY-Source-Project-Name`. Each folder holds one `.html` file (the Audio Controller has a second, reviewed version) plus its own `README.md`.

> 🔮 Planned: rename to `YYYY-MM-DD-...` so the folders genuinely sort into a timeline, and settle on one capitalization style.

---

## 💥 Honest corner (known gremlins)

I'm rebuilding my skills in public, so not everything here is polished, and I'd rather say so than hide it.

| Project | The gremlin |
|---------|-------------|
| 📚 XYZ Bookstore | The buttons are decorative. There's no JavaScript yet. Buttons also need a `type` and unique names. |
| 📱 Six pages | Cat App, Bookstore, Cat Blog, Hotel Form, Exam Table, and Schedule Table have no `viewport` meta tag yet, so they're not phone-friendly. |
| 🎬 Video Player | No `<track>` captions yet. |
| 📊 Exam Table | Header cells need `scope` (the Schedule Table already has it). |
| 🗓️ Schedule Table | Raw `&` in two event names should be `&amp;`, and the last row's indentation doesn't match. |
| 🎨 All of them | No CSS yet, so everything looks like 1995. |

**✅ Already fixed (3 Oct):** a stray `"` in the Job Tips page, crooked indentation in the Cat App and Music Player, and the "Jop" typo in a folder name.

I'll collect the lessons in `notes/things-i-broke.md` and `notes/things-i-finally-understood.md` once the notes folder exists.

If you're a fellow learner: steal anything useful. If you're an employer: this is what my process looks like, iterating from **Mark I toward Mark 85**. 🦾

---

## 🔮 Mark II backlog

- 🎨 Dress every page up with CSS (the Bookstore and Cat Blog are begging for it)
- ⚡ Give the Bookstore buttons a brain with JavaScript
- 🎧 Hook the Audio Controller up to a real `<audio>` element
- 📱 Add the `viewport` meta tag to the six pages that are missing it
- ♿ Add `scope` to the Exam Table headers, captions to the video, and an accessibility pass on the form
- 🧹 Fix `&amp;` and indentation in the Schedule Table
- 📅 Rename folders to `YYYY-MM-DD` and unify capitalization
- 🌍 Turn on GitHub Pages so every example opens live in the browser

---

<p align="center"><i>Build. Break. Fix. Repeat. 🔁</i></p>
