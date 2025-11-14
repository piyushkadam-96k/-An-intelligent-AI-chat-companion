<h1 align="center">✨ Joe — Your AI Companion 🤖</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-WebApp-orange?logo=flask" />
  <img src="https://img.shields.io/badge/AI-Gemini%20API-8B5CF6?logo=google" />
  <img src="https://img.shields.io/badge/Voice-Pyttsx3-green?logo=windows" />
  <img src="https://img.shields.io/badge/UI-Animated%20Waveform-EC4899?logo=css3" />
</p>

<h3 align="center">💬 An intelligent AI chat companion with a soft female voice and glowing live waveform animations.</h3>

---

## 🌟 Features

- 🤖 **Gemini AI Integration** — Uses Google’s Gemini model for natural, context-aware replies  
- 🎙️ **Real Female Voice (Offline)** — Soft, calm tone via `pyttsx3`  
- 🌈 **Animated Voice Waveform** — Glowing color-shifting bars while Joe speaks  
- 🧠 **Persistent Memory** — Stores all chat history in SQLite  
- 🔇 **Voice Toggle Button** — Turn voice mode on or off anytime  
- 💻 **Modern UI** — Clean ChatGPT-style design with smooth animations  
- 📊 **Dashboard** — Easily view stored memory and chat history  

---

## 🖼️ Preview

<p align="center">
  <img src="https://github.com/piyushkadam96k/Joe_AI_Companion/blob/main/preview.png" width="700" alt="Joe AI Companion Preview">
</p>

*(Add a screenshot of your running app here — name it `preview.png` and place it in your repo root)*

---

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone this repository
git clone https://github.com/piyushkadam96k/Joe_AI_Companion.git
cd Joe_AI_Companion

# 2️⃣ (Optional) Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # on Windows
source .venv/bin/activate   # on Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Gemini API key in app.py
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

# 5️⃣ Run the app
python app.py
```

Then open: 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧩 Project Structure

```
Joe_AI_Companion/
│
├── app.py                 # Flask backend with Gemini + voice system
├── requirements.txt
│
├── templates/
│   └── index.html         # Chat interface (Joe’s UI)
│
└── static/
    └── style.css          # UI styling & glowing animations
```

---

## 🗣️ Voice Customization

Inside `app.py`, modify these lines to adjust Joe’s voice tone:

```python
local_engine.setProperty('rate', 160)   # Speed (lower = slower)
local_engine.setProperty('volume', 0.9) # Volume (0.0 - 1.0)
```

To change the accent:
```python
local_engine.setProperty(
    'voice',
    'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0'
)
```

| Accent | Token ID |
|---------|----------|
| 🇺🇸 US Female | `ZIRA_11.0` |
| 🇬🇧 UK Female | `HAZEL_11.0` |

---

## 🧠 Dashboard

Access all your past conversations here:
```
http://127.0.0.1:5000/dashboard
```

---

## 🧾 Requirements

```
flask
google-generativeai
pyttsx3
```

---

## 👨‍💻 Author

**Amit Kadam**  
💻 Python Developer | 🤖 AI Enthusiast | 🌱 Always Learning  
📧 [kadamamit462@gmail.com](mailto:kadamamit462@gmail.com)  
🌐 [GitHub: piyushkadam96k](https://github.com/piyushkadam96k)

---

<p align="center">
  <b>✨ Joe – Always listening, learning, and caring. ✨</b>
</p>
