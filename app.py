from flask import Flask, request, jsonify
import random, html

app = Flask(__name__)

COMPLIMENTS = [
    "You look amazing today 🎀",
    "You have the kindest heart 🎀",
    "Your laugh is contagious 🎀",
    "You make everything better 🌸",
    "You’re effortlessly charming 🎀",
    "You light up every room 🎀",
    "Talking to you makes my day 🎀",
    "Your smile is pure sunshine 🎀",
    "You have great taste 🎀",
    "You’re wonderfully thoughtful 💐",
]

def pick_compliment(name: str | None) -> str:
    text = random.choice(COMPLIMENTS)
    if name:
        safe = html.escape(name.strip())
        # “Name, you look amazing today…”
        # Lowercase first letter of compliment if needed for flow
        c = text[0].lower() + text[1:] if text and text[0].isupper() else text
        return f"{safe}, {c}"
    return text

@app.get("/")
def home():
    # personalize with ?n=Name or ?name=Name
    name = request.args.get("n") or request.args.get("name")
    compliment = pick_compliment(name)
    # simple, pretty HTML so the link feels nice to open
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🎀 A Little Compliment</title>
<style>
  html,body{{height:100%;margin:0;font-family:-apple-system,system-ui,Segoe UI,Roboto,Inter,sans-serif;}}
  body{{display:flex;align-items:center;justify-content:center;background:#fff8f0;}}
  .card{{padding:2.5rem 2rem;border-radius:18px;box-shadow:0 10px 30px rgba(0,0,0,.08);background:white;max-width:680px;text-align:center}}
  .big{{font-size:2rem;line-height:1.3}}
  .hint{{margin-top:1rem;color:#666}}
  a{{color:inherit}}
</style>
</head>
<body>
  <div class="card">
    <div class="big">{compliment}</div>
    <div class="hint">Refresh ↻ for another one</div>
  </div>
</body></html>"""

@app.get("/api")
def api():
    name = request.args.get("n") or request.args.get("name")
    return jsonify({"compliment": pick_compliment(name)})

if __name__ == "__main__":
    # Local dev
    app.run(host="0.0.0.0", port=5001, debug=True)
