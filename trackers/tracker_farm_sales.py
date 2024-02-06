import sqlite3
import datetime
import tracker_base as tb
import tkinter as tk
import sql_interactions as sql
today = datetime.date.today()
year = today.year
table = "farm_sales_tracker"
columnList = ["date", "product", "quantity", "customer", "dollar_amount", "contact_info", "location"]


def connect():
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)

def verifyTable():
    if sql.tableCheck(table,cur) != 1:
        list = str(columnList).strip("[]")
        sql.tableConstructor(table,cur,con,list)
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
root.title("Farm Sales Tracker")
mf = tb.mainFrame(root)
mf.menuBar()
tb.headerRow(mf.mainframe)
tb.generateTiles(mf.mainframe)

root.mainloop()