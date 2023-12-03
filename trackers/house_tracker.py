#DEV NOTES:
#TO DO:
# - replace where necessary queries not using queryConstructor
# - add data validation (check proper dates are inserted, numbers where numbers should be, etc)
# - add confirmation for deleting row
# - figure out what else would be proper to turn into a class (tileConstructor, for example)
# - write proper tests (late now, but would be good to practice)
# - fix styling
# - transform into a universal "tracker" package, and create "house finance" overlay. will allow other trackers 
# to be easily created using same basic structure, would just need to create custom overlays.

#WANTED FUTURE ADDITIONS:
# - row editing (now that insertion/deletion have been sorted, shouldn't be too hard)
# - sorting feature
# - ability to add or remove columns
# - per request, adding "categories" drop down column(ie. electrical, foundation, plumbing, etc.)


import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime


today = datetime.date.today()
year = today.year
deleteQueue = []
select = "SELECT"
insert = "INSERT"
delete = "DELETE"
all = "*"

def connect():
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)

def tableCheck(cur):
    try:
        tableCheck = "SELECT 1 FROM SQLITE_SCHEMA WHERE name = 'house_tracker' AND type = 'table'"
        tablePrime = """INSERT INTO house_tracker(id, date, service, amount, source, check_number)
                        VALUES(0, '01/21/2020', 'Table Created.', 0, 'Admin', 000000)"""
        cur.execute(tableCheck)
        tableResult = cur.fetchall()
        if tableResult == []:
            tableGen = """CREATE TABLE house_tracker(
                            id NOT NULL PRIMARY KEY,
                            date,
                            service NOT NULL,
                            amount NOT NULL,
                            source NOT NULL,
                            check_number)
                            """
            cur.execute(tableGen)
            cur.execute(tablePrime)
            con.commit()
            print("Initial setup successful!")
  
        print("yes")
    except ValueError as error:
        print(error)

def queryConstructor(action, target,conditions):
    try:
        if (conditions is None or conditions == ""):
            query = action +" "+ target + " FROM house_tracker WHERE id != 0 ORDER BY DATE ASC"
        else:
            query = action +" " + target + " FROM house_tracker WHERE id != 0 AND " + conditions + " ORDER BY DATE ASC"
        
        return query
    except:
        return("error in queryConstructor")

def tileConstructor(rowId, index, parent, cur):
    try:
        rowNumber = str(index +2)
        pull = queryConstructor(select,all, "id = "+ str(rowId))
        defaultValue = IntVar()
        cur.execute(pull)
        row = cur.fetchone()
        def queueDelete(*args):
            try:
                ldeleteQueue = globals()["deleteQueue"]
                if rowId not in ldeleteQueue:                  
                    globals()["deleteQueue"].append(rowId)
                elif rowId in ldeleteQueue:
                    globals()["deleteQueue"].remove(rowId)
            except ValueError as error:
                print("error in queueDelete: " + error)
        
        Checkbutton(parent,\
                    variable=defaultValue, \
                    name = "checkBox "+str(row[0]),\
                    command=queueDelete).grid(column=1, row=rowNumber)
        ttk.Label(parent, text="   |   ").grid(column=2, row=rowNumber)
        ttk.Label(parent, name = "date "+str(row[0]), text=str(row[1])).grid(column=3, row=rowNumber)
        ttk.Label(parent, text="   |   ").grid(column=4, row=rowNumber)
        ttk.Label(parent, name = "service "+str(row[0]), text=str(row[2])).grid(column=5, row=rowNumber)
        ttk.Label(parent, text="   |   ").grid(column=6, row=rowNumber)
        ttk.Label(parent, name = "amount "+str(row[0]), text=str(row[3])).grid(column=7, row=rowNumber)
        ttk.Label(parent, text="   |   ").grid(column=8, row=rowNumber)
        ttk.Label(parent, name = "source "+str(row[0]), text=str(row[4])).grid(column=9, row=rowNumber)
        ttk.Label(parent, text="   |   ").grid(column=10, row=rowNumber)
        ttk.Label(parent, name = "checkNumber "+str(row[0]),   text=str(row[5])).grid(column=11, row=rowNumber)
    except ValueError as error:
        print("Error in tileConstructor: ",error)

def generateTiles(parent, cur):
    try:
        pull = queryConstructor(select, "*", "")
        cur.execute(pull)
        results = cur.fetchall()
        index = 1
        for row in results:
            tileConstructor(row[0],index,parent,cur)
            index = index + 1

    except ValueError as error:
        print("Error in generateTiles: ",error)

def insertButton():
    try:
        date = StringVar()
        service = StringVar()
        amount = StringVar()
        source = StringVar()
        check = StringVar()

        def validateDate(date):
            try:
                resultDate = str(date).split("/")

                def validateFormat(resultDate):
                    check = 0
                    if len(resultDate) == 3:
                        check = 0
                    else:
                        check = 1
                        return(check) 
                    if \
                    len(resultDate[0]) == 2 and \
                    len(resultDate[1]) == 2 and \
                    len(resultDate[2]) == 4: 
                        check = 0
                    else:
                        check = 1
                        return(check) 
                    if \
                        resultDate[0].isnumeric() is True and \
                        resultDate[1].isnumeric() is True and \
                        resultDate[2].isnumeric() is True:
                            check = 0
                    else:
                        check = 1
                    return(check)
                
                def validateMonth(resultDate):
                    check = 0
                    if \
                        int(resultDate[0]) <= 12 and \
                        int(resultDate[0]) >= 1:
                        check = 0
                    else:
                        check =1
                    return(check)
                        
                def validateDay(resultDate):   
                    check = 0      
                    if int(resultDate[0]) == 2:
                        if \
                        int(resultDate[1]) >= 1 and \
                        int(resultDate[1]) <= 29:
                            check = 0
                        else:
                            check = 1

                    elif int(resultDate[0]) in [9,4,6,11]:
                        if \
                            int(resultDate[1]) >= 1 and \
                            int(resultDate[1]) <= 30:
                                check = 0
                        else:
                            check = 1
                    else:
                        if \
                            int(resultDate[1]) >= 1 and \
                            int(resultDate[1]) <= 31:
                                check = 0
                        else:
                            check = 1
                    return(check)
                
                def validateYear(resultDate):
                    check = 0
                    if  \
                        int(resultDate[2]) >= 2000 and \
                        int(resultDate[2]) <= year:
                            check = 0
                    else:
                        check = 1
                    return(check)
                

                if validateFormat(resultDate) != 0:
                    return 1
                else:
                    if validateMonth(resultDate) != 0:
                        return 1
                    else:
                        if validateDay(resultDate) != 0:
                            return 1
                        else:
                            if validateYear(resultDate) != 0:
                                return 1
                            else:
                                return 0 
            except ValueError as error:
                print("error in validateDate: " + str(error))

        def saveNewRow(*args):
            try:
                validDate = validateDate(date.get())
                if validDate == 0:
                    cur = globals()["cur"]
                    pullId = "SELECT MAX(id) + 1 FROM house_tracker;"
                    cur.execute(pullId)
                    newId = cur.fetchone()[0]
                    insertStatement = """INSERT INTO house_tracker(id, date, service, amount, source, check_number)
                            VALUES(""" + str(newId) + """, '""" + date.get() + """', '""" + service.get() + """',
                                """+ amount.get() + """, '""" + source.get() + """', '""" + check.get() + """')"""
                    cur.execute(insertStatement)
                    con.commit()
                    globals()["mf"] = mainFrame(root)
                    newWindow.destroy()
                    print("new row inserted successfully!")
                else:
                    messagebox.showerror("showerror", "Please enter a valid date in 'MM/DD/YYYY' format.")
            except ValueError as error:
                print(error)

        newWindow = Toplevel(root)
        ttk.Label(newWindow, text="           ").grid(row=1, column=1)
        ttk.Label(newWindow, text = "Please Enter New Row").grid(row=1, column=2)
        ttk.Entry(newWindow,width= 20, textvariable=date).grid(row=2, column=2, sticky= (N,W,E,S))
        ttk.Label(newWindow, text= "Date").grid(row=2, column=3, sticky= (N,W,E,S))
        ttk.Entry(newWindow,width= 20, textvariable=service).grid(row=3, column=2)
        ttk.Label(newWindow, text= "Service").grid(row=3, column=3, sticky= (N,W,E,S))
        ttk.Entry(newWindow,width= 20, textvariable=amount).grid(row=4, column=2)
        ttk.Label(newWindow, text= "Amount").grid(row=4, column=3, sticky= (N,W,E,S))
        ttk.Entry(newWindow,width= 20, textvariable=source).grid(row=5, column=2)
        ttk.Label(newWindow, text= "Source").grid(row=5, column=3, sticky= (N,W,E,S))
        ttk.Entry(newWindow,width= 20, textvariable=check).grid(row=6, column=2)
        ttk.Label(newWindow, text= "Check #").grid(row=6, column=3, sticky= (N,W,E,S))
        saveButton = ttk.Button(newWindow, text="save", command=saveNewRow)
        saveButton.grid(row=1, column=3)
    except ValueError as error:
        print("error in insertButton: " + error)

def deleteButton():
    try:
        cur = globals()["cur"]
        if globals()["deleteQueue"] != []:
            deleteStatement = """DELETE FROM house_tracker WHERE id IN (""" + str(globals()["deleteQueue"]).strip('[]') +""")"""
            cur.execute(deleteStatement)
            con.commit()

            print("delete successful.")
            globals()["deleteQueue"] = []
            globals()["mf"] = mainFrame(root)
        else:
            print("nothing to delete")
    except ValueError as error:
        print("error in deleteFromQueue: " + error)

class mainFrame():
    def __init__(self,parent):
        mainframe = ttk.Frame(parent,padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N,W, E, S))
        ttk.Label(mainframe, text="Date").grid(column=3, row=2)
        ttk.Label(mainframe, text="   |   ").grid(column=4, row=2)
        ttk.Label(mainframe, text="Service").grid(column=5, row=2)
        ttk.Label(mainframe, text="   |   ").grid(column=6, row=2)
        ttk.Label(mainframe, text="Amount").grid(column=7, row=2)
        ttk.Label(mainframe, text="   |   ").grid(column=8, row=2)
        ttk.Label(mainframe, text="Source").grid(column=9, row=2)
        ttk.Label(mainframe, text="   |   ").grid(column=10, row=2)
        ttk.Label(mainframe,text="Check #").grid(column=11, row=2)
        generateTiles(mainframe, globals()["cur"])
        ttk.Button(mainframe, text = "Insert", command= insertButton).grid(column=3, row=1)
        ttk.Button(mainframe, text="Delete", command= deleteButton).grid(column=4, row=1)

def onClose():
    try:
        globals()["con"].close()
        globals()["root"].destroy()
    except ValueError as error:
        print("Error in onClose: " + error)

con = connect()
cur = con.cursor()
tableCheck(cur)
root = Tk()
root.title("House Finance Tracker")
mf = mainFrame(root)
root.protocol("WM_DELETE_WINDOW",onClose)
root.mainloop()














#---- For testing ----#
def insert_test():
    con = connect()
    cur = con.cursor()
    cur.execute("select MAX(id)+ 1 FROM house_tracker")
    newId = 0 #cur.fetchone()[0]
    query= """INSERT INTO house_tracker(id, date, service, amount, source, check_number)
                        VALUES(""" + str(newId) + """, '10/30/2020', 'Initial Load', 0, 'Admin', 123456)"""
    cur.execute(query)
    con.commit()
    cur.close()
    print("Insert complete!")

def quickQuery():
    con = connect()
    cur = con.cursor()
    #cur.execute("SELECT * FROM house_tracker;")
    cur.execute("SELECT MAX(id) + 1 FROM house_tracker;")
    print(str(cur.fetchall()))
#---- For testing ----#

# tableCheck()
#quickQuery()
#insert_test()
