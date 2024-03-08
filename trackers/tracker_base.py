# TO DO:
# straighten out individual tiles so they line up
# add edit row functionality
# add sorting function



import sqlite3
import datetime
import sql_interactions as sql
import tkinter as tk 
from tkinter import messagebox
import date_management as dm
import re

today = datetime.date.today()
year = today.year

columns = []
selectedQueue = []
table = "table"
con = ""
cur = ""
root = ""
mainframe = ""
sortToggle = ['ASC','']

def loadRoot(root):
    globals()["root"] = root

def loadConnection(con):
    globals()["con"] = con
    globals()["cur"] = con.cursor()
    
def loadMainframe(mainframe):
    globals()["mainframe"] = mainframe

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
        listColumns = columns[1:]
        listInfo = {}
        
        row = 2
        for column in listColumns:
            listInfo[column] = tk.StringVar()
            tk.Label(newWindow, text= column).grid(row=row, column=3, sticky= (tk.N,tk.W))
            entry = tk.Entry(newWindow,width= 20, textvariable=listInfo[column])
            entry.grid(row=row, column=2)
            if column == 'date':
                entry.insert(0,"MM/DD/YYYY")                
            row = row + 1
        
        def saveNewRow(cur,con,mainframe):
            try:
                pullId = sql.tableQuery(table,"MAX(id)+1","",cur)
                newId = str(pullId[0]).strip("()").replace(",","")
                values = [newId]
                for column in listInfo:
                    if column == 'date':
                        date = listInfo['date'].get()
                        if dm.validateDate(date) != 1:
                            print(date)
                            messagebox.showerror("showerror", "Please enter a valid date in 'MM/DD/YYYY' format.")
                            return 0
                        else: 
                            formattedDate = dm.tableFormat(listInfo['date'].get())
                            values.append(formattedDate)
                    elif listInfo[column].get().isnumeric():
                            values.append(int(listInfo[column].get()))
                    else:
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
        viewmenu = tk.Menu(menubar,tearoff= 0)
        sortmenu = tk.Menu(viewmenu,tearoff= 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New Row...", \
                             command = lambda :addRow(globals()["table"],\
                                                      globals()["cur"],\
                                                      globals()["con"],\
                                                      globals()["root"],\
                                                      self.mainframe))
        filemenu.add_command(label = "Delete Rows", command = lambda :deleteSelected(self.mainframe))
        menubar.add_cascade(label= "Edit", menu = editmenu)
        editmenu.add_command(label = "New Column", command = addColumn)
        editmenu.add_command(label = "Edit Row", command = editRow)
        menubar.add_cascade(label= "View", menu= viewmenu)
        viewmenu.add_cascade(label = "Sort By...", menu = sortmenu)

        for column in columns[1:]:
            sortmenu.add_command(label= column, command= lambda col = column: newSort(self.mainframe,col))    
       
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
    checkbox = tk.Checkbutton(parent,name=name, variable=parent.checkbox_var, command= lambda: queueRows(name))
    checkbox.grid(column= column, row= row, padx=5, pady=1)

def generateTiles(frame,params=''):
    data = sql.tableQuery(table,"*","id != 0 "+ params,cur)
    rowNo = 2
    for row in data:
        rowFrame = tileFrame(frame,rowNo,1)
        createCheckbox(rowFrame.frame,column=1,row = 1,name = str(row[0]))
        column = 2
        for item in row[1:]:
            if item is not None and isinstance(item,int) is False and re.search("..../../..",item) is not None:
                item = dm.displayFormat(item)
            newLabel(parent=rowFrame.frame, text = item, column = column, row = 1)
            column = column + 1
        rowNo = rowNo +1

def queueRows(rowId):
    try:
        ldeleteQueue = globals()["selectedQueue"]
        if rowId not in ldeleteQueue: 
            ldeleteQueue.append(rowId)                 
        elif rowId in ldeleteQueue:
            ldeleteQueue.remove(rowId)
        print(globals()["selectedQueue"])
    except ValueError as error:
        print("error in queueRows: " + error)

def deleteSelected(mainframe):
    try:
        cur = globals()["cur"]
        con = globals()["con"]
        if globals()["selectedQueue"] != []:
            deleteConfirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all selected rows?")
            if deleteConfirmation:
                conditions = """id IN (""" + str(globals()["selectedQueue"]).strip('[]') +""")"""
                sql.tableDelete(table,conditions,cur,con)
                print("delete successful.")
                globals()["selectedQueue"] = []
                refreshPage(mainframe)
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


def refreshPage(frame,params = ''):
    child_frames = frame.winfo_children()
    for child_frame in child_frames:
        child_frame.destroy()
    headerRow(frame)
    generateTiles(frame,params)
    globals()["selectedQueue"] = []

def newSort(frame, sortby):
    try:
        print(sortby)
        print(globals()['sortToggle'][1])
        print(globals()['sortToggle'][0])
        if sortby == globals()['sortToggle'][1]:
            if globals()['sortToggle'][0] == 'ASC':
                globals()['sortToggle'][0] = 'DESC'
            else:
                globals()['sortToggle'][0] = 'ASC'
        else:
            globals()['sortToggle'][1] = sortby
            globals()['sortToggle'][0] = 'ASC'
        params = 'ORDER BY ' + sortby + ' ' + globals()['sortToggle'][0]
        print (params)
        refreshPage(frame,params)
    except ValueError as error:
        print("error in newSort: "+ error)

def editRow():
    try:
        if len(selectedQueue) != 1:
            messagebox.showerror("showerror", "Please ensure you have one(1) row selected before editing.")
        else:
            print(selectedQueue[0])
            data = sql.tableQuery(table,sql.all," id = '"+selectedQueue[0]+"'",globals()["cur"])
            #make a form here, autofill values with pre-existing ones
            newWindow = tk.Toplevel(root)
            columns = globals()["columns"]
            listColumns = columns[1:]
            listInfo = {}
            
            row = 2
            for column in listColumns:
                listInfo[column] = tk.StringVar()
                tk.Label(newWindow, text= column).grid(row=row, column=3, sticky= (tk.N,tk.W))
                entry = tk.Entry(newWindow,width= 20, textvariable=listInfo[column])
                entry.grid(row=row, column=2)
                item = data[0][row-1]
                if column == 'date':
                    item = dm.displayFormat(item)
                entry.insert(0,item)                
                row = row + 1
            
            def saveRow(cur,con,mainframe):
                try:
                    values = [data[0][0]]
                    for column in listInfo:
                        if column == 'date':
                            date = listInfo['date'].get()
                            if dm.validateDate(date) != 1:
                                print(date)
                                messagebox.showerror("showerror", "Please enter a valid date in 'MM/DD/YYYY' format.")
                                return 0
                            else: 
                                formattedDate = dm.tableFormat(listInfo['date'].get())
                                values.append("'"+formattedDate+"'")
                        elif listInfo[column].get().isnumeric():
                                values.append(int(listInfo[column].get()))
                        else:
                            values.append("'"+listInfo[column].get()+"'")
                    
                    sets = ""
                    columnCount = 1
                    for column in listColumns:
                        subString = column + " = " + str(values[columnCount]) + " , "
                        sets = sets + subString
                        columnCount = columnCount + 1
                    sets = sets[:-2]
                    query = "UPDATE " + globals()["table"] + " SET " \
                        + sets + " WHERE id = '" + values[0] + "'" 
                    print(query)                     
                    cur.execute(query)
                    con.commit()
                    newWindow.destroy()
                    refreshPage(mainframe)
                    print("Row Edited successfully!")
                except ValueError as error:
                  print(error)

        saveButton = tk.Button(newWindow, text="save", command=lambda: saveRow(cur,con,mainframe.mainframe))
        saveButton.grid(row=1, column=3)
        print('yes')
    except ValueError as error:
        print("Error in editRow: " + error)


    # def onClose():
    #     try:
    #         globals()["con"].close()
    #         globals()["root"].destroy()
    #     except ValueError as error:
    #         print("Error in onClose: " + error)
