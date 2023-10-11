from connect import *
import time



menu = MenuFile("PYTHON\TextFiles\Stock\GroupItems\menu_groupItemsDisplay.txt")  # menu choices
menu_input = MenuInputFile("PYTHON/TextFiles/Stock/menuInput.txt")  # menu for user input
#
db_field = ('itemID\t\t', 'Name\t\t', 'Description\t', 'Quantity\t', 'Price\t\t', 'ImgFileDir\t', 'ItemGroupID\t')



# 
def Display_ByID():
    _id = input('\n' + menu_input[40])
    try:
        db_cur.execute(F"SELECT * FROM stock_groupItems WHERE itemID = {_id}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[42], menu_input[47])
    except:
        Display([], [], menu_input[42], menu_input[47])
    


def Display_ByName():
    _name = input(menu_input[27]).title()
    _name = "'" + _name + "'"
    try:
        db_cur.execute(F"SELECT * FROM stock_groupItems WHERE name = {_name}")
        db_data = db_cur.fetchone()
        Display(db_field, db_data, menu_input[43], menu_input[47])
    except:
        Display([], [], menu_input[43], menu_input[47])



def Display_AllItems(id_in):
    count = 0
    list_state = 'Empty'
    #
    if id_in == '-1':
        db_cur.execute("SELECT COUNT(*) FROM stock_groupItems")
        count = db_cur.fetchone()[0]
        db_cur.execute("SELECT * FROM stock_groupItems")
    else:
        db_cur.execute(F"SELECT COUNT(*) FROM stock_groupItems WHERE itemGroupID = {id_in}")
        count = db_cur.fetchone()[0]
        db_cur.execute(F"SELECT * FROM stock_groupItems WHERE itemGroupID = {id_in}")
    #
    if count == 0:
        Display([], [], menu_input[41], menu_input[47])
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
            Display_AllItems('-1')
        elif user_choice == '4':
            subMain_prog = False
        elif user_choice == '0':
            subMain_prog = exit()



#
if __name__ == "__main__":
    Main_Prog()
