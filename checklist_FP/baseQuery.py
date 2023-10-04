import sqlite3

try:
    con = sqlite3.connect("appdb.db")
    cur = con.cursor()
    print("Successfully Connected to app")

    query = """SELECT * FROM checklist"""
    cur.execute(query)
    result = cur.fetchall()
    print("row count: ", len(result))
    for row in result:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print("\n")
    
    cur.close()

except con.Error as error:
    print("failed to read data", error)
finally:
    if con:
        con.close()
        print("connection closed")
# try:
#     con = sqlite3.connect("appdb.db")
#     cur = con.cursor()
#     print("Successfully Connected to app")

#     insert = """INSERT INTO checklist (task_id,priority_level, task, steps)
#                  VALUES
#                  (0,1,'something','testing')"""
#     endResult = cur.execute(insert)
#     con.commit()
#     print("Record inserted successfully",cur.rowcount)
#     cur.close()
# except sqlite3.Error as error:
#     print("failed to insert", error)
# finally:
#     if con:
#         con.close()
#         print("Connection closed")
# def query():
#     cur.execute("""SELECT * FROM checklist""")
#     result = cur.fetchall()
#     if result is None:
#         result = "nothing to return"
#     print(result)

# def insert():
#     cur.execute("""INSERT INTO checklist (task_id,priority_level, task, steps)
#                 VALUES
#                 (0,1,'something','testing')""")
#     con.commit
#     print("insert complete")
# query()
# #insert()