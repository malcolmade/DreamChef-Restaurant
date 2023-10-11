from connect import *
import HomePageEdit, AboutPageEdit, HelpPageEdit



menu = MenuFile("PYTHON\TextFiles\WebSiteEdit\menu_webSiteEdit.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\WebSiteEdit\menuInput.txt")



def MenuWebSiteEdit():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4'], menu, menu_input)
        if user_choice == '1':
            HomePageEdit.MenuHomePageEdit()
        elif user_choice == '2':
            AboutPageEdit.MenuAboutPageEdit()
        elif user_choice == '3':
            HelpPageEdit.MenuHelpPageEdit()
        elif user_choice == '4':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuWebSiteEdit()

