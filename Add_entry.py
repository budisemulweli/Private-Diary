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
