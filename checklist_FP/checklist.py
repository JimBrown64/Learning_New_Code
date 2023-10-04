import sqlite3


def connect():
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)

def query(connection):
    try:
        con = connection
        cur = con.cursor()
        query = """SELECT priority_level,complete,task,steps FROM checklist ORDER BY priority_level ASC"""
        cur.execute(query)
        result = cur.fetchall()
        print("Row count: ", len(result))
        print("priority level|  complete?  |       task      |steps")        
        for row in result:
            print("      " + row[0] + "       |     " + row[1] + "       |   " + row[2] + "    |    " + row[3] + "\n")
        cur.close()
    except con.Error as error:
        print("failed to read data: ",error)

def insert(connection):
    try:
        con = connection
        cur = con.cursor()
        collectId = """SELECT MAX(task_id)+1 FROM checklist"""
        cur.execute(collectId)
        newTaskId = str(cur.fetchall()).strip('[](),')
        if newTaskId == 'None':
            newTaskId = '1'
            print("no prior tasks, task id set to 1")
        priority = input("What priority level would you like this set to? (numeric, typically a scale of 1(most important)to 5(least important))")
        task = "'" + input("What is the task at hand?") + "'"
        steps = "'" + input("What steps are required for this task? (list format, seperate with commas)") + "'"
        statement = """INSERT INTO checklist(task_id, complete, priority_level, task, steps)
                       VALUES(""" + newTaskId + """, 'N', """ + priority + """, """ + task + """, """ + steps + """
                        ) """
        cur.execute(statement)
        con.commit()
        print("Record inserted succesfully")
        cur.close()
    except con.Error as error:
        print("failed to read data: ", error)

def deleteAll(connection):
    try:
        con = connection
        cur = con.cursor()
        confirm = input("Are you sure you want to clear the table?(This cannot be undone!)")
        if confirm.upper() in ['Y','YES']:
            cur.execute("""DELETE FROM checklist""")
            con.commit()
            print("Table has been cleared")
            cur.close()
        else:
            cur.close()
    except con.Error as error:
        print("failed to read data: ", error)

def completeTask(connection):
    try:
        con = connection
        cur = con.cursor()
        succ = 'N'
        chosenRow = ''
        while succ == 'N':
            selectedRow = "'" + input("What Task would you like to complete?") + "'"
            cur.execute("SELECT 1 FROM checklist WHERE UPPER(task) = UPPER(" + selectedRow +")")
            checkData = cur.fetchall()
            if checkData is None:
                print("Could not find a task by that name, please try again.")
            else: 
                succ = 'Y' 
                chosenRow = selectedRow
        confirm = input("Are you sure you want to mark" + chosenRow + " as complete?")
        if confirm.upper() in["Y","YES"]:
            print("you got it")
            update = "UPDATE checklist SET complete = 'Y' WHERE task = " + chosenRow
            cur.execute(update)
            con.commit()
            print("Row " + chosenRow + " set to complete!")
            cur.close()
        else: 
            cur.close()
    except con.Error as error:
        print("failed to read data: ", error)


def deleteOne(connection):
    try:
        con = connection
        cur = con.cursor()
        succ = 'N'
        chosenRow = ''
        while succ == 'N':
            selectedRow = "'" + input("What Task would you like to delete?") + "'"
            cur.execute("SELECT 1 FROM checklist WHERE UPPER(task) = UPPER(" + selectedRow +")")
            checkData = str(cur.fetchall()).strip('[](),')
            if checkData == '':
                print("Could not find a task by that name, please try again.")
            else: 
                succ = 'Y' 
                chosenRow = selectedRow
        confirm = input("Are you sure you want to delete" + chosenRow + "?")
        if confirm.upper() in["Y","YES"]:
            print("you got it")
            update = "DELETE FROM checklist WHERE task = " + chosenRow
            cur.execute(update)
            connection.commit()
            print("Row " + chosenRow + " deleted!")
            cur.close()
    except connection.Error as error:
        print("failed to read data: ", error)
    finally:
        cur.close()

def runApp():
    try:
        con = connect()
        cur = con.cursor()
        tableCheck = "SELECT 1 FROM SQLITE_SCHEMA WHERE name = 'checklist' AND type = 'table'"
        cur.execute(tableCheck)
        tableExist = str(cur.fetchall()).strip('[](),')
        if tableExist == '':
            tableGen = """CREATE TABLE checklist(
                            task_id int NOT NULL PRIMARY KEY,
                            priority_level varchar(255) NOT NULL,
                            complete varchar(5) NOT NULL,
                            task varchar(255) NOT NULL,
                            steps varchar(500))
                            """
            cur.execute(tableGen)
            print("Initial setup successful!")
        cur.close()
        cont = 'Y'
        print("Welcome to your checklist!")
        while cont == 'Y':
            selection = input("Would you like to View your checklist, Insert a new task, or set a task to Complete?")
            if selection.upper() in ['INSERT', 'I']:
                insert(con)
            elif selection.upper() in ["VIEW", "V"]:
                query(con)
            elif selection.upper() in ["COMPLETE","C"]:
                completeTask(con)
            elif selection.upper() in ["DELETE","D"]:
                deleteOne(con)
            elif selection.upper() in ['DELETEALL']:
                deleteAll(con)
            elif selection.upper() in ['EXIT','QUIT']:
                cont = 'N'
                print("Thank you!")
            else:
                print("Please provide a valid input")
    except con.Error as error:
        print("failed to read data: ", error)
    finally:
        con.close()

runApp()    