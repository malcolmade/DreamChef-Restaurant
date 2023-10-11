import sqlite3 as sql
import msvcrt as mv
import os, datetime, time



db_con = sql.connect("PYTHON\DBs\DefChef.db")
db_cur = db_con.cursor()



#
def ClearPrint(msg_in):
    os.system('cls')
    print(msg_in)



# retrieve menu-input txt file
def MenuInputFile(file_in):
    query_file = open(file_in, "r")
    querys = query_file.readlines()
    query_file.close()
    #
    return querys



# retrieve menu txt file
def MenuFile(file_in):
    with open(file_in) as menu_file:
        menu = menu_file.read()
    #
    return menu



def Menu_subMenu(optionsIn, menuIn, menu_inputIn):
    option = '-1'
    #
    while option not in optionsIn:
        ClearPrint(menuIn)
        option = input(menu_inputIn[46])
        #
        if option not in optionsIn:
            print(option + menu_inputIn[45])
            #time.sleep(1.5)
            Display([], [], '', 'Press Any Key To Continue!')
            ClearPrint(menu_inputIn[47])
    #
    return option



def FieldNames(table_nameIn, tab_countIn):
    db_cur.execute(f"SELECT * FROM {table_nameIn}")
    _fields = db_cur.description
    #
    field_name = {}
    for _index, _list in enumerate(_fields):
        # print(f"Field #{_index+1} = {_list[0]}")
        # print(f"list[0] = {_list[0]}")
        field_name[_index] = _list[0]
        if len(field_name[_index]) < tab_countIn:
            field_name[_index] = f"{field_name[_index]}\t\t"
        else:
            field_name[_index] = f"{field_name[_index]}\t"
    #
    return field_name
        


# display db table content(s)
def Display(field_in, data_in, msg1_in, msg2_in): # (data, error, userWait)
    if data_in == []:
        print(msg1_in)
    else:
        os.system('cls')
        i = 0
        for each_data in data_in:
            print(f"{field_in[i]}: {each_data}")
            i += 1
    #
    print('\n' + msg2_in)
    mv.getch()



# id search
def FindID(dbTable_in, field_in, id_in):
    valid_in = False
    _name = ''
    #
    try:
        db_cur.execute(F"SELECT * FROM {dbTable_in} WHERE {field_in} = {id_in}")
        _data = db_cur.fetchone()
        if _data == None:
            valid_in = False
        else:
            db_cur.execute(F"SELECT name FROM {dbTable_in} WHERE {field_in} = {id_in}")
            _name = db_cur.fetchone()
            valid_in = True
    except:
        valid_in = False
    #
    return valid_in, _name



# name search
def FindName(dbTable_in, name_in):
    valid_in = False
    #
    try:
        db_cur.execute(F"SELECT * FROM {dbTable_in} WHERE name = {name_in}")
        _data = db_cur.fetchone()
        if _data == None:
            valid_in = False
        else:
            valid_in = True
    except:
        valid_in = False
    #
    return valid_in



# email search
def FindEmail(dbTable_in, email_in):
    valid_in = False
    #
    try:
        db_cur.execute(F"SELECT * FROM {dbTable_in} WHERE email = {email_in}")
        _data = db_cur.fetchone()
        if _data == None:
            valid_in = False
        else:
            valid_in = True
    except:
        valid_in = False
    #
    return valid_in



# time of day (am / pm)
def GetTime_Info(time_in):
    time_now = time_in.strftime("%M:%S")   # extract current time without hour from timeDate_now string
    time_inHr = int(time_in.strftime("%H"))    # extract hour and cast to int
    _hr = time_inHr
    if time_inHr < 12:
        time_symbol = "am"
        time_ofDay = "Morning."
    else:
        if _hr > 12:
            _hr = _hr - 12
        #
        time_symbol = "pm"
        if time_inHr <= 17:
            time_ofDay = "Afternoon."
        else:
            time_ofDay = "Evening."
    #
    _time = f"{_hr}:{time_now}"
    #
    return time_symbol, time_ofDay, _time



def GetDate_2Day():
    timeDate_now = datetime.datetime.now()
    date_now = timeDate_now.strftime("%Y-%m-%d")    # extract date from timeDate_now string
    #
    return date_now

