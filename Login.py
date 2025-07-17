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
      
