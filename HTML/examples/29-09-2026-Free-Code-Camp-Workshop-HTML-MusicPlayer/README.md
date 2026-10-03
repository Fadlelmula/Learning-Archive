# 🌺 freeCodeCamp Tunes 🌺

*A tiny HTML jukebox that blooms in autumn, like a red spider lily. No JavaScript. No petals harmed.*

---

## 🥀 What is this?

Three songs. Three `<audio>` tags. Zero build tools.

This is the HTML step of the freeCodeCamp music player workshop (29-09-2026): a plain page that shows off what the humble `<audio>` element can do all by itself, before JavaScript shows up and starts rearranging the furniture.

## 🎶 The Setlist

| # | Track | Artist |
|---|-------|--------|
| 1 | Can't Stay Down | Quincy Larson |
| 2 | Cruising for a Musing | Quincy Larson |
| 3 | Scratching the Surface | Quincy Larson |

Yes, it's one artist. Quincy is doing a lot of heavy lifting. 🎤

## 🔴 How to run it

1. Save the file as `index.html` (or keep the original name, it doesn't judge).
2. Double-click it.
3. Press play. 🌺

That's it. If your browser can open a web page, it can open this. Needs internet, because the songs live on freeCodeCamp's CDN, not on your computer.

## 🌸 Anatomy of a track

```html
<h2>Can't Stay Down</h2>
<p>Artist: Quincy Larson</p>
<audio src="..." loop controls></audio>
```

- `<h2>` is the song title, wearing its best outfit.
- `<p>` is the artist credit.
- `<audio>` is the star of the show:
  - `src` tells the browser where the music lives.
  - `controls` gives you the play / pause / volume buttons. Without it, the player is invisible, and so is your music. 👻
  - `loop` makes the song start over when it ends. Forever. Like a spider lily coming back every year, but louder.

## ⚠️ Known quirks (a.k.a. "it's not a bug, it's a feature")

- Every song loops, so no track ever "finishes" and hands over to the next one.
- You can play all three at once. Enjoy your accidental remix. 🎛️
- No internet means no music. The lilies need water.

## 🌱 What's next?

The `js-music-player` in the file's URLs is a hint: the sequel adds JavaScript for a real playlist with next / previous buttons, one song at a time, and better manners.

## 🪷 Credits

Songs from the [freeCodeCamp](https://www.freecodecamp.org/) curriculum. Page assembled during a workshop, with love and a little too much enthusiasm.

*Bloom where you're planted. 🌺*
