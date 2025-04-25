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

class TabbedWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Vertical Tabs Example")
        self.root.geometry("500x400")

        # Create a custom style for larger and left-side tabs
        style = ttk.Style()
        style.configure("TNotebook", tabposition="wn")  # 'w' = Left, 'n' = Top alignment
        style.configure("TNotebook.Tab", padding=(20, 10), font=("Arial", 12))  # Increase tab size

        # Create the Notebook (Tab Container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # Create Tabs
        self.create_tabs()

    def create_tabs(self):
        """Creates tabs in the Notebook"""
        # Tab 1
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Tab 1")
        self.setup_tab(self.tab1, "This is Tab 1")

        # Tab 2
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Tab 2")
        self.setup_tab(self.tab2, "This is Tab 2")

        # Tab 3
        self.tab3 = tk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Tab 3")
        self.setup_tab(self.tab3, "This is Tab 3")

    def setup_tab(self, tab, text):
        """Sets up content for each tab"""
        label = tk.Label(tab, text=text, font=("Arial", 12))
        label.pack(pady=20)

# Run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = TabbedWindow(root)
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


