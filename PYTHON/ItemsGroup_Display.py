from connect import *
from groupItem_Display import Display_AllItems



menu = MenuFile("PYTHON\TextFiles\Stock\Groups\menu_stockGroupDisplay.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input
#
db_field = ('ID\t\t', 'Name\t\t', 'Description\t', 'Sub Menus\t')



def Display_ByID():
    _id = input('\n' + menu_input[15])
    try:
        db_cur.execute(F"SELECT * FROM stock_itemGroups WHERE groupID = {_id}")
        db_data = db_cur.fetchone()
        #
        ClearPrint('')
        Display(db_field, db_data, menu_input[17], menu_input[47])
        #
        _userKey = input(f"\n{menu_input[8]}")
        print()
        if _userKey == '1':
            Display_AllItems(_id)
    except:
        Display([], [], menu_input[17], menu_input[47])
    


def Display_ByName():
    _name = input(menu_input[16]).title()
    _name = "'" + _name + "'"
    try:
        db_cur.execute(F"SELECT * FROM stock_itemGroups WHERE name = {_name}")
        db_data = db_cur.fetchone()
        _id = str(db_data[0])
        #
        ClearPrint('')
        Display(db_field, db_data, menu_input[18], menu_input[47])
        #
        _userKey = input(f"\n{menu_input[8]}")
        print()
        if _userKey == '1':
            Display_AllItems(_id)
    except:
        Display([], [], menu_input[18], menu_input[47])



def Display_AllGroups():
    db_cur.execute("SELECT COUNT(*) FROM stock_itemGroups")
    count = db_cur.fetchone()[0]
    db_cur.execute("SELECT * FROM stock_itemGroups")
    #
    if count == 0:
        Display([], [], menu_input[0], menu_input[47])
    else:    
        for i in range(count):
            db_data = db_cur.fetchone()
            Display(db_field, db_data, '', menu_input[47])



def Main_Prog():
    subMain_prog = True
    while subMain_prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4'], menu, menu_input)
        if user_choice == '1':
            ClearPrint(menu_input[9])
            Display_ByID()
        elif user_choice == '2':
            ClearPrint(menu_input[9])
            Display_ByName()
        elif user_choice == '3':
            ClearPrint(menu_input[10])
            Display_AllGroups()
        elif user_choice == '4':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
