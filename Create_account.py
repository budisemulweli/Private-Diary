
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
