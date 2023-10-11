from connect import *
import groupItem_Add, groupItem_Display, groupItem_Update, groupItem_Delete



menu = MenuFile("PYTHON\TextFiles\Stock\GroupItems\menu_groupItems.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")



def MenuItems():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5'], menu, menu_input)
        if user_choice == '1':
            groupItem_Display.Main_Prog()
        elif user_choice == '2':
            groupItem_Add.Insert_GroupItem()
        elif user_choice == '3':
            groupItem_Update.Main_Prog()
        elif user_choice == '4':
            groupItem_Delete.Main_Prog()
        elif user_choice == '5':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuItems()
