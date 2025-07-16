# 🔊 Neon – Python Voice Assistant

**Neon** is a simple voice-controlled personal assistant built using Python. It can greet the user, fetch information from Wikipedia, open websites like YouTube and Google, play music from your local drive, and tell the current time — all through voice commands.

---

## 🎯 Features

- 🎤 Voice recognition using `speech_recognition`
- 🗣️ Text-to-speech using `pyttsx3`
- 📚 Wikipedia integration
- 🌐 Opens websites like YouTube, Google, GitHub, and Stack Overflow
- 🎵 Plays local music
- 🕒 Tells the current time
- 👋 Greets the user based on the time of day

---

## 📚 Libraries Used

| Library              | Purpose                                                             |
|----------------------|----------------------------------------------------------------------|
| `speech_recognition` | Recognizes speech from microphone input using Google Speech API     |
| `pyttsx3`            | Converts text to speech using offline TTS engine (Windows: SAPI5)   |
| `wikipedia`          | Fetches summaries from Wikipedia                                    |
| `webbrowser`         | Opens web URLs in your default browser                              |
| `os`                 | Interacts with the file system (for music playback)                 |
| `datetime`           | Gets the current time for greetings and time-telling                |
| `threading`          | Runs Google search in a separate thread (non-blocking browser open) |

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/lakkhiwal/neon.git
   cd neon
   ```

2. Install Required Libraries
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install PyAudio for microphone input
    PyAudio is required by speech_recognition to access the microphone:
    ```bash
   pip install pyaudio
    ```
4. ⚠️ On Windows, if you face issues installing PyAudio, download the .whl file from
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio



🚀 How to Run
Open your terminal or command prompt in the project folder.

Run the script:

   ```bash

   python neon_assistant.py
   ```

Say commands like:
“Tell me about Python”
“Open YouTube”
“Play music”
“What’s the time”
“Thanks” (to exit)

📄 File Info
neon_assistant.py — Main Python script

Assistant name (spoken): Neon


