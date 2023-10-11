from connect import *



menu = MenuFile("PYTHON\TextFiles\WebSiteEdit\HelpPage\menu_helpPageEdit.txt")  # menu choices
menu_edit = MenuFile("PYTHON\TextFiles\WebSiteEdit\subMenu.txt")
menu_input = MenuInputFile("PYTHON\TextFiles\WebSiteEdit\menuInput.txt")
#
edit_fileDir = "PYTHON\TextFiles\WebSiteEdit\HelpPage\File_webPageEdit.txt"
edit_file = MenuInputFile(edit_fileDir)



# SUB MENU OPTIONS ................................

#
def DisplayChoice(field_in, data_in):
    print(f"\n{field_in}{data_in}")
    print('\n' + menu_input[47])
    mv.getch()



#
def UpdateChoice(query_in, file_posIn):
    print()
    user_data = input(query_in)
    if user_data != '':
        edit_file[file_posIn] = f"{user_data}\n"
        _file = open(edit_fileDir, "w")
        _file.writelines(edit_file)
        _file.close()
    #
    Display([], [], menu_input[16], menu_input[47])



#
def Sub_Prog(display_field, display_data, update_query, update_filePos):
    while True:
        _choice = Menu_subMenu(['0', '1', '2', '3'], menu_edit, menu_input)
        if _choice == '1':
            DisplayChoice(display_field, display_data)
        elif _choice == '2':
            UpdateChoice(update_query, update_filePos)
        elif _choice == '3':
            break
        elif _choice == '0':
            exit()



# MAIN MENU OPTIONS ................................

#
def  DaysOpen():
    Sub_Prog(edit_file[3], edit_file[4], menu_input[41], 4)



#
def  TimeOpen():
    Sub_Prog(edit_file[1], edit_file[2], menu_input[40], 2)



#
def  Address():
    Sub_Prog(edit_file[5], edit_file[6], menu_input[42], 6)



#
def  Phone():
    Sub_Prog(edit_file[7], edit_file[8],menu_input[43], 8)


#

def  Email():
    Sub_Prog(edit_file[9], edit_file[10],menu_input[44], 10)



#
def MenuHelpPageEdit():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5', '6'], menu, menu_input)
        if user_choice == '1':
            DaysOpen()
        elif user_choice == '2':
            TimeOpen()
        elif user_choice == '3':
            Address()
        elif user_choice == '4':
            Phone()
        elif user_choice == '5':
            Email()
        elif user_choice == '6':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuHelpPageEdit()

