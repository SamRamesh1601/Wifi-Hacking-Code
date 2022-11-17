import math
LENGTH = 26
KEY = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def plain():
    start =True
    plain =str(input("Plaintext  is :    "))
    while start:
        if(plain.isalpha()):
            break
        else:
            print(" Please Enter the String....")
            plain =str(input("Plaintext  is :    "))
            start=True
    return plain.lower()

def position(temp):
    a=[]
    for j in range(len(temp)):
        for i in range(LENGTH):
            if(temp[j] == KEY[i]):
                a.append(i)
    return a

mod =0

def encryption(temp,temp1):
    c,ci=[],[]
    for i in range(len(temp)):
        n =( int(temp[i]) + temp1)
        form = n % LENGTH
        mod = math.ceil(form)
        c.append(mod)
    for j in range(len(c)):
        for i in range(len(KEY)):
            if( c[j] == i):
                ci.append(KEY[i])
    return ci

def decryption(temp,temp1):
    c,ci=[],[]
    for i in range(len(temp)):
        n =( int(temp[i]) - temp1)
        form = n % LENGTH
        mod = math.ceil(form)
        c.append(mod)
    for j in range(len(c)):
        for i in range(len(KEY)):
            if( c[j] == i):
                ci.append(KEY[i])
    return ci

def listd(s):
    str1 = ""
    for x in s:
        str1 += x
    return str1


def position1(temp):
    a=[]
    for j in range(len(temp)):
        for i in range(LENGTH):
            if(temp[j] == KEY[i]):
                a.append(i)
    return a


print("")
k = int(input("Secrect Key :   "))
print("")
plain= plain()
position = position(plain)
print("")
print(f"plain text crpted values is  {position}")
cipher=encryption(position,k)
ciphertext =str(listd(cipher))
print("")
p=position1(ciphertext)
print(f"Cipher text is  {ciphertext.upper()}")
print("")
print(f"Cipher text crpted values is  {p}")
text=decryption(p,k)
print("")
text=listd(text)
print(f"Finaly.... Plain text is {text.upper()}")
print("")
