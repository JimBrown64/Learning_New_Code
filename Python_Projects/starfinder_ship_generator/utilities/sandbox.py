import sqlite3
import sql_interactions as sql
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import app.bootup as bootup

def connect():
    con = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return(con)

# def createText():
#     text =''
#     for table in bootup.tableList:
#         columns = '","'.join(bootup.tableList[table])
#         newInsert = 'sql.tableInsert("'+ table+'","'+ columns+'","'+ columns+'",cur,con)\n'
#         text = text + newInsert
#     return text
# file = open("Python_Projects/starfinder_ship_generator/utilities/inserts.txt", "w")
# file.write( createText())
# file.close()



