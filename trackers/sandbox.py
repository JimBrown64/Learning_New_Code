# import sqlite3
# import datetime
# import sql_interactions as sql
# import tracker_base as tb
# import tkinter as tk
# import tracker_base as tb
import date_management as dm
import calendar

def monthRange(year,month,testNumber):
    rawRange = calendar.monthcalendar(year,month)
    range = []
    for list in rawRange:
        for item in list:
            if item != 0:
                range.append(item)
    print(range)
    if testNumber not in range:
        print("not a day of the month")
    elif testNumber in range:
        print("is a day of the month")

monthRange(2023,1,32)