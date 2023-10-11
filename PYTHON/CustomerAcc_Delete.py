from connect import *



menu = MenuFile("PYTHON\TextFiles\CustomerAccounts\menu_userAccountDelete.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\CustomerAccounts\menuInput.txt")  # menu for user input



#
def DeleteAccount(db_fieldIn, user_fieldIn):
    _count = '1'
    print()
    if db_fieldIn == []:
        user_delete = input(menu_input[31])
    else:
        user_delete = input(menu_input[32])
    #
    if user_delete == "1":
        if db_fieldIn == []:
            db_cur.execute("DELETE FROM customerAccounts")
            db_cur.execute("SELECT COUNT(*) FROM customerAccounts")
            _count = db_cur.fetchone()[0]
        else:
            if len(db_fieldIn) > 1:
                db_cur.execute(f"DELETE FROM customerAccounts WHERE {db_fieldIn[0]} = {user_fieldIn[0]} AND {db_fieldIn[1]} = {user_fieldIn[1]}")
            else:
                db_cur.execute(f"DELETE FROM customerAccounts WHERE {db_fieldIn[0]} = {user_fieldIn[0]}")
        #
        _count = int(_count)
        if _count >= 1:
            db_con.commit()
            Display([], [], menu_input[33], menu_input[47])
        else:
            Display([], [], menu_input[38], menu_input[47])
    else:
        Display([], [], menu_input[34], menu_input[47])


# 
def Delete_ByID():
    _id = input(menu_input[21])
    valid_id = FindID("customerAccounts", "userID", _id)
    #
    if valid_id[0]:
        DeleteAccount(['userID'], [_id])
    else:
        Display([], [], menu_input[25], menu_input[47])



#
def Delete_ByName():
    f_name = input(menu_input[22]).title()
    f_name = "'" + f_name + "'"
    #
    l_name = input(menu_input[23]).title()
    l_name = "'" + l_name + "'"
    #
    valid_fName = FindName("customerAccounts", f_name)
    if valid_fName:
        valid_name = FindName("customerAccounts", l_name)
        if valid_name:
            DeleteAccount(['nameFirst', 'nameLast'], [f_name, l_name])
        else:
            Display([], [], menu_input[26], menu_input[47])
    else:
        Display([], [], menu_input[26], menu_input[47])



def Delete_ByEmail():
    _email = input(menu_input[24]).title()
    _email = "'" + _email + "'"
    #
    valid_email = FindEmail("customerAccounts", _email)
    if valid_email:
        DeleteAccount(['email'], [_email])
    else:
        Display([], [], menu_input[27], menu_input[47])
        


def Delete_AllAccounts():
    DeleteAccount([], [])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[8])
            Delete_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[8])
            Delete_ByName()
        elif user_choice == '3':
            ClearPrint(menu_input[8])
            Delete_ByEmail()
        elif user_choice == '4':
            ClearPrint(menu_input[9])
            Delete_AllAccounts()
        elif user_choice == '5':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
