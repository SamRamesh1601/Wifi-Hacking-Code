import face_recognition
# import picamera
import numpy as np

from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import os, random
import difflib





namess = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
import datetime

now = datetime.datetime.now()

name = 'foxtrot'


code = name + '-'


random.seed(now.year + now.day + now.hour + now.minute)

num = str(random.random())
num = num[2] #0x21c
num = int(num)

code = code + namess[num] + '-'

num = str(random.random())
num = num[3] #3x18g
num = int(num)

code = code + namess[num] + '-'

num = str(random.random())
num = num[4] #2x13f
num = int(num)

code = code + namess[num] + '-'

num = str(random.random())
num = num[5] #8x01i
num = int(num)

code = code + namess[num] + '-'

num = str(random.random())
num = num[6] #0u34f
num = int(num)

code = code + namess[num] + '-'

num = str(random.random())
num = num[7] #8r19q
num = int(num)

code = code + namess[num] + '-'


code = code + namess[int(now.month)*2] + '-' #9h61c
if now.day // 2 > 0 and now.day >= 7: #1v65v
    code = code + namess[int(now.day) - 7] + '-' #4h25b
else:
    code = code + namess(int(now.day)/2) + '-' #0k31c
if now.hour // 2 > 0: #5x81c
    code = code + namess[int(now.hour)]  + '-' #5y92c
else:
    code = code + namess(int(now.day)/2) + '-' #1j23c
if now.minute // 2 > 0: #0f14c
    if now.minute < 27:
        code = code + namess[int(now.minute)] + '-' #2x21c
    else:
        random.seed(now.hour + now.minute) 
        num = str(random.random())
        num = num[2]
        num = int(num)
        code = code + namess[num] + '-'
else:
    code = code + namess(int(now.minute)/2) + '-' #4x21c
random.seed(now.minute)

num = str(random.random())
num = num[2] #6x21c
num = int(num)

code = code + namess[num] 

print(code)

code = hash(code)

c_code = hash(input())






# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")



Aleksey_image = face_recognition.load_image_file("photo1.jpg")
Aleksey_face_encoding= face_recognition.face_encodings(Aleksey_image)[0]


    
Roman_image = face_recognition.load_image_file("photo2.jpg")
Roman_face_encoding = face_recognition.face_encodings(Roman_image)

if len(Roman_face_encoding) > 0:
    Roman_face_encoding = Roman_face_encoding[0]

# Initialize some variables
face_locations = []
face_encodings = []


names = []
i=0
seq = []
word = ''
message = ''
p=0
pics = []
txt = ''
bgst = 0
event_created = False
eventm = []
uid = ''
symb = ''
llist = ''

name = ''
fame = ''
otch = ''
phone = ''
inter = ''
email =''
points = ''
hr = ''

#Use start() to parce docs in directory (only .file files)
def start():
    global i, seq, names
    if code == c_code:
        print('[DEV] STARTING...')
        print('[DEV] FINDING FILES...')
        for root, dirs, files in os.walk("./"):  
            for filename in files:
                if '.file' in filename:
                    print('<--', filename)
                    filename = filename.replace('.file', '')
                    names.append(filename)
        print('[DEV] OK!')
        print('[DEV] SEQ.CHECK...')
        while i != len(files):
            seq.append(1)
            i+=1
        i=0
        print('[DEV] DONE!')
    else:
        for root, dirs, files in os.walk("./"):  
            for filename in files:
                if '.file' in filename:
                    filename = filename.replace('.file', '')
                    names.append(filename)
        while i != len(files):
            seq.append(1)
            i+=1
        i=0
#To compare word and filenames use comparison() with word parametr
def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))
def comparison_2(word):
    if code == c_code:
        print('Comparison2 started!')
    global i, seq, names, l, p, txt, nname, name, fam, otch,phone,email,inter, points, hr
    txt = ''
    i=0
    while i != len(names):
                if code == c_code:
                    print('Comparison stage ', i)
                diff = difflib.SequenceMatcher(None, word.lower(), names[i].lower())
                if code == c_code:
                    print('[DEV] СРАВНИВАЕТСЯ: ', word.lower(), ' и ', names[i].lower())
                p = diff.ratio()*100
                p = int(p)
                p = round(p, 2)
                seq[i] = p
                if code == c_code:
                    print(seq[i])
                i+=1
    bgst = max(seq)
    if code == c_code:
        print('Opened ', names[seq.index(bgst)], '\n\n')
    f = open(names[seq.index(bgst)] + '.file', 'r')
    nname = names[seq.index(bgst)]
    for line in f.readlines():
            if '<id:' in line:
                uid = line.replace('<id:', '')
                uid = 'ID:' + uid.replace('>', '')
            elif '<n:' in line:
                name = line.replace('<n:', '')
                name = 'Имя:' + name.replace('>', '')
            elif '<s:' in line:
                fam = line.replace('<s:', '')
                fam = 'Фамилия:' +  fam.replace('>', '')
                print(fam)
            elif '<p:' in line:
                otch = line.replace('<p:', '')
                otch ='Отчество:' +  otch.replace('>', '')
            elif '<pn:' in line:
                phone = line.replace('<pn:', '')
                phone ='Телефон:' +  phone.replace('>', '')
            elif '<email:' in line:
                email = line.replace('<email:', '')
                email ='Почта:' +  email.replace('>', '')
            elif '<in:' in line:
                inter = line.replace('<in:', '')
                inter = 'Интересы:' + inter.replace('>', '')
            elif '<points:' in line:
                points = line.replace('<points:', '')
                points ='Очки:' +  points.replace('>', '')
            elif '<hr:' in line:
                hr = line.replace('<hr:', '')
                hr = 'Характеристика:' + hr.replace('>', '')
    txt =  uid + name + fam + otch + phone + email + inter + points + hr    
    lns_c = count_lines(names[seq.index(bgst)] + '.file')
    if code == c_code:
        print(lns_c)
        print(pics)
        print(txt)
        print('\n\n')
    draw2()
    i=0
    word = ''
    p=0

def draw2():
    from tkinter import Tk
    global message,l,word,l2, txt
    root2 = Tk()
    root2.title('PFL')
    root2.geometry("800x600")

    frame2  = Frame(root2, relief=RAISED, borderwidth=1)
    frame2.pack(fill=BOTH, expand=True)

    l2 = Label(frame2, text = txt)
    l2.pack()

    txt = ''
    root2.mainloop()




start()


while True:
    if code == c_code:
        print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")
    
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    
    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([Roman_face_encoding], face_encoding)
        name = "<Unknown Person>"    
    
        if match[0]:
            name = "Roman"

        match = face_recognition.compare_faces([Aleksey_face_encoding], face_encoding)

        if match[0]:
            name = "Aleksey"
            
        print("I see someone named {}!".format(name))
   
