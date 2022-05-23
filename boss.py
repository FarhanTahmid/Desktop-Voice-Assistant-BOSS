from importlib.util import spec_from_file_location
import pyttsx3
import datetime
engine=pyttsx3.init('sapi5') #API for microsoft speech
voices=engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voices[0].id)

def audio(sound):
    engine.say(sound)
    engine.runAndWait()
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
    print(
        "hello"
    )
    greetings()