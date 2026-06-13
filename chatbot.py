# ============================================================
#  DecodeLabs · Batch 2026 · Artificial Intelligence
#  Project 1  : Rule-Based AI Chatbot
#  File       : chatbot.py
#  Author     : <your name>
#  Date       : 2026
# ============================================================
#
#  ARCHITECTURE  →  IPO Model (from the DecodeLabs PPT)
#  ┌─────────┐     ┌──────────────────────┐     ┌──────────┐
#  │  INPUT  │────▶│  PROCESS             │────▶│  OUTPUT  │
#  │ Raw text│     │  Sanitize + Match    │     │ Response │
#  └─────────┘     └──────────────────────┘     └──────────┘
#
#  ENGINE  →  Dictionary O(1) Lookup   (NOT if-elif ladder)
#  WHY?    →  if-elif = O(n), slows down with more rules
#             dict.get() = O(1), instant regardless of size
# ============================================================


# ── KNOWLEDGE BASE ───────────────────────────────────────────
# This is the "brain" of the chatbot.
# It's a Python dictionary → key = intent, value = response.
#
# WHY a dictionary and not if-elif?
#   if   clean_input == "hello": ...   ← checks every condition
#   elif clean_input == "hi":    ...      one by one = O(n)
#   elif clean_input == "hey":   ...
#   ...100 more rules = very slow
#
#   vs.
#
#   responses.get("hello")  ← jumps directly = O(1), always fast

RESPONSES = {

    # ── Greetings ──────────────────────────────────────────
    "hello"        : "Hey there! 👋 I'm RuleBot. How can I help you today?",
    "hi"           : "Hi! 😊 Type 'help' to see what I can do.",
    "hey"          : "Hey! What's on your mind?",
    "howdy"        : "Howdy! 🤠 What can I do for you?",
    "good morning" : "Good morning! ☀️ Hope you have a great day.",
    "good night"   : "Good night! 🌙 Rest well.",

    # ── Identity ───────────────────────────────────────────
    "who are you"  : "I'm RuleBot 🤖 — a rule-based chatbot built using a Python dictionary. No ML, no magic. Just clean rules!",
    "your name"    : "My name is RuleBot v1.0. Nice to meet you!",
    "who made you" : "I was built as DecodeLabs AI Project 1 — Batch 2026!",

    # ── Help ───────────────────────────────────────────────
    "help"         : (
        "\n📋 Here's what I understand:\n"
        "  👋  hello / hi / hey / howdy\n"
        "  🤔  who are you / your name\n"
        "  😄  joke\n"
        "  💡  fact\n"
        "  ⏰  time\n"
        "  📅  date\n"
        "  🌤  weather\n"
        "  🙏  thanks / thank you\n"
        "  🚪  bye / quit / exit  (ends the chat)\n"
    ),

    # ── Jokes ──────────────────────────────────────────────
    "joke"         : "Why do programmers prefer dark mode? 🌑 Because light attracts bugs!",

    # ── Fun facts ──────────────────────────────────────────
    "fact"         : "💡 The first computer bug was a real moth found inside Harvard's Mark II in 1947!",

    # ── Weather ────────────────────────────────────────────
    "weather"      : "I can't fetch live data 🌤, but check weather.com for forecasts!",

    # ── Gratitude ──────────────────────────────────────────
    "thanks"       : "You're welcome! 😊",
    "thank you"    : "Anytime! 🙌",

    # ── Small talk ─────────────────────────────────────────
    "how are you"  : "I'm just code — but all systems are running! 💻 How about you?",
    "what is ai"   : (
        "AI = making machines behave intelligently.\n"
        "I'm the simplest form: a rule-based system where\n"
        "every response is hard-coded. No learning involved!"
    ),
}

# ── EXIT KEYWORDS ────────────────────────────────────────────
# Stored in a Python set for O(1) lookup.
# WHY a set and not a list?
#   "bye" in ["bye","quit","exit"]  → checks one by one = O(n)
#   "bye" in {"bye","quit","exit"}  → hash lookup = O(1)

EXIT_KEYWORDS = {"bye", "goodbye", "quit", "exit", "cya", "see you"}

# ── FALLBACK ─────────────────────────────────────────────────
# Shown when no rule matches. Always have a fallback!
FALLBACK = "🤔 I don't understand that yet. Type 'help' to see what I know."


# ════════════════════════════════════════════════════════════
#  PHASE 1 — INPUT SANITIZATION
#  (from the DecodeLabs PPT: "Sanitization & Normalization")
#
#  Problem: "Hello", "HELLO", " hello " are the same word
#           but Python sees them as 3 different strings.
#  Fix   : .lower()  → converts to lowercase
#           .strip() → removes leading/trailing spaces
#
#  raw  = input('You: ')          → "  HELLO  "
#  clean = raw.lower().strip()    → "hello"
# ════════════════════════════════════════════════════════════

def sanitize(raw_input):
    """
    Normalize user input.
    Step 1: .lower()  → "HELLO" becomes "hello"
    Step 2: .strip()  → "  hello  " becomes "hello"
    """
    clean_input = raw_input.lower().strip()
    return clean_input


# ════════════════════════════════════════════════════════════
#  PHASE 2 — PROCESS: INTENT MATCHING
#  (from the DecodeLabs PPT: "Intent Matching & State")
#
#  The .get() method is the key technique here.
#  RESPONSES.get(key, default)
#    → if key exists  : returns the response
#    → if key missing : returns the fallback (default)
#  This is ONE atomic operation — lookup + fallback together.
# ════════════════════════════════════════════════════════════

def get_response(clean_input):
    """
    Match user input to a response using dictionary lookup.

    Strategy:
    1. Try exact match         → O(1), fastest
    2. Try partial keyword scan → handles "tell me a joke"
    3. Return fallback          → unknown input
    """

    # Step 1 — Exact match (O(1) dictionary lookup)
    if clean_input in RESPONSES:
        return RESPONSES[clean_input]

    # Step 2 — Partial match
    # Handles phrases like "tell me a joke" or "give me a fact"
    # Scans each key to see if it's contained in the input
    for keyword in RESPONSES:
        if keyword in clean_input:
            return RESPONSES[keyword]

    # Step 3 — Fallback (no rule matched)
    return FALLBACK


# ════════════════════════════════════════════════════════════
#  PHASE 3 — THE INFINITE LOOP (The Heartbeat)
#  (from the DecodeLabs PPT: "The Heartbeat: The Infinite Loop")
#
#  while True:               ← runs forever
#      get input             ← Phase 1
#      if exit command → break  ← Kill Command
#      process input         ← Phase 2
#      print response        ← Phase 3 (Output)
#
#  The loop only stops when the user types an EXIT keyword.
#  This is called a "Kill Command" — a controlled break.
# ════════════════════════════════════════════════════════════

def run_chatbot():
    """
    Main chatbot loop.
    Implements the IPO model: Input → Process → Output
    Runs continuously until an exit command is received.
    """

    # Welcome banner
    print("=" * 52)
    print("  RuleBot v1.0  |  DecodeLabs AI Project 1  ")
    print("  Engine: Dictionary O(1)  |  Batch 2026    ")
    print("=" * 52)
    print("  Bot: Hello! I'm RuleBot. Type 'help' to start.")
    print("       Type 'bye' or 'quit' to exit.\n")

    # ── THE HEARTBEAT: while True loop ───────────────────
    while True:

        # ── PHASE 1: INPUT & SANITIZATION ────────────────
        raw_input   = input("  You : ")           # get raw text
        clean_input = sanitize(raw_input)          # normalize it

        # Skip empty input (user just hit Enter)
        if not clean_input:
            continue

        # ── EXIT STRATEGY: Kill Command ───────────────────
        # Check if the sanitized input is an exit keyword.
        # We use a SET for O(1) membership check.
        if clean_input in EXIT_KEYWORDS:
            print("  Bot : Goodbye! 👋 See you next time!\n")
            break  # ← exits the while True loop cleanly

        # ── PHASE 2: PROCESS (Intent Matching) ───────────
        response = get_response(clean_input)

        # ── PHASE 3: OUTPUT (Response Generation) ────────
        print(f"  Bot : {response}\n")


# ── ENTRY POINT ───────────────────────────────────────────────
# This block only runs when you execute THIS file directly.
# It does NOT run if another file imports this one.
# Best practice: always protect your main code with this guard.

if __name__ == "__main__":
    run_chatbot()
