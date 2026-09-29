# 🌺 Working with the HTML Video Element

> *Higanbana blooms where you least expect it, and so does a video player when you write four `<source>` tags and pray.* 🥀

A tiny, single-file HTML page from the **freeCodeCamp workshop** on the `<video>` element. One heading, one video, zero JavaScript. Even the smallest garden starts with a single bulb. 🌱

---

## 🕯️ What's Inside

One file. That's it. No build step, no `npm install`, no 900 MB of `node_modules` haunting your disk.

```
📁 project
 └── 📄 29-09-2026-Free-Code-Camp-Workshop-HTML-VideoPlayer.html
```

## 🌸 What It Does

It shows a 640px-wide video player about the JavaScript `map()` method (because even spider lilies need to loop over things sometimes 🔁).

| Attribute | What it does | Vibe |
|-----------|--------------|------|
| `width="640"` | Sets the player width | A comfy, medium-sized garden plot 🌿 |
| `controls` | Shows play, pause, volume, fullscreen | Gives the viewer the steering wheel 🎛️ |
| `loop` | Restarts the video when it ends | *Eternal recurrence, but make it educational* ♾️ |
| `muted` | Starts silent | Politely whispering, so nobody's office meeting gets ambushed 🤫 |
| `poster` | Thumbnail shown before playback | The pretty flower bud before the bloom 🌺 |

## 🎞️ The `<source>` Fallback Chain

Different browsers speak different video languages, so the page offers several formats and lets the browser pick the first one it understands:

1. 🥇 **MP4** (`video/mp4`): the friendly one that plays nearly everywhere
2. 🥈 **WebM** (`video/webm`): the open-source cousin
3. 🥉 **Ogg** (`video/ogg`): the old-school hippie uncle
4. 🍎 **MOV** (`video/quicktime`): the Apple-flavored last resort

The browser reads them top to bottom and stops at the first one it can play. Like picking a door in a haunted mansion, but nicer. 🚪

## 🚀 How to Run It

1. Download the HTML file 📥
2. Double-click it 🖱️
3. Watch the video ✨

That's the whole ritual. No incense required (though it does add ambiance 🕯️).

> 🌐 The video, poster, and sources load from freeCodeCamp's CDN, so you'll need an internet connection. No Wi-Fi means a very quiet, very empty garden.

## 🧠 What You'll Learn

- How to embed video with the native `<video>` element 🎬
- What `controls`, `loop`, `muted`, and `poster` do
- How multiple `<source>` tags act as a fallback chain
- That you don't need a library for everything (shocking, I know) 😌

## 🥀 Credits

Built during the **freeCodeCamp** workshop on the HTML video element. Video and poster assets courtesy of freeCodeCamp's CDN. 💛

---

<p align="center">🌺 <i>Bloom where you're planted. Buffer where you're loaded.</i> 🌺</p>
