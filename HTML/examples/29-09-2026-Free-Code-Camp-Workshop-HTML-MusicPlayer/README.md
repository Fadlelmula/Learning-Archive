# 🎵 HTML Music Player

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-29%20Sep%202026-lightgrey?style=flat-square)

> No Spotify, no problem. Three tracks, three players, zero JavaScript. 🎧

A freeCodeCamp workshop page that plays audio straight from HTML using the `<audio>` element.

📄 **File:** [`29-09-2026-Free-Code-Camp-Workshop-HTML-MusicPlayer.html`](./29-09-2026-Free-Code-Camp-Workshop-HTML-MusicPlayer.html)

---

## 🎶 The tracklist

| Track | Artist |
|-------|--------|
| Can't Stay Down | Quincy Larson |
| Cruising for a Musing | Quincy Larson |
| Scratching the Surface | Quincy Larson |

---

## 🧱 What's inside

| Piece | What it does |
|-------|--------------|
| `<audio src="...">` | Loads an audio file from a URL |
| `controls` | Shows the browser's built-in play/pause/volume bar |
| `loop` | Restarts the track when it ends |
| `<h2>` + `<p>` | Track title and artist above each player |
| `<meta name="viewport">` | Helps the page behave on phones 📱 |

---

## 🚀 How to run it

Open the `.html` file in a browser, then hit play on any track. The audio streams from freeCodeCamp's servers, so you need an internet connection.

---

## 🧠 What I practiced

- Embedding audio with the `<audio>` element
- Boolean attributes (`controls`, `loop`) that work just by being present
- Repeating a small pattern (title, artist, player) for each track

---

## 💥 Honest corner

- ✅ *Fixed on 3 Oct:* the third track's code was **indented differently** from the first two. All three match now.
- Because of `loop`, every track repeats forever until you pause it.
- There's no fallback text for browsers that can't play audio (the video example has one).

---

## 🔮 Mark II ideas

- Add fallback text inside `<audio>` for unsupported browsers
- Offer multiple formats with `<source>` (like the [Video Player](../29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer) does)
- Wrap each track in an `<article>` or a list
- Later: build a real playlist with JavaScript 🎼

---

↩️ [Back to examples](../README.md)

*Press play on progress. ▶️*
