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

def loadRoot(root): #gets the root of the app generated in the specific application
    globals()["root"] = root

def loadConnection(con): #gets the connection to the db from the specific application
    globals()["con"] = con
    globals()["cur"] = con.cursor()
    
def loadMainframe(mainframe): #gets the main window from the specific app 
    globals()["mainframe"] = mainframe

def loadTableName(table): #gets the table name from the specific app
    globals()["table"] = table

def loadColumns(table,cur): #gets the column names from the table
    listColumns = []
    pullColumns = "SELECT * FROM " + table
    data = cur.execute(pullColumns)
    for column in data.description:
        listColumns.append(str(column[0]))
    globals()["columns"] = listColumns


def addRow(table,cur,con,root,mainframe): #creates a form the user can utilize to add new info into the app
    try:
        newWindow = tk.Toplevel(root)
        columns = globals()["columns"]
        listColumns = columns[1:] #pulls all columns except for id
        listInfo = {}
        
        row = 2
        for column in listColumns: #creates an entry field, labeled with a column name for the entry form
            listInfo[column] = tk.StringVar()
            tk.Label(newWindow, text= column).grid(row=row, column=3, sticky= (tk.N,tk.W))
            entry = tk.Entry(newWindow,width= 20, textvariable=listInfo[column])
            entry.grid(row=row, column=2)
            if column == 'date':   #if there is a date field, have pre-existing text to note date format
                entry.insert(0,"MM/DD/YYYY")                
            row = row + 1
        
        def saveNewRow(cur,con,mainframe): #takes values entered into the form and saves it into the table
            try:
                pullId = sql.tableQuery(table,"MAX(id)+1","",cur) #query table for the next id
                newId = pullId[0][0] #extract the next id
                values = [newId] 
                for column in listInfo:
                    if column.upper() == 'DATE': #if there is a date column, check for a valid format, if not show an error
                        date = listInfo['date'].get()
                        if dm.validateDate(date) != 1:
                            messagebox.showerror("showerror", "Please enter a valid date in 'MM/DD/YYYY' format.")
                            return 0
                        else: 
                            formattedDate = dm.tableFormat(listInfo['date'].get()) #change date format before storing
                            values.append(formattedDate)
                    elif listInfo[column].get().isnumeric(): #form takes in all values as a string, so numbers must be converted to an integer before storing
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

class mainFrame(): #class used to create the main window, with primary needed functions attached
    def __init__(self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W),padx=5, pady=5)

    def menuBar(self): #adds a menubar to the mainFrame
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

class tileFrame(): #each row of info is stored in a seperate frame, called tiles.
    def __init__(self,parent,row,column):
        self.parent = parent
        self.frame = tk.Frame(parent, bd = 4, relief=tk.GROOVE)
        self.frame.grid(column= column, row= row, sticky=tk.W)    

def newLabel(parent, text, column, row): #adds a new text label
    try:
        info = text
        size =12
        if isinstance(text,str): #limit characters shown for improved readability
            info = text[:12]
        def showFullText(): # open a window to show the full text of a given element on the page
            textWindow =tk.Toplevel(root,width=50, height=50)
            textWindow.title="Full Item"
            textFrame = tk.Frame(textWindow,width=50, height=50)
            textFrame.grid(row=1, column=1)
            fullText = tk.Label(textFrame,text= text, wraplength=300)
            fullText.grid(row=2, column=2, padx=10, pady=10)

        label = tk.Label(parent, text= info, width=size, cursor="hand2")
        label.grid(column= column, row= row, pady=1,sticky= tk.W)
        label.bind("<Button-1>",lambda event:showFullText())
    except ValueError as error:
        print("Error in newLabel: " + error)

def createCheckbox(parent,column,row, name): 
    parent.checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(parent,name=name, variable=parent.checkbox_var, command= lambda: queueRows(int(name)))
    checkbox.grid(column= column, row= row, padx=5, pady=1)

def generateTiles(frame,params=''): #gathers data from the table and creates a row tile for each row in the table
    data = sql.tableQuery(table,"*","id != 0 "+ params,cur)
    rowNo = 2
    for row in data:
        rowFrame = tileFrame(frame,rowNo,1)
        createCheckbox(rowFrame.frame,column=1,row = 1,name = str(row[0]))
        column = 2
        for item in row[1:]: #ignores the first item, which is id
            if item is not None and isinstance(item,int) is False and re.search("..../../..",item) is not None: #if the item is a date, convert to easier to read version
                item = dm.displayFormat(item)
            newLabel(parent=rowFrame.frame, text = item, column = column, row = 1)
            column = column + 1
        rowNo = rowNo +1

def queueRows(rowId): #adds row id's to selectedQueue, preparing for deletion or editing
    try:
        ldeleteQueue = globals()["selectedQueue"]
        if rowId not in ldeleteQueue: 
            ldeleteQueue.append(rowId)                 
        elif rowId in ldeleteQueue:
            ldeleteQueue.remove(rowId)
    except ValueError as error:
        print("error in queueRows: " + error)

def deleteSelected(mainframe): #deletes all rows from the table based on id's store in selectedQueue
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

def headerRow(parent): #creates headers for table columns
    columns = globals()["columns"]
    noId = columns[1:]
    header = tileFrame(parent,row=1, column=1)
    tk.Label(header.frame, text= '', width=3).grid(column= 1, row= 1, padx=5, pady=1, sticky='W')
    columnNo = 2
    for item in noId:
        newLabel(header.frame,item,columnNo,1)
        columnNo = columnNo +1

def addColumn(): #form for a user to add columns to the table VIA the UI
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
            refreshPage(globals()['mainframe'].mainframe)
            print("column added successfully!")
        tk.Label(newWindow, text= "New Column").grid(row=2, column=3, sticky= (tk.N,tk.W))
        tk.Entry(newWindow,width= 20, textvariable=entry).grid(row=2, column=2)
        saveButton = tk.Button(newWindow, text="save", command=lambda: applyColumn())
        saveButton.grid(row=1, column=3)
    except ValueError as error:
        print("error in addColumn: " + error)


def refreshPage(frame,params = ''): #used to refresh data on screen when changes are made
    child_frames = frame.winfo_children()
    for child_frame in child_frames:
        child_frame.destroy()
    headerRow(frame)
    generateTiles(frame,params)
    globals()["selectedQueue"] = []

def newSort(frame, sortby): #sorting feature so a user may order data shown based on any preffered column. 
    try:
        if sortby == globals()['sortToggle'][1]:
            if globals()['sortToggle'][0] == 'ASC':
                globals()['sortToggle'][0] = 'DESC'
            else:
                globals()['sortToggle'][0] = 'ASC'
        else:
            globals()['sortToggle'][1] = sortby
            globals()['sortToggle'][0] = 'ASC'
        params = 'ORDER BY ' + sortby + ' ' + globals()['sortToggle'][0]
        refreshPage(frame,params)
    except ValueError as error:
        print("error in newSort: "+ error)

def editRow(): #form to allow a row to be edited after creation
    try:
        if len(selectedQueue) != 1: #editing can only be performed on one row at a time
            messagebox.showerror("showerror", "Please ensure you have one(1) row selected before editing.")
        else:
            data = sql.tableQuery(table,sql.all," id = "+str(selectedQueue[0])+"",globals()["cur"])
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
            
            def saveRow(cur,con,mainframe): #store the values currently in the form, overwritting the previous data
                try:
                    values = [data[0][0]]
                    for column in listInfo:
                        if column == 'date':
                            date = listInfo['date'].get()
                            if dm.validateDate(date) != 1:
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
                        + sets + " WHERE id = " + str(values[0])           
                    cur.execute(query)
                    con.commit()
                    newWindow.destroy()
                    refreshPage(mainframe)
                    print("Row Edited successfully!")
                except ValueError as error:
                  print(error)

        saveButton = tk.Button(newWindow, text="save", command=lambda: saveRow(cur,con,mainframe.mainframe))
        saveButton.grid(row=1, column=3)
    except ValueError as error:
        print("Error in editRow: " + error)
