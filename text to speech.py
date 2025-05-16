import pyttsx3

engine = pyttsx3.init()
user_input = input("Please enter a text so we can read it: ")

# Check if the input is only digits
if user_input.strip().isdigit():
    engine.say("You did not enter a proper sentence or string.")
else:
    engine.say(user_input) 

engine.runAndWait()
