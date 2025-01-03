import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech and speech recognition
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
recognizer = sr.Recognizer()
mic = sr.Microphone()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            return "Error understanding audio"


def run_assistant():
    speak("Hello! How can I help?")
    while True:
        text = listen()
        print(f"You said: {text}")

        if text == "exit":
            speak("Goodbye!")
            break
        elif "hello" in text:
            speak("Hi there!")
        elif "how are you" in text:
            speak("I'm doing well!")
        else:
            speak("You said: " + text)


# Start assistant
run_assistant()