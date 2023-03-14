import pyttsx3
import os
import ctypes

def AudioBook_read(temp):
    for i in temp:
        print(i)
        tell(i)

def tell(audio):
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()

print(" Hello My Friend Ramesh Sam")
tell(" Hello My Friend Ramesh Sam")

Access = True

while Access:
    tell(" Enter The Book Name : ")
    filename = input(" Enter The Book Name : ")
    try:
        file = open( os.getcwd()+"/"+filename+".txt" , "r")
        text = file.readlines()
        file.close()
        print(" File Readed Started...")
        tell(" File Readed Started")
        Access=False

    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0," This Book Can't Imported ",'Warnings!',16)
        Access = True
        
AudioBook_read(text)

print(" Audio Book Completed ")
tell(" Audio Book Completed ")