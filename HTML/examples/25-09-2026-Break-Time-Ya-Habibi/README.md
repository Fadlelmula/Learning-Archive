# Break Time, Ya Habibi 🕌☕

A tiny Python script with one job: **make you stop and rest**, whether you like it or not.

## What it does

Every **2 hours**, it forces open a YouTube video in your browser as your reminder to step away from the screen. It does this **10 times**, so you get roughly 18-20 hours of guaranteed breaks before it clocks out.

yes because i'm crazy workaholic

No notifications to dismiss. No "remind me later" button. Just a tab that pops open and says: *yalla, break time.*

## How it works

```
start_time = time.ctime()   # logs when you started
target = 10                 # how many times it'll nag you
while start <= target:
    webbrowser.open(...)    # opens the video
    time.sleep(2*60*60)     # waits 2 hours
    start += 1
```

Simple `while` loop, simple math, zero dependencies outside the standard library.

## How to run it

```bash
python3 "25-09-2026-Break-Time-Ya-Habibi.py"
```

Then just... leave it running in the background. Go do your thing. It'll interrupt you when it's time.

## Good to know

- The **first** break happens immediately when you launch it — so kick it off right when you sit down to work.
- It opens a **new tab** each time, so after a full run you'll have a small graveyard of 10 tabs to close.
- After the last break, it idles for 2 more hours before the script actually exits (it's not doing anything, just being lazy on its way out).
- Want to stop it early? `Ctrl + C` in the terminal.

## Why

Because habibi, you weren't going to take breaks on your own. Now the computer makes you.
