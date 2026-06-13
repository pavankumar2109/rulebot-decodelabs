# RuleBot v1.0 — DecodeLabs AI Project 1

> **Batch 2026 · Powered by DecodeLabs**  
> A rule-based AI chatbot built using Python dictionary lookup (O(1) engine).

---

## What This Project Demonstrates

| Concept | What it means | Where in code |
|---|---|---|
| Input Sanitization | `.lower().strip()` normalizes all input | `sanitize()` function |
| Dictionary O(1) Lookup | Instant response matching, no if-elif ladder | `RESPONSES` dict + `get_response()` |
| Infinite Loop | `while True` keeps the bot alive | `run_chatbot()` |
| Kill Command | `break` on exit keywords ends the loop | `EXIT_KEYWORDS` set |
| Fallback Response | Default reply for unknown input | `FALLBACK` variable |
| IPO Model | Input → Process → Output architecture | Full `run_chatbot()` flow |

---

## Project Structure

```
rulebot_project/
│
├── chatbot.py      ← Main chatbot (run this)
└── README.md       ← This file
```

---

## How to Run

### Step 1 — Open in VS Code
```
File → Open Folder → select the rulebot_project folder
```

### Step 2 — Open Terminal in VS Code
```
Terminal → New Terminal   (or press Ctrl + ` )
```

### Step 3 — Run the chatbot
```bash
python chatbot.py
```

### Step 4 — Try these inputs
```
hello
help
joke
fact
time
who are you
bye
```

---

## How to Push to GitHub

```bash
# Step 1 — Initialise git inside the project folder
git init

# Step 2 — Stage all files
git add .

# Step 3 — Make your first commit
git commit -m "feat: DecodeLabs AI Project 1 - Rule-Based Chatbot"

# Step 4 — Create a repo on github.com, then link it
git remote add origin https://github.com/YOUR_USERNAME/rulebot.git

# Step 5 — Push to GitHub
git push -u origin main
```

---

## Extending the Bot

To add a new rule, just add a line to `RESPONSES`:

```python
"your topic": "Your response here.",
```

That's it. No if-elif chain to update.

---

## DecodeLabs Project 1 Checklist

- [x] INPUT LOOP — Continuous `while True` cycle
- [x] SANITIZATION — Handle case & whitespace
- [x] KNOWLEDGE BASE — Dictionary with 5+ intents
- [x] FALLBACK — Default response for unknowns
- [x] EXIT STRATEGY — Clean break command
