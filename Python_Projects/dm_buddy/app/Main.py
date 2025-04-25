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

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "logo.png")

bgcolor = 'light gray'


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
table_names = [row[0] for row in sql.tableQuery("sqlite_master","name","type = 'table'",cur)]
print(table_names)
root = tk.Tk()
root.title('DM Buddy')
icon = tk.PhotoImage(file=icon_path)  # Ensure the file path is correct
root.iconphoto(True, icon)  # Apply the icon to the window
mf = gui.MainFrame(root)
# dropdown_frame = gui.TileFrame(mf,1,1,1,tk.FLAT,bgcolor)
# dropdown_frame.create_dropdown(table_names,1,1,'derp')
# form = gui.NewWindow(root,bgcolor)
form = gui.TileFrame(mf,1,1,1,tk.FLAT,bgcolor)
form.new_entry_field(1,"test")
form.new_button("Save",3,3)

root.mainloop()
