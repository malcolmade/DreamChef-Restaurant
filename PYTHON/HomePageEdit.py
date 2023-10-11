from connect import *



menu = MenuFile("PYTHON\TextFiles\WebSiteEdit\HomePage\menu_homePageEdit.txt")  # menu choices
menu_input = MenuInputFile("PYTHON\TextFiles\WebSiteEdit\menuInput.txt")
#
db_field  = FieldNames('webSite_editHome', 8)



#
def DisplayFavs():
    _count = 0
    #
    db_cur.execute("SELECT COUNT(*) FROM webSite_editHome")
    _count = db_cur.fetchone()[0]
    if _count > 0:
        db_cur.execute("SELECT * FROM webSite_editHome")
        for i in range(_count):
            db_data = db_cur.fetchone()
            Display(db_field, db_data, '', menu_input[47])
    else:
        Display([], [], menu_input[39], menu_input[47])



#
def AddFav():
    fav_count = 0
    valid = True
    err_msg = ''
    #
    db_cur.execute("SELECT COUNT(*) FROM webSite_editHome")
    fav_count = db_cur.fetchone()[0]
    #
    if fav_count < 5:
        try:
            os.system('cls')
            print(menu_input[1])
            #
            fav_id = input(menu_input[3])
            valid_id = FindID("stock_groupItems", "itemID", fav_id)
            if valid_id[0]:
                # verify not duplicate favourite
                db_cur.execute(F"SELECT * FROM webSite_editHome WHERE favID = {fav_id}")
                _favID = db_cur.fetchone()
                if _favID == None:
                    fav_pos = int(input(menu_input[4]))
                    try:
                        # verify fav position within range 1 to 5
                        if fav_pos in range(1,6):
                            db_cur.execute(F"SELECT * FROM webSite_editHome WHERE favPos = {fav_pos}")
                            _favPos = db_cur.fetchone()                        
                            if _favPos == None:
                                valid = True
                            else:
                                valid = False
                                err_msg = menu_input[28]
                        else:
                            valid = False
                            err_msg = menu_input[29]
                    except:
                            valid = False
                else:
                    valid = False
                    err_msg = menu_input[25]
            else:
                valid = False
                err_msg = menu_input[25]
        except:
            valid = False
            err_msg = menu_input[25]
        #
    else:
        valid = False
        err_msg = menu_input[26]
    #
    if valid:
        db_cur.execute("INSERT INTO webSite_editHome(favPos, favID) VALUES(?,?)",(fav_pos, fav_id))
        db_con.commit()
        Display([], [], menu_input[15], menu_input[47])
    else:
        Display([], [], err_msg, menu_input[47])



#
def UpdateFavPos():
    valid_pos = True
    err_msg = ''
    #
    # get favourite position to update
    fav_pos = int(input('\n' + menu_input[22]) )
    if fav_pos in range(1, 6):  # verify favourite position within range 1 - 5
        # verify favourite position exist in db-webSite_editHome
        db_cur.execute(F"SELECT * FROM webSite_editHome WHERE favPos = {fav_pos}")
        pos_data = db_cur.fetchone()
        if pos_data != None:
            fav_id = pos_data[1]    # item id at pos
            # get new favourite position
            fav_posNew = int(input('\n' + menu_input[23]))
            if fav_posNew in range(1, 6):
                if fav_posNew != fav_pos:   # verify new favourite position not same as favourite position to update
                    # check if favourite position exist in db-webSite_editHome
                    db_cur.execute(F"SELECT * FROM webSite_editHome WHERE favPos = {fav_posNew}")
                    posCur_data = db_cur.fetchone()
                    #
                    db_cur.execute(F"DELETE FROM webSite_editHome WHERE favPos = {fav_pos}")    # delete old data to be updated
                    db_con.commit()
                    if posCur_data == None:
                        # if favourite position empty, assign new position
                        db_cur.execute("INSERT INTO webSite_editHome(favPos, favID) VALUES(?,?)",(fav_posNew, fav_id))
                    else:
                        # if favourite position occupied, swap favourite positions
                        db_cur.execute(F"DELETE FROM webSite_editHome WHERE favPos = {posCur_data[0]}")    # delete occupied favourite position data
                        db_con.commit()
                        #
                        # upload the swapped data
                        db_cur.execute("INSERT INTO webSite_editHome(favPos, favID) VALUES(?,?)",(fav_posNew, fav_id))
                        db_cur.execute("INSERT INTO webSite_editHome(favPos, favID) VALUES(?,?)",(fav_pos, posCur_data[1]))
                    #
                    db_con.commit()
                    Display([], [], menu_input[16], menu_input[47])
                else:
                    valid_pos = False
                    err_msg = menu_input[36]
            else:
                valid_pos = False
                err_msg = menu_input[29]
        else:
            valid_pos = False
            err_msg = menu_input[19]
    else:
        valid_pos = False
        err_msg = menu_input[29]
    #
    if valid_pos == False:
         Display([], [], err_msg, menu_input[47])

         

#
def UpdateFavItem():
    _valid = True
    err_msg = ''
    #
    # get favourite position to update
    fav_pos = int(input('\n' + menu_input[24]) )
    if fav_pos in range(1, 6):
        # verify favourite position exist in db-webSite_editHome
        db_cur.execute(F"SELECT * FROM webSite_editHome WHERE favPos = {fav_pos}")
        pos_data = db_cur.fetchone()
        if pos_data != None:
            # get replacement item id
            fav_id = int(input('\n' + menu_input[21]))
            # verify item id exists in db-stock_groupItems
            db_cur.execute(F"SELECT * FROM stock_groupItems WHERE itemID = {fav_id}")
            id_data = db_cur.fetchone()
            if id_data != None:
                # REPLACE ITEM ID
                db_cur.execute(F"UPDATE webSite_editHome SET favID = {fav_id} WHERE favPos = {fav_pos}") 
                db_con.commit()
                Display([], [], menu_input[16], menu_input[47])
            else:
                _valid = False
                err_msg = menu_input[20]
        else:
            _valid = False
            err_msg = menu_input[19]
    else:
        _valid = False
        err_msg = menu_input[29]
    #
    if _valid == False:
        Display([], [], err_msg, menu_input[47])



#
def DeleteFav():
    os.system('cls')
    print(menu_input[11])
    #
    fav_pos = int(input(menu_input[4]))
    if fav_pos in range(1,6):
        try:
            db_cur.execute(F"DELETE FROM webSite_editHome WHERE favPos = {fav_pos}")
            db_con.commit()
            Display([], [], menu_input[33], menu_input[47])
        except:
            Display([], [], menu_input[19], menu_input[47])
    else:
        Display([], [], menu_input[29], menu_input[47])



#
def MenuHomePageEdit():
    _prog = True
    while _prog:
        os.system('cls')
        user_choice = Menu_subMenu(['0', '1', '2', '3', '4', '5', '6'], menu, menu_input)
        if user_choice == '1':
            DisplayFavs()
        elif user_choice == '2':
            AddFav()
        elif user_choice == '3':
            UpdateFavPos()
        elif user_choice == '4':
            UpdateFavItem()
        elif user_choice == '5':
            DeleteFav()
        elif user_choice == '6':
            _prog = False
        elif user_choice == '0':
            _prog = exit()



#
if __name__ == "__main__":
    MenuHomePageEdit()

