from connect import *



menu = MenuFile("PYTHON\TextFiles\Orders\menu_ordersDisplay.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\Orders\menuInput.txt")  # menu for user input
#
db_field  = FieldNames('orders', 8)


# 
def Display_ByID():
    _id = input('\n' + menu_input[21])
    #
    try:
        db_cur.execute(F"SELECT * FROM orders WHERE accountID = {_id}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[25], menu_input[47])
    except:
        Display([], [], menu_input[25], menu_input[47])



def Display_AllOrders():
    _count = 0
    #
    db_cur.execute("SELECT COUNT(*) FROM orders")
    _count = db_cur.fetchone()[0]
    if _count > 0:
        db_cur.execute("SELECT * FROM orders")
        for i in range(_count):
            db_data = db_cur.fetchone()
            Display(db_field, db_data, '', menu_input[47])
    else:
        Display([], [], menu_input[39], menu_input[47])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[2])
            Display_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[3])
            Display_AllOrders()
        elif user_choice == '3':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()