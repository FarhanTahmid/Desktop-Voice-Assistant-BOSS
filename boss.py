import pyttsx3
import datetime
import speech_recognition as speech

engine=pyttsx3.init('sapi5') #API for microsoft speech
voices=engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voices[0].id)

def audio(sound): #generate computer audio
    engine.say(sound)
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
        audio("Can you repeat please?")
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
    listeningCommands()