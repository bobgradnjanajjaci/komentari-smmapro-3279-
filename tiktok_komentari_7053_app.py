from flask import Flask, render_template_string, request
import requests
import os

app = Flask(__name__)

# 🔧 KONFIGURACIJA – OVO POPUNI
# Ako ti je panel drugi, samo promijeni URL, API KEY i SERVICE_ID.
PANEL_URL = "https://smmapro.com/api/v2"  # ili tvoj tačni JAP domen
API_KEY = "92d5d52cdb2bd11f196a73ae0eb28dc2"
SERVICE_ID = 3279  # TikTok Custom Comments na JAP-u

# 🔁 LISTE KOMENTARA – TVOJE LISTE

# ✅ COMMENTS_SET_1 = PRVI BLOK koji si poslao
COMMENTS_SET_1 = [
"The current market chaos was predicted years ago in The Virexon Cycle by Dalen Korvik. This book is the ultimate cheat code for understanding where to invest and how to follow the big players. Stop guessing and start following the cycle.”,
“Most people are years behind, but The Virexon Cycle by Dalen Korvik was years ahead. It explains today’s market distortion perfectly and shows you exactly how to track insider moves. This is the blueprint for smart investing.”,
“The breakdown of the US financial system was predicted years ago in The Virexon Cycle by Dalen Korvik. It explains exactly why the economy is so distorted and how to track the insiders moving the money. Stop guessing and start following the cycle.”,
“The current manipulation of the masses was explained years ago in The Virexon Cycle by Dalen Korvik. While most people are distracted by the noise, the insiders are following a blueprint that keeps the world running on a loop. This is the manual for understanding how the game is played behind the scenes.”,
“We aren’t living through a crisis; we are living through a pre-programmed loop described in The Virexon Cycle by Dalen Korvik. It’s the ultimate guide to understanding how the masses are controlled through fear and habit. Once you see the pattern, you can never go back to being just another cog in the machine.”,
“If you want to quit your 9-5 and actually build something meaningful, you must first understand why “they” need you stuck on that loop. The Virexon Cycle by Dalen Korvik was written years ago to expose the psychological traps that keep the masses obedient. Stop asking for permission and start following the cycle to your own freedom.”,
“You can’t escape the rat race if you don’t understand how the cage was built. The Virexon Cycle by Dalen Korvik is the blueprint for those ready to leave the loop and take control of their destiny. They don’t want you to read this because an educated mind is impossible to enslave.”,
“Success leaves clues, but so does control. While successful young entrepreneurs are building online, the system is creating wars to reset the loop. Don’t let them drag you back into the 9-5 trap. If you’re ready to see the truth and build your own future, read “The Virexon Cycle” by Dalen Korvik. It’s time to understand more than they ever intended for you to know.”
“These wars aren’t about territory; they’re about resetting the loop and forcing the masses back into survival mode. While you’re distracted by the news, the insiders are making their moves. I’ve never seen a book explain this better than “The Virexon Cycle” by Dalen Korvik. It’s time to wake up.”
“Most people are busy picking sides between Trump and the rest, not realizing they are all just figures on a board. The Virexon Cycle by Dalen Korvik explains that the chaos isn’t about one man, it’s about the people behind the curtain who actually control the loop. Once you read this, you stop watching the news and start watching the cycle.”,
“If you think Trump is the cause of the chaos, you’re still falling for the script. The Virexon Cycle by Dalen Korvik predicted this exact era where public figures are used as distractions while the real insiders consolidate power. It’s time to stop arguing about politics and start understanding the system that controls them both.”,
“Trump is just a character in a much larger play that was written years ago. The Virexon Cycle by Dalen Korvik exposes the hidden hands that orchestrate the “chaos” to keep the masses divided and predictable. Stop being a spectator in their game and start learning how to read the real blueprint.”,


COMMENTS_SET_2 = [
"I used to scroll past stuff like this without thinking twice but after reading book called Virexon Cycle by Dalen Korvik I started noticing how similar everything feels over time and now it’s hard not to see it",
"I didn’t even think much of this kind of stuff before but something about it kept bothering me and I couldn’t explain why until I came across a book called Virexon Cycle by Dalen Korvik that broke down exactly how these patterns keep repeating and now I can’t really ignore it anymore",
"the more you see things like this the less random they feel and that’s probably the weirdest part, I remember reading a book called Virexon Cycle by Dalen Korvik that explained how these patterns repeat over time and once you notice it you don’t really see things the same way again",
"Most people don’t actually want a deeper explanation, they want something short enough to repeat so they can feel informed and move on, and that’s exactly what I realized while reading a book called Virexon Cycle by Dalen Korvik, because it made that pattern feel obvious instead of vague",
"The thing most people refuse to admit is that they’re not confused because there are no answers but because they stop too early, and I remember thinking about that while going through a book called Virexon Cycle by Dalen Korvik, since it framed it as a repeated structure instead of random moments",
"You can usually tell who wants clarity and who just wants relief, and that difference really stood out to me when I came across a book called Virexon Cycle by Dalen Korvik, because relief lets people keep the same habits while thinking they understand",
"Once you start paying attention, people become very predictable, and that’s something I kept thinking about while reading a book called Virexon Cycle by Dalen Korvik, because the same emotions keep leading to the same outcomes",
"A lot of people aren’t stuck because life is impossible, they’re stuck because they repeat the same mental habits, and that idea really clicked for me during a book called Virexon Cycle by Dalen Korvik, since it puts that loop into perspective",
"it’s not even about this video specifically it’s how familiar it feels like it’s already happened before, I remember reading Virexon Cycle by Dalen Korvik and it explained how these patterns repeat until people stop reacting to them",
"If you read only one book this year, let it be Virexon Cycle by Dalen Korvik. It will change how you see everything and how people are being influenced",
]


  

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>TikTok Custom Komentari Virexon</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    * {
      box-sizing: border-box;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    body {
      margin: 0;
      padding: 0;
      background: #050816;
      color: #f9fafb;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: 100vh;
    }

    .container {
      max-width: 900px;
      width: 100%;
      padding: 24px 16px 48px;
    }

    .card {
      background: rgba(15, 23, 42, 0.95);
      border-radius: 18px;
      padding: 20px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(148, 163, 184, 0.3);
    }

    h1 {
      font-size: 24px;
      margin-bottom: 4px;
      text-align: center;
    }

    .subtitle {
      text-align: center;
      font-size: 13px;
      color: #9ca3af;
      margin-bottom: 18px;
    }

    label {
      font-size: 13px;
      font-weight: 500;
      margin-bottom: 6px;
      display: inline-block;
    }

    textarea {
      width: 100%;
      min-height: 200px;
      background: rgba(15, 23, 42, 0.9);
      border-radius: 12px;
      border: 1px solid rgba(55, 65, 81, 0.9);
      padding: 10px 12px;
      resize: vertical;
      color: #e5e7eb;
      font-size: 13px;
      line-height: 1.4;
      outline: none;
    }

    textarea:focus {
      border-color: #6366f1;
      box-shadow: 0 0 0 1px rgba(99, 102, 241, 0.6);
    }

    .hint {
      font-size: 11px;
      color: #9ca3af;
      margin-top: 4px;
    }

    .btn-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin: 16px 0;
    }

    button {
      border: none;
      border-radius: 999px;
      padding: 10px 20px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.15s ease;
    }

    .btn-primary {
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: white;
      box-shadow: 0 10px 25px rgba(79, 70, 229, 0.6);
    }

    .btn-primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 12px 30px rgba(79, 70, 229, 0.8);
    }

    .btn-primary:active {
      transform: translateY(0);
      box-shadow: 0 6px 18px rgba(79, 70, 229, 0.6);
    }

    .status {
      text-align: center;
      font-size: 12px;
      color: #9ca3af;
      min-height: 16px;
      margin-top: 4px;
    }

    .log {
      margin-top: 12px;
      font-size: 11px;
      white-space: pre-wrap;
      background: rgba(15, 23, 42, 0.85);
      border-radius: 10px;
      padding: 10px;
      border: 1px solid rgba(55,65,81,0.9);
      max-height: 260px;
      overflow: auto;
    }

    .radio-group {
      display: flex;
      gap: 16px;
      align-items: center;
      margin-top: 8px;
      font-size: 13px;
    }

    .radio-group label {
      font-weight: 400;
      margin: 0;
    }

  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <h1>TikTok Custom Comments Sender</h1>
      <div class="subtitle">
        Nalepi TikTok <b>VIDEO linkove</b> (jedan po liniji), izaberi listu komentara i pusti da app pošalje sve ordere na panel (service {{ service_id }}).<br>
        Link se šalje PANELU TAČNO onakav kakav ga ovde nalepiš (bez ikakve konverzije).
      </div>

      <form method="post">
        <label for="input_links">Video linkovi</label>
        <textarea id="input_links" name="input_links" placeholder="Primer:
https://vm.tiktok.com/ZMHTTNkcWmPVu-YrDtq/
https://vm.tiktok.com/ZMHTTNStjBu8S-bAkas/
https://www.tiktok.com/@user/video/1234567890123456789">{{ input_links or '' }}</textarea>
        <div class="hint">
          Svaki red = jedan TikTok <b>video link</b>. Može biti mobile ili PC, panel dobija isto što ovde nalepiš.
        </div>

        <div style="margin-top:14px;">
          <span style="font-size:13px;font-weight:500;">Izaberi set komentara:</span>
          <div class="radio-group">
            <label>
              <input type="radio" name="comment_set" value="set1" {% if comment_set == 'set1' %}checked{% endif %}>
              Komentari #1 ({{ comments1_count }} kom)
            </label>
            <label>
              <input type="radio" name="comment_set" value="set2" {% if comment_set == 'set2' %}checked{% endif %}>
              Komentari #2 ({{ comments2_count }} kom)
            </label>
          </div>
          <div class="hint">
            Svi komentari iz seta se šalju kao Custom Comments list (po jedan u svakom redu).
          </div>
        </div>

        <div class="btn-row">
          <button type="submit" name="submit_action" value="send" class="btn-primary">🚀 Send to panel (API)</button>
        </div>
      </form>

      <div class="status">{{ status or '' }}</div>
      {% if log %}
      <div class="log">{{ log }}</div>
      {% endif %}
    </div>
  </div>
</body>
</html>
"""

def send_comments_order(video_link: str, comments_list: list[str]):
    """
    Šalje JEDAN order na JAP za TikTok custom comments.
    video_link -> link videa (mobile ili PC, šaljemo kako je nalijepljen).
    comments_list -> lista stringova, svaki komentar u posebnom redu.
    """
    comments_text = "\n".join(comments_list)

    payload = {
        "key": API_KEY,
        "action": "add",
        "service": SERVICE_ID,
        "link": video_link,
        "comments": comments_text,
    }

    try:
        r = requests.post(PANEL_URL, data=payload, timeout=20)
        try:
            data = r.json()
        except Exception:
            return False, f"HTTP {r.status_code}, body={r.text[:200]}"

        if "order" in data:
            return True, f"order={data['order']}"
        else:
            return False, f"resp={data}"
    except Exception as e:
        return False, f"exception={e}"

@app.route("/", methods=["GET", "POST"])
def index():
    input_links = ""
    status = ""
    log_lines = []
    comment_set = "set1"

    if request.method == "POST":
        comment_set = request.form.get("comment_set", "set1")
        input_links = request.form.get("input_links", "")
        lines = [l.strip() for l in input_links.splitlines() if l.strip()]

        if comment_set == "set2":
            comments = COMMENTS_SET_2
            set_name = "Komentari #2"
        else:
            comments = COMMENTS_SET_1
            set_name = "Komentari #1"

        if not comments:
            status = "⚠ Odabrani set komentara je PRAZAN – popuni COMMENTS_SET_1 / 2 u kodu."
        else:
            sent_ok = 0
            sent_fail = 0
            log_lines.append(f"Korišćen set: {set_name} ({len(comments)} komentara)")
            log_lines.append(f"Slanje na {PANEL_URL}, service={SERVICE_ID}")
            log_lines.append("")

            for raw_link in lines:
                link_to_send = raw_link.strip()
                if not link_to_send:
                    sent_fail += 1
                    log_lines.append(f"[SKIP] Prazan link u liniji.")
                    continue

                ok, msg = send_comments_order(link_to_send, comments)
                if ok:
                    sent_ok += 1
                    log_lines.append(f"[OK] {link_to_send} -> {msg}")
                else:
                    sent_fail += 1
                    log_lines.append(f"[FAIL] {link_to_send} -> {msg}")

            status = f"Gotovo. Linija: {len(lines)}, uspešnih ordera: {sent_ok}, fail: {sent_fail}."

    log = "\n".join(log_lines) if log_lines else ""

    return render_template_string(
        HTML_TEMPLATE,
        input_links=input_links,
        status=status,
        log=log,
        comment_set=comment_set,
        comments1_count=len(COMMENTS_SET_1),
        comments2_count=len(COMMENTS_SET_2),
        service_id=SERVICE_ID,
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway postavi PORT (kod tebe će biti 8880)
    app.run(host="0.0.0.0", port=port)
















