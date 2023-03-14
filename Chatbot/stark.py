import pyttsx3
import datetime
import speech_recognition as sp

boss=input(" AI request Name     <   ")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good        Morning")
        speak(boss)
    elif hour>=12 and hour<17:
        speak("good        Afternoon")
        speak(boss)
    elif hour>=17 and hour<20:
        speak("good        Evening")
        speak(boss)
    else:
        speak("Good        Night")
        speak(boss)

def take():
    r=sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening....   ")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
          print(" Wait For Recognitioning...... ")
          query=r.recognize_google(audio,language='en-in')
          return query

    except Exception as e:
         print(e)
         speak(" It's Not Clear So Say Again Please")

 
speak(" My           name           is         Stark   A      I ")
print(" ")
print("              Stark AI is Started..... ")
wishme()
print("")
speak(" How         can         i      help        You ")
    
start=False    
while not start:
     query=take()
     if query=="how are you":
         speak(" I              am                 Fine            Thank       You ")
         print(" I am Fine Thank You ")
     elif query=="call me":
         speak(" Hey            sam")
         print(" Hey ",boss)
     elif query=="miss you":
         speak(" I              too                Miss              you")
         speak(boss)
         print(" I too Miss you ",boss)
     elif query=="love you":
         speak(" I              love               you               too        dear")
         speak(boss)
         print(" I love you too dear ",boss)
     elif query==boss:
         speak(" That                    is                 Your                      Name    Mister..")
         speak(boss)
         print(" That is Your Name mr.  ",boss)
     elif query=="stark":
         speak(" I              am                 listening.....")
         print(" I am  listening.....")
     else:
         start=True
         speak(" I              Don't               Understand ")
         print(" I Don't Understand ")


