# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DAlexandrov,11.5.19,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
lstMenu = []   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
while(True):
    try:
        objF = open(objFile, "r") # Tries to read the file
        break
    except FileNotFoundError: # If the file isn't found, throws an exception and creates the file and restarts the program.
        print()
        print("Cannot find file, creating the " + objFile + " and restarting...")
        objF = open(objFile, "x")
        continue

for row in objF:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objF.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        lstMenu.append(strChoice) # Keep track of what choices the user has made
        if not lstTable: # checks if the lstTable is empty
            print("No data stored in " + objFile + ".")
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        lstMenu.append(strChoice) # Keep track of what choices the user has made
        strUserTask = input("What task would you like to add: ")
        strUserPriority = input("What priority would you give to this task: ")
        dicRow = {"Task": strUserTask.strip(), "Priority": strUserPriority.strip()}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        lstMenu.append(strChoice) # Keep track of what choices the user has made
        if not lstTable: # checks if the lstTable is empty
            print("No data stored in " + objFile + ". Nothing to delete, please add task(s) first.")
            continue

        print("Current Task(s):") # display current tasks
        for row in lstTable:
            print(row["Task"])

        strRemoveTask = input("Which task would you like to remove from the list above? (Case Sensitive) ") #ask the user which task they would like to delete
        for row in lstTable:
            if strRemoveTask in row["Task"]: #search for the user selected task in the list of tasks
                print()
                print("Found the Task, " + "\"" + strRemoveTask + "\"" + "; deleting from task list.")
                lstTable.remove({"Task": row["Task"], "Priority": row["Priority"]}) #if task is found in the last, delete that row from the list
                break
        else:
            print()
            print("Task not found, please try again.") #task not found
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        lstMenu.append(strChoice) # Keep track of what choices the user has made
        objF = open(objFile, "w")
        for row in lstTable:
            objF.write(row["Task"] + "," + row["Priority"] + "\n")
        objF.close()
        print()
        print("Data Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        if (("2" in lstMenu or "3" in lstMenu) and "4" not in lstMenu):
        #if the user has added or deleted tasks from the list and they have not saved the data, ask them if they want to save
            strExit = input("You added or deleted task(s) without saving, are you sure you want to quit? (y/n) ")
            if (strExit.lower().strip() == 'y'):
                print()
                print("Exiting...")
                break # Exit the program
            elif (strExit.lower().strip() == 'n'):
                continue
        else:
            print()
            print("Exiting...")
            break  # Exit the program