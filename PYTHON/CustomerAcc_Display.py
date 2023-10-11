from connect import *



menu = MenuFile("PYTHON\TextFiles\CustomerAccounts\menu_userAccountDisplay.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\CustomerAccounts\menuInput.txt")  # menu for user input
#
db_field  = FieldNames('customerAccounts', 8)


# 
def Display_ByID():
    _id = input('\n' + menu_input[21])
    #
    try:
        db_cur.execute(F"SELECT * FROM customerAccounts WHERE userID = {_id}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[25], menu_input[47])
    except:
        Display([], [], menu_input[25], menu_input[47])



def Display_ByName():
    f_name = input(menu_input[22]).title()
    f_name = "'" + f_name + "'"
    #
    l_name = input(menu_input[23]).title()
    l_name = "'" + l_name + "'"
    #
    try:
        db_cur.execute(F"SELECT * FROM customerAccounts WHERE nameFirst = {f_name} AND nameLast = {l_name}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[26], menu_input[47])
    except:
        Display([], [], menu_input[26], menu_input[47])



def Display_ByEmail():
    _email = input(menu_input[24]).title()
    f_name = "'" + f_name + "'"
    #
    try:
        db_cur.execute(F"SELECT * FROM customerAccounts WHERE email = {_email}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[27], menu_input[47])
    except:
        Display([], [], menu_input[27], menu_input[47])



def Display_AllAccounts():
    _count = 0
    #
    db_cur.execute("SELECT COUNT(*) FROM customerAccounts")
    _count = db_cur.fetchone()[0]
    if _count > 0:
        db_cur.execute("SELECT * FROM customerAccounts")
        for i in range(_count):
            db_data = db_cur.fetchone()
            Display(db_field, db_data, '', menu_input[47])
    else:
        Display([], [], menu_input[38], menu_input[47])



def Display_AccountOrders():
    order_field  = FieldNames('orders', 8)
    _count = 0
    #
    _id = input('\n' + menu_input[21])
    #
    try:
        db_cur.execute(F"SELECT * FROM orders WHERE accountID = {_id}")
        db_data = db_cur.fetchone()
        #
        db_cur.execute(F"SELECT COUNT(*) FROM orders WHERE accountID = {_id}")
        _count = db_cur.fetchone()[0]
        if _count > 0:
            for i in range(_count):
                db_data = db_cur.fetchone()
                Display(order_field, db_data, '', menu_input[47])
        else:
            Display([], [], menu_input[39], menu_input[47])
    except:
        Display([], [], menu_input[25], menu_input[47])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5', '6'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[2])
            Display_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[2])
            Display_ByName()
        elif user_choice == '3':
            ClearPrint(menu_input[2])
            Display_ByEmail()
        elif user_choice == '4':
            ClearPrint(menu_input[3])
            Display_AllAccounts()
        elif user_choice == '5':
            ClearPrint(menu_input[14])
            Display_AccountOrders()
        elif user_choice == '6':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()