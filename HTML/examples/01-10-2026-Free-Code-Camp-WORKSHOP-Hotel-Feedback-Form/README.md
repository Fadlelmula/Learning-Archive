# 🌺 Hotel Feedback Form 🌺

> *Like the red spider lily, this form blooms at the very end of a stay, right when guests are leaving. Then it asks, very politely: "So... how was it?"*

A freeCodeCamp workshop project: a clean, semantic HTML feedback form for a hotel. No CSS, no JavaScript, just pure HTML petals. 🥀

---

## 🕯️ What is this?

Guests check out. Guests have opinions. This form catches those opinions before they float away like lantern smoke.

It collects:

- 🪪 **Who they are**: name, email, and (optionally) age
- 🛎️ **First time here?**: a yes / no radio choice
- 🧭 **Why they picked us**: checkboxes, pick as many as you like
- ⭐ **How we did**: dropdown ratings for service and food
- 💌 **Anything else**: a big open textarea for the juicy stuff

---

## 🌿 What's inside (the anatomy of the bloom)

| Part | Tag(s) | Job |
|------|--------|-----|
| Welcome | `<header>`, `<h1>`, `<p>` | Says thank you like a good host |
| The form | `<form method="POST" action="...">` | Sends everything off when guests press Submit |
| Grouping | `<fieldset>` + `<legend>` | Keeps related questions together, like petals on one stem |
| Text answers | `<input type="text">`, `type="email"`, `type="number"` | Name, email, age |
| One choice | `<input type="radio">` | First visit: yes or no |
| Many choices | `<input type="checkbox">` | Reasons for staying |
| Pick from a list | `<select>` + `<option>` | Service and food ratings |
| Long answer | `<textarea>` | Free-form comments |
| Send it | `<button type="submit">` | The final step |

---

## 🪷 Little details that matter

- **Every input has a `<label>`**, linked with `for` and `id`. Click the label, and the field wakes up. Screen readers also love this. 🔗
- **`required`** on name and email, so nobody sneaks past without them. 🚪
- **`type="email"`** gives free built-in validation. The browser plays bouncer. 🕴️
- **`min="3"` and `max="100"`** keep the age field realistic.
- **Radio buttons share one `name`** (`hotel-stay`), so only one can be chosen. Checkboxes share `choice`, so many can be.
- **Defaults:** "Reputation" starts checked, and both ratings start on "Excellent". 🌟

---

## 🚀 How to run it

1. Save the file as `index.html`
2. Open it in any browser
3. Fill it in, press **Submit**
4. The data goes off to the freeCodeCamp practice endpoint. ✨

No installs, no build step, no drama.

---

## 🌸 What I practiced

- Building forms the right way, with `action` and `method`
- Grouping controls with `fieldset` and `legend`
- Connecting labels to inputs
- Choosing the right input type for each job
- Using `required`, `placeholder`, `checked`, and `selected`

---

## 🔮 Maybe next...

- 🎨 Add CSS so the form stops looking like a 1999 tax document
- 📱 Make it responsive for guests filling it in from their phone in the taxi
- ✅ Add a "thank you" page after submit

---

*Made with curiosity, a cup of tea, and a field of red spider lilies in the back of my mind.* 🌺
