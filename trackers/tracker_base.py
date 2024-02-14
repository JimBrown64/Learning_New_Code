# TO DO:
# add validation for form
# straighten out individual tiles so they line up
# add edit row functionality



import sqlite3
import datetime
import sql_interactions as sql
import tkinter as tk 
import date_management as dm

today = datetime.date.today()
year = today.year

columns = []
deleteQueue = []
table = "table"
con = ""
cur = ""
root = ""

def test():
    print(0)

def test2():
    print(1)

def loadRoot(root):
    globals()["root"] = root

def loadConnection(con):
    globals()["con"] = con
    globals()["cur"] = con.cursor()
    

def loadTableName(table):
    globals()["table"] = table

def loadColumns(table,cur):
    listColumns = []
    pullColumns = "SELECT * FROM " + table
    data = cur.execute(pullColumns)
    for column in data.description:
        listColumns.append(str(column[0]))
    globals()["columns"] = listColumns


def addRow(table,cur,con,root,mainframe):
    try:
        newWindow = tk.Toplevel(root)
        columns = globals()["columns"]
        listColumns = []
        for item in columns:
            if item != "id":
                listColumns.append(item)
        listInfo = {}
        
        row = 2
        for column in listColumns:
            listInfo[column] = tk.StringVar()
            tk.Label(newWindow, text= column).grid(row=row, column=3, sticky= (tk.N,tk.W))
            tk.Entry(newWindow,width= 20, textvariable=listInfo[column]).grid(row=row, column=2)            
            row = row + 1
        
        def saveNewRow(cur,con,mainframe):
            try:
                pullId = sql.tableQuery(table,"MAX(id)+1","",cur)
                newId = str(pullId[0]).strip("()").replace(",","")
                values = [newId]
                for column in listInfo:
                    values.append(listInfo[column].get())
                insertVals = str(values).strip("[]")
                columnList = str(columns).strip("[]")                   
                sql.tableInsert(table,columnList,insertVals,cur,con)
                newWindow.destroy()
                refreshPage(mainframe)
                print("new row inserted successfully!")
            except ValueError as error:
                print(error)

        saveButton = tk.Button(newWindow, text="save", command=lambda: saveNewRow(cur,con,mainframe))
        saveButton.grid(row=1, column=3)
    except ValueError as error:
        print("error in insertButton: " + error)

class mainFrame():
    def __init__(self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W),padx=5, pady=5)

    def menuBar(self):
        root = self.root
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff = 0)
        editmenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New Row...", command = lambda :addRow(globals()["table"],globals()["cur"],globals()["con"],globals()["root"],self.mainframe))
        filemenu.add_command(label = "Delete Rows", command = lambda :deleteSelected(self.mainframe))
        menubar.add_cascade(label= "Edit", menu = editmenu)
        editmenu.add_command(label = "New Column", command = addColumn)
        root.config(menu = menubar)

class tileFrame():
    def __init__(self,parent,row,column):
        self.parent = parent
        self.frame = tk.Frame(parent, bd = 4, relief=tk.GROOVE)
        self.frame.grid(column= column, row= row, sticky=tk.W)    

def newLabel(parent, text, column, row):
    try:
        label = tk.Label(parent, text= text).grid(column= column, row= row, padx=5, pady=1)
    except ValueError as error:
        print("Error in newLabel: " + error)

def createCheckbox(parent,column,row, name):
    parent.checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(parent,name=name, variable=parent.checkbox_var, command= lambda: queueDelete(name))
    checkbox.grid(column= column, row= row, padx=5, pady=1)

def generateTiles(frame):
    # noId = []
    # for column in globals()["columns"]:
    #     if column != "id":
    #         noId.append(column)
    #         print(column)
    # noId = str(noId).strip("[]").replace("'", "")
    # print(noId)
    data = sql.tableQuery(table,"*","id != 0",cur)
    rowNo = 2
    for row in data:
        rowFrame = tileFrame(frame,rowNo,1)
        createCheckbox(rowFrame.frame,column=1,row = 1,name = str(row[0]))
        column = 2
        for item in row[1:]:
            newLabel(parent=rowFrame.frame, text = item, column = column, row = 1)
            column = column + 1
        rowNo = rowNo +1

def queueDelete(rowId):
    try:
        ldeleteQueue = globals()["deleteQueue"]
        if rowId not in ldeleteQueue: 
            ldeleteQueue.append(rowId)                 
        elif rowId in ldeleteQueue:
            ldeleteQueue.remove(rowId)
        print(str(deleteQueue))
    except ValueError as error:
        print("error in queueDelete: " + error)

def deleteSelected(mainframe):
    try:
        cur = globals()["cur"]
        con = globals()["con"]
        if globals()["deleteQueue"] != []:
            conditions = """id IN (""" + str(globals()["deleteQueue"]).strip('[]') +""")"""
            sql.tableDelete(table,conditions,cur,con)

            print("delete successful.")
            globals()["deleteQueue"] = []
            refreshPage(mainframe)
            # mainframe.mainframe.destroy()
            # mainframe = mainFrame(root)
            # generateTiles(root)
        else:
            print("nothing to delete")
    except ValueError as error:
        print("error in deleteFromQueue: " + error)

def headerRow(parent):
    columns = globals()["columns"]
    noId = []
    for column in columns:
        if column != "id":
            noId.append(column)
    header = tileFrame(parent,row=1, column=1)
    newLabel(header.frame,"     ",1,1)
    columnNo = 2
    for item in noId:
        newLabel(header.frame,item,columnNo,1)
        columnNo = columnNo +1

def addColumn():
    try:
        table = globals()["table"]
        cur = globals()["cur"]
        con = globals()["con"]
        entry = tk.StringVar()
        newWindow = tk.Toplevel(root)
                
        def applyColumn():
            newColumn = entry.get()
            sql.editTable(table,cur,con,sql.add,newColumn)
            newWindow.destroy()
            # refreshPage(mainframe)
            print("column added successfully!")
        
        tk.Label(newWindow, text= "New Column").grid(row=2, column=3, sticky= (tk.N,tk.W))
        tk.Entry(newWindow,width= 20, textvariable=entry).grid(row=2, column=2)
        saveButton = tk.Button(newWindow, text="save", command=lambda: applyColumn())
        saveButton.grid(row=1, column=3)

    except ValueError as error:
        print("error in addColumn: " + error)


def refreshPage(frame):
    child_frames = frame.winfo_children()
    for child_frame in child_frames:
        child_frame.destroy()
    headerRow(frame)
    generateTiles(frame)


    # def onClose():
    #     try:
    #         globals()["con"].close()
    #         globals()["root"].destroy()
    #     except ValueError as error:
    #         print("Error in onClose: " + error)