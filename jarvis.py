import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess, sys
from pygame import mixer  # Load the popular external library
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()
engine.setProperty('rate',125)

def song():

    mixer.init()
    mixer.music.load('/home/anamikeya/music',music[0])
    mixer.music.play()

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
        r.pause_threshold=2
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
def screenshot():
    img= pyautogui.screenshot()
    speak("tell the name of the image")
    x=take()
    
    img.save('/home/anamikeya/Pictures/'+x+'.jpg')
def cpu():
    usage=str(psutil.cpu_percent())
    speak('spu is at'+usage)
    battery= psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
def joke():

    speak(pyjokes.get_joke())





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
        elif "go ofline" in query:
             speak("bye sir")
             os._exit(1)
        elif "who is my brother" in query:
            speak("veer")  
        elif "add" in query:
            speak("enter two numbers with your keyboard")
            x=int(input("enter dirst number\n"))
            y=int(input("ennter second number\n"))
            z=x+y
            speak(z)
        elif "play song" in query:
            
            song()
        elif "remember that" in query:
            speak("what should i remember")
            data=take()
            speak("you told me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you told me to remember that"+remember.read())
        elif "go offline" in query:
            speak("bye sir")
            os._exit(1)
        elif 'screenshot' in query:
            screenshot()
            speak("done!")
        elif 'system info' in query:
            cpu()
        elif "joke" in query:
            joke()
        elif "who created you" in query:
            speak("anurag pandey")
        elif ""