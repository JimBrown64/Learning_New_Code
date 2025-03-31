import sqlite3
import tkinter as tk
import sys
import os
import raw_data
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from utilities import sql_interactions as sql,gui



def connect():
    connection = sqlite3.connect('python_projects/dm_buddy/app.db')
    return connection

def verify_tables(cursor,connection):
    """checks if tables exists, if they don't, creates a them"""
    for table, column_set in raw_data.table_list.items():
        if sql.tableCheck(table,cur) != 1:
            columns = ",".join(column_set)
            sql.tableConstructor(table,cursor,connection,columns)
            print("Table ",table," created!")
        else:
            print("table confirmed.")


con = connect()
cur = con.cursor()
verify_tables(cur,con)

# root = tk.Tk()
# gui.loadRoot(root)
# root.geometry("600x300")
# root.title("House Finance Tracker")
# mf = gui.mainFrame(root)
# mf.menuBar()
# gui.loadMainframe(mf)
# gui.headerRow(mf.mainframe)
# gui.generateTiles(mf.mainframe)

# root.mainloop()
