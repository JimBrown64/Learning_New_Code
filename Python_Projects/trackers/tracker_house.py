import sqlite3
import datetime
import tracker_base as tb
import tkinter as tk
import sql_interactions as sql
today = datetime.date.today()
year = today.year
table = "house_tracker"
columnList = ["date", "service", "amount", "source", "check_number"]


def connect(): #create connection to the database, if it doesn't exist, will create a new one of the same name.
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)

def verifyTable(): #checks if table exists, if it doesn't, creates a new one and sets a row into the table as a placeholder
    if sql.tableCheck(table,cur) != 1:
        list = str(columnList).strip("[]")
        sql.tableConstructor(table,cur,con,list)
        sql.tableInsert(table,"id, "+ list,"0, '01/01/2020', 'initial_setup', 0, 'Admin', 'na'", cur, con)
        print("initial setup successful!")
    else:
        print("table confirmed.")


con = connect()
cur = con.cursor()
verifyTable()
tb.loadTableName(table)
tb.loadColumns(table,cur)
tb.loadConnection(con)

root = tk.Tk()
tb.loadRoot(root)
root.geometry("600x300")
root.title("House Finance Tracker")
mf = tb.mainFrame(root)
mf.menuBar()
tb.loadMainframe(mf)
tb.headerRow(mf.mainframe)
tb.generateTiles(mf.mainframe)

root.mainloop()