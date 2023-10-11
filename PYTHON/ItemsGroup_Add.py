from connect import *
from groupItem_Add import *



# get user input
def Insert_ItemGroup():
    menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input
    #
    valid = False
    while not valid:
        try:
            os.system('cls')
            print(menu_input[2])
            #
            group_name = input(menu_input[4]).title()
            group_info = input(menu_input[5])
            #
            _groupItems = input(menu_input[6])
            try:
                group_items = int(_groupItems)
            except:
                group_items = 0
            #
            db_cur.execute("INSERT INTO stock_itemGroups(name, description, groupItems) VALUES(?,?,?)",(group_name, group_info, '0'))
            valid = True
        except:
            print(menu_input[18])
            valid = False
    #
    db_con.commit()
    #
    if group_items > 0:
        _id = db_cur.lastrowid  # get the id just assigned
        for i in range(group_items):
            print(f"\nItem #{i+1}:")
            Insert_Item(_id, menu_input)    # enter group items



#
if __name__ == "__main__":
    Insert_ItemGroup()
