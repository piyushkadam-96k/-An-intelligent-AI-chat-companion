from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import sqlite3
import datetime
import re
import threading
import pyttsx3
import os

app = Flask(__name__)

# ------------------------------------
# 🔑 GEMINI API CONFIGURATION
# ------------------------------------
genai.configure(api_key="AIzaSyCg75szAUTAA-EqySG1ytFFl0moHb7OpFE")  # Replace with your Gemini API key

DB_FILE = "memory.db"
voice_enabled = True  # Global voice toggle

# ------------------------------------
# 🧠 DATABASE SETUP
# ------------------------------------
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                topic TEXT,
                date TEXT
            )
        """)
        conn.commit()

init_db()

# ------------------------------------
# 🧩 MEMORY FUNCTIONS
# ------------------------------------
def save_message(role, content):
    topic = extract_topic(content)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO chat_history (role, content, topic, date) VALUES (?, ?, ?, ?)",
                  (role, content, topic, date))
        conn.commit()

def load_recent_messages(limit=10):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT role, content FROM chat_history ORDER BY id DESC LIMIT ?", (limit,))
        rows = c.fetchall()
    rows.reverse()
    return [{"role": r, "content": c} for r, c in rows]

def extract_topic(text):
    keywords = re.findall(r'\b[A-Za-z]{4,}\b', text)
    return keywords[0].lower() if keywords else "general"

# ------------------------------------
# 🔊 OFFLINE FEMALE VOICE (SOFT + SLOW)
# ------------------------------------
def speak_text(text):
    """Speak Joe's reply using soft, calm female voice"""
    try:
        local_engine = pyttsx3.init()
        voices = local_engine.getProperty('voices')
        if len(voices) > 1:
            local_engine.setProperty(
                'voice',
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
            )
        local_engine.setProperty('rate', 160)   # slower speaking rate
        local_engine.setProperty('volume', 0.9) # gentle volume
        local_engine.say(text)
        local_engine.runAndWait()
        local_engine.stop()
    except Exception as e:
        print("⚠️ Voice generation error:", e)

# ------------------------------------
# 🌐 ROUTES
# ------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/history")
def history():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT role, content, topic, date FROM chat_history ORDER BY id DESC LIMIT 100")
        rows = c.fetchall()
    return jsonify(rows)

@app.route("/toggle_voice", methods=["POST"])
def toggle_voice():
    global voice_enabled
    voice_enabled = not voice_enabled
    return jsonify({"status": "on" if voice_enabled else "off"})

@app.route("/chat", methods=["POST"])
def chat():
    global voice_enabled
    user_msg = request.json.get("message")
    save_message("user", user_msg)
    context = load_recent_messages()

    try:
        model = genai.GenerativeModel("gemini-2.0-flash-exp")

        context_text = "\n".join([f"{m['role']}: {m['content']}" for m in context])
        prompt = (
            f"You are Joe, Amit’s intelligent, emotional, and caring female AI companion. "
            f"Speak softly and naturally.\n\n"
            f"Conversation:\n{context_text}\n\nJoe:"
        )

        response = model.generate_content(prompt)
        bot_reply = response.text.strip()

        # Speak Joe’s reply asynchronously (only if voice is ON)
        if voice_enabled:
            threading.Thread(target=speak_text, args=(bot_reply,)).start()

    except Exception as e:
        bot_reply = f"⚠️ AI error: {e}"

    save_message("assistant", bot_reply)
    return jsonify({"response": bot_reply, "voice": "on" if voice_enabled else "off"})

# ------------------------------------
# 🚀 RUN SERVER
# ------------------------------------
if __name__ == "__main__":
    print("✨ Joe AI Companion running at http://127.0.0.1:5000")
    app.run(debug=True)
