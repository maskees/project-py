import speech_recognition as sr
import webbrowser
import pyttsx3 

recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak("sir how may i help you")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio=recognizer.listen(source)
            try:
                text=recognizer.recognize_google(audio)
                if "Jarvis" in text.lower():
                    print("Activation keyword detected.")
                    speak("Yes, how can I help you?")
                else:
                    print(f"You said: {text}")
                if "open" in text and "YouTube" in text:
                    webbrowser.open("https://www.youtube.com")
                    speak("Opening YouTube")
                    # Set Google Chrome as the browser
                    chrome_path = webbrowser.get(using='chrome').name if 'chrome' in webbrowser._browsers else None
                    if chrome_path:
                        webbrowser.get('chrome').open("https://www.youtube.com")
                    else:
                        webbrowser.open("https://www.youtube.com")
                elif "open" in text and "Google" in text:
                    webbrowser.open("https://www.google.com")
                    speak("Opening Google")
                elif "exit" in text or "quit" in text:
                    speak("Goodbye!,i am always in your service")
                    print("Exiting...")
                    break
                else:
                    speak("I didn't understand that command.")
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
    engine.runAndWait()