"""used to unit test"""


import tkinter as tk
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from utilities import sql_interactions as sql,gui



faux_table = ['Spaghetti','Meatballs','Cheese','asparagus','tuna','matcha','bread','duck',
              'goose','sirloin','zuchini','sausage','pastrami','eggs']
faux_table2 = ['Spaghetti','Meatballs','Cheese','asparagus','tuna','matcha','bread','duck',
              'goose','sirloin','zuchini','sausage','pastrami','eggs']
bgcolor = 'light blue'
size = "400x300"


root = tk.Tk()
root.title("test window")
root.geometry(size)
mf = gui.MainFrame(root)
# testFrame = gui.TileFrame(mf,2,2,tk.RAISED,bgcolor).frame
baseY = 2
baseX = 2
identifier = 1
options = ['Toss','New','Used','Accident']
frames = []

tileFrame = gui.TileFrame(mf,identifier,baseY,2,tk.SUNKEN,bgcolor)
tileFrame.create_table(baseX,baseY,['Column1'],faux_table)
# for item in faux_table:
#     tile = gui.TileFrame(mf,identifier,baseY,2,tk.RAISED,bgcolor)
#     tile.new_label( item,2,2,0)
#     tile.create_checkbox(3,2,str(identifier))
#     tile.create_dropdown(options,4,2)
#     frames.append(tile)
#     baseY+=1
#     identifier+=1
# for item in faux_table2:
#     gui.new_label(testFrame, item,baseX,2,bgcolor,0)
#     baseX+=1
root.mainloop()



# SELECT name FROM sqlite_master WHERE type = 'table' order by name