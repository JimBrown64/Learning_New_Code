import sqlite3
#import utlities.sql_interactions as sql
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# print('Chili\'s')

# def connect():
#     lcon = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
#     return lcon
# con = connect()
# cur =con.cursor()
import tkinter as tk
from tkinter import ttk

def display_data():
    # Simulated data from an SQL database (list of tuples)
    data = [
        (1, "Alice", "Engineer"),
        (2, "Bob", "Designer"),
        (3, "Charlie", "Manager"),
    ]

    # Clear existing data in the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert new data into the treeview
    for row in data:
        tree.insert("", tk.END, values=row)

# Create main window
root = tk.Tk()
root.title("SQL Table Display")
root.geometry("400x300")

# Create a frame to hold the table
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Define table columns
columns = ("ID", "Name", "Role")

# Create Treeview widget
tree = ttk.Treeview(frame, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)  # Set column headings
    tree.column(col, anchor="center", width=100)  # Center text and set width

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the table
tree.pack(fill=tk.BOTH, expand=True)

# Button to refresh data
btn_refresh = tk.Button(root, text="Load Data", command=display_data)
btn_refresh.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()















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

# def insertFrames():
#     # text = ''
    
#     columns = "'"+'"'+'","'.join(bootup.tableList["Frames"])+'"'+"'" 
#     for row in data.frameValues:
#         newRow = ','.join(row)
#         newInsert = 'sql.tableInsert("Frames",'+ columns+',"'+ newRow +'",cur,con)'
        # print(newInsert)
        # exec(newInsert)
        #text = text + newInsert
    #return text
     
# insertFrames()

# def printOptions():
#     alt_Statement =  "SELECT  tier.build_points AS BP, \
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
#     cur.execute(alt_Statement)
#     result = cur.fetchall()
#     return str(result)
# file = open("Python_Projects/starfinder_ship_generator/utilities/ship_options.txt", "w")
# file.write( printOptions())
# file.close()   


