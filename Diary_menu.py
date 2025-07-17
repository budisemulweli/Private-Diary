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
