import datetime
import hashlib
import os
import random
import time

from replit import db


def Userchoice(prompt):
  try:
    userinput = int(input(prompt + ' >> '))
    if userinput == 1:
      return True
    elif userinput == 2:
      return False
    else:
        print('Invalid input. Try again')
        time.sleep(2)
        return Userchoice(prompt) #Returns boolean
  except ValueError:
      print('Error.\nTry again\n')
      time.sleep(1)
      return Userchoice(prompt) #Returns boolean



    

def Hashing(str):
 #utilize hashlib to return a hex version of string
  
  encoded_str = str.encode()
  hashed_str = hashlib.sha256(encoded_str)
  hex = hashed_str.hexdigest()
  return hex

def Create():
  #collect username and hashed pass and store in database
  #if user exists, give user option to login or create another user

  while True:  
    username = input('Register your username >> ')
    password = input('Register your new password >> ')
    keys = list(db.keys())
    if username not in keys:
      salt = random.randint(1000, 9999)
      full_password = f"{password}{salt}"
      hashed_pass = Hashing(full_password)
      db[f"{username}"] = {'Password': hashed_pass, 'salt': salt, 'entries': {}}
      print('User has been registered!')
      time.sleep(2)
      return
    else:
      option = Userchoice('Username already exists.\n1.Login instead\n2.Create User\n ')
      if option:
        os.system('clear')
        Login()
      elif not option:
        os.system('clear')
        Create()
      
      else:
        print('Unrecognized input. Returning home...')
        time.sleep(2)
        os.system('clear')
        break
  
def Login():
  #salt and hash collected input password
  #compare w password in database
  #return username for user entry access after login

  
  while True:  
    username = input('Username >> ')
    password = input('password >> ')
    keys = list(db.keys())
    if username in keys:
      try: 
        salt = db[f"{username}"]['salt']
        stored_pass = db[f"{username}"]["Password"]
        userpassword = f"{password}{salt}"
        hiddenpass = Hashing(userpassword)
        if hiddenpass == stored_pass:
          print(f"Succesfully Logged in.\nWelcome Back {username}")
          time.sleep(2)
          os.system('clear')
          return username
  
        else:
          option = Userchoice('Username or password mismatch.\n1. Try again\n2.Exit')
          if option:
            os.system('clear')
            continue
          else:
            os.system('clear')
            break
      except KeyError:
        print('Key is missing from database.')
        for items in keys:
          print(items)
         
    else:
      option = Userchoice('Username not found.\n1. Try again\n2.Exit')
      if option:
        os.system('clear')
        continue
      else:
        os.system('clear')
        break
      
  
def Add_entry():
  #save user entry along w timestamp in database
  
  while True:
    entry = input('Insert entry >> ')
    timestamp = datetime.datetime.now()
    f_timestamp = timestamp.strftime('%c')
    db[f"{username}"]['entries'][f_timestamp] = entry
    print('Entry saved.')
    time.sleep(2)


    try:  
      more = Userchoice('1.Add another\n2.Exit\n')
      if more:
        os.system('clear')
        continue
      else:
        os.system('clear')
        break
    except ValueError:
      print('Exiting...')
      time.sleep(2)
      break

def Paginate():
  #Show user entries in reverse chrono order
  #paginate them for optimal UI.

  user_entries = db[f"{username}"]['entries']
  reversed_dict = dict(reversed(list(user_entries.items())))
  
  
  for key in reversed_dict:
    os.system('clear')
    print(f"{key}: {reversed_dict[key]}\n")
    next_page = Userchoice('1.Show next entry\n2.Exit\n')
    if next_page:
      os.system('clear')
      continue
    else:
      os.system('clear')
      break

#// Menu hub
def Diary_menu():  
  while True: 
    print('Private Diary\n')
    selection = Userchoice('1.Add\n2.View\n')
    if selection: #adds entry
      Add_entry()
      continue
    elif not selection: #views entry
      Paginate()
      continue
    else:
      print('Closing...')
      time.sleep(2)
      break




print('Private Diary\n')
#//-- Registration & Authentication --//
while True:  
  init = Userchoice('1.Register Account\n2.Login\n')
  if init:
    Create()
    continue
  
  else:
    username = Login()
  #//-- Diary Hub --//
    Diary_menu()



