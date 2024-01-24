import sqlite3
import datetime
import sql_interactions as sql
from tkinter import *
import tracker_base as tb
today = datetime.date.today()
year = today.year
columns = ["Apple","Cherry","Math","Asparagus"]

def connect():
    con = sqlite3.connect("testdb.db")
    print("connection successful")
    return(con)


def test():
    print(0)

def test2():
    print(1)



con = connect()
cur = con.cursor()

root = Tk()
root.title("House Finance Tracker")


root.mainloop()