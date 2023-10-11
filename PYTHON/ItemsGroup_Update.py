from connect import *



menu = MenuFile("PYTHON\TextFiles\Stock\Groups\menu_stockGroupUpdate.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input



# 
def UpdateGroup(db_searchFieldIn, group_searchFieldIn):
    group_name = input(menu_input[4]).title()
    group_info = input(menu_input[5])
    group_name = "'" + group_name + "'"
    group_info = "'" + group_info + "'"
    # update the Group
    db_cur.execute(F"UPDATE stock_itemsGroup SET name = {group_name}, description = {group_info} WHERE {db_searchFieldIn} = {group_searchFieldIn}")
    db_con.commit()



def Update_ByID():
    group_id = input('\n' + menu_input[15])
    valid_id = FindID("stock_itemGroups", "groupID", group_id)
    #
    if valid_id[0]:
        UpdateGroup('groupID', group_id)
        """
        group_name = input(menu_input[4]).title()
        group_info = input(menu_input[5])
        group_name = "'" + group_name + "'"
        group_info = "'" + group_info + "'"
        # update the Group
        db_cur.execute(F"UPDATE stock_itemsGroup SET name = {group_name}, description = {group_info} WHERE groupID = {group_id}")
        db_con.commit()
        """
        Display([], [], menu_input[23], menu_input[47])
    else:
        Display([], [], menu_input[17], menu_input[47])
    


def Update_ByName():
    group_name = input('\n' + menu_input[16])
    valid_name = FindName("stock_itemGroups", group_name)
    #
    if valid_name:
        UpdateGroup('name', group_name)
        """
        group_name = input(menu_input[4]).title()
        group_info = input(menu_input[5])
        group_name = "'" + group_name + "'"
        group_info = "'" + group_info + "'"
        # update the Group
        db_cur.execute(F"UPDATE stock_itemsGroup SET name = {group_name}, description = {group_info} WHERE name = {group_name}")
        db_con.commit()
        """
        Display([], [], menu_input[23], menu_input[47])
    else:
        Display([], [], menu_input[17], menu_input[47])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[13])
            Update_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[13])
            Update_ByName()
        elif user_choice == '3':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
