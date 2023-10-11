from connect import *



menu = MenuFile("PYTHON\TextFiles\Orders\menu_ordersDelete.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\Orders\menuInput.txt")  # menu for user input



#
def DeleteOrder(db_fieldIn, user_fieldIn):
    _count = '1'
    print()
    if db_fieldIn == []:
        user_delete = input(menu_input[31])
    else:
        user_delete = input(menu_input[32])
    #
    if user_delete == "1":
        if db_fieldIn == []:
            db_cur.execute("DELETE FROM orders")
            db_cur.execute("SELECT COUNT(*) FROM orders")
            _count = db_cur.fetchone()[0]
        else:
            if len(db_fieldIn) > 1:
                db_cur.execute(f"DELETE FROM orders WHERE {db_fieldIn[0]} = {user_fieldIn[0]} AND {db_fieldIn[1]} = {user_fieldIn[1]}")
            else:
                db_cur.execute(f"DELETE FROM orders WHERE {db_fieldIn[0]} = {user_fieldIn[0]}")
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
    valid_id = FindID("orders", "accountID", _id)
    #
    if valid_id[0]:
        DeleteOrder(['accountID'], [_id])
    else:
        Display([], [], menu_input[25], menu_input[47])
        


def Delete_AllOrders():
    DeleteOrder([], [])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[8])
            Delete_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[9])
            Delete_AllOrders()
        elif user_choice == '3':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
