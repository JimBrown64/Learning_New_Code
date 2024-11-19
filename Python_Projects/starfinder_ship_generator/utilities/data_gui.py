import tkinter as tk
import sql_interactions as sql
import sqlite3
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from app.sql_statement_placeholder import query_construction as statement

table = "Tier"
columns = []
COND = """tier.tier = 1
            AND frame.Maximum_crew >= 4
            AND mount_quantity > 1
            AND remaining_bp > 25
            AND power_core.PCU > 100"""
alt_Statement = statement(COND)#"SELECT * FROM thrusters;"
# alt_Statement = "SELECT * FROM frame_mounts WHERE frame_id = 3"
# alt_Statement = "SELECT  tier.build_points AS BP, \
#                     Frame.name,size.size, \
#                     mount_totals.weight AS mount_weight, mount_totals.mount_count AS mount_quantity, \
#                     maneuverability.maneuverability, \
#                     frame.expansion_bays, \
#                     power_core.name AS power_core_name, power_core.pcu, \
#                     thrusters.name AS thruster_name, \
#                     (tier.build_points - Frame.cost - power_core.cost - thrusters.cost) AS remaining_bp\
#                 FROM Frame \
#                 JOIN (SELECT SUM(frame_mounts.count) AS mount_count,frame_mounts.weight,frame_mounts.frame_id \
#                      FROM frame_mounts \
#                      GROUP BY frame_mounts.frame_id,frame_mounts.weight)AS mount_totals ON Frame.id = mount_totals.frame_id \
#                 JOIN maneuverability ON Frame.maneuverability = maneuverability.id \
#                 JOIN Tier ON Frame.Cost < Tier.Build_Points \
#                 JOIN size ON Frame.size = size.id \
#                 JOIN power_core ON power_core.id = power_core_size.power_core_id \
#                 JOIN power_core_size ON Frame.size = power_core_size.size \
#                 JOIN thrusters ON Frame.size = thrusters.size \
#                 WHERE tier.tier = 1 \
#                     AND frame.Maximum_crew >= 4 \
#                     AND mount_quantity > 1 \
#                     AND remaining_bp > 25 \
#                     AND power_core.PCU > 100 \
#                 ;"

def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return con

class mainFrame(): 
    """class used to create the main window, with primary needed functions attached"""
    def __init__(self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0, row=1, sticky=(tk.N, tk.W),padx=5, pady=5)


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
    if globals()["alt_Statement"] == "":
        pullColumns = "SELECT * FROM " + table
    else:
        pullColumns = globals()["alt_Statement"]
    data = cur.execute(pullColumns)
    for column in data.description:
        listColumns.append(str(column[0]))
    globals()["columns"] = listColumns


con = connect()
cur = con.cursor()

# cur.execute(alt_Statement)
# print(cur.fetchall())
root = tk.Tk()
root.geometry("600x300")

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.grid(column= 0, row =0)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.grid(column=0, row=1)
# canvas.pack(fill=tk.BOTH, expand=True)
scrollbar.config( command=canvas.yview)
mf= mainFrame(canvas)
loadColumns(table,cur)
headerRow(mf.mainframe)
generateTiles(mf.mainframe,cur)
mf.mainframe.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))
root.mainloop()