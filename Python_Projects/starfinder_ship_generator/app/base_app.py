import sqlite3

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import utilities.sql_interactions as sql
import bootup


def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return(con)

def verifyTables(): #checks if tables exists, if it doesn't, 
    #creates a new one and sets a row into the table as a placeholder
    for table in bootup.tableList:
        if sql.tableCheck(table,cur) != 1:
            columns = ",".join(bootup.tableList[table])
            sql.tableConstructor(table,cur,con,columns)
            print("Table ",table," created!")
        else:
            print("table confirmed.")

con = connect()
cur = con.cursor()
verifyTables()





