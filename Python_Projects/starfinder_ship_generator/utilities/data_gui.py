import tkinter as tk
import sql_interactions as sql
import sqlite3


table = "Frames"
columns = []
alt_Statement = ""

def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return con

class mainFrame(): #class used to create the main window, with primary needed functions attached
    def __init__(self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W),padx=5, pady=5)

    # def menuBar(self): #adds a menubar to the mainFrame
    #     root = self.root
    #     menubar = tk.Menu(root)
    #     filemenu = tk.Menu(menubar, tearoff = 0)
    #     editmenu = tk.Menu(menubar, tearoff = 0)
    #     viewmenu = tk.Menu(menubar,tearoff= 0)
    #     sortmenu = tk.Menu(viewmenu,tearoff= 0)
    #     menubar.add_cascade(label = "File", menu = filemenu)
    #     filemenu.add_command(label = "New Row...", \
    #                          command = lambda :addRow(globals()["table"],\
    #                                                   globals()["cur"],\
    #                                                   globals()["con"],\
    #                                                   globals()["root"],\
    #                                                   self.mainframe))
    #     filemenu.add_command(label = "Delete Rows", command = lambda :deleteSelected(self.mainframe))
    #     menubar.add_cascade(label= "Edit", menu = editmenu)
    #     editmenu.add_command(label = "New Column", command = addColumn)
    #     editmenu.add_command(label = "Edit Row", command = editRow)
    #     menubar.add_cascade(label= "View", menu= viewmenu)
    #     viewmenu.add_cascade(label = "Sort By...", menu = sortmenu)

    #     for column in columns[1:]:
    #         sortmenu.add_command(label= column, command= lambda col = column: newSort(self.mainframe,col))    
       
    #     root.config(menu = menubar)

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
    checkbox = tk.Checkbutton(parent,name=name, variable=parent.checkbox_var)
    checkbox.grid(column= column, row= row, padx=5, pady=1)

def generateTiles(frame,cur,params=''): #gathers data from the table and creates a row tile for each row in the table
    if globals()["alt_Statement"] == "":
        data = sql.tableQuery(table,"*",""+ params,cur)
    else:
        cur.execute(globals()["alt_Statement"])
        data = cur.fetchall()
    rowNo = 2
    for row in data:
        rowFrame = tileFrame(frame,rowNo,1)
        createCheckbox(rowFrame.frame,column=1,row = 1,name = str(row[0]))
        column = 2
        for item in row: #ignores the first item, which is id
            # if item is not None and isinstance(item,int) is False and re.search("..../../..",item) is not None: #if the item is a date, convert to easier to read version
            #     item = dm.displayFormat(item)
            newLabel(parent=rowFrame.frame, text = item, column = column, row = 1)
            column = column + 1
        rowNo = rowNo +1

def headerRow(parent): #creates headers for table columns
    columns = globals()["columns"]
    noId = columns
    header = tileFrame(parent,row=1, column=1)
    tk.Label(header.frame, text= '', width=3).grid(column= 1, row= 1, padx=5, pady=1, sticky='W')
    columnNo = 2
    for item in noId:
        newLabel(header.frame,item,columnNo,1)
        columnNo = columnNo +1

def loadColumns(table,cur): #gets the column names from the table
    listColumns = []
    pullColumns = "SELECT * FROM " + table
    data = cur.execute(pullColumns)
    for column in data.description:
        listColumns.append(str(column[0]))
    globals()["columns"] = listColumns


con = connect()
cur = con.cursor()


root = tk.Tk()
root.geometry("600x300")
mf= mainFrame(root)
loadColumns(table,cur)
headerRow(mf.mainframe)
generateTiles(mf.mainframe,cur)

root.mainloop()