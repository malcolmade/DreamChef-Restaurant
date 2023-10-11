from connect import *
import Orders_Display, Orders_Delete



menu = MenuFile("PYTHON\TextFiles\Orders\menu_orders.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\Orders\menuInput.txt")



def MenuOrders():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3'], menu, menu_input)
        if user_choice == '1':
            Orders_Display.Main_Prog()
        elif user_choice == '2':
            Orders_Delete.Main_Prog()
        elif user_choice == '3':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuOrders()
