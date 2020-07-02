import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb



engine=pyttsx3.init()
engine.setProperty('rate',125)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
        return query
    except Exception as e:
        print(e)
        speak("say that again...")
        return "none"

    return query


def wish():
    speak("I am rabona , how can i help you")

def sendemail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nayakpearl2@gmail.com','anamika05')
    server.sendmail('nayakpearl2@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
        query=take().lower()
        if "date" in query:
            date()
        
        elif "time" in query:
            Time()
        
        elif "wikipedia" in query:
            speak("searching.....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            speak("what to send")
            content=take()
            to=input("enter the recipiant id")
            sendemail(to,content)
            speak("email sent")
        
        elif "search in chrome" in query:
            speak("what should i search")
            chromepath='/etc/alternatives/google-chrome'
            search=take().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
           

