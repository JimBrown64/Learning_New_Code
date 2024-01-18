import sqlite3

select = "SELECT"
insert = "INSERT"
delete = "DELETE"
all = "*"
add = " ADD "
drop = " DROP COLUMN "


def tableCheck(table,cur): #checks if there is a table called {table}, returning false(0) if there is not, or true(1) if there is
    try:
        output = 0
        tableCheck = "SELECT 1 FROM SQLITE_SCHEMA WHERE name = '" + table + "' AND type = 'table'"
        cur.execute(tableCheck)
        tableResult = cur.fetchall()
        if tableResult != []:
            output = 1
        else: output = 0
        return output
    except ValueError as error:
        print("error in tableCheck: " + error)

# def queryConstructor(table, action, target,conditions):
#     try:
#         if action == select:
#             if (conditions is None or conditions == ""):
#                 query = action +" "+ target + " FROM " + table + " WHERE id != 0"
#             else:
#                 query = action +" " + target + " FROM " + table + " WHERE id != 0 AND " + conditions 
#         elif action == insert:
#             if (conditions is None or conditions == "" or target is None or target ==""):
#                 print("please enter valid values")
#             else:
#                 query = action + " INTO " + table + "(" + target + ")" + " VALUES(" + conditions + ")"
#         elif action == delete:
#             if (conditions is None or conditions == ""):
#                  query = action + " FROM " + table + " WHERE " + conditions
#             else:
#                 query = action + " FROM " + table + " WHERE " + conditions
#         return query
#     except ValueError as error:
#         return("error in queryConstructor: " + error)

def tableQuery(table, target, conditions, cur): #returns the result of the query requested.
    try:
        if (conditions is None or conditions == ""):
            query =  "SELECT "+ target + " FROM " + table #+ " WHERE id != 0"
        else:
            query = "SELECT " + target + " FROM " + table + " WHERE " + conditions 
        cur.execute(query)
        result = cur.fetchall()
        return result
    except ValueError as error:
        print("Error in tableQuery: " + error)
        return 0
    
def tableDelete(table, conditions, cur, con): #deletes items where CONDITIONS are met from TABLE 
    try:
        if (conditions is None or conditions == ""):
            query = "DELETE FROM " + table
        else:
            query = "DELETE FROM " + table + " WHERE " + conditions
        cur.execute(query)
        con.commit()                         #commit is built in. Always check data before running.
        print("Delete successful.")
        return 1
    except ValueError as error:
        print(error)
        return 0

def tableInsert(table, columns, values, cur, con): #inserts new row into {table}, using the {columns} and {values} provided.
    try:
        if (values is None or values == "" or columns is None or columns ==""):
            print("please enter valid values")
        else:
            query = "INSERT INTO " + table + "(" + columns + ")" + " VALUES(" + values + ")"
        cur.execute(query)
        con.commit()                         #commit is built in. Always check data before running.
        print("Row inserted successfully!")
        return 1
    except ValueError as error:
        print("Error in tableInsert: " + error)
        return 0



def tableConstructor(tableName, cur, con, columns):
    try:
        tableConstruction = "CREATE TABLE " + tableName + " (" + columns + ")"
        cur.execute(tableConstruction)
        con.commit()
    except ValueError as error:
        return("error in tableConstructor: " + error)

def editTable(table, cur, con, action, column):
    try:
        edit = "ALTER TABLE" + table + action + column
        print(edit)
        cur.execute(edit)
        con.commit()
        print("Column "+ column + " altered successfully!")
    except ValueError as error:
        return("error in editTable: " + error)
    
