import smtplib
import speech_recognition as sp
import pyttsx3
from email.message import EmailMessage
import subprocess as s
import time

email_list = {
    'bro' : "Josarun1601@gmail.com",
    'sam' : "Rameshsam1601@gmail.com"
}

# this need Pyttsx == 2.7

# please enter the 

engine=pyttsx3.init('sapi5')
# print(engine)
voices=engine.getProperty('voices')
print(len(voices))
# print(voices)
engine.setProperty('voice',voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def get_info():
    try:
        with sp.Microphone() as source :
            print(" I'm Listening ")
            listener = sp.Recognizer()
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(rev, subject , message ):
    server = smtplib.SMTP('smtp.google.com',587)
    server.starttls()
    Sender_Email = "josarun1601@gmail.com"
    send_Email_password = "Ramesh16"
    server.login(Sender_Email,send_Email_password)
    email = EmailMessage()
    email['From'] =Sender_Email
    email['To'] = rev 
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_Email_info():
    talk(" TO Whom You Want to Send Email ")
    print("TO Whom You Want to Send Email ")
    name = get_info()
    rev = email_list[name]
    print(rev)
    talk(" What is Subject to Send Email ")
    print("What is Subject to Send Email  ")
    subject= get_info()
    talk(" Tell me The Content of Email ")
    print("Tell me The Content of Email ")
    mesg = get_info()
    send_email(rev , subject , mesg )
    talk(" hey Buddy You Sent Email Succesfully ")
    talk(" Hey Buddy do Want Sent More Email ")
    send_more = get_info()
    if send_more in ["yes" , "I want" ]:
        get_Email_info()


# if __name__ == "__main__":

def set_To():
    s.call(['pip','uninstall','pyttsx3'],stdout = True)
    time.sleep(3)
    s.call(['y'],stdout = True)
    s.call(['pip','install','pyttsx3==2.7'],stdout=True)

get_Email_info()

