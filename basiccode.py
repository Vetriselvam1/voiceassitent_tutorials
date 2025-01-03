import speech_recognition as sr
import pyttsx3
import openai

# Initialize components
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Set OpenAI key
openai.api_key = "your_api_key"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "Error understanding audio"


def get_gpt_response(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content


def run_assistant():
    speak("Hello! How can I help?")
    while True:
        user_input = listen()
        print(f"You said: {user_input}")

        if user_input.lower() == "exit":
            speak("Goodbye!")
            break

        response = get_gpt_response(user_input)
        speak(response)


# Start assistant
run_assistant()