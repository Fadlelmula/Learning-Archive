# 🎬 HTML Video Player

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-29%20Sep%202026-lightgrey?style=flat-square)

> One video, four formats, and a graceful fallback. Because not every browser deserves the same treatment. 📽️

A freeCodeCamp workshop page about the `<video>` element: controls, a poster image, multiple source formats, and a fallback message.

📄 **File:** [`29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer.html`](./29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer.html)

---

## 🧱 What's inside

| Attribute / tag | What it does |
|-----------------|--------------|
| `width="640"` | Sets the starting width of the player |
| `controls` | Shows play, pause, volume, and fullscreen buttons |
| `loop` | Replays the video when it ends |
| `muted` | Starts with the sound off (browsers like this) |
| `playsinline` | Keeps it inside the page on iPhones instead of forcing fullscreen |
| `preload="metadata"` | Loads only the basics (like duration) until you press play, saving data |
| `poster="..."` | The thumbnail image shown before playing |
| `<source>` ×4 | The same video as **MP4, WebM, Ogg, and QuickTime** |
| Fallback `<p>` | Text and a download link for browsers that can't play video |

**How `<source>` works:** the browser walks down the list and plays the **first format it supports**.

There's also a tiny `<style>` block (`max-width: 100%; height: auto;`) so the video shrinks on small screens instead of overflowing. 📱

---

## 🚀 How to run it

Open the `.html` file in a browser. The video and poster stream from freeCodeCamp's servers, so you'll need an internet connection.

---

## 🧠 What I practiced

- Embedding video with several formats for compatibility
- Providing a **fallback** for when media can't play
- Using `preload` and `poster` to make pages friendlier
- Making media responsive with a few lines of CSS

---

## 💥 Honest corner

- There are no captions or subtitles yet (`<track>`), which hurts accessibility.
- The video is `muted`, so it's easy to think the sound is broken. It's just off.

---

## 🔮 Mark II ideas

- Add a `<track kind="captions">` for accessibility ♿
- Try my own video and compare how the formats behave
- Style the player inside a nicer layout

---

↩️ [Back to examples](../README.md)

*Lights. Camera. `<source>`. 🎥*
