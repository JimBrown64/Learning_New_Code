# revisit at a later date.... need to learn how to work with classes


import tkinter as tk




# menubar tools
#-------------------------------------------------------------------------------------------
class menuBar(): #creates a master menu bar, populating in the window that is {parent}
    def __init__(self, parent,tk):
        tk.Menu(parent)

class newMenu(): #creates a menu tab called {label}, and assigns it {self} to the {parent} (ex. 'file', 'help', or 'tools')
    def __init__(self, parent, label):
        tk.Menu(parent, tearoff=0)
        parent.add_cascade(label = label, menu = self)

class menuItem(): #adds items to a dropdown in the menu (ex. 'edit' under 'file')
    def __init__(self, parent, label, command):
        parent.add_command(label= label, command= command)
#---------------------------------------------------------------------------------------------
#menubar tools

def test():
    print(0)


root = tk.Tk()

menubar = tk.Menu(root)#menuBar(root,tk)
fileMenu = newMenu(menubar,"File")
# fileMenu = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label="File", menu=fileMenu)
testItem = menuItem(fileMenu,"test",test)
#fileMenu.add_command(label="test", command=test)

root.config(menu=menubar)
root.mainloop()