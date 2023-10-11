from connect import *



menu = MenuFile("PYTHON\TextFiles\Stock\Groups\menu_stockGroupDelete.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input



# 
def Delete_ByID():
    _id = input(menu_input[15])
    valid_id = FindID("stock_itemGroups", "groupID", _id)
    #
    if valid_id[0]:
        print()
        user_delete = input(menu_input[19])
        if user_delete == "1":
            db_cur.execute(f"DELETE FROM stock_itemGroups WHERE groupID = {_id}")
            db_cur.execute(f"DELETE FROM stock_groupItems WHERE itemGroupID = {_id}")
            db_con.commit()
            Display([], [], menu_input[14], menu_input[47])
        else:
            Display([], [], menu_input[39], menu_input[47])
    else:
        Display([], [], menu_input[26], menu_input[47])



def Delete_ByName():
    _name = input(menu_input[16]).title()
    _name = "'" + _name + "'"
    valid_name = FindName("stock_itemGroups", _name)
    #
    if valid_name:
        print()
        user_delete = input(menu_input[19])
        if user_delete == "1":
            try:
                db_cur.execute(f"DELETE FROM stock_itemGroups WHERE name = {_name}")
                db_cur.execute(f"DELETE FROM stock_groupItems WHERE name = {_name}")
                db_con.commit()
                Display([], [], menu_input[14], menu_input[47])
            except:
                Display([], [], menu_input[26], menu_input[47])
        else:
            Display([], [], menu_input[39], menu_input[47])
    else:
        Display([], [], menu_input[26], menu_input[47])



def Delete_AllGroups():
    user_delete = input(menu_input[21])
    if user_delete == "1":
        db_cur.execute("DELETE FROM stock_groupItems")
        db_cur.execute("DELETE FROM stock_itemGroups")
        #db_cur.execute("DELETE stock_itemGroups, stock_groupItems FROM stock_itemGroups INNER JOIN stock_groupItems ON stock_itemGroups.groupID = stock_groupItems.itemGroupID")
        db_con.commit()
        Display([], [], menu_input[14], menu_input[47])
    else:
        Display([], [], menu_input[39], menu_input[47])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[11])
            Delete_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[11])
            Delete_ByName()
        elif user_choice == '3':
            ClearPrint(menu_input[12])
            Delete_AllGroups()
        elif user_choice == '4':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
