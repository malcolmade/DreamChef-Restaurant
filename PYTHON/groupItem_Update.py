from connect import *



menu = MenuFile("PYTHON\TextFiles\Stock\GroupItems\menu_groupItemsUpdate.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input



# 
def UpdateField(db_tableIn, db_fieldIn, item_fieldIn, db_searchFieldIn, item_searchFieldIn, typeIn):
    if typeIn == 'str':
        if item_fieldIn != "":
            item_fieldIn = "'" + item_fieldIn + "'"
            db_cur.execute(F"UPDATE {db_tableIn} SET {db_fieldIn} = {item_fieldIn} WHERE {db_searchFieldIn} = {item_searchFieldIn}")
    elif typeIn == 'num':
        if item_fieldIn != "":
            try:
                _count = float(_count)    # test if number
            except:
                item_fieldIn = '1'
            #
            item_fieldIn = "'" + item_fieldIn + "'"
            db_cur.execute(F"UPDATE {db_tableIn} SET {db_fieldIn} = {item_fieldIn} WHERE {db_searchFieldIn} = {item_searchFieldIn}")




def Update_ByID():
    item_id = input('\n' + menu_input[40])
    valid_id = FindID("stock_groupItems", "itemID", item_id)
    #
    if valid_id[0]:
        ClearPrint(menu_input[3])
        #
        item_name = input(f"\n{menu_input[27]}").title()
        UpdateField('stock_groupItems', 'name', item_name, 'itemID', item_id, 'str')
        #
        item_info = input(menu_input[28])
        UpdateField('stock_groupItems', 'description', item_info, 'itemID', item_id, 'str')
        #
        item_count = input(menu_input[29])
        UpdateField('stock_groupItems', 'quantity', item_count, 'itemID', item_id, 'num')
        #
        item_price = input(menu_input[30])
        UpdateField('stock_groupItems', 'price', item_price, 'itemID', item_id, 'num')
        #
        item_image = input(menu_input[31])
        UpdateField('stock_groupItems', 'imgFileDir', item_image, 'itemID', item_id, 'str')
        # update the Group
        db_con.commit()
        #
        Display([], [], menu_input[23], menu_input[47])
    else:
        Display([], [], menu_input[42], menu_input[47])



def Update_ByName():
    item_name = input('\n' + menu_input[27])
    valid_name = FindName("stock_groupItems", item_name)
    #
    if valid_name:
        ClearPrint(menu_input[3])
        #
        item_name = input(f"\n{menu_input[27]}").title()
        UpdateField('stock_groupItems', 'name', item_name, 'name', item_name, 'str')
        #
        item_info = input(menu_input[28])
        UpdateField('stock_groupItems', 'description', item_info, 'name', item_name, 'str')
        #
        item_count = input(menu_input[29])
        UpdateField('stock_groupItems', 'quantity', item_count, 'name', item_name, 'num')
        #
        item_price = input(menu_input[30])
        UpdateField('stock_groupItems', 'price', item_price, 'name', item_name, 'num')
        #
        item_image = input(menu_input[31])
        UpdateField('stock_groupItems', 'imgFileDir', item_image, 'name', item_name, 'str')
        # update the Group
        db_con.commit()
        #
        Display([], [], menu_input[23], menu_input[47])
    else:
        Display([], [], menu_input[43], menu_input[47])



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
