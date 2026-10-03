# 🏨 Hotel Feedback Form

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-workshop-0a0a23?style=flat-square&logo=freecodecamp&logoColor=white)
![Date](https://img.shields.io/badge/built-1%20Oct%202026-lightgrey?style=flat-square)
![Forms](https://img.shields.io/badge/topic-forms-blueviolet?style=flat-square)

> The biggest suit upgrade yet: a page that **asks you things** and lets the browser check the answers. 📝

A freeCodeCamp workshop form where guests rate their hotel stay. It uses nearly every common form control in one page.

📄 **File:** [`01-10-2026-Free-Code-Camp-WORKSHOP-Hotel-Feedback-Form.html`](./01-10-2026-Free-Code-Camp-WORKSHOP-Hotel-Feedback-Form.html)

---

## 🧩 The form, section by section

| Section (`<fieldset>`) | Controls | Notes |
|------------------------|----------|-------|
| 👤 Personal Information | Text, email, number inputs | Name and email are `required`; age is optional with `min="3"` and `max="100"` |
| 🔘 First time at the hotel? | Two **radio** buttons (Yes / No) | Same `name`, so only one can be chosen |
| ☑️ Why did you choose us? | Five **checkboxes** | Pick several; *Reputation* starts pre-checked |
| ⭐ Ratings | Two **dropdowns** (`<select>`) | Service and food, each defaulting to *Excellent* |
| 💬 Comments | `<textarea>` | A 30 × 10 box for free text |
| 📤 Submit | `<button type="submit">` | Sends the form with `method="POST"` |

---

## 🧱 Form features worth remembering

| Feature | What it does |
|---------|--------------|
| `<label for="x">` + `id="x"` | Connects a label to its input, so clicking the text focuses the field |
| `<fieldset>` + `<legend>` | Groups related controls and gives the group a title |
| `required` | The browser blocks submission if the field is empty |
| `type="email"` | The browser checks for a valid-looking email address |
| `placeholder` | Faint example text inside the field |
| `checked` / `selected` | Sets the default choice |
| `name` | The key the data is sent under; radios and checkboxes share one per group |
| `value` | What actually gets sent for each option |

---

## 🚀 How to run it

Open the `.html` file in a browser and fill it in. Try leaving **Name** or **Email** empty, or typing something that isn't an email, and watch the browser complain. 😄

The form's `action` points to a freeCodeCamp practice URL, so treat submitting as practice and don't expect a real thank-you page.

---

## 🧠 What I practiced

- Choosing the right control: radio for one choice, checkbox for many, select for a list
- Built-in browser validation (no JavaScript needed!)
- Accessible labeling with `for` and `id`
- Grouping with `fieldset` and `legend`

---

## 💥 Honest corner

- The radio buttons aren't `required`, so someone can skip that question.
- Spacing is rough since there's no CSS yet: everything sits in a line.
- `size="20"` appears on some inputs and not others. A tiny inconsistency to tidy up.
- No `viewport` meta tag.

---

## 🔮 Mark II ideas

- Style the form with CSS: spacing, focus states, a friendly layout 🎨
- Add `required` to the radio group
- Add a star-rating or range slider
- Handle the submission for real with a small backend or JavaScript

---

↩️ [Back to examples](../README.md)

*Your feedback is important to us. (Said every form ever.) 💌*
