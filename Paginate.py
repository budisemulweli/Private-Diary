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
