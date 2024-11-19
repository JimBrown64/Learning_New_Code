"""Module to utilize other app components to build a ship"""
import sqlite3
#import random
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
import app.raw_data
import app.starship_selection_ai as ai
from app.sql_statement_placeholder import query_construction as statement
import utilities.sql_interactions as sql


def connect():
    """create connection to database"""
    connection = sqlite3.connect('python_projects/starfinder_ship_generator/app.db')
    return connection

def verify_tables():
    """checks if tables exists, if they don't, creates a them"""                
    for table, column_set in app.raw_data.table_list.items():
        if sql.tableCheck(table,cur) != 1:
            columns = ",".join(column_set)
            sql.tableConstructor(table,cur,con,columns)
            print("Table ",table," created!")
        else:
            print("table confirmed.")

class CollectedData():
    """collect data to be utilized by selection AI"""
    def __init__(self,conditions,cursor):
        self.conditions = conditions
        self.cursor = cursor
        self.ship_collection = []
        self.stat_averages = []
        self.converted_values = []

    def get_ship_list(self):
        """pulls list of ships"""
        try:
            self.cursor.execute(statement(self.conditions))
            lship_list = self.cursor.fetchall()
            return lship_list
        except ValueError as error:
            print('error in function: ', error)
            return None

    def get_average(self,llist, column_index):
        """averages items from the same column in a query result"""
        try:
            ltotal = 0
            lcount = 0
            for item in llist:
                ltotal = ltotal + item[column_index]
                lcount += 1
            laverage = ltotal/lcount
            return laverage
        except ValueError as error:
            print("error in get_average: ", error)
            return None

    def convert_values(self):
        """convert raw values to represent above, below or at average"""
        collected_values = []
        cur_row = 0
        for row in self.ship_collection:
            collected_values.append([])
            print("test: ", cur_row)
            index = 0
            for item in row:
                if item > self.stat_averages[index]:
                    collected_values[cur_row].append(1)
                elif item < self.stat_averages[index]:
                    collected_values[cur_row].append(-1)
                else:
                    collected_values[cur_row].append(0)
                index += 1
            cur_row += 1
        return collected_values

    def assign(self):
        """populate collected data values"""

        #collect ship list
        self.ship_collection = self.get_ship_list()

        #collect averages used in determining ship quality
        index = 0
        while index < len(self.ship_collection[0]):
            self.stat_averages.append(self.get_average(self.ship_collection,index))
            index += 1

        #build list of where stats exist in relation to the average
        self.converted_values = self.convert_values()




con = connect()
cur = con.cursor()
COND = """tier.tier = 1
            AND frame.Maximum_crew >= 4
            AND mount_quantity > 1
            AND remaining_bp > 25
            AND power_core.PCU > 100"""
verify_tables()
data_set = CollectedData(COND,cur)
data_set.assign()
agent = ai.agent
agent.actions = data_set.converted_values
print("ship collection: ",data_set.ship_collection[0])
print("collected averages: ", data_set.stat_averages)
print("converted values: ",data_set.converted_values[0])
