# 🖥️ Computer Basics

> The foundation layer. Understand the machine, and everything you build on top of it makes more sense.

## 📑 Table of Contents

1. [Understanding Computers](#1--understanding-computers)
2. [Internet Basics](#2--internet-basics)
3. [Tooling Basics](#3--tooling-basics)
4. [Working with File Systems](#4--working-with-file-systems)
5. [Browsing the Web Effectively](#5--browsing-the-web-effectively)
6. [Quick Recap](#6--quick-recap)

---

## 1. 🧠 Understanding Computers

A computer takes **input**, **processes** it, **stores** data, and produces **output**. Everything else is detail.

### Hardware (the parts you can touch)

| Part | Job | Analogy |
|------|-----|---------|
| **CPU** | Executes instructions, does the thinking | The brain |
| **RAM** | Short-term memory for whatever is running right now. Wiped when power goes off | Your desk |
| **Storage (SSD/HDD)** | Long-term memory. Keeps files when the power is off | Filing cabinet |
| **GPU** | Specialized for graphics and massively parallel math (also used for AI) | A team of specialists |
| **Motherboard** | Connects everything together | The nervous system |
| **Power supply** | Delivers electricity | The heart |
| **Input devices** | Keyboard, mouse, microphone, camera | Senses |
| **Output devices** | Screen, speakers, printer | Voice |

**RAM vs storage** is the one people mix up most. A 16 GB RAM / 512 GB storage machine can juggle a lot at once (RAM) and keep a lot saved (storage). They're different things.

### Software (the instructions)

| Layer | What it is | Examples |
|-------|-----------|----------|
| **Firmware** | Tiny built-in software that starts the hardware | BIOS/UEFI |
| **Operating system (OS)** | Manages hardware and runs programs | Windows, macOS, Linux, Android, iOS |
| **Applications** | Programs you actually use | Browser, VS Code, Spotify |

The OS is the middleman: apps ask the OS for things (open a file, use the network), and the OS talks to the hardware.

### Binary: how computers "think"

Computers only understand **on/off**, written as `1` and `0`. One of these is a **bit**; 8 bits make a **byte**.

| Unit | Size |
|------|------|
| 1 byte | 8 bits (one character, roughly) |
| 1 KB | ~1,000 bytes |
| 1 MB | ~1,000 KB |
| 1 GB | ~1,000 MB |
| 1 TB | ~1,000 GB |

Text, images, music, video: all of it is just long strings of 1s and 0s, interpreted differently.

### What happens when you press the power button

1. Power flows in and the firmware (BIOS/UEFI) wakes up the hardware
2. Firmware finds the OS on storage and loads it into RAM (this is **booting**)
3. The OS starts background services and shows you the desktop
4. You open an app: it loads from storage into RAM, and the CPU runs its instructions

---

## 2. 🌐 Internet Basics

**The internet** is a giant network of connected computers. **The web** (websites) is just one thing that runs on top of it, alongside email, video calls, and online games.

### How a website loads (the short version)

```
You type google.com
      ↓
Your browser asks DNS: "what's the address of google.com?"
      ↓
DNS answers with an IP address (like 142.250.x.x)
      ↓
Your browser sends a request to that server (HTTP/HTTPS)
      ↓
The server sends back HTML, CSS, JavaScript, images
      ↓
Your browser assembles it into the page you see
```

### Key vocabulary

| Term | Meaning |
|------|---------|
| **IP address** | A computer's address on a network |
| **DNS** | The internet's phonebook: turns names into IP addresses |
| **URL** | The full address of a page, e.g. `https://example.com/page` |
| **Domain** | The name part, e.g. `example.com` |
| **Server** | A computer that stores and serves websites or data |
| **Client** | The device asking for things (your phone or laptop) |
| **HTTP / HTTPS** | The rules for sending web pages. The **S** means encrypted and safer |
| **Router** | Directs traffic between your devices and the internet |
| **ISP** | The company that sells you internet access |
| **Bandwidth** | How much data can move at once (speed) |
| **Latency** | The delay before data starts arriving (lag) |
| **Cloud** | Just "someone else's computer" that you reach over the internet |

### Anatomy of a URL

```
https://www.example.com:443/blog/post?id=7#comments
└─┬──┘   └──────┬──────┘└┬─┘└───┬───┘└──┬──┘└───┬───┘
protocol    domain     port   path   query   fragment
```

### Staying safe

- Look for **https** and the padlock, but know that a padlock only means the connection is encrypted, not that the site is trustworthy
- Use a password manager and a unique password for each account
- Turn on two-factor authentication (2FA) wherever you can
- Be suspicious of urgent messages and unexpected links (phishing)
- Keep your OS and browser updated

---

## 3. 🔧 Tooling Basics

Tools are how you stop doing things the slow way.

### Essential tool categories

| Category | What it does | Examples |
|----------|-------------|----------|
| **Text editor / IDE** | Where you write code | VS Code, Notepad++, PyCharm |
| **Terminal / command line** | Control the computer with text commands | Terminal, PowerShell, Bash |
| **Browser + DevTools** | View sites and inspect how they work | Chrome, Firefox, Edge |
| **Version control** | Track changes and collaborate | Git, GitHub |
| **Package managers** | Install software and libraries by command | npm, pip, winget, Homebrew |
| **Note-taking** | Keep your knowledge organized | Markdown files, Obsidian, Notion |

### The terminal in 60 seconds

The terminal looks scary but it's just another way to do what you do with a mouse.

| Command (Mac/Linux) | Windows PowerShell equivalent | What it does |
|---------------------|-------------------------------|--------------|
| `pwd` | `pwd` | Show the current folder |
| `ls` | `ls` or `dir` | List files here |
| `cd folder` | `cd folder` | Move into a folder |
| `cd ..` | `cd ..` | Go up one level |
| `mkdir name` | `mkdir name` | Create a folder |
| `touch file.txt` | `ni file.txt` | Create an empty file |
| `cp a b` | `cp a b` | Copy a file |
| `mv a b` | `mv a b` | Move or rename |
| `rm file` | `rm file` | Delete a file (no recycle bin!) |
| `clear` | `clear` | Clean the screen |

> ⚠️ **Careful:** `rm` deletes permanently. Double-check before pressing Enter.

### Shortcuts worth memorizing

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Copy / Paste / Cut | `Ctrl+C` / `V` / `X` | `Cmd+C` / `V` / `X` |
| Undo / Redo | `Ctrl+Z` / `Ctrl+Y` | `Cmd+Z` / `Cmd+Shift+Z` |
| Select all | `Ctrl+A` | `Cmd+A` |
| Find | `Ctrl+F` | `Cmd+F` |
| Save | `Ctrl+S` | `Cmd+S` |
| Switch apps | `Alt+Tab` | `Cmd+Tab` |
| Switch tabs | `Ctrl+Tab` | `Cmd+Option+→` |
| Reopen closed tab | `Ctrl+Shift+T` | `Cmd+Shift+T` |

### Why Markdown?

Markdown (`.md`) is plain text with light formatting symbols (`#` for headings, `**bold**`, `-` for lists). It works everywhere, GitHub renders it automatically, and it'll still open in 30 years. That's why this whole archive is written in it.

---

## 4. 📁 Working with File Systems

A **file system** is how the OS organizes data on storage: files inside folders (directories) inside folders.

### Core ideas

| Concept | Meaning |
|---------|---------|
| **File** | A named chunk of data (document, image, program) |
| **Folder / directory** | A container for files and other folders |
| **Path** | The "address" of a file in the file system |
| **Root** | The top of the tree (`C:\` on Windows, `/` on Mac/Linux) |
| **Home folder** | Your personal space (`C:\Users\you`, `/Users/you`, `/home/you`) |
| **Extension** | The ending that hints at file type (`.txt`, `.jpg`, `.py`) |

### Paths: absolute vs relative

| Type | Example | Meaning |
|------|---------|---------|
| **Absolute** | `/Users/sam/projects/app/index.html` | Starts from the root, always points to the same place |
| **Relative** | `./images/logo.png` | Starts from where you are right now |
| `.` | | The current folder |
| `..` | | The parent folder (one level up) |
| `~` | | Your home folder (Mac/Linux) |

Path separators differ: Windows uses `\`, Mac/Linux use `/`. Code and URLs almost always use `/`.

### Common file types

| Category | Extensions |
|----------|-----------|
| Text / docs | `.txt`, `.md`, `.pdf`, `.docx` |
| Images | `.jpg`, `.png`, `.gif`, `.svg`, `.webp` |
| Audio / video | `.mp3`, `.wav`, `.mp4`, `.mov` |
| Code | `.html`, `.css`, `.js`, `.py`, `.sql` |
| Data | `.csv`, `.json`, `.xlsx` |
| Archives | `.zip`, `.tar`, `.7z` |

> 💡 On Windows, turn on **File name extensions** in File Explorer's View menu. Hidden extensions cause real confusion (and hide malware like `invoice.pdf.exe`).

### Good habits

1. **Name files clearly**: `html-forms-notes.md`, not `new document (3).md`
2. **Avoid spaces** in names for code and web files. Use `-` or `_` (`my-notes.md`)
3. **Use lowercase** for web and code files to avoid case-sensitivity bugs between systems
4. **Group by topic**, not by file type, and keep the nesting shallow
5. **Date things** when versions matter: `2026-10-11-plan.md` sorts nicely
6. **Back up** with the 3-2-1 rule: 3 copies, 2 different media, 1 off-site (cloud counts)
7. **Know the difference** between *delete* (recycle bin, recoverable) and *permanently delete*

### Example: a tidy project folder

```
my-project/
├── README.md
├── index.html
├── css/
│   └── style.css
├── js/
│   └── app.js
└── images/
    └── logo.png
```

---

## 5. 🔍 Browsing the Web Effectively

The browser is probably the tool you use most. Use it on purpose.

### Search like a pro

| Trick | Example | Effect |
|-------|---------|--------|
| Exact phrase | `"flexbox vs grid"` | Matches that exact phrase |
| Exclude a word | `python tutorial -snake` | Removes results with "snake" |
| Specific site | `site:developer.mozilla.org fetch` | Searches only that site |
| File type | `filetype:pdf css cheat sheet` | Finds only PDFs |
| Either word | `html OR css` | Matches either term |
| Wildcard | `"how to * in python"` | `*` fills in any word |

**Tip:** put the error message in quotes when debugging. Someone has almost certainly hit it before.

### Judge sources quickly

| Check | Ask yourself |
|-------|--------------|
| **Who wrote it?** | Is there an author or organization behind it? |
| **When?** | Tech goes stale fast. Prefer recent content |
| **Evidence** | Does it cite or link to sources? |
| **Official docs** | MDN, Python docs, and similar beat random blogs |
| **Agreement** | Do several reliable sources say the same thing? |

Good starting places for learners: MDN Web Docs, official language docs, freeCodeCamp, and the source repo's README.

### Browser skills

- **Tabs:** pin the ones you always need, group the rest, and close what you're done with
- **Bookmarks:** organize in folders or you'll never find anything again
- **Profiles:** separate work, learning, and personal browsing
- **Extensions:** install few, from trusted sources. Each one can see what you browse
- **Find on page:** `Ctrl+F` / `Cmd+F` saves tons of scrolling
- **Reader mode:** strips clutter from articles
- **Private/incognito:** doesn't save history locally, but does *not* make you anonymous online

### DevTools (open with `F12` or `Ctrl+Shift+I` / `Cmd+Option+I`)

| Tab | What it's for |
|-----|---------------|
| **Elements** | Inspect and live-edit HTML and CSS |
| **Console** | See errors and run JavaScript |
| **Network** | Watch every request the page makes |
| **Application** | Look at storage, cookies, and more |

Right-click anything on a page → **Inspect** is one of the best ways to learn how websites are built.

### Privacy and safety

- Check what permissions sites ask for (location, notifications, camera)
- Clear cookies and cache when something acts weird (it's the classic fix)
- Don't download from unfamiliar sites; get software from the official source
- Hover over links to see the real destination before clicking
- If a deal or alert feels too urgent or too good, it's probably a scam

---

## 6. ✅ Quick Recap

| Topic | The one thing to remember |
|-------|---------------------------|
| 🧠 Computers | CPU thinks, RAM is the desk, storage is the cabinet, the OS manages it all |
| 🌐 Internet | Browser → DNS → server → page. HTTPS means encrypted |
| 🔧 Tooling | Learn your editor, terminal, and shortcuts. They compound |
| 📁 File systems | Clear names, tidy folders, know your paths, back things up |
| 🔍 Web browsing | Search with operators, check sources, learn DevTools |

---

## 🪞 Honest Notes

*(Space for me to fill in as I learn. Add to `notes/things-i-finally-understood.md` too.)*

- [ ] Practice terminal commands daily for a week
- [ ] Reorganize my own file system using these habits
- [ ] Set up a proper backup

---

⬅️ [Back to the computer folder](./README.md) · 🏠 [Back to the main archive](../README.md)
