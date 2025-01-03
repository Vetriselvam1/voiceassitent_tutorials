import speech_recognition as sr
import pyttsx3
import datetime


class VoiceAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Set voice (0 for male, 1 for female)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Female voice
        self.engine.setProperty('rate', 150)  # Speed

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text.lower()
            except:
                return "Could not understand"

    def handle_command(self, command):
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        elif "hello" in command:
            return "Hello! How can I help you?"
        elif "how are you" in command:
            return "I'm doing well, thank you for asking!"
        else:
            return "I heard you say: " + command

    def run(self):
        self.speak("Hello! I'm your voice assistant")

        while True:
            command = self.listen()

            if command == "exit":
                self.speak("Goodbye!")
                break

            response = self.handle_command(command)
            self.speak(response)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()