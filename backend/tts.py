import pyttsx3

engine = pyttsx3.init()

# Optional voice tuning
engine.setProperty('rate', 130)     # speed
engine.setProperty('volume', 1.0)   # volume

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hi, I am Yui, your personal AI assistant.")

