# 📝 HTML Forms

> Collect input without crying.
> Mark III of the armor: the part where the suit finally listens back.

![Topic](https://img.shields.io/badge/topic-forms-E34F26?logo=html5&logoColor=white)
![Level](https://img.shields.io/badge/level-intermediate-yellow)
![Status](https://img.shields.io/badge/status-growing-brightgreen)
![Validation](https://img.shields.io/badge/validation-built%20in-blue)
![Last updated](https://img.shields.io/badge/updated-Oct%202026-lightgrey)

---

## 🗂️ Table of Contents

1. [What a form is](#-what-a-form-is)
2. [The form element](#-the-form-element)
3. [How forms send data](#-how-forms-send-data)
4. [Labels](#-labels)
5. [Input types](#-input-types)
6. [Input attributes](#-input-attributes)
7. [Checkboxes and radio buttons](#-checkboxes-and-radio-buttons)
8. [Select, datalist and textarea](#-select-datalist-and-textarea)
9. [Buttons](#-buttons)
10. [Grouping with fieldset and legend](#-grouping-with-fieldset-and-legend)
11. [Built-in validation](#-built-in-validation)
12. [Autocomplete](#-autocomplete)
13. [Accessible forms](#-accessible-forms)
14. [Full example: the feedback form, improved](#-full-example-the-feedback-form-improved)
15. [Security reality check](#-security-reality-check)
16. [Mistakes I actually made](#-mistakes-i-actually-made)
17. [Cheat sheet](#-cheat-sheet)
18. [Practice ideas](#-practice-ideas)
19. [Tools](#-tools)
20. [Related](#-related)

---

## 🧠 What a Form Is

A form is how a web page **asks the user for something**: a login, a search, a signup, a review, a payment. It is a group of controls (inputs, dropdowns, buttons) wrapped in a `<form>` element that knows how to collect their values and send them somewhere.

```
 user fills in controls  →  clicks Submit  →  browser packages the data
                                          →  sends it to the server (action)
                                          →  server responds with a new page
```

> 💡 **HTML alone only builds the form and does the basic checking.** To actually *receive* and store the data, you need a server (or a form service). Frontend practice pages like mine can build and validate forms, but the data goes nowhere useful yet.

---

## 📦 The Form Element

```html
<form action="/subscribe" method="post">
  <!-- controls go here -->
</form>
```

| Attribute | Purpose | Notes |
|---|---|---|
| `action` | URL that receives the data | Empty or missing means "this same page" |
| `method` | How to send: `get` or `post` | Default is `get` |
| `enctype` | How the data is encoded | Use `multipart/form-data` when uploading files (with `post`) |
| `novalidate` | Turns off the browser's built-in validation | Useful when I handle validation myself |
| `autocomplete` | `on` / `off` for the whole form | Usually leave on |
| `target` | Where the response opens | `_blank` opens a new tab |

Controls can live anywhere inside the `<form>`. Pressing **Enter** in a text field submits the form (when there is a submit button).

---

## 📮 How Forms Send Data

Each control's data is sent as a **name=value** pair:

```
username=tony&email=tony%40stark.com&rating=excellent
```

### 🔑 The golden rule: `name` is what gets sent

| Attribute | Used for |
|---|---|
| `name` | The key sent to the server. **No `name` = the control's data is not submitted.** |
| `id` | Linking a `<label for>`, anchor links, CSS/JS targeting. Must be unique. |
| `value` | The data itself (for text it's what the user types) |

Easy trap: `id` and `name` are **not** the same thing and don't replace each other.

### GET vs POST

| | `GET` | `POST` |
|---|---|---|
| Where the data goes | In the URL: `?q=cats&page=2` | In the request body |
| Visible in the address bar? | ✅ Yes | ❌ No |
| Can be bookmarked/shared? | ✅ Yes | ❌ No |
| Good for | **Searching, filtering** (safe, repeatable) | **Logins, signups, payments, anything that changes data** |
| Size limit | Small | Large |
| Passwords/sensitive data? | ❌ Never | ✅ Yes (over HTTPS) |

### What does *not* get submitted

| Situation | Sent? |
|---|---|
| Control with no `name` | ❌ |
| Unchecked checkbox or radio | ❌ |
| `disabled` control | ❌ |
| `readonly` control | ✅ |
| Empty text field | ✅ (as an empty value) |
| `<input type="hidden">` | ✅ (invisible to the user) |

---

## 🏷️ Labels

Every control needs a **label**. It tells the user (and screen readers) what to type, and it makes the clickable area bigger.

### Two ways to connect them

```html
<!-- 1. Explicit: for + id must match -->
<label for="email">Email</label>
<input type="email" id="email" name="email">

<!-- 2. Implicit: wrap the input -->
<label>
  Email
  <input type="email" name="email">
</label>
```

| Method | Pros | Cons |
|---|---|---|
| `for` + `id` | Most reliable, label and input can be anywhere | Needs a unique `id` |
| Wrapping | No `id` needed | Can complicate layout |

### Placeholder is NOT a label

```html
<!-- ❌ -->
<input type="email" placeholder="Email">

<!-- ✅ -->
<label for="email">Email</label>
<input type="email" id="email" name="email" placeholder="you@example.com">
```

Why placeholders fail as labels:
- They **vanish** as soon as you type, so you forget what the field was.
- Their default color has poor contrast.
- Screen readers don't treat them as reliable labels.

Use placeholders for **format hints** only.

---

## 🎛️ Input Types

The `type` attribute decides what the `<input>` does. Choosing the right one gives me **free validation, the correct mobile keyboard, and built-in widgets**.

### Text-like

| Type | For | Bonus |
|---|---|---|
| `text` | Short free text (default) | |
| `email` | Email addresses | Validates format; email keyboard on phones |
| `password` | Passwords | Hides characters |
| `tel` | Phone numbers | Phone keypad on mobile; **no format validation** |
| `url` | Web addresses | Validates URL format |
| `search` | Search boxes | May show a clear (✕) button |

### Numbers and ranges

| Type | For | Notes |
|---|---|---|
| `number` | Quantities, ages, counts | Supports `min`, `max`, `step` |
| `range` | Slider | Add a visible value display; sliders hide the exact number |

> ⚠️ **Don't use `type="number"` for** phone numbers, zip codes, credit cards, or IDs. They're not quantities (you can't "add 1" to a phone number), and leading zeros get lost. Use `type="text"` with `inputmode="numeric"`.

### Dates and times

| Type | For | Value format |
|---|---|---|
| `date` | A day | `2026-10-03` |
| `time` | A time | `14:30` |
| `datetime-local` | Date + time | `2026-10-03T14:30` |
| `month` | A month | `2026-10` |
| `week` | A week | `2026-W40` |

### Choices and other

| Type | For |
|---|---|
| `checkbox` | Zero, one, or many yes/no choices |
| `radio` | Exactly one choice from a group |
| `color` | Color picker |
| `file` | File upload (`accept`, `multiple`) |
| `hidden` | Data the user doesn't see (like an ID) |

### Button-like inputs

| Type | Behavior |
|---|---|
| `submit` | Submits the form |
| `reset` | Clears the form back to defaults (rarely a good idea; users hit it by accident) |
| `button` | Does nothing by itself (for JS) |

> 💡 If a browser doesn't understand a `type`, it falls back to `text`. So newer types are safe to use.

---

## 🔧 Input Attributes

| Attribute | What it does | Example |
|---|---|---|
| `name` | Key for the submitted data | `name="email"` |
| `id` | Unique ID for the label link | `id="email"` |
| `value` | Initial/default value (or the value sent for checkbox/radio) | `value="excellent"` |
| `placeholder` | Format hint, **not a label** | `placeholder="you@example.com"` |
| `required` | Field must be filled in | `required` |
| `disabled` | Greyed out, not editable, **not submitted** | `disabled` |
| `readonly` | Visible but not editable, **is submitted** | `readonly` |
| `min` / `max` | Limits for numbers and dates | `min="3" max="120"` |
| `step` | Allowed increments | `step="0.01"` |
| `minlength` / `maxlength` | Limits for text length | `maxlength="200"` |
| `pattern` | Regex the value must match (whole value) | `pattern="[0-9]{5}"` |
| `autocomplete` | Hint for autofill | `autocomplete="email"` |
| `autofocus` | Focus on page load | Use sparingly; it can disorient screen reader users |
| `multiple` | Allow several values (email, file) | `multiple` |
| `accept` | File types for uploads | `accept="image/*"` |
| `list` | Link to a `<datalist>` for suggestions | `list="cities"` |
| `inputmode` | Mobile keyboard hint | `inputmode="numeric"` |

### `pattern` tips

```html
<label for="zip">ZIP code</label>
<input type="text" id="zip" name="zip"
       pattern="[0-9]{5}"
       inputmode="numeric"
       title="Five digits, like 90210">
```

- Do not write slashes (`/…/`); the browser handles it.
- The pattern must match the **entire** value.
- Use `title` to explain the format. It shows up in the error message.

---

## ☑️ Checkboxes and Radio Buttons

### Radio buttons: pick ONE

Radios are grouped by sharing the **same `name`**.

```html
<fieldset>
  <legend>How was your stay?</legend>

  <label><input type="radio" name="stay" value="great" required> Great</label>
  <label><input type="radio" name="stay" value="okay"> Okay</label>
  <label><input type="radio" name="stay" value="poor"> Poor</label>
</fieldset>
```

- Different `name` = different group = can select both.
- Put `required` on **one** radio in the group (it applies to the whole group), or on all of them. Without it, users can skip the question.
- Use `checked` to pre-select one. Think carefully before doing it, because defaults bias answers.
- Same `name` + different `value` is how the server knows which one was chosen.

### Checkboxes: pick ANY

```html
<fieldset>
  <legend>What did you like?</legend>

  <label><input type="checkbox" name="liked" value="food"> Food</label>
  <label><input type="checkbox" name="liked" value="staff"> Staff</label>
  <label><input type="checkbox" name="liked" value="pool"> Pool</label>
</fieldset>
```

- Same `name` for a group lets the server receive multiple values.
- A single checkbox (like "I agree to the terms") can use `required`.
- If unchecked, nothing is sent. If checked with no `value`, the value is `on`.

| | Radio | Checkbox |
|---|---|---|
| Selection | Exactly one in group | Zero or many |
| Grouped by | Same `name` | Optional same `name` |
| Can the user unselect? | ❌ Not once chosen | ✅ Yes |
| Use for | Mutually exclusive options | Independent options |

---

## 🔽 Select, Datalist and Textarea

### `<select>`: dropdown

```html
<label for="rating">Overall rating</label>
<select id="rating" name="rating" required>
  <option value="">Choose one…</option>
  <option value="excellent">Excellent</option>
  <option value="good">Good</option>
  <option value="poor">Poor</option>
</select>
```

| Feature | How |
|---|---|
| Placeholder option | First `<option value="">` + `required` forces a real choice |
| Pre-selected | `selected` attribute on an `<option>` |
| Group options | `<optgroup label="Europe">...</optgroup>` |
| Pick several | `multiple` (shows a list box) |

> ⚠️ **Default bias:** if "Excellent" is pre-selected and the user doesn't touch the dropdown, the data says everyone loved the hotel. Always start with a blank placeholder option on feedback forms.

For 3-5 options, **radio buttons are often better** than a dropdown because all choices are visible at once.

### `<datalist>`: suggestions, but free typing allowed

```html
<label for="city">City</label>
<input type="text" id="city" name="city" list="cities">
<datalist id="cities">
  <option value="Riyadh">
  <option value="Jeddah">
  <option value="Dammam">
</datalist>
```

| `<select>` | `<datalist>` |
|---|---|
| Must pick from the list | Can pick **or** type anything |

### `<textarea>`: long text

```html
<label for="comments">Comments</label>
<textarea id="comments" name="comments" rows="5" cols="40" maxlength="500"></textarea>
```

- Not a void element: it has a closing tag, and the default text goes **between** the tags.
- `rows` / `cols` set the starting size (CSS can override).
- Whitespace inside is preserved, so don't indent the closing tag onto a new line by accident.

---

## 🔘 Buttons

```html
<button type="submit">Send feedback</button>
<button type="reset">Clear</button>
<button type="button">Do something with JS</button>
```

| Type | Behavior |
|---|---|
| `submit` | Submits the form (**the default inside a form!**) |
| `reset` | Resets the controls |
| `button` | Does nothing on its own |

> ⚠️ **The sneaky default:** a `<button>` with no `type` inside a form acts as `submit`. Always write the `type` explicitly.

### `<button>` vs `<input type="submit">`

| | `<button>` | `<input type="submit">` |
|---|---|---|
| Content | Can hold text, `<strong>`, images, icons | Plain text only (`value`) |
| Preferred? | ✅ More flexible | Works, but limited |

Use clear text: "Send feedback," not "Submit" or "Go".

---

## 🧩 Grouping with fieldset and legend

```html
<form>
  <fieldset>
    <legend>Contact details</legend>
    <label for="name">Name</label>
    <input id="name" name="name" type="text" autocomplete="name">

    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email">
  </fieldset>
</form>
```

| Element | Role |
|---|---|
| `<fieldset>` | Groups related controls (browsers draw a border by default) |
| `<legend>` | The group's caption (must be the **first child**) |

**Why it matters:** for radio and checkbox groups, a screen reader reads the legend *before* each option: "How was your stay? Great, radio button, 1 of 3." Without it, "Great" has no context.

`<fieldset disabled>` disables every control inside it at once.

---

## ✅ Built-in Validation

The browser can validate before the form is even sent, with **no JavaScript**.

| Attribute / type | Checks |
|---|---|
| `required` | Not empty |
| `type="email"` / `url` | Format |
| `min` / `max` | Number or date range |
| `minlength` / `maxlength` | Text length |
| `pattern` | Matches the regex |
| `step` | Value fits the increment |

```html
<label for="age">Age</label>
<input type="number" id="age" name="age" min="3" max="120" required>
```

If something is invalid, the browser blocks the submit, focuses the first bad field, and shows a message.

### Styling valid/invalid states with CSS

| Selector | Matches |
|---|---|
| `:required` / `:optional` | Fields by requirement |
| `:valid` / `:invalid` | Current validity (can flag fields *before* the user touches them) |
| `:user-invalid` / `:user-valid` | Only **after** the user interacted (nicer UX, newer support) |
| `:focus-visible` | Keyboard focus ring |
| `:disabled` | Disabled controls |

### Turning it off

```html
<form novalidate>…</form>
<button type="submit" formnovalidate>Save draft</button>
```

### Limits of built-in validation

- Error messages are browser-controlled and vary between browsers.
- It only checks **format**, not whether data is truthful or acceptable.
- **It can be bypassed in seconds** (see [Security reality check](#-security-reality-check)).

> 🧠 Client-side validation = better UX. Server-side validation = actual safety. I need both eventually.

---

## ⚡ Autocomplete

`autocomplete` lets browsers fill fields from saved data. It's quick to add and a big usability win.

| Value | Field |
|---|---|
| `name` | Full name |
| `given-name` / `family-name` | First / last name |
| `email` | Email |
| `tel` | Phone |
| `street-address` | Address |
| `postal-code` | ZIP/postal code |
| `country-name` | Country |
| `username` | Username |
| `current-password` | Existing password (login) |
| `new-password` | New password (signup; triggers password manager suggestions) |
| `one-time-code` | SMS/2FA codes |
| `cc-number` | Credit card number |
| `off` | Disable (browsers often ignore it for passwords) |

```html
<input type="email" id="email" name="email" autocomplete="email">
```

---

## ♿ Accessible Forms

Forms are where bad accessibility hurts the most, because people literally can't finish what they came to do.

### Checklist of habits

| Do ✅ | Why |
|---|---|
| A visible `<label>` on **every** control | Screen readers, bigger click area, voice control |
| `fieldset` + `legend` for radio/checkbox groups | Gives the options context |
| Tell users which fields are required, in text | Don't rely on color or a lone `*` |
| Put hints in text, linked with `aria-describedby` | Read out with the field |
| Tell users **what went wrong and how to fix it** | "Enter a valid email, like name@example.com" |
| Keep a logical Tab order (follow the DOM order) | Keyboard users |
| Make sure the focus outline is visible | Don't `outline: none` without a replacement |
| Use proper `type` and `autocomplete` | Helps everyone, especially on mobile |

### Linking hints and errors

```html
<label for="password">Password</label>
<input type="password" id="password" name="password"
       minlength="8" required
       autocomplete="new-password"
       aria-describedby="pw-hint">
<p id="pw-hint">At least 8 characters.</p>
```

`aria-describedby` tells the screen reader to read the hint right after the label.

### Required fields

```html
<label for="name">Name <span aria-hidden="true">*</span><span class="sr-only">(required)</span></label>
```

Simpler option: say it once at the top, **"All fields are required unless marked optional,"** and mark the exceptions "(optional)".

---

## 🏨 Full Example: The Feedback Form, Improved

A cleaned-up version of my Hotel Feedback Form, using everything above:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hotel Feedback Form</title>
  </head>
  <body>
    <main>
      <h1>Hotel Feedback Form</h1>
      <p>All fields are required unless marked optional.</p>

      <form action="/submit-feedback" method="post">

        <fieldset>
          <legend>About you</legend>

          <p>
            <label for="name">Name</label><br>
            <input type="text" id="name" name="name" autocomplete="name" required>
          </p>

          <p>
            <label for="email">Email</label><br>
            <input type="email" id="email" name="email" autocomplete="email" required>
          </p>

          <p>
            <label for="age">Age (optional)</label><br>
            <input type="number" id="age" name="age" min="3" max="120">
          </p>
        </fieldset>

        <fieldset>
          <legend>Would you recommend us to a friend?</legend>
          <label><input type="radio" name="recommend" value="yes" required> Yes</label>
          <label><input type="radio" name="recommend" value="maybe"> Maybe</label>
          <label><input type="radio" name="recommend" value="no"> No</label>
        </fieldset>

        <fieldset>
          <legend>Your experience</legend>

          <p>
            <label for="service">Service</label><br>
            <select id="service" name="service" required>
              <option value="">Choose one…</option>
              <option value="excellent">Excellent</option>
              <option value="good">Good</option>
              <option value="fair">Fair</option>
              <option value="poor">Poor</option>
            </select>
          </p>

          <p>
            <label for="comments">Comments (optional)</label><br>
            <textarea id="comments" name="comments" rows="5" cols="40" maxlength="500"></textarea>
          </p>
        </fieldset>

        <fieldset>
          <legend>What did you like? (optional)</legend>
          <label><input type="checkbox" name="liked" value="room"> Room</label>
          <label><input type="checkbox" name="liked" value="food"> Food</label>
          <label><input type="checkbox" name="liked" value="staff"> Staff</label>
        </fieldset>

        <p>
          <label>
            <input type="checkbox" name="consent" required>
            I agree to have my feedback used to improve the hotel.
          </label>
        </p>

        <button type="submit">Send feedback</button>
      </form>
    </main>
  </body>
</html>
```

### What I improved

| Change | Reason |
|---|---|
| Added the viewport meta tag | Works properly on phones |
| Wrapped label + input pairs in `<p>` | Fields stack on separate lines with no CSS |
| `fieldset` + `legend` for each question group | Proper grouping for screen readers |
| Radio group is now `required` | Can't skip the question |
| Dropdown starts on a blank option and is `required` | No hidden "Excellent" bias |
| Added `autocomplete` tokens | Autofill for name and email |
| Marked optional fields in the label text | Required-ness is clear to everyone |
| Explicit `type="submit"` and a descriptive label | No sneaky defaults, no vague "Submit" |
| Wrapped everything in `<main>` | Landmark for screen readers |
| Consistent formatting | Readable, diff-friendly code |

---

## 🛡️ Security Reality Check

Forms are the front door of a website. A few things to burn into my brain now, even though my practice pages don't have a backend:

| Rule | Why |
|---|---|
| **Never trust client-side validation alone** | Anyone can edit HTML in DevTools, remove `required`, or send requests without a browser. Validate again on the server. |
| **Use `POST` for anything sensitive or state-changing** | `GET` data lands in browser history, server logs, and shared links |
| **Only collect passwords/payments over HTTPS** | Plain HTTP can be read in transit |
| **Don't put secrets in `hidden` fields** | "Hidden" only means not visible. View Source shows it. |
| **Escape/sanitize output on the server** | Prevents cross-site scripting (XSS) from submitted text |
| **Don't use `autocomplete="off"` to "protect" passwords** | Browsers ignore it, and password managers help security |
| **Ask for the minimum data you need** | Less data collected means less to leak |

> 🔐 Future me: when I reach Python/backend, come back to this table and make sure every one of these is handled.

---

## 💥 Mistakes I Actually Made

From reviewing my Hotel Feedback Form and others:

| # | Mistake | Why it's a problem | The fix |
|---|---|---|---|
| 1 | Dropdowns pre-selected on "Excellent" | Skews the data toward the top rating | Blank `<option value="">` + `required` |
| 2 | Radio group not `required` | Users can silently skip it | `required` on the group |
| 3 | No `autocomplete` on name/email | Users retype everything | Add the right tokens |
| 4 | No viewport meta tag | Form is tiny on phones | Add it to my template |
| 5 | Label/input pairs had no layout wrappers | Everything ran together on one line | Wrap each pair in `<p>` or `<div>` |
| 6 | Mixed formatting (some inputs on one line, others split) | Hard to read and maintain | Format on save (Prettier) |
| 7 | Used `size="20"` for width | Presentational attribute | Use CSS `width` |
| 8 | Relied on `id` thinking it gets submitted | Only `name` is sent | Always set `name` |
| 9 | Vague button text ("Submit") | Not descriptive | "Send feedback" |
| 10 | Pointed `action` at someone else's URL | The data went to a placeholder, not to me | Use my own endpoint, or a form service when I have one |

> 🧪 Mistakes are just the damage report that builds Mark IV.

---

## 🧾 Cheat Sheet

### Which control do I use?

| I need... | Use |
|---|---|
| Short text | `<input type="text">` |
| Email | `<input type="email">` |
| Password | `<input type="password">` |
| Phone number | `<input type="tel">` |
| A quantity | `<input type="number" min max>` |
| A date | `<input type="date">` |
| Choose exactly one (2-5 options) | Radio buttons in a `fieldset` |
| Choose exactly one (many options) | `<select>` |
| Choose any number | Checkboxes in a `fieldset` |
| Long text | `<textarea>` |
| Typing with suggestions | `<input list>` + `<datalist>` |
| Upload a file | `<input type="file" accept>` |
| Slider | `<input type="range">` |
| Send the form | `<button type="submit">` |

### Pre-flight checklist ✅

- [ ] Form has `action` and `method` (and `enctype` if uploading files)
- [ ] Every control has a `name`
- [ ] Every control has a visible, connected `<label>`
- [ ] Placeholders are hints, not labels
- [ ] Right `type` for every input
- [ ] `required`, `min`, `max`, `pattern` where they make sense
- [ ] Radio and checkbox groups use `fieldset` + `legend`
- [ ] No misleading default selections
- [ ] `autocomplete` set on personal-data fields
- [ ] Every `<button>` has an explicit `type`
- [ ] Button text describes the result
- [ ] Optional vs required is clear in text, not just color
- [ ] I can complete the whole form with the keyboard only
- [ ] Viewport meta tag is present
- [ ] Remembered: the server must validate again

---

## 🎮 Practice Ideas

1. 🌱 **Login form.** Email, password, "remember me," a submit button. Use the correct `autocomplete` tokens.
2. 🌱 **Sign-up form.** Add `minlength` on the password and a confirm-terms checkbox.
3. 🔧 **Contact form.** `name`, `email`, `select` for subject, `textarea` for the message.
4. 🔧 **Break the validation.** Open DevTools, delete `required` from a field, submit, and see what happens. (That's why servers must validate too.)
5. 🔧 **See the data.** Use `method="get"` and watch the URL change after submitting. Then switch to `post` and look at the Network tab.
6. 🔧 **Pattern practice.** Build a ZIP code, a username (letters/numbers only), and a phone number field with `pattern` and helpful `title`s.
7. 🚀 **Accessibility run.** Complete one of my forms using only the keyboard, then with a screen reader on.
8. 🚀 **Style the states.** Once I reach CSS, style `:focus-visible`, `:user-invalid`, and `:disabled`.
9. 🚀 **Multi-step form.** Split a long form into sections with `fieldset`s, then later add JS to show one at a time.

---

## 🛠️ Tools

| Tool | What it's for |
|---|---|
| 🔍 **DevTools → Network tab** | See exactly what a form sends (method, URL, payload) |
| 🔍 **DevTools → Elements** | Edit the form live and test the validation |
| ✅ [W3C Validator](https://validator.w3.org/) | Catch bad nesting and attribute mistakes |
| ♿ **Lighthouse / axe / WAVE** | Spot missing labels and contrast issues |
| 📖 [MDN: HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn/Forms) | Thorough walkthrough of everything above |
| 📖 [MDN: `<input>` reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) | Every type and attribute |
| 🧪 [Formspree](https://formspree.io/) / [Netlify Forms](https://docs.netlify.com/forms/setup/) | Backend-free ways to receive form submissions when I'm ready |
| 🎓 [freeCodeCamp](https://www.freecodecamp.org/) | Where the Hotel Feedback Form workshop came from |

---

## 🔗 Related

- 📄 [`basics.md`](./basics.md): tags, attributes, nesting
- 🏛️ [`semantic-html.md`](./semantic-html.md): `fieldset`, `label`, `button` and why the right element matters
- ♿ [`accessibility.md`](./accessibility.md): the bigger accessibility picture
- 🖼️ [`media-and-links.md`](./media-and-links.md): images, audio, video, and paths
- 🧪 [`examples/`](./examples): the Hotel Feedback Form workshop lives here
- ⚡ [`../JavaScript`](../JavaScript): where custom validation and form handling will live
- 🐍 [`../Python`](../Python): where the server-side half will live
- 💥 [`../notes/things-i-broke.md`](../notes/things-i-broke.md): the full list of disasters

---

<p align="center"><i>A suit that can't listen to its pilot is just a statue. Forms make it respond. 🦾</i></p>
