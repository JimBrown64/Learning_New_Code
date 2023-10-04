import sqlite3


def connect():
    con = sqlite3.connect("appdb.db")
    print("connection successful")
    return(con)

def query():
    try:
        connection = connect()
        cur = connection.cursor()
        query = """SELECT priority_level,task,steps FROM checklist ORDER BY priority_level ASC"""
        cur.execute(query)
        result = cur.fetchall()
        print("Row count: ", len(result))
        print("priority level|       task      |steps")        
        for row in result:
            print(row[0] +"             |   " + row[1] + "   |   " + row[2] + "\n")
        cur.close()
    except connection.Error as error:
        print("failed to read data: ",error)
    finally:
        if connection:
            connection.close()

def insert():
    try:
        connection = connect()
        cur = connection.cursor()
        collectId = """SELECT MAX(task_id)+1 FROM checklist"""
        cur.execute(collectId)
        newTaskId = str(cur.fetchall()).strip('[](),')
        if newTaskId == 'None':
            newTaskId = '1'
            print("no prior tasks, task id set to 1")
        priority = input("What priority level would you like this set to? (numeric, typically a scale of 1(most important)to 5(least important))")
        task = "'" + input("What is the task at hand?") + "'"
        steps = "'" + input("What steps are required for this task? (list format, seperate with commas)") + "'"
        statement = """INSERT INTO checklist(task_id, priority_level, task, steps)
                       VALUES(""" + newTaskId + """, """ + priority + """, """ + task + """, """ + steps + """
                        ) """
        cur.execute(statement)
        connection.commit()
        print("Record inserted succesfully")
        cur.close()
    except connection.Error as error:
        print("failed to read data: ", error)
    finally:
        if connection:
            connection.close()

def deleteAll():
    try:
        connection = connect()
        cur = connection.cursor()
        confirm = input("Are you sure you want to clear the table?(This cannot be undone!)")
        if confirm.upper() in ['Y','YES']:
            cur.execute("""DELETE FROM checklist""")
            connection.commit()
            print("Table has been cleared")
            cur.close()
            connection.close()
        else:
            cur.close()
            connection.close()
    except connection.Error as error:
        print("failed to read data: ", error)
    finally:
        if connection:
            connection.close()

def completeTask():
    try:
        connection = connect()
        cur = connection.cursor()
        succ = 'N'
        chosenRow = ''
        while succ == 'N':
            selectedRow = input("What Task would you like to complete?")
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
            connection.commit()
            print("Row " + chosenRow + " set to complete!")
            cur.close()
            connection.close()
        else: 
            cur.close()
            connection.close()
    except connection.Error as error:
        print("failed to read data: ", error)
    finally:
        if connection:
            connection.close()

def deleteOne(connection):
    try:
        con = connection
        cur = con.cursor()
        succ = 'N'
        chosenRow = ''
        while succ == 'N':
            selectedRow = input("What Task would you like to delete?")
            cur.execute("SELECT 1 FROM checklist WHERE UPPER(task) = UPPER(" + selectedRow +")")
            checkData = cur.fetchall()
            if checkData is None:
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
        connection = connect()
        cur = connection.cursor()
        tableCheck = "SELECT 1 FROM appdb.tables WHERE table_name = 'checklist'"
        cur.execute(tableCheck)
        tableExist = cur.fetchall()
        if tableExist is None:
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
            selection = input("Would you like to View your checklist, Insert a new row, or Delete the Table?")
            if selection.upper() in ['INSERT', 'I']:
                insert()
            elif selection.upper() in ["VIEW", "V"]:
                query()
            elif selection.upper() in ["DELETE","D"]:
                deleteOne(connection)
            elif selection.upper() in ['DELETEALL']:
                deleteAll()
            elif selection.upper() in ['EXIT','QUIT']:
                cont = 'N'
                print("Thank you!")
            else:
                print("Please provide a valid input")
    except connection.Error as error:
        print("failed to read data: ", error)
    finally:
        connection.close()


runApp()    