from connect import *
import CustomerAcc_Display, CustomerAcc_Delete



menu = MenuFile("PYTHON\TextFiles\CustomerAccounts\menu_userAccount.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\CustomerAccounts\menuInput.txt")



def MenuCustomerAcc():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3'], menu, menu_input)
        if user_choice == '1':
            CustomerAcc_Display.Main_Prog()
        elif user_choice == '2':
            CustomerAcc_Delete.Main_Prog()
        elif user_choice == '3':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuCustomerAcc()
