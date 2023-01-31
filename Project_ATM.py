
# using modules
# import pywhatkit
import datetime
import random
import time
import pyttsx3
from playsound import playsound 

number = random.randint(0,10)
start = time.time()
# customer details 

# assume as databases

customer1 = {
              "username" : "abishesk",
              "pin" : 4858 ,
              "phonenumber" : 9099889983 , 
              "amount" : 5000
             }

customer2 = {
              "username" : "bala" ,
              "pin" : 8342 ,
              "phonenumber" : 9094358993 ,
              "amount" : 7000
             }

customer3 = {
              "username" : "moorthy" ,
              "pin" : 3432 ,
              "phonenumber" : 6694358993 ,
              "amount" : 15000
            }

customer4 = {
              "username" : "sam" ,
              "pin" : 5065 ,
              "phonenumber" : 95654358993 ,
              "amount" : 10000
            }

customer5 = {
              "username" : "santha" ,
              "pin" : 8112 ,
              "phonenumber" : 9123358993 ,
              "amount" : 22000
            }

customers = {
              "abishesk" : customer1 ,
              "bala" : customer2 ,
              "moorthy" : customer3 , 
              "sam" : customer4 , 
              "santha" : customer5
            }

admin =     {
            "username": "admin" ,
            "pin" : 0 ,
            "secrect_number" : number ,
            "phone_number" : 9360908285
            }

# variable declaration 

hour2=int(datetime.datetime.now().hour)

hour3=int(datetime.datetime.now().minute)

hour4=int(datetime.datetime.now().second)

atm_balance = 22000

exit = True

admin_entry = 0

false_entry = 0

confim =False

Phone = False

exit1 = False

pin_list = [customers[i].get("pin") for i in customers]

user_list = [customers[i].get("username") for i in customers]

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


# declare funtions

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getuser(temp):
  if temp:
    while True:
      temp1 = input(" Enter New Username  -->>  ")
      if ( temp1.isalpha()):
        break
      else: 
        print(" ")
        print(" please enter the valid username ")
        print(" ")
    return temp1.lower()

  else:
    while True:
      temp1 = input(" Enter the Username  -->>  ")
      if ( temp1.isalpha()):
       break
      else: 
        print(" ")
        print(" please enter the valid username ")
        print(" ")
    return temp1.lower()

def getpass(temp):
  if not temp:
    while True:
      temp1 = input(" Enter the Password -->>  ")
      if (temp1.isdigit()):
        break
      else:
       print(" ")
       print(" please enter the valid password ")
       print(" ")
    return str(temp1)

  elif temp:
      while True:
       temp1 = input(" Enter Confirm Password -->>  ")
       if (temp1.isdigit()):
          break
       else:
         print(" ")
         print(" please enter the valid password ")
         print(" ")
      return str(temp1)

  else:
      while True:
       temp1 = input(" Enter New Password -->>  ")
       if (temp1.isdigit()):
          break
       else:
         print(" ")
         print(" please enter the valid password ")
         print(" ")
      return str(temp1)

def getpoption():
  while True:
     temp = input(" Enter the option -->>  ")
     if (temp.isdigit()):
      break
     else:
      print(" ")
      print(" please enter the valid option ")
      print(" ")
  return int(temp)

def getnum(temp):
  if temp:
   while True:
     temp1 = input(" Enter Phone Number  -->>  ")
     if ((temp1.isdigit()) and len(temp1) == 10):
      break
     else:
      print(" ")
      print(" Please Enter Valid Phone Number 10 integer ")
      print(" ")
   return int(temp1)
  else:
    while True:
     temp1 = input(" Enter Configuration Number  -->>  ")
     if (temp1.isdigit()) :
      break
     else:
      print(" ")
      print(" Please Enter Valid Configuration Number  ")
      print(" ")
    return int(temp1)

def getamount():
  while True:
     temp = input(" Enter Amount  -->> $ ")
     if (temp.isdigit()):
      break
     else:
      print(" ")
      print(" Amount does not have characters or symbol ")
      print(" ")
  return int(temp)

def activer_security(temp):
  if temp >= 4:
    speak(" you continouly enter worng password ")
    speak(" atm security services activated,,,,")
    playsound("E:/alarm.mp3")
    return False
  else :
    return True

def sent(temp,temp1):
  #   pywhatkit.sendwhatmsg(str("+91")+str(admin["phone_number"]),number,temp,temp1+1)
  print(f" Message sent to Your Authentication Number in time {temp-12} Hours : {temp1+1} Minutes ")
  return True


# main methods 

if __name__ == "__main__":
    # start=time.time()
    speak(" hello interface of atm")
    while exit:
     print(" ")
     print(f" ATM balance amoount is $ {atm_balance:,}")
     print(" ")
     user = getuser(False)
     print(" ")
     password = getpass(confim)
     for i in range(len(pin_list)):
      if ((user in user_list[i]) and (password in str(pin_list[i]))) or ((user.lower() == admin["username"]) and (int(password) == admin["pin"])):
        exit1 = True
    #  print(f" {exit1 =}")
     if exit1: 
        print(" ")
        print(f" Welcome {user.title()}")
        print(" ")

# admin options ===

        if (user == admin.get("username")):
          print(" ")
          admin_entry += 1
          sent(hour2,hour3)
          print(" Admin are has privilaged allow granted ")
          print(" ")
          print(" option are availble....")
          print("      1)  Increment Money for ATM ")
          print("      2)  Atm Records ")
          print("      3)  Add User ")
          print("      4)  Exit ")
          print(" ")
          option =getpoption()

          if option == 4:
            print(" Transaction Complete...")
            speak(" Transaction Complete...")
            print(" ")
            end=time.time()
            print(f" total seconds used in atm  : {end-start} seconds")
            exit = False

          elif option == 1:
            print(f" this process needed configuration number Sent to the Admin phone Number ",number)
            num = getnum(Phone)
            if num == number : 
              atm_balance += getamount()
              print(" ")
              print(" Transaction Completed..")
              print("")
              speak(" Transaction Complete")

            else:
              print(" You enter wrong Configration Number  ")
              print(" Error occured.. ")
              speak("wrong number ")
          
          elif option == 2:
            print(f" this process needed configuration number Sent to the Admin phone Number ",number)
            num = getnum(False)
            if num == number : 
              print("")
              print("_______ATM RECORDS______")
              print(" ")
              print(f"  ATM balance amount is $ {atm_balance:,}") 
              print(" ")
              print(f"  ATM Admin Entry collection -->> {admin_entry}") 
              print(" ")
              print(f"  ATM Wrong Entry collection -->> {false_entry}") 
              print(" ")
              for i in customers: 
                print(f" Banking Customers Details {customers[i]} ")  
                print(" ") 
              print(" Transaction Completed..")
              speak(" Transaction Complete")
            else:
              print(" You enter wrong Configration Number  ")
              print(" Error occured.. ")
              speak("wrong number ")
            false_entry = 0

          elif option == 3:
            print(f" this process needed configuration number Sent to the Admin phone Number ",number)
            num = getnum(Phone)
            if num == number :  
              print(" ") 
              print(" ADD Banking customers details ") 
              print(" ") 
              while True:
                new_user = getuser(True)
                new_password = getpass(confim)
                if (new_user in user_list) or (new_user == "admin"): 
                  print(" ")
                  print(" Username is already exist try another name")
                  print("")
                else:
                  confirm_password = getpass(True)
                  
                  if new_password == confirm_password:
                    Phone = True
                    new_phonenumber = getnum(Phone)
                    new_amount = getamount()
                    break
                  
              new_customer = { "username" : new_user ,
                                "pin" : new_password ,
                                "phonenumber" : new_phonenumber ,
                                "balance" : new_amount
                             }

              customers[new_user] = new_customer 
              print(" ")
              print(" new records created successfully....")
              speak(" new records created successfully....")
              print(" ")
              print(" Transaction Completed..")
              speak(" Transaction Complete")

            else:
              print(" You enter wrong Configration Number  ")
              print(" Error occured.. ")
              speak("wrong number ")

          else:
            print(" Option is not availale ")
            print("    Wrong option using another option")
          exit1=False

# user privilages option ====

        else:
          false_entry = 0
          print(" ")
          print(f"           Hello {user.title()} ,")
          print("  ATM serivces Started..... ")
          print(" ")
          print(" option are availble....")
          print("      1)  WithDrawal ")
          print("      2)  Banking Statements ")
          print("      3)  Change Pin ")
          print("      4)  Exit ")
          print(" ")
          option =getpoption()

          if option == 1:
            print(" checking Account Balance ")
            while True:
              check_pin = getpass(True)
              if check_pin == password :
                print(" ")
                print(" WithDrawal processed.. ")
                print(" ")
                WithDrawal_amount = getamount()
                balance = customers[user].get("amount")
                user_account = customers[user]
                if WithDrawal_amount < atm_balance :
                  if WithDrawal_amount < balance :
                    balance -= WithDrawal_amount
                    atm_balance -= WithDrawal_amount
                    user_account["amount"] = int(balance)
                    print(" ")
                    print(f" collect the cash , Balance is {balance}")
                    print(" ")
                    print(" Transaction Completed..")
                    speak(" Transaction Complete")
                    break
                  else:
                    print(" ")
                    print(" kindly sorry to say that This Account Doesnot have this Amount ")
                    print("        enter lower amount")

                else:
                  print(" ")
                  print(" kindly sorry to say that our Atm Doesnot have this Amount ")
                  print("        enter lower amount")

              else:
                print(" ")
                print(" You Enter the Wrong Password ,  Try again") 
                print(" ")

          elif option == 2:
            print(" Accesing Banking serivces ")
            while True:
              check_pin = getpass(True)
              balance = customers[user].get("amount")
              if check_pin == password :
                print(" ")
                print(" balance cash amount ",balance)
                print(" ")
                print(" serivces denied")
                print(" server is low ,  Sorry Try again ")
                break
              else:
                print(" ")
                print(" Accesing denied.....")
                print(" You Enter the Wrong Password ,  Try again") 
                print(" ")

          elif option == 3:
            print(" Accesing Banking serivces Change password for this Account ")
            while True:
              check_pin = getpass(True)
              if check_pin == password :
                print(" ")
                print(" This Services needed Data of your Databases")
                print("      wanted Phone Number")
                check_phone = getnum(True)
                if check_phone == customers[user].get("phone") :
                  print(" Access Granted...")
                  print(" ")
                  new_pin = getpass(False1)
                  current_pin = customers[user].get("pin") 
                  current_pin= new_pin
                  print(" successfully , Pin changed ....")
                  print(" ")
                  print(" Transaction Completed..")
                  speak(" Transaction Complete")
                  break

                else:
                  print(" ")
                  print(" Accesing denied.....")
                  print(" You Enter the Wrong Data ,  Try again") 
                  print(" ")
                

              else:
                print(" ")
                print(" Accesing denied.....")
                print(" You Enter the Wrong Password ,  Try again") 
                print(" ")

          elif option == 4:
            print(" Transaction Complete...")
            speak(" Transaction Complete...")
            print(" ")
            end1=time.time()
            print(f" total seconds used in atm  : {end1-start} seconds")
            exit = False
          else:
            print(" Option is not availale ")
            print("    Wrong option using another option")
          exit1=False

     else:
        print(" ")
        false_entry += 1
        print(" Wrong Password or Username ")
        print("            Try again......")
        print(" ")
        exit = activer_security(false_entry)
      
