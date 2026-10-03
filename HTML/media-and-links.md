# 🖼️ Media and Links

> The web is a web because of links. It's worth watching because of media.
> Mark V of the armor: the suit learns to connect, show, and play.

![Topic](https://img.shields.io/badge/topic-media%20%26%20links-E34F26?logo=html5&logoColor=white)
![Level](https://img.shields.io/badge/level-beginner%20to%20intermediate-yellow)
![Status](https://img.shields.io/badge/status-growing-brightgreen)
![Covers](https://img.shields.io/badge/covers-links%20%7C%20images%20%7C%20audio%20%7C%20video%20%7C%20embeds-blue)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-lightgrey)

---

## 🗂️ Table of Contents

1. [Links and paths](#-links-and-paths)
2. [Link attributes and safety](#-link-attributes-and-safety)
3. [Images](#-images)
4. [Responsive images](#-responsive-images)
5. [Image formats](#-image-formats)
6. [SVG](#-svg)
7. [Audio](#-audio)
8. [Video](#-video)
9. [Embedding other content](#-embedding-other-content)
10. [Performance](#-performance)
11. [Accessibility for media and links](#-accessibility-for-media-and-links)
12. [Licensing and hotlinking](#-licensing-and-hotlinking)
13. [Audit of my own examples](#-audit-of-my-own-examples)
14. [Mistakes I actually made](#-mistakes-i-actually-made)
15. [Cheat sheet](#-cheat-sheet)
16. [Practice ideas](#-practice-ideas)
17. [Tools](#-tools)
18. [Related](#-related)

---

## 🔗 Links and Paths

The `<a>` (anchor) element is the "hyper" in hypertext.

```html
<a href="https://example.com/about">About us</a>
```

### Anatomy of a URL

```
https://www.example.com:443/blog/post.html?id=7&sort=new#comments
└─┬─┘   └──────┬──────┘└┬┘└──────┬──────┘└────┬──────┘└───┬───┘
scheme       host     port      path        query     fragment
```

| Part | Meaning |
|---|---|
| **Scheme** | How to talk to the server: `https`, `http`, `mailto`, `tel` |
| **Host** | The server's name |
| **Port** | Usually hidden (443 for https, 80 for http) |
| **Path** | Which file or route |
| **Query** | Extra data after `?`, as `key=value` pairs joined by `&` |
| **Fragment** | A spot within the page, after `#` (never sent to the server) |

### Types of `href`

| Type | Example | Where it goes |
|---|---|---|
| **Absolute URL** | `href="https://example.com/page"` | Any site |
| **Relative path** | `href="about.html"` | Same folder |
| **Parent folder** | `href="../index.html"` | One level up |
| **Subfolder** | `href="pages/contact.html"` | Down into a folder |
| **Root-relative** | `href="/images/logo.png"` | From the site root |
| **Fragment** | `href="#contact"` | Element with `id="contact"` on this page |
| **Page + fragment** | `href="faq.html#shipping"` | A spot on another page |
| **Email** | `href="mailto:me@example.com"` | Opens the mail app |
| **Phone** | `href="tel:+15555555555"` | Dials on phones |
| **Text message** | `href="sms:+15555555555"` | Opens messages (support varies) |

### Relative paths cheat sheet

```
project/
├── index.html
├── about.html
├── images/
│   └── cat.jpg
├── audio/
│   └── song.mp3
└── pages/
    └── contact.html
```

| From | To | Path to write |
|---|---|---|
| `index.html` | `about.html` | `about.html` |
| `index.html` | `cat.jpg` | `images/cat.jpg` |
| `index.html` | `contact.html` | `pages/contact.html` |
| `pages/contact.html` | `index.html` | `../index.html` |
| `pages/contact.html` | `cat.jpg` | `../images/cat.jpg` |
| `pages/contact.html` | `song.mp3` | `../audio/song.mp3` |

**Mnemonic:** `./` = here · `../` = up one level · `/` = from the site root.

### File naming rules I'm adopting

- ✅ lowercase, with hyphens: `cat-photo.jpg`
- ✅ letters, numbers, hyphens only
- ❌ no spaces (they become `%20` in URLs)
- ❌ no apostrophes or special characters (`can't-stay-down.mp3` needs encoding as `can%27t-stay-down.mp3`; just rename it)
- ⚠️ Many servers are **case-sensitive**: `Cat.JPG` and `cat.jpg` can be different files. It works on my computer and breaks when deployed.

### Linking within a page

```html
<nav>
  <ul>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<section id="about">…</section>
<section id="contact">…</section>
```

```css
html { scroll-behavior: smooth; }
section { scroll-margin-top: 4rem; } /* so a sticky header doesn't cover the heading */
```

### Link states (CSS)

Style order matters. Remember **LVHFA**:

```css
a:link    { color: #0645ad; }
a:visited { color: #6b3fa0; }
a:hover   { text-decoration: underline; }
a:focus-visible { outline: 3px solid #1a73e8; outline-offset: 2px; }
a:active  { color: #c00; }
```

---

## 🛡️ Link Attributes and Safety

| Attribute | Purpose | Notes |
|---|---|---|
| `href` | The destination | An `<a>` without `href` is just a placeholder, not a link |
| `target` | Where to open | `_self` (default), `_blank` (new tab), `_parent`, `_top` |
| `rel` | Relationship to the target | See table below |
| `download` | Download instead of navigate | Works for same-origin files; can suggest a file name |
| `hreflang` | Language of the target | Informational |
| `type` | MIME type hint | Informational |
| `title` | Extra tooltip | Don't hide important info here |

### Useful `rel` values

| Value | Meaning |
|---|---|
| `noopener` | New tab can't control the original tab (modern browsers already imply this with `_blank`) |
| `noreferrer` | Doesn't send the referring page (implies `noopener`) |
| `nofollow` | "Don't treat this as my endorsement" (for search engines) |
| `sponsored` | Paid or affiliate links |
| `ugc` | User-generated content links (comments, forum posts) |
| `external` | Hint that it's another site |

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  Example (opens in a new tab)
</a>

<a href="brochure.pdf" download="my-brochure.pdf">Download the brochure (PDF)</a>

<a href="mailto:hello@example.com?subject=Hello%20there">Email me</a>
```

### Should a link open in a new tab?

Default: **no.** Let the user decide (they can middle-click or long-press). Use `_blank` only when leaving would lose the user's work (like a half-filled form) or for documents/help pages. When you do, **say so in the link text**: "(opens in a new tab)".

### Link text rules

| ✅ Good | ❌ Bad |
|---|---|
| "Read the 2026 accessibility report" | "Click here" |
| "Download the brochure (PDF, 2 MB)" | "Download" |
| "Contact our support team" | "http://example.com/support?id=7" |

Keep any space *outside* the `<a>` so the underline doesn't start with a gap.

### Linked images

```html
<a href="/gallery.html">
  <img src="cats.jpg" alt="View the full cat photo gallery">
</a>
```

When an image is the **only** content of a link, the alt text should describe where the link goes, not what the picture looks like.

---

## 🖼️ Images

```html
<img src="images/cat.jpg"
     alt="An orange cat sleeping on a sunny windowsill"
     width="800" height="533">
```

| Attribute | Purpose | Notes |
|---|---|---|
| `src` | Image file | Required |
| `alt` | Text alternative | Required. Use `alt=""` for decorative images |
| `width` / `height` | Intrinsic size in pixels | Lets the browser reserve space, avoiding layout jumps |
| `loading` | `lazy` or `eager` | Lazy-load images below the fold |
| `decoding` | `async` | Hint to decode off the main thread |
| `fetchpriority` | `high` | For the single most important image on the page |
| `srcset` / `sizes` | Multiple resolutions | See next section |
| `title` | Tooltip | Rarely useful |

### Always set width and height

Without them the page "jumps" when the image arrives, which is annoying and bad for performance scores (Cumulative Layout Shift). Pair them with CSS so images still shrink on small screens:

```css
img {
  max-width: 100%;
  height: auto;
}
```

### Lazy loading, used wisely

```html
<!-- Below the fold: lazy -->
<img src="photo.jpg" alt="…" width="600" height="400" loading="lazy">

<!-- Hero image at the top: do NOT lazy-load -->
<img src="hero.jpg" alt="…" width="1200" height="600" fetchpriority="high">
```

### Figures with captions

```html
<figure>
  <img src="lasagna.jpg" alt="A slice of lasagna on a white plate" width="600" height="400">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
```

Use `<figure>` when the media is a self-contained unit referenced from the text. Alt and caption should **complement**, not repeat, each other.

### Alt text quick guide

| Image is... | Alt text |
|---|---|
| Informative | Describe what matters in context |
| Decorative | `alt=""` |
| A link or button | Describe the destination or action |
| A logo | The company name |
| A chart | Key takeaway + a longer description nearby |
| Text in an image | Same words |

Details in [`accessibility.md`](./accessibility.md).

### Favicon

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
```

The small icon in the browser tab. It goes in `<head>`.

---

## 📱 Responsive Images

A phone doesn't need a 4000px-wide photo, and a big retina display wants a sharp one. HTML lets the browser choose.

### `srcset` + `sizes`: same image, different sizes

```html
<img
  src="cat-800.jpg"
  srcset="cat-400.jpg 400w,
          cat-800.jpg 800w,
          cat-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 800px"
  alt="An orange cat on a windowsill"
  width="800" height="533">
```

| Piece | Meaning |
|---|---|
| `400w`, `800w` | The **actual pixel width** of each file |
| `sizes` | How wide the image will be displayed at different viewport widths |
| `src` | Fallback for old browsers |

The browser combines `sizes` with the screen's pixel density and picks the best file.

### Pixel-density version (fixed-size images)

```html
<img src="logo.png"
     srcset="logo.png 1x, logo@2x.png 2x"
     alt="XYZ Bookstore" width="200" height="60">
```

### `<picture>`: different formats or different crops

```html
<picture>
  <source srcset="cat.avif" type="image/avif">
  <source srcset="cat.webp" type="image/webp">
  <img src="cat.jpg" alt="An orange cat on a windowsill" width="800" height="533">
</picture>
```

The browser takes the **first** `<source>` it supports. The `<img>` is the required fallback (and carries `alt` and size).

**Art direction** (different crop for mobile):

```html
<picture>
  <source media="(max-width: 600px)" srcset="cat-square.jpg">
  <img src="cat-wide.jpg" alt="An orange cat on a windowsill" width="1200" height="600">
</picture>
```

| Use... | When |
|---|---|
| `srcset` + `sizes` | Same picture, different resolutions |
| `<picture>` + `type` | Offer modern formats with a fallback |
| `<picture>` + `media` | Different **crops** for different screens |

---

## 🧱 Image Formats

| Format | Best for | Notes |
|---|---|---|
| **JPEG** (`.jpg`) | Photos | Small, lossy, no transparency |
| **PNG** | Screenshots, graphics, transparency | Lossless, larger files |
| **WebP** | Photos and graphics | Smaller than JPEG/PNG, supports transparency and animation, widely supported |
| **AVIF** | Photos | Often the smallest files, excellent quality, slower to create |
| **GIF** | Tiny animations | Huge for what it does; prefer short video or animated WebP |
| **SVG** | Logos, icons, diagrams | Vector, scales forever, can be styled with CSS |
| **ICO** | Favicons | Legacy favicon format |

**Rule of thumb:** photos → WebP/AVIF (JPEG fallback) · logos and icons → SVG · screenshots with text → PNG or WebP.

---

## 🎨 SVG

SVG is an image made of **code** (XML), so it stays crisp at any size and is usually tiny.

### Three ways to use it

| Method | Code | Style with page CSS? | Cached? |
|---|---|---|---|
| As an image | `<img src="logo.svg" alt="XYZ Bookstore">` | ❌ | ✅ |
| Inline | `<svg>…</svg>` in the HTML | ✅ | ❌ |
| CSS background | `background-image: url(icon.svg)` | ❌ | ✅ |

### Inline SVG, accessibly

```html
<!-- Decorative icon next to text -->
<button type="button">
  <svg aria-hidden="true" focusable="false" width="16" height="16" viewBox="0 0 16 16">
    <path d="M2 8h12M8 2v12" stroke="currentColor" stroke-width="2"/>
  </svg>
  Add item
</button>

<!-- Meaningful standalone graphic -->
<svg role="img" aria-labelledby="t" width="120" height="120" viewBox="0 0 120 120">
  <title id="t">Red circle</title>
  <circle cx="60" cy="60" r="50" fill="red"/>
</svg>
```

Tip: `fill="currentColor"` makes an icon match the text color automatically.

---

## 🎵 Audio

```html
<audio controls preload="metadata">
  <source src="audio/song.mp3" type="audio/mpeg">
  <source src="audio/song.ogg" type="audio/ogg">
  <p>Your browser doesn't support audio. <a href="audio/song.mp3">Download the track</a>.</p>
</audio>
```

### Attributes

| Attribute | Effect |
|---|---|
| `controls` | Show the browser's player UI. **Without it, the audio is invisible and unusable.** |
| `src` | Single source (or use child `<source>` tags for several) |
| `autoplay` | Start immediately (blocked by most browsers unless muted, and annoying) |
| `loop` | Repeat forever |
| `muted` | Start silent |
| `preload` | `none`, `metadata` (just duration and info), or `auto` |
| `crossorigin` | For files from other origins that need CORS |

### Audio formats

| Format | MIME type | Notes |
|---|---|---|
| **MP3** | `audio/mpeg` | Universal support |
| **AAC / M4A** | `audio/mp4` | Great quality, widely supported |
| **Ogg Vorbis / Opus** | `audio/ogg` | Open formats, efficient |
| **WAV** | `audio/wav` | Uncompressed, very large |
| **FLAC** | `audio/flac` | Lossless, large |

Practical choice: **MP3 or AAC** as the main file, optionally Opus too.

### A simple playlist

```html
<section>
  <h2>Playlist</h2>

  <article>
    <h3>Track title</h3>
    <p>Artist name</p>
    <audio controls preload="none" src="audio/track-one.mp3">
      <a href="audio/track-one.mp3">Download this track</a>
    </audio>
  </article>

  <!-- repeat for each track -->
</section>
```

Don't use `loop` on every track in a playlist unless you want each one to repeat forever.

---

## 🎬 Video

```html
<video controls width="640" height="360" poster="images/poster.jpg"
       preload="metadata" playsinline>
  <source src="video/demo.mp4"  type="video/mp4">
  <source src="video/demo.webm" type="video/webm">
  <track kind="captions" src="video/captions-en.vtt" srclang="en" label="English" default>
  <p>Your browser doesn't support video. <a href="video/demo.mp4">Download it</a>.</p>
</video>
```

### Attributes

| Attribute | Effect |
|---|---|
| `controls` | Show playback controls |
| `poster` | Image shown before playback starts |
| `width` / `height` | Reserve space |
| `preload` | `none` / `metadata` / `auto` |
| `autoplay` + `muted` | Browsers generally only allow autoplay when muted |
| `loop` | Repeat |
| `playsinline` | On iPhones, play within the page instead of full-screen |
| `muted` | Start silent |

### Video formats

| Container | Codec | MIME type | Notes |
|---|---|---|---|
| **MP4** | H.264 (AVC) | `video/mp4` | Plays almost everywhere; best default |
| **WebM** | VP9 / AV1 | `video/webm` | Smaller files, great in modern browsers |
| **Ogg** | Theora | `video/ogg` | Legacy; rarely needed now |
| **MOV** | varies | `video/quicktime` | Apple's format, not reliably supported; convert to MP4 |

List sources from **most preferred to least**. The browser uses the first one it can play.

### Captions and other tracks

```html
<track kind="captions"  src="captions-en.vtt" srclang="en" label="English" default>
<track kind="subtitles" src="subs-ar.vtt"     srclang="ar" label="العربية">
<track kind="descriptions" src="desc-en.vtt"  srclang="en" label="Audio description">
```

| `kind` | For |
|---|---|
| `captions` | Dialogue + important sounds, for deaf and hard-of-hearing users |
| `subtitles` | Translation of dialogue |
| `descriptions` | Text description of visuals |
| `chapters` | Navigation points |

A minimal `.vtt` file:

```
WEBVTT

00:00:00.000 --> 00:00:03.000
Welcome to the video.

00:00:03.500 --> 00:00:07.000
[upbeat music] Let's get started.
```

### Autoplay etiquette

- Don't autoplay with sound. Browsers block it anyway.
- Muted, looping background video is OK when it's purely decorative, but provide a pause control and respect `prefers-reduced-motion`.

---

## 🧩 Embedding Other Content

`<iframe>` puts another web page inside this one: YouTube videos, maps, forms, widgets.

```html
<iframe
  src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
  title="Intro to HTML: full tutorial"
  width="560" height="315"
  loading="lazy"
  allowfullscreen
  referrerpolicy="strict-origin-when-cross-origin">
</iframe>
```

| Attribute | Purpose |
|---|---|
| `src` | The page to embed |
| `title` | **Required for accessibility.** Describes the frame to screen readers. |
| `width` / `height` | Size (use CSS to make it responsive) |
| `loading="lazy"` | Defer loading until near the viewport |
| `allowfullscreen` | Permit full-screen |
| `allow` | Permissions like `autoplay`, `clipboard-write`, `fullscreen` |
| `sandbox` | Locks the embed down. Add only the permissions needed. |
| `referrerpolicy` | What referrer info to send |

### Responsive 16:9 embed (CSS)

```css
.video-wrapper iframe {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  border: 0;
}
```

### Safety notes

- Only embed sources you trust. An iframe runs someone else's code on your page.
- Use `sandbox` for anything you're unsure about.
- Many sites **refuse** to be embedded (`X-Frame-Options` / CSP headers). That's their choice, not a bug in my HTML.
- Privacy-friendly YouTube embeds use `youtube-nocookie.com`.

### Other embed elements (rarely needed)

| Element | Notes |
|---|---|
| `<embed>`, `<object>` | Legacy plugin-style embeds. Prefer `img`, `video`, `iframe`. |
| `<map>` + `<area>` | Image maps: clickable regions on an image. Fiddly and not responsive. Prefer real links over an image where possible. |
| `<canvas>` | Drawing surface for JavaScript. Not covered here. |

---

## ⚡ Performance

Media is usually the **heaviest part of a page**. Small habits add up.

| Habit | Why |
|---|---|
| Resize images before uploading | Don't ship a 4000px photo to display at 400px |
| Compress (Squoosh, TinyPNG) | Often 50-80% smaller with no visible difference |
| Use modern formats (WebP/AVIF) with fallback | Smaller files |
| `width` + `height` on every image/video | No layout jumps |
| `loading="lazy"` on below-the-fold media | Faster first load |
| `fetchpriority="high"` on the hero image | Gets it sooner |
| `preload="metadata"` or `none` on audio/video | Don't download megabytes nobody asked for |
| Use SVG for logos and icons | Tiny and sharp |
| Prefer video over big animated GIFs | Dramatically smaller |
| Avoid autoplay | Saves data and sanity |

### Quick mental budget

| Content | Rough target |
|---|---|
| Hero image | Under ~200 KB if possible |
| Regular content image | Under ~100 KB |
| Icons | SVG, a few KB |
| Background video | Short, compressed, muted |

---

## ♿ Accessibility for Media and Links

| Item | Requirement |
|---|---|
| Images | Meaningful `alt`; `alt=""` for decoration |
| Linked images | Alt describes the destination |
| Link text | Understandable out of context; no bare "click here" |
| New-tab links | Say so in the text |
| Downloads | Mention the type and size: "(PDF, 2 MB)" |
| Video | Captions (`<track>`), audio description for key visuals, keyboard-operable controls |
| Audio | Transcript on the page or linked |
| Autoplay | None with sound; provide pause for moving content |
| `<iframe>` | A descriptive `title` |
| Motion | Respect `prefers-reduced-motion` |
| Link styling | Underlines for links in text; visible `:focus-visible` |
| Touch targets | Big enough to tap (about 44px is comfortable) |

Full detail is in [`accessibility.md`](./accessibility.md).

---

## ⚖️ Licensing and Hotlinking

### Hotlinking

Using a file hosted on someone else's server (like my practice pages loading freeCodeCamp's cat pictures):

```html
<img src="https://cdn.example.com/someone-elses-image.jpg" alt="…">
```

| Problem | Why |
|---|---|
| 💥 **Breaks without warning** | They can move, rename, or delete it |
| 🐌 **Out of your control** | Slow or blocked by their server |
| 💸 **Uses their bandwidth** | Rude, and some sites block hotlinking |
| 🔒 **Privacy** | Third parties see your visitors' requests |

Fine for practice workshops. For real projects, **download (with permission) and host your own copy.**

### Copyright and licenses

"It was on Google" does not mean "free to use."

| Source | Notes |
|---|---|
| 📷 [Unsplash](https://unsplash.com/), [Pexels](https://www.pexels.com/), [Pixabay](https://pixabay.com/) | Free-to-use photos; check each site's license terms |
| 🌐 [Wikimedia Commons](https://commons.wikimedia.org/) | Many files under Creative Commons; **follow the attribution requirements** |
| 🎵 [Free Music Archive](https://freemusicarchive.org/), [Pixabay Music](https://pixabay.com/music/) | Check the individual license |
| 🖌️ Your own work | The safest source |

Common Creative Commons terms: **BY** (give credit), **SA** (share alike), **NC** (non-commercial), **ND** (no derivatives). Always give credit when required:

```html
<figcaption>
  Photo by <a href="https://example.com/author">Author Name</a> /
  <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
</figcaption>
```

---

## 🔍 Audit of My Own Examples

How my media-and-links practice pages stack up (see [`examples/`](./examples)):

| Project | ✅ Good | ⚠️ To fix |
|---|---|---|
| **Cat Photo App** | Links, `figure` + `figcaption`, `target="_blank"` link | Linked image's alt should describe the destination; add `rel="noopener noreferrer"`; add `width`/`height`; hotlinked images |
| **Cat Blog** | Working in-page navigation with matching ids, descriptive alt | Space inside the email link; hotlinked image; add viewport meta |
| **Music Player** | Native `controls`, clear track structure | Apostrophe in the file name (`can't-stay-down.mp3`) should be renamed or encoded; no fallback text; no transcript; `loop` on every track; no `<main>` |
| **Video Player** | `poster`, `preload="metadata"`, multiple formats, fallback link, responsive CSS | **No `<track>` captions**; `.mov` source is unreliable; consider `playsinline` |
| **Bookstore** | n/a | If it ever gets cover images, plan `alt`, `width`, `height`, `loading="lazy"` |

> 🧪 Pattern: my media pages work, but they lack **captions, transcripts, file-name hygiene, and `rel` safety.** All quick wins.

---

## 💥 Mistakes I Actually Made

| # | Mistake | Why it's a problem | The fix |
|---|---|---|---|
| 1 | Alt text on a linked image described the picture | Screen reader users don't learn where the link goes | Describe the destination |
| 2 | Left out `width` and `height` on images | Page jumps as images load | Always set them, plus `max-width: 100%; height: auto` |
| 3 | Used `target="_blank"` with no `rel` and no warning | Surprises users; minor security habit gap | `rel="noopener noreferrer"` + "(opens in a new tab)" |
| 4 | Left a space inside the link text | The underline starts with a gap | Move the space outside the `<a>` |
| 5 | Put an apostrophe in a file name | Needs URL-encoding and can break links | Lowercase-hyphenated names only |
| 6 | Skipped captions on the video | Deaf users miss everything | `<track kind="captions">` |
| 7 | Put `loop` on every audio track | Tracks never move on | Use `loop` deliberately |
| 8 | Included a `.mov` source | Not reliably supported | MP4 (+ WebM) |
| 9 | Hotlinked workshop assets | They can vanish | Host my own copies for real projects |
| 10 | Used `href="#"` as a placeholder | Jumps to the top of the page | Use a real URL, or a `<button>` if it triggers an action |

> 🛠️ Each of these is now on my pre-flight checklist.

---

## 🧾 Cheat Sheet

### Which tag do I need?

| I want to... | Use |
|---|---|
| Link to another page | `<a href="page.html">` |
| Jump within the page | `<a href="#id">` |
| Open the email app | `<a href="mailto:…">` |
| Download a file | `<a href="file.pdf" download>` |
| Show an image | `<img src alt width height>` |
| Show an image with a caption | `<figure>` + `<figcaption>` |
| Serve different image sizes | `srcset` + `sizes` |
| Serve modern formats with fallback | `<picture>` + `<source type>` |
| Show a logo or icon | SVG |
| Play audio | `<audio controls>` |
| Play video | `<video controls poster>` |
| Add captions | `<track kind="captions">` |
| Embed YouTube / a map | `<iframe title>` |

### Pre-flight checklist ✅

**Links**
- [ ] Link text makes sense out of context
- [ ] Paths are correct (`./`, `../`, `/`) and case matches the real file name
- [ ] File names: lowercase, hyphens, no spaces or special characters
- [ ] `target="_blank"` has `rel="noopener noreferrer"` and a warning
- [ ] No `href="#"` placeholders
- [ ] Downloads mention type and size

**Images**
- [ ] Every `<img>` has `alt` (empty if decorative)
- [ ] Linked images use destination-describing alt
- [ ] `width` and `height` set; CSS makes them fluid
- [ ] Below-the-fold images use `loading="lazy"`
- [ ] Images are resized and compressed
- [ ] Right format for the job (photos → WebP/JPEG, logos → SVG)

**Audio and video**
- [ ] `controls` present
- [ ] Fallback content inside the element
- [ ] Multiple source formats where needed (MP3/MP4 as the baseline)
- [ ] Captions (`<track>`) and/or transcripts
- [ ] No autoplay with sound
- [ ] `preload` set deliberately

**Embeds and rights**
- [ ] `<iframe>` has a `title`
- [ ] Embed source is trusted; `sandbox` considered
- [ ] I have the right to use every image, sound, and video
- [ ] Required attribution is included

---

## 🎮 Practice Ideas

1. 🌱 **Link map.** Make three pages in different folders that link to each other with relative paths. Break one on purpose and see what happens.
2. 🌱 **Alt text workout.** Pick 10 images and write good alt text for each, including one decorative image and one linked image.
3. 🌱 **Photo gallery.** Use `figure`, `figcaption`, and `loading="lazy"` for six photos.
4. 🔧 **Responsive image.** Create three sizes of one photo and use `srcset` + `sizes`. Check the Network tab to see which one loads at different window widths.
5. 🔧 **Format showdown.** Convert one photo to JPEG, WebP, and AVIF. Compare file sizes and quality.
6. 🔧 **`<picture>` fallback.** Serve AVIF → WebP → JPEG and test by disabling formats in DevTools.
7. 🔧 **Caption the video.** Write a `.vtt` file for the Video Player and add `<track>`.
8. 🔧 **Audio with transcript.** Add a transcript page and link to it from the Music Player.
9. 🚀 **Anchor navigation.** Build a one-page site with a sticky header, smooth scrolling, and `scroll-margin-top`.
10. 🚀 **Safe embed.** Embed a YouTube video with a `title` and lazy loading, then make it responsive with CSS.
11. 🚀 **Performance audit.** Run Lighthouse on a media-heavy page, then fix the top three issues.
12. 🚀 **Link rot check.** Revisit this repo's external links in a month and note which ones broke.

---

## 🛠️ Tools

| Tool | What it's for |
|---|---|
| 🗜️ [Squoosh](https://squoosh.app/) | Compress and convert images (WebP, AVIF) in the browser |
| 🗜️ [TinyPNG](https://tinypng.com/) | Quick PNG/JPEG compression |
| ✏️ [SVGOMG](https://jakearchibald.github.io/svgomg/) | Optimize SVG files |
| 🎬 [HandBrake](https://handbrake.fr/) | Convert and compress video (MP4/WebM) |
| 🎧 [Audacity](https://www.audacityteam.org/) | Edit and export audio |
| 💬 [Subtitle Edit](https://www.nikse.dk/subtitleedit) | Create and edit caption files |
| 🔍 **DevTools → Network tab** | See file sizes, which `srcset` image loaded, load order |
| ♿ **Lighthouse / axe / WAVE** | Catch missing alt text, bad link text, missing captions |
| ✅ [W3C Validator](https://validator.w3.org/) | Catch bad nesting and attributes |
| 🔗 [W3C Link Checker](https://validator.w3.org/checklink) | Find broken links |
| 📖 [MDN: Multimedia and embedding](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding) | Excellent step-by-step guide |
| 📖 [MDN: `<a>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) | Every link attribute explained |

---

## 🔗 Related

- 📄 [`basics.md`](./basics.md): tags, attributes, and the beginner version of links and images
- 🏛️ [`semantic-html.md`](./semantic-html.md): `figure`, `nav`, and choosing the right element
- 📝 [`forms.md`](./forms.md): file uploads and form controls
- ♿ [`accessibility.md`](./accessibility.md): alt text, captions, and link text in depth
- 🧪 [`examples/`](./examples): Cat Photo App, Cat Blog, Music Player, and Video Player live here
- 🎨 [`../CSS`](../CSS): responsive images, `object-fit`, and link styling
- ⚡ [`../JavaScript`](../JavaScript): custom players and dynamic media
- 🌐 [`../notes/useful-resources.md`](../notes/useful-resources.md): where I keep the good bookmarks
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>A suit that can't connect or show anything is just a shell. Mark V can reach out and light up the room. 🦾</i></p>
