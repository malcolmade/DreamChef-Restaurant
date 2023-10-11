from connect import *
from HelpPageEdit import DisplayChoice, Sub_Prog



menu = MenuFile("PYTHON\TextFiles\WebSiteEdit\AboutPage\menu_aboutPageEdit.txt")  # menu choices
menu_edit = MenuFile("PYTHON\TextFiles\WebSiteEdit\subMenu.txt")
menu_input = MenuInputFile("PYTHON\TextFiles\WebSiteEdit\menuInput.txt")
#
edit_fileDir = "PYTHON\TextFiles\WebSiteEdit\HelpPage\File_webPageEdit.txt"
edit_file = MenuInputFile(edit_fileDir)
#
titleInfo1_fileDir = "PYTHON\TextFiles\WebSiteEdit\HelpPage\File_Title1Info.txt"
titleInfo2_fileDir = "PYTHON\TextFiles\WebSiteEdit\HelpPage\File_Title2Info.txt"



# MAIN MENU OPTIONS ................................

#
def  Title1():
    Sub_Prog(edit_file[21], edit_file[22], menu_input[30], 22)
    


#
def  Title1_Info():
    while True:
        _choice = Menu_subMenu(['0', '1', '2', '3'], menu_edit, menu_input)
        if _choice == '1':
            _file = open(titleInfo1_fileDir, 'r')
            DisplayChoice(edit_file[23], _file.read())
            _file.close()
        elif _choice == '2':
            user_data = input(f"\n{menu_input[32]}")
            if user_data != '':
                _file = open(titleInfo1_fileDir, "w")
                _file.write(user_data)
                _file.close()
                #
                Display([], [], menu_input[16], menu_input[47])
        elif _choice == '3':
            break
        elif _choice == '0':
            exit()




#
def  Title2():
    Sub_Prog(edit_file[25], edit_file[26], menu_input[35], 26)



#37
def  Title2_Info():
    while True:
        _choice = Menu_subMenu(['0', '1', '2', '3'], menu_edit, menu_input)
        if _choice == '1':
            _file = open(titleInfo2_fileDir, 'r')
            DisplayChoice(edit_file[27], _file.read())
            _file.close()
        elif _choice == '2':
            user_data = input(f"\n{menu_input[37]}")
            if user_data != '':
                _file = open(titleInfo2_fileDir, "w")
                _file.write(user_data)
                _file.close()
                #
                Display([], [], menu_input[16], menu_input[47])
        elif _choice == '3':
            break
        elif _choice == '0':
            exit()



#
def  Img():
    Sub_Prog(edit_file[29], edit_file[30],menu_input[38], 30)



def MenuAboutPageEdit():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5', '6'], menu, menu_input)
        if user_choice == '1':
            Title1()
        elif user_choice == '2':
            Title1_Info()
        elif user_choice == '3':
            Title2()
        elif user_choice == '4':
            Title2_Info()
        elif user_choice == '5':
            Img()
        elif user_choice == '6':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuAboutPageEdit()

