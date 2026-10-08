# Jarvis - AI Voice Assistant🤖

Jarvis ek Python-based Virtual Voice Assistant hai jo voice commands ke zariye baatein sunta hai, OpenAI API ke sath chat karta hai, aur music play karne jaise tasks perform karta hai.

---

## 🌟 Features

- **Voice Recognition:** Aapki aawaz sunta hai aur use text me convert karta hai.
- **OpenAI Integration:** OpenAI GPT model ka use karke aapke jawabon ko generate karta hai.
- **Text-to-Speech (TTS):** Python gTTS / pyttsx3 ke zariye aawaz me jawab deta hai.
- **Custom Music Library:** Native Python script ke zariye music play karta hai.

---

## 🛠️ Requirements

Project ko chalaane ke liye ye libraries zaroori hain:

- `speechrecognition`
- `gTTS`
- `pygame`
- `openai`

---

## 🚀 How to Run locally

1. **Repository ko clone karein:**
   ```bash
   git clone [https://github.com/rupeshgupta24/Jarvis-AI.git](https://github.com/rupeshgupta24/Jarvis-AI.git)
   cd Jarvis-AI
2.̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨̨Virtual Environment banayein aur activate karein:
    python3 -m venv .venv
    source .venv/bin/activate  # Mac/Linux par
    # .venv\Scripts\activate   # Windows par

    
3. Required libraries install karein:
   pip install -r requirements.txt


4. Project start karein:
   python3 main.py

5.Environment Variables
  export OPENAI_API_KEY="your_api_key_here"
