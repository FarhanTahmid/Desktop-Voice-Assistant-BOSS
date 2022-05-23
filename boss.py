import imp
from unittest import result
import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
import webbrowser

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


if __name__=="__main__":
    greetings()
    while True:
        query=listeningCommands().lower()
        #executing tasks
        if 'wikipedia' in query:
            audio("Boss is searching from wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            audio("According to wikipedia")
            print(results)
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
        

