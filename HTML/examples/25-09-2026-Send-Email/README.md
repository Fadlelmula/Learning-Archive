```
                      🌺
                    🌺🌺🌺
                   🌺 🕷️ 🌺
                    🌺🌺🌺
                      |
                      |
```

# Send Email Script 🩸

*"Some things bloom only once — this script just wants to send you an email."*

A small, unassuming Python script that whispers a test email into the void
via a local SMTP server. No drama. No cliffhangers. Just `sendmail()` doing
its quiet, ritual work.

---

## 🕸️ What It Does

Reaches out through `localhost`, hands a plain-text message to whatever
SMTP daemon happens to be lurking there, and reports back whether the
message made it out alive.

From: `work@fadlelmula.com`
To: `edu@fadlelmula.com`
Subject: *Test Email* (thrilling, we know)

---

## 🥀 Requirements

- Python 3 — the vessel
- An SMTP server listening on `localhost` — the medium
  (`sendmail`, `postfix`, or for local testing:
  `python -m smtpd -c DebuggingServer -n localhost:25`)

---

## 🖤 Usage

```bash
python3 send_email.py
```

If it works, you'll see:

```
Successfully sent email
```

If it doesn't, the script won't hide behind a vague shrug — it'll tell you
*exactly* what went wrong, because ambiguity is for horror movies, not
error handling.

---

## 🌺 Configuration

Change who's speaking and who's listening:

```python
sender = 'work@fadlelmula.com'
receivers = ['edu@fadlelmula.com']
```

Sending through a real, faraway SMTP server instead of the quiet local
one? You'll need to add a host, a port, and a login — think of it as
crossing into someone else's garden, you knock first:

```python
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.starttls()
smtpObj.login('username', 'password')
```

---

## 🕷️ Notes from the Undergrowth

- Fixed the two things that were quietly strangling this script:
  a mistyped `import stmplib` and a `try:` block with its colon
  wandering off on its own line.
- Errors now print with real detail (`except Exception as e`) —
  no more mysterious, unmarked graves of failed sends.
- The connection politely shows itself out with `smtpObj.quit()`
  when the job is done.

---

*Red spider lilies bloom, drop their leaves, then vanish —*
*this script is a little more reliable than that. Probably.*
