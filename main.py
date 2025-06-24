import datetime
import os
import time

from replit import db


def Userchoice(prompt):

    userinput = int(input(prompt + ' >> '))
    if userinput == 1:
      return True
    elif userinput == 2:
      return False
    else:
        print('Invalid input. Try again')
        time.sleep(2)
        return Userchoice(prompt) #Returns boolean

def password_check():
  while True:
     try: 
      login = input('Insert password >> ')
      if login == db['password']:
        print('Verified!')
        time.sleep(2)
        break
      else:
        print('Password incorrect. Try again')
        continue
     except Exception as e:
      print(f"Error: {e}\nClosing...")
      time.sleep(2)
      exit()

       
  
def Add_entry():
  while True:
    entry = input('Insert entry >> ')
    timestamp = datetime.datetime.now()
    f_timestamp = timestamp.strftime('%c')
    db[f_timestamp] = entry
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

def Extract_list():
  keys = list(db.keys())
  sorted_keys = sorted(keys, reverse= True)
  return sorted_keys

def Paginate():
  sorted_keys = Extract_list()
  try:
   sorted_keys.remove('password') #Cleans password key from list. Leaves timestamps only.
  except ValueError:
    print('password not found. Cannot be removed')
    
  for keys in sorted_keys:
    os.system('clear')
    print(f"{keys}:\n{db[keys]}\n")
    next_page = Userchoice('1.Show next entry\n2.Exit\n')
    if next_page:
      os.system('clear')
      continue
    else:
      os.system('clear')
      break
  




print('Private Diary\n')
#// Registration and Login

init = Userchoice('1.Register Password\n2.Login\n')
if init:
  while True: 
   try: 
    password = input('Register password >> ')
    if password == db['password']:
      print('password already exists. Logging in...')
      time.sleep(2)
      os.system('clear')
      break
  
    else:
     db['password'] = password
     print('Password created! Logging in...')
     time.sleep(2)
     os.system('clear')
     break
    
   except Exception as e:
     print(f"Error: {e}\nClosing...")
     time.sleep(2)
     exit()

    
elif not init:
  password_check()
  os.system('clear')



#// Menu hub
while True: 
  print('Private Diary\n')
  selection = Userchoice('1.Add\n2.View\nPress any other key to exit\n')
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



