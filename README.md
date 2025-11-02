# 🎧 Audio Translation App (Flask + OpenAI Whisper + GPT-3.5)

This is a simple **Flask web application** that takes an **audio file (speech in English)**,  
**transcribes it** using OpenAI’s **Whisper model**, and then **translates** the text into a selected language using **GPT-3.5-Turbo**.

---

## 🚀 Features

- 🎙️ Upload an audio file (MP3, WAV, etc.)
- 🧠 Transcribes speech to text using `whisper-1`
- 🌍 Translates the transcribed text to any target language using GPT-3.5
- 🧾 Displays the result neatly on a web interface
- ⚡ Built with Flask + OpenAI API

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Backend language |
| **Flask** | Web framework |
| **OpenAI API** | Whisper (speech-to-text) and GPT-3.5 (translation) |
| **HTML/CSS (Jinja2)** | Frontend UI |
| **dotenv** | For managing API keys securely |

---


---

## ⚙️ Setup Instructions

### 1 Clone the Repository
```bash
git clone https://github.com/Bavan-M/Audio-Translation-
```
### 2 Load the project
```bash
python -m venv audiotranslate
```
```bash
.\audiotranslate\Scripts\activate     
```
```bash
pip install -r requirements.txt
```


