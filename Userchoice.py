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



    
