import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import threading

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Neon. How can I help you?")

# Function to take voice input
def takecommand():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for audio input with a timeout of 5 seconds
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-IN")
            print(f"You said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Timeout occurred. Restarting listening...")
            return "none"
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please say it again.")
            return "none"

# Function to search Google


# Main function
if __name__ == "__main__":
    wishme()
    while True:
        try:
            query = takecommand().lower()
            if query == "none":
                continue
            elif 'wikipedia' in query or 'information about' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")
            elif 'open google' in query:
                def google_search(query):
                 speak("Searching Google...")
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                threading.Thread(target=google_search, args=(query,)).start()
            
            elif 'open stackoverflow' in query:
                webbrowser.open("https://www.stackoverflow.com")
            elif 'open github' in query:
                webbrowser.open("https://www.github.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\aryas\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'thanks' in query:
                speak("You're welcome")
                break
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't process your request. Please try again.")
