import pyttsx3
import speech_recognition as sr

def get():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        print("Done!")

    try:
        text = recognizer.recognize_google(audio) # type: ignore
        print("You said:", text)
    except Exception as e:
        print("Sorry, I couldn't understand. Error:", e)

get()
