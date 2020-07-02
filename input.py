import pyttsx3
import speech_recognition as sr


engine=pyttsx3.init()
voices=engine.getProperty('voices')

def speak(audio):
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[13].id)
                                     
    engine.say(audio)
    engine.runAndWait()  

def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("recognizing....")
        query=r.recognize_google(audio , language='en-in')
        print(query)
        speak(query)
        
    except Exception as e:
        print(e)
        speak("say that again.....")
        return "None"
    return query

take()
