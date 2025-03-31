import tkinter as tk
from tkinter import ttk
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
import utilities.sql_interactions as sql
######################################################################
#temporary vars for testing
statement = ""
table = "NPCs"
columns = []
COND = ""
######################################################################
selectedQueue = []

class MainFrame():
    """class used to create the main window, with primary needed functions attached"""
    def __init__(self, root):
        self.root = root
        self.menu_bar()
        self.selection = []
        #create a Canvas that will hold everything in the app
        self.canvas = tk.Canvas(root)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        #create a vertical and horizontal scrollbar and configure them
        v_scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.h_scrollbar = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        #create the frame and window that will display the app
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        #bind the scrolling events to the frame
        self.frame.bind("<Configure>", lambda event, \
                canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))
        #ensure content is always the same size as the window
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        #enable mouse wheel to control scrollbar
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        """utility to allow scrollbars to be controlled with mousewheel"""
        if event.state & 0x0001:  # 0x0001 represents the Shift key (state bit mask)
            if event.delta > 0:
                self.canvas.xview_scroll(-1, "units")  # Scroll left
            else:
                self.canvas.xview_scroll(1, "units")  # Scroll right
        # Scroll the canvas based on the mouse wheel movement
        else:
            if event.delta > 0:
                self.canvas.yview_scroll(-1, "units")  # Scroll up
            else:
                self.canvas.yview_scroll(1, "units")  # Scroll down

    def menu_bar(self):
        """adds a menubar to the frame"""
        root = self.root
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff = 0)
        editmenu = tk.Menu(menubar, tearoff = 0)
        viewmenu = tk.Menu(menubar,tearoff= 0)
        # sortmenu = tk.Menu(viewmenu,tearoff= 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New Row...")#, \
                            # command = lambda :addRow(globals()["table"],\
                            #                         globals()["cur"],\
                            #                         globals()["con"],\
                            #                         globals()["root"],\
                            #                         self.frame))
        filemenu.add_command(label = "Delete Rows")
        #, command = lambda :deleteSelected(self.frame))
        menubar.add_cascade(label= "Edit", menu = editmenu)
        editmenu.add_command(label = "New Column")#, command = addColumn)
        editmenu.add_command(label = "Edit Row")#, command = editRow)
        menubar.add_cascade(label= "View")#, menu= viewmenu)
        viewmenu.add_cascade(label = "Sort By...")#, menu = sortmenu)
        root.config(menu = menubar)

class TileFrame():
    """Class used to create segments of information to display"""
    def __init__(self,parent,tile_id,cordy,cordx,border,color):
        #border options:
        #FLAT	No border.
        #RAISED	Appears raised (like a button).
        #SUNKEN	Appears sunken into the UI.
        #GROOVE	Creates a grooved (indented) border.
        #RIDGE	Creates a ridged (raised and lowered) border.
        self.parent = parent.frame
        self.id = tile_id
        self.color = color
        self.frame = tk.Frame(self.parent, bd = 4, relief=border,bg=self.color)
        self.frame.grid(column= cordx, row= cordy,padx=5,pady=5)
        self.checkbox_var = tk.BooleanVar()#defaults false
        self.selection = parent.selection

    def new_label(self, text, cordx, cordy,size_req):
        """adds a new text label"""
        try:
            info = text
            if size_req == 1:
                size =12
                if isinstance(text,str): #limit characters shown for improved readability
                    info = text[:size]

                def show_full_text():
                    """open a window to show the full text of a given element on the page"""
                    text_window =tk.Toplevel(self.parent.root,width=50, height=50)
                    text_window.title="Full Item"
                    text_frame = tk.Frame(text_window,width=50, height=50)
                    text_frame.grid(row=1, column=1)
                    full_text = tk.Label(text_frame,text= text, wraplength=300)
                    full_text.grid(row=2, column=2, padx=10, pady=10)

            label = tk.Label(self.frame, text= info, cursor="hand2", background=self.color)
            label.grid(column= cordx, row= cordy, pady=1,sticky= tk.W)
            label.bind("<Button-1>",lambda event:show_full_text())
        except ValueError as error:
            print("Error in new_label: " + error)

    def queue_selection(self,row_id):
        """utility function for checkboxes. removes or adds selections from queue"""
        try:
            lqueue = self.selection
            if row_id not in lqueue:
                lqueue.append(row_id)
                print('added!')
            elif row_id in lqueue:
                lqueue.remove(row_id)
                print('removed!')
            print(str(self.selection))
        except ValueError as error:
            print("error in queueRows: " + error)

    def create_checkbox(self,cordx,cordy, name):
        """creates a checkbox in the tile"""
        try:
            checkbox = tk.Checkbutton(self.frame,name=name, variable=self.checkbox_var,\
                    command= lambda: self.queue_selection(int(name)),background=self.color)
            checkbox.grid(column= cordx, row= cordy, padx=5, pady=1)
        except ValueError as error:
            print("error in queueRows: " + error)
    def on_select(self,func):
        """utility that takes in a specific case function and applies it to the display"""
        try:
            func()
        except ValueError as error:
            print("error in on_select: " + error)       

    def create_dropdown(self,options,cordx,cordy):
        """creates a dropdown menu providing {options} as possible selections"""
        self.selection = tk.StringVar()
        dropdown = tk.OptionMenu(self.frame,self.selection,*options,command= self.on_select)
        dropdown.grid(column= cordx, row=cordy)

    def create_table(self,cordx,cordy,columns,data):
        """creates a table to display information in the frame"""
        # Create Treeview widget
        tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        tree.grid(column=cordy, row=cordx)
        
        datarows = tree.get_children()
        if datarows:
            for row in tree.get_children():
                tree.delete(row)

        # Insert new data into the treeview
        for row in data:
            tree.insert("", tk.END, values=row)
        # Define column headings
        for col in columns:
            tree.heading(col, text=col)  # Set column headings
            tree.column(col, anchor="e", width=100) 

