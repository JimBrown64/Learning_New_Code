

import sqlite3
import datetime
import sql_interactions as sql
import gui
from tkinter import *
today = datetime.date.today()
year = today.year

def connect():
    con = sqlite3.connect("testdb.db")
    print("connection successful")
    return(con)

con = connect()
cur = con.cursor()


def testIt():
   print(0)

def test2():
    print(1)
 
root = Tk()

menubar = Menu(root)
fileMenu = gui.newMenu(menubar,"File")
addItem = gui.menuItem(fileMenu,"Add...",testIt)
# removeItem = gui.menuItem(fileMenu,"Remove...",test2)


root.config(menu=menubar)
root.mainloop()








# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)

# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)


# def checkTable(test):
#    result = sql.tableCheck(test,cur)
#    print(result)

# def checkTableCreate(tableName, cur, con, columns):
#     try:
#         check = sql.tableCheck(tableName, cur)
#         if check == 0:
#             sql.tableConstructor(tableName, cur, con, columns)
#         else:
#             print("table already exists!")
#     except ValueError as error:
#         print("error in checkTableCreate: " + error)

# def checkEdit(table, cur, con, action, column):
#     sql.editTable(table, cur, con, action, column)

# def checkQuery(table, target, conditions):
#     try:
#         result = sql.tableQuery(table, target, conditions, cur)
#         print(result)
#     except ValueError as error:
#         print(error)

# def checkInsert(table,columns,values):
#     try:
#         result = sql.tableInsert(table,columns,values,cur)
#         print(result)
#     except ValueError as error:
#         print(error)    

# def checkDelete(table,conditions):
#     try:
#         result = sql.tableDelete(table,conditions,cur,con)
#         print(result)
#     except ValueError as error:
#         print(error)   


# def test():
#     result = sql.tableQuery("testTable","*","", cur)
#     print(result)


# #test()
# checkTableCreate("testTable",cur,con,"a,b,c,d")
# checkTable("apple")
# checkTable("testTable")
# checkQuery("testTable",sql.all,"")
# #checkInsert("testTable","a,b,c,d","2,22,222,2222")
# checkDelete("testTable","a = 2")
# checkQuery("testTable",sql.all,"")
# #checkEdit(" testTable ",cur,con," ADD ","id")











# def validateDate(date):
#     try:
#         resultDate = date.split("/")

#         def validateFormat(resultDate):
#             check = 0
#             if len(resultDate) == 3:
#                 check = 0
#             else:
#                 check = 1
#                 return(check) 
#             if \
#             len(resultDate[0]) == 2 and \
#             len(resultDate[1]) == 2 and \
#             len(resultDate[2]) == 4: 
#                 check = 0
#             else:
#                 check = 1
#                 return(check) 
#             if \
#                 resultDate[0].isnumeric() is True and \
#                 resultDate[1].isnumeric() is True and \
#                 resultDate[2].isnumeric() is True:
#                     check = 0
#             else:
#                 check = 1
#             return(check)
        
#         def validateMonth(resultDate):
#             check = 0
#             if \
#                 int(resultDate[0]) <= 12 and \
#                 int(resultDate[0]) >= 1:
#                 check = 0
#             else:
#                 check =1
#             return(check)
                
#         def validateDay(resultDate):   
#             check = 0      
#             if int(resultDate[0]) == 2:
#                 if \
#                 int(resultDate[1]) >= 1 and \
#                 int(resultDate[1]) <= 29:
#                     check = 0
#                 else:
#                     check = 1

#             elif int(resultDate[0]) in [9,4,6,11]:
#                 if \
#                     int(resultDate[1]) >= 1 and \
#                     int(resultDate[1]) <= 30:
#                         check = 0
#                 else:
#                     check = 1
#             else:
#                 if \
#                     int(resultDate[1]) >= 1 and \
#                     int(resultDate[1]) <= 31:
#                         check = 0
#                 else:
#                     check = 1
#             return(check)
        
#         def validateYear(resultDate):
#             check = 0
#             if  \
#                 int(resultDate[2]) >= 2000 and \
#                 int(resultDate[2]) <= year:
#                     check = 0
#             else:
#                 check = 1
#             return(check)
        

#         if validateFormat(resultDate) != 0:
#            return 1
#         else:
#             if validateMonth(resultDate) != 0:
#                return 1
#             else:
#                 if validateDay(resultDate) != 0:
#                     return 1
#                 else:
#                     if validateYear(resultDate) != 0:
#                         return 1
#                     else:
#                         return 0 
#     except ValueError as error:
#         print("error in validateDate: " + str(error))

# def testValidation(input,expectation):
#     try:
#         result = validateDate(input)
#         failMsg = "test failed. expected: " + str(expectation) + " | received: " + str(result) + " | input: " + input
#         succMsg = "Test passed! expected: " + str(expectation) + " | received: " + str(result) + " | input: " + input
#         if result == expectation:
#             print(succMsg)
#             return(0)
#         else:
#             print(failMsg)
#             return(1)
#     except ValueError as error:
#         print("error")


# def dateTestSet():
#     try:

#         result = \
#             testValidation("10/10/2012",0) + \
#             testValidation("10-12-2010",1) + \
#             testValidation("10/10/12",1) + \
#             testValidation("1/10/2012",1) + \
#             testValidation("01/3/2010",1) + \
#             testValidation("10102012",1) + \
#             testValidation("Jan/12/2010",1) + \
#             testValidation("Ja/12/2010",1) + \
#             testValidation("13/12/2010",1) + \
#             testValidation("10/32/2010",1) + \
#             testValidation("10/31/2032",1) + \
#             testValidation("10/31/1994",1) + \
#             testValidation("09/09/2001",0)

#         if result == 0:
#             print("All tests passed!")
#         else: 
#             print("number of tests failed: " + str(result))
#     except ValueError as error:
#         print(error)

# #dateTestSet()


# def testNumberValidation():
#     try:
#         print("yes")
#     except ValueError as error:
#         print("error")
