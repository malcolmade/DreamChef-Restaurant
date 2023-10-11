from connect import *
import ItemsGroup_Add, ItemsGroup_Display, ItemsGroup_Update, ItemsGroup_Delete



menu = MenuFile("PYTHON\TextFiles\Stock\Groups\menu_stockGroup.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")



def MenuGroups():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5'], menu, menu_input)
        if user_choice == '1':
            ItemsGroup_Display.Main_Prog()
        elif user_choice == '2':
            ItemsGroup_Add.Insert_ItemGroup()
        elif user_choice == '3':
            ItemsGroup_Update.Main_Prog()
        elif user_choice == '4':
            ItemsGroup_Delete.Main_Prog()
        elif user_choice == '5':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuGroups()
