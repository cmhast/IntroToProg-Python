# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script   < 1.1.2030?
# C.Hastings,5.11.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = '''   
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    '''
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)


#Based on how things are presented, it seems that what is wanted is a dictionary of a form like
#{task:cleaning, priority:high}. But instead, structuring it as {cleaning:high} would seem better.
#There is no loss of clarity, so long as that structure is used consistently.
#The use of a list of dictionaries removes the main benefit, though, which is that a single key
#cannot have multiple values. i.e. as things seem to be intended, you could have a list like
#[{task:cleaning, priority:high},{task:cleaning, priority: low}]. How should that be interpreted?
#Wouldn't it be better to use a single dictionary and, when adding new items, check if that key
#already exists, then either prompt the user if they *really* want to change the priority,
#or simply add the addition if there isn't any conflict to double-check?

try:
    file_in = open(objFile,'r')
    for line in file_in:
        strData = line.strip('\r\n').split(',')  # There is probably a better way to remove newlines?
        dicRow = {strData[0]:strData[1]}
        lstTable.append(dicRow)
    file_in.close()
except FileNotFoundError:
    print('ToDoList.txt cannot be opened. If it does not exist, this is not a problem.')
    print('If it does exist, then something odd has happened and the data in it has not been read.')
    print('In that case, it is recommended that you quit and do not save.')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    #input() already returns a string. Is there a reason for str() here?
    #also, I'm moving the .strip() up here, so that it only has to be done
    #once, even if we have to go through multiple elifs
    strChoice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
    print()  # adding a new line for looks
    # Show the current items in the table
    if (strChoice == '1'):
        print('Current to do list is:')
        for row in lstTable:
            for i in row:
                print('    ',i,': ',row[i],' priority',sep='')
        continue
    # Add a new item to the list/Table
    elif (strChoice == '2'):
        strChoice = input('Please enter new task > ').strip()
        for row in lstTable:
            if strChoice in row:
                print('That task is already on the list, please remove it first')
                break
        else:
            lstTable.append({strChoice:input('Please enter the new task\'s priority > ').strip()})
        continue
    # Remove a new [sic?] item from the list/Table
    elif (strChoice == '3'):
        strChoice = input('Which entry would you like to remove? > ').strip()
        for row in lstTable:
            if strChoice in row:
                lstTable.remove(row)
                break
        else:
            print()
            print('That entry does not exist!')
        continue
    # Save tasks to the ToDoToDoList.txt file
    elif (strChoice == '4'):
        print('Saving')
        file_out = open(objFile,'w')
        for row in lstTable:
            for i in row:
                file_out.write(i)
                file_out.write(',')
                file_out.write(row[i])
                file_out.write('\n')
        file_out.close()
        continue
    # Exit program (giving the user the option to save first)
    # Maybe I should also ask for confirmation? Not going to add that for the moment
    elif (strChoice == '5'):
        print('Would you like to save data before exiting?')
        print('Enter "save" to save, any other input will simply exit without saving')
        if input('> ').strip().lower() == 'save':
            print('Saving and Exiting')
            file_out = open(objFile,'w')
            for row in lstTable:
                for i in row:
                    file_out.write(i)
                    file_out.write(',')
                    file_out.write(row[i])
                    file_out.write('\n')
            file_out.close()
        else:
            print('Exiting without saving')
        break  # and Exit the program
