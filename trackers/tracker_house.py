import sqlite3
import datetime
import sql_interactions as sql
import tracker_base as tb
import tkinter as tk
import tracker_base as tb
today = datetime.date.today()
year = today.year
table = "house_tracker"


def connect():
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)



con = connect()
cur = con.cursor()
tb.loadTableName(table)
tb.loadColumns(table,cur)
tb.loadConnection(con)
root = tk.Tk()
tb.loadRoot(root)
root.geometry("600x300")
root.title("House Finance Tracker")
mf = tb.mainFrame(root)
mf.menuBar()
tb.headerRow(mf.mainframe)
tb.generateTiles(mf.mainframe)

root.mainloop()