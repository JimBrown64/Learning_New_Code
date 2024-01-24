import sqlite3
import datetime
import sql_interactions as sql
import tkinter as tk 
import date_management as dm

today = datetime.date.today()
year = today.year

columns = ["Apple", "Spaghetti","Tuna"]
deleteQueue = []

def connect():
    con = sqlite3.connect("testdb.db")
    print("connection successful")
    return(con)


def test():
    print(0)

def test2():
    print(1)

# def addRow(table):
#     try:
#         date = tk.StringVar()
#         service = tk.StringVar()
#         amount = tk.StringVar()
#         source = tk.StringVar()
#         check = tk.StringVar()
#         def saveNewRow(*args):
#             try:
#                 validDate = dm.validateDate(date.get())
#                 if validDate == 0:
#                     cur = globals()["cur"]
#                     listColumns = []
#                     pullColumns = sql.tableQuery(table,"*","", cur)
#                     data = cur.execute(pullColumns)
#                     for column in data.description:
#                         listColumns = listColumns + column[0]

#                     listColumns = str(listColumns).strip("[]")                   
#                     pullId = sql.tableQuery(table,"MAX(id)","",cur)#"SELECT MAX(id) + 1 FROM house_tracker;"
#                     cur.execute(pullId)
#                     newId = cur.fetchone()[0]
#                     sql.tableInsert(table,listColumns)
#                     # insertStatement = """INSERT INTO house_tracker(id, date, service, amount, source, check_number)
#                     #         VALUES(""" + str(newId) + """, '""" + date.get() + """', '""" + service.get() + """',
#                     #             """+ amount.get() + """, '""" + source.get() + """', '""" + check.get() + """')"""
#                     # cur.execute(insertStatement)
#                     # con.commit()
#                     globals()["mf"] = mainFrame(root)
#                     #newWindow.destroy()
#                     print("new row inserted successfully!")
#                 else:
#                     print("derp")
#                     # tk.messagebox.showerror("showerror", "Please enter a valid date in 'MM/DD/YYYY' format.")
#             except ValueError as error:
#                 print(error)

#         newWindow = tk.Toplevel(root)
#         tk.Label(newWindow, text="           ").grid(row=1, column=1)
#         tk.Label(newWindow, text = "Please Enter New Row").grid(row=1, column=2)
#         tk.Entry(newWindow,width= 20, textvariable=date).grid(row=2, column=2, sticky= (tk.N,tk.W,tk.E,tk.S))
#         tk.Label(newWindow, text= "Date").grid(row=2, column=3, sticky= (tk.N,tk.W,tk.E,tk.S))
#         tk.Entry(newWindow,width= 20, textvariable=service).grid(row=3, column=2)
#         tk.Label(newWindow, text= "Service").grid(row=3, column=3, sticky= (tk.N,tk.W,tk.E,tk.S))
#         tk.Entry(newWindow,width= 20, textvariable=amount).grid(row=4, column=2)
#         tk.Label(newWindow, text= "Amount").grid(row=4, column=3, sticky= (tk.N,tk.W,tk.E,tk.S))
#         tk.Entry(newWindow,width= 20, textvariable=source).grid(row=5, column=2)
#         tk.Label(newWindow, text= "Source").grid(row=5, column=3, sticky= (tk.N,tk.W,tk.E,tk.S))
#         tk.Entry(newWindow,width= 20, textvariable=check).grid(row=6, column=2)
#         tk.Label(newWindow, text= "Check #").grid(row=6, column=3, sticky= (tk.N,tk.W,tk.E,tk.S))
#         saveButton = tk.Button(newWindow, text="save", command=saveNewRow)
#         saveButton.grid(row=1, column=3)
#     except ValueError as error:
#         print("error in insertButton: " + error)

class mainFrame():
    def __init__(self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W),padx=5, pady=5)

    def menuBar(self):
        root = self.root
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New Row...", command = test)
        filemenu.add_command(label = "Delete Rows", command = test2)
        root.config(menu = menubar)

class tileFrame():
    def __init__(self,parent,row,column):
        self.parent = parent
        self.frame = tk.Frame(parent, bd = 4, relief=tk.GROOVE)#, bg='lightgrey')
        self.frame.grid(column= column, row= row, sticky=tk.W)    
        #self.frame.pack(padx=0,pady=3,sticky = )

def newLabel(parent, text, column, row):
    try:
        label = tk.Label(parent, text= text).grid(column= column, row= row, padx=5, pady=1)
    except ValueError as error:
        print("Error in newLabel: " + error)

def createCheckbox(parent,column,row, name):
    parent.checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(parent,name=name, variable=parent.checkbox_var, command= lambda: queueDelete(name))
    checkbox.grid(column= column, row= row, padx=5, pady=1)

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


def headerRow(parent,columns):
    header = tileFrame(parent,row=1, column=1)
    newLabel(header.frame,"     ",1,1)
    columnNo = 2
    for item in columns:
        newLabel(header.frame,item,columnNo,1)
        columnNo = columnNo +1

    # def onClose():
    #     try:
    #         globals()["con"].close()
    #         globals()["root"].destroy()
    #     except ValueError as error:
    #         print("Error in onClose: " + error)


con = connect()
cur = con.cursor()

root = tk.Tk()
root.geometry("600x300")
root.title("House Finance Tracker")
mf = mainFrame(root)
mf.menuBar()
headerRow(mf.mainframe,columns)
testframe = tileFrame(mf.mainframe,2,1)
additionalframe = tileFrame(mf.mainframe,3,1)
checkbox1 = createCheckbox(testframe.frame,column=1,row=1,name = "1")
checkbox2 = createCheckbox(additionalframe.frame,column=1,row=1, name = "2")
newLabel(parent=testframe.frame, text = "column1", column = 2, row = 1)
newLabel(parent=additionalframe.frame, text = "column1", column = 2, row = 1)
newLabel(parent=testframe.frame, text = "column2", column = 3, row = 1)
newLabel(parent=additionalframe.frame, text = "column2", column = 3, row = 1)


root.mainloop()
        


