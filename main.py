import datetime
import hashlib
import os
import random
import time

from replit import db
from Add_entry import Add_entry
from Create_account import Create
from Diary_menu import Diary_menu
from Login import Login
from paginate import paginate
from Userchoice import Userchoice
from Hashing import Hashing

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



