import smtplib
from unittest import result
import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
import webbrowser
import random  
import os
engine=pyttsx3.init('sapi5') #API for microsoft speech
voices=engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voices[0].id)


def audio(sound): #generate computer audio
    engine.say(sound)
    print(sound)
    engine.runAndWait()


def listeningCommands(): #listens to users and shows what is told in text
    recognizer=speech.Recognizer()
    with speech.Microphone() as source:
        print("Boss is listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    
    try:
        print("User Speech Recognition....")
        query=recognizer.recognize_google(audio,language='en-in')
        print(f"{query}")
    except Exception as exc:
        #print(exc)
        #audio("Can you repeat please?")
        print("Can you repeat please?")
        return "None" 
    return query

def greetings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        audio("Good Morning sir!")
    elif hour>=12 and hour<17:
        audio("Good Afternoon sir!")
    else:
        audio("Good Evening sir!")
    audio("This is the boss here. How may i help you, sir?")

def sendEmail(address,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username','password')
    server.sendmail('username')
    server.close()
if __name__=="__main__":
    greetings()
    while True:
        query=listeningCommands().lower()
        #executing tasks
        if 'wikipedia' in query:
            audio("Boss is searching from wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            audio("According to wikipedia")
            audio(results)
        elif 'open youtube' in query:
            audio("Opening Youtube!")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            audio("Opening google")
            webbrowser.open("google.com")
        elif 'search in google' in query:
            audio("Searching in google..")
            query=query.replace("search in google","")
            webbrowser.open(f"{query}")
        elif 'open stackoverflow' in query:
            audio("Opening stack overflow")
            webbrowser.open("stackoverflow.com")
        elif 'in stackoverflow' in query:
            query=query.replace("in stackoverflow","")
            audio(f"{query} opening in stack overflow..")
            webbrowser.open(f"stackoverflow.com/{query}")
        elif 'facebook' in query:
            audio("Opening facebook")
            webbrowser.open("facebook.com") 
        elif 'play a music' in query:
            music_directory='E:\\music mobile'
            songList=os.listdir(music_directory)
            randomNumber=random.randint(0,len(songList)-1)
            os.startfile(os.path.join(music_directory,songList[randomNumber]))  #starts playing a random music from the directory
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H: %M: %S")
            audio(f"It is {time} now")
        elif 'open android studio' in query:
            path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)
        elif 'send an email' in query:
            try:
                audio("what should I mail them?")
                message=listeningCommands()
                print(message)
                emailAdress='toemailaddress'
                sendEmail(emailAdress,message)
                audio("The email has been sent!")
            except Exception  as e:
                audio("Sorry, Email couldn't be sent!")
