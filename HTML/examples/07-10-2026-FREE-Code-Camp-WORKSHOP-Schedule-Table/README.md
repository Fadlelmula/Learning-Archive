# 🗓️ Conference Schedule Table

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Accessibility](https://img.shields.io/badge/Accessibility-first-4c1?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Mark%20I-orange?style=for-the-badge)
![Part of](https://img.shields.io/badge/Part%20of-Learning--Archive-blue?style=for-the-badge)

> **Mark I of "make a table that doesn't suck."** 🛠️
> A conference schedule built from pure HTML: no CSS, no JavaScript, just the bones. Before you can armor the suit, you need a solid skeleton.

---

## 🎯 What is this?

A one-day tech conference schedule laid out as an HTML table: **3 tracks**, **6 time slots**, and a couple of full-width break rows.

It came out of a free Code Camp workshop, and it's here because tables are one of those things I *thought* I knew until I had to build one properly.

---

## 📁 What's inside

| File | What it does |
|------|--------------|
| `07-10-2026-FREE-Code-Camp-WORKSHOP-Schedule-Table.html` | The schedule table itself |
| `README.md` | You are here 👋 |

---

## 🧠 Concepts practiced

| Concept | Where it shows up |
|---------|-------------------|
| `<table>` structure | `<thead>` for headers, `<tbody>` for the schedule rows |
| `<caption>` | Describes the table for screen readers: "Schedule by Track and Time" |
| `scope="col"` | Marks Time / Track A / Track B / Track C as **column** headers |
| `scope="row"` | Marks each time slot as a **row** header |
| `colspan="3"` | Break and Lunch rows stretch across all three tracks |
| Semantic HTML | `<th>` for headers, `<td>` for data. No `<div>` soup 🍜 |

---

## 🗺️ The schedule

| Time | Track A | Track B | Track C |
|------|---------|---------|---------|
| 9:00 AM | Keynote: Tech Future | Intro to Web Dev | UX for All |
| 10:00 AM | Accessibility Deep Dive | CSS for Beginners | Inclusive Design Principles |
| 11:00 AM | ☕ *Break (all tracks)* | | |
| 11:30 AM | AR/VR in Education | JavaScript Fundamentals | Design Systems at Scale |
| 12:30 PM | 🍽️ *Lunch Break (all tracks)* | | |
| 2:00 PM | Voice UI Workshop | Git & GitHub Essentials | Color & Contrast in UI |

---

## 💡 Why `scope` matters

Screen readers use `scope` to announce the right header as you move through cells. Without it, someone navigating to "Intro to Web Dev" might hear nothing about *which time* or *which track* it belongs to. With it, they hear "9:00 AM, Track B, Intro to Web Dev."

Same table, completely different experience. Accessibility isn't a bonus feature; it's part of building it right. ♿

---

## 🐛 Things I caught while reviewing

Honest log, because mistakes are the whole point of this repo:

| Issue | Why it matters | Fix |
|-------|----------------|-----|
| Raw `&` in `Git & GitHub Essentials` and `Color & Contrast in UI` | Browsers forgive it, but it's invalid HTML | Use `&amp;` |
| Missing `<meta name="viewport">` | Page won't scale properly on phones | Add `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| Last row indented differently from the rest | Works fine, but harder to read | Match the indentation |

---

## 🚀 Run it

1. Download or clone the repo
2. Open the `.html` file in any browser
3. That's it. No build step, no dependencies 🎉

---

## 🔮 Mark II ideas

- [ ] Add CSS: borders, zebra stripes, hover states
- [ ] Style the break rows so they stand out
- [ ] Make it responsive (tables on phones are a puzzle 🧩)
- [ ] Fix the issues in the table above
- [ ] Maybe generate the rows with JavaScript later

---

## 🧰 Part of the Learning-Archive

This is one example in my [Learning-Archive](../../README.md), a public log of rebuilding rusty skills one project at a time. Mark I today, Mark 85 eventually. 🦾

*Built by [@Fadlelmula](https://github.com/Fadlelmula)*
