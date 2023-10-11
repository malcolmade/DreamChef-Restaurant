from connect import *



# get user input
def Insert_GroupItem():
    menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input
    group_id = 0
    #
    ClearPrint(menu_input[22])
    _id = input('\n' + menu_input[15])
    valid_id = FindID("stock_itemGroups", "groupID", _id)
    #
    if valid_id[0]:
        group_id = int(_id)
        print(f"{menu_input[7]} {valid_id[1][0]}")
        Insert_Item(group_id, menu_input)
    else:
        Display([], [], menu_input[17], menu_input[47])



def Insert_Item(id_in, menu_in):
    #
    valid = False
    while not valid:
        try:
            item_name = input(menu_in[27]).title()
            # item_name = input(f"\n{menu_in[27]}").title()
            #
            item_info = input(menu_in[28])
            #
            try:
                item_count = int(input(menu_in[29]))
            except:
                item_count = 1
            #
            try:
                item_price = float(input(menu_in[30]))
            except:
                item_price = 0.0
            #
            item_image = input(menu_in[31])
            #
            db_cur.execute("INSERT INTO stock_groupItems(name, description, quantity, price, imgFileDir, itemGroupID) VALUES(?,?,?,?,?,?)",(item_name, item_info, item_count, item_price, item_image, id_in))
            valid = True
        except:
            print(menu_in[43])
            valid = False
    #
    db_con.commit()
    # update GROUP's sub count
    db_cur.execute(F"SELECT groupItems FROM stock_itemGroups WHERE groupID = {id_in}")
    db_con.commit()
    _count = db_cur.fetchone()[0]
    groupSubs_count = int(_count)
    groupSubs_count += 1
    groupSubs_count = str(groupSubs_count)
    groupSubs_count = "'" + groupSubs_count + "'"
    # update the Group's groupItems count
    db_cur.execute(F"UPDATE stock_itemGroups SET groupItems = {groupSubs_count} WHERE groupID = {id_in}")
    db_con.commit()
    #
    Display([], [], menu_in[1], menu_in[47])
    


#
if __name__ == "__main__":
    Insert_GroupItem()
