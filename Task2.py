import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a command and return the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def execute_command(command):
    """Perform tasks based on the command."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I am not sure how to help with that.")
    return True

def main():
    """Main function to run the voice assistant."""
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = listen()
        if not command:
            continue
        if not execute_command(command):
            break

if _name_ == "_main_":
    main()
