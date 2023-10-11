from connect import *
import getpass
import Menu_StockGroups, Menu_StockItems



admin_menu = MenuFile("PYTHON\TextFiles\menu_adminControl.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\menu_AdminInput.txt")


"""
#def LogIn_Admin():
ClearPrint(menu_input[0])
#
timeDate_now = datetime.datetime.now()
time_info = GetTime_Info(timeDate_now)
# time_symbol, time_ofDay, _time
print(f"{time_info[2]} {time_info[0]}\nGood {time_info[1]}\n")
print(menu_input[1])
print()
#
user_name = input(menu_input[3])
print()
user_pwd = input(menu_input[4])
"""


import keyboard
while True:
    if keyboard.read_key() == "a":
        print("You pressed 'a'.")
        break



user = getpass.getuser()
while True:
   pwd = getpass.getpass("User Name : ",user)
   if pwd == 'Crimson':
      print("You are in!")
   else:
      print("The password you entered is wrong.")





"""
main_prog = True
while main_prog:
    os.system('cls')
    user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5'], admin_menu, menu_input)
    if user_choice == '1':
        Menu_StockGroups.MenuGroups()
    elif user_choice == '2':
        Menu_StockItems.MenuItems()
    #elif user_choice == '3':
        # customer accounts
    #elif user_choice == '4':
        # orders
    #elif user_choice == '5':
        # website edit
    elif user_choice == '0':
        main_prog = False   # exit()
"""


