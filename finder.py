
from unicodedata import category
from classes import Employee, Test, Zone
import pandas as pd
import sys
import time
from datetime import date, datetime
import math
import re
import os

# Establish the help string for when help is called
HELP_STRING = """\nWelcome to the Help Menu:\n
[F] - Find | Find an employee or test in the database\n
[A] - Add | Add an employee or test to the database\n
[E] - Edit | Edit a pre-existing employee or test in the database\n
[H] - Help | Print out this message\n
[X] - Quit | Exit the program\n
press [Enter] to return to the main menu
"""

# Initialise a place to store the employees
# and a place to store the tests
all_employees = []
tests = []
all_departments = []

# Function to determine employee, test or back
# option choice in a sub menu enviroment
def sub_menu(bad_input, func):
    
    while True:
        
        # If the input is bad, the while
        # loop is in play
        if not bad_input:
            print("\nWelcome to " + func + "! You can " + func + ":\n")
        
        # Print the avilable options every time
        print("[E] - An Employee\n")
        print("[T] - A Test\n")
        print("[B] - Go back (to Main Menu)\n")
        
        # Reset the input and it's status
        bad_input = False
        data = input("\n> ")
        
        # Use if statement to dictate which 
        # option they have chosen
        
        if data.upper() == 'E':
            
            e_or_t = "Employee"
            # list_or_individual_menu(bad_input, func, e_or_t)
            dictator(func, e_or_t)
            
        elif data.upper() == 'T':
            
            e_or_t = "Test"
            # list_or_individual_menu(bad_input, func, e_or_t)
            dictator(func, e_or_t)
            
        elif data.upper() == 'B':
            
            print("\nReturning to Main Menu!\n")
            break
        
        # Otherwise it was bad input,
        # so remind them of inputs
        else: 
            
            bad_input = True
            print("\nPlease enter one of the options listed to " + func + " or")
            print("[B] if you would like to return to the Main Menu:\n")
            
    return False

"""
# Function to determine if the person is adding,
# editing or finding a list or individual person(s)
# or test(s)
def list_or_individual_menu(bad_input, func, e_or_t):
    
    while True:
    
        if not bad_input:
            print("\nWelcome to " + e_or_t + " " + func + "! You can " + func + ":\n")
            
        print("[L] - Multiple (list)\n")
        print("[I] - Singular (individual)\n")
        print("[B] - Go back (to Employee/Test Menu)\n")
        
        bad_input = False
        
        data = input("\n> ")
        
        if data.upper() == 'L':
            print("\nWelcome to " + e_or_t + " List " + func + "!\n")
            
        elif data.upper() == 'I':
            print("\nWelcome to " + e_or_t + " Individual " + func + "!\n")
            
        elif data.upper() == 'B':
            print("\nReturning to Main Menu!\n")
            break
            
        else: 
            bad_input = True
            print("\nPlease enter one of the options listed to " + func + " or")
            print("[B] if you would like to return to Employee/Test Menu:\n")
            
    return False

""" 

# Function to dictate what function they are using
def dictator(func, e_or_t):
    
    if func.upper() == "ADD":
        
        add(e_or_t)
        
    if func.upper() == "EDIT":
        
        edit(e_or_t)
        
    if func.upper() == "FIND":
        
        find(e_or_t)

# Function for adding
def add(e_or_t):
    
    print("\nAdding " + e_or_t + "\n")
    
    # Check if adding Test
    if e_or_t.upper() == "TEST":
        
        # First while loop put in place to find an employee
        # to add a test, employee_exists is a requirement to
        # be met to proceed
        employee_exists = False
        while not employee_exists:
            
            # Allow for the user to be able to enter the first 
            # name and last name, but also be able to cancel at
            # any time if they enter [X]
            print("\nPlease enter the employee's first name")
            first_name = input("or [X] to cancel: ")
            
            if first_name.upper() == 'X':
                return False
            
            print("\nPlease enter the employee's last name")
            last_name = input("or [X] to cancel: ")
            
            if last_name.upper() == 'X':
                return False
            
            # Go through database of current employees and check
            # if they exist in the system
            for e in all_employees:
                
                # If they do, change the boolean that the while
                # loop is dependant on and set that employee as the
                # individual recieving the new test
                if (e.first_name.upper() == first_name.upper() and
                    e.last_name.upper() == last_name.upper()):
                    
                    test_employee = e
                    employee_exists = True
                    break
                
            # If the employee didnt exist, notify the user and 
            # let them try again    
            if employee_exists == False:
                print("\nEmployee does not exist, please try again\n")
        
        # Proceed with a similar pattern to the above while loop but 
        # for checking the validity of the date for the test
        valid_date = False
        while not valid_date:
            
            # Allow for the user to be able to enter the date of the test but
            # still also be able to cancel at any time if they enter [X]
            print("\nPlease enter the date of the test in format (dd/mm/yyyy)")
            date_str = input("or [X] to cancel: ")
            
            if date_str.upper() == 'X':
                return False
            
            # Check the date's validity and 
            elif date_valid(date_str):
                valid_date = True
                test_date = datetime.strptime(date_str, "%d/%m/%y")
            
            # Notify if the date is not valid
            else:
                print("\nThe entered date was not valid!")
                
        
        # Proceed with a similar pattern to the above while loop but 
        # for checking the category of the test (PCR or RAT)
        valid_category = False
        while not valid_category:
            
            
            # Allow for the user to specify the type of test or cancel with [X]
            print("\nPlease enter the category of the test. Either RAT [R], PCR [P]")
            category = input("or [X] to cancel: ")
            
            # Check the validity of the input and allow for the while
            # loop to break where there is valid input
            if (category.upper() == "R" or
                category.upper().startswith("RAT")):

                valid_category = True
                category = "RAT"
                
            elif (category.upper() == "P" or
                category.upper().startswith("PCR")):

                valid_category = True
                category = "PCR"
            
            # If the input is not valid, notify the user
            else:
                print("\nThe entered category was not valid!")
        
        # Proceed with a similar pattern to the above while loop but 
        # for checking the result of the test (Pos, Neg or Pending)
        valid_result = False
        while not valid_result:
            
            # Allow for the user to specify the result of the test or cancel with [X]
            print("Please enter the result of the test, either positive [POS],")
            result = input("Negative [NEG], Pending [PEND] or [X] to cancel: ")
            
            # Check the validity of the input and allow for the while
            # loop to break where there is valid input
            if (result.upper().startswith("POS")):

                valid_result = True
                result = "Pos"
                
            elif (result.upper().startswith("NEG")):

                valid_result = True
                result = "Neg"
            
            elif (result.upper().startswith("PEND")):
                
                valid_result = True
                result = "Pending"
            
            # If the input is not valid, notify the user    
            else:
                print("\nThe entered result was not valid!")
                
        # Create the test object with the new inputs from the user
        new_t = Test(category, test_date, result, test_employee)
        
        i = 0
        # Need to check if the test will override an existing test,
        # go through all the test objects already in place
        while i <  len(test_employee.tests):
            
            # Establish the test to check
            t = test_employee.tests[i]
            
            # If tests are equal based on __eq__ function for testing
            if new_t == t:
                
                # Set up for the user to choose wether
                # they want to override the test
                valid_response = False
                while not valid_response:
                    
                    # Print this message to the screen including the test that
                    # will be deleted and take input from user
                    print("\nThis test will override the existing test for this employee:")
                    print(t)
                    y_or_n = input("Are you sure you want to do this? yes [Y] or no/cancel [N]: ")
                    
                    # Cancel the new test
                    if y_or_n.upper() == "N":
                        return False
                    
                    # Remove the test instance that clashes and continue on
                    elif y_or_n.upper() == "Y":
                        valid_response = True
                        del test_employee.tests[i]
            
            # Increment            
            i += 1      
            
        # Add the test
        test_employee.tests.append(new_t)
        tests.append(new_t)
        
        # Notify the user that it was successful
        print("\nTest successfully added\n")
    
    # Check if adding Employee
    elif e_or_t.upper() == "EMPLOYEE":
        
        # Set employee to aldready existing to enter loop,
        # then continue to loop if employee does exist
        employee_exists = True
        while employee_exists:
            
            # Allow for the user to be able to enter the first 
            # name and last name, but also be able to cancel at
            # any time if they enter just [X]
            print("\nPlease enter the new employee's first name")
            first_name = input("\nor [X] to cancel: ")
            
            # Boolean check to make sure the first_name is valid
            valid_name = bool(re.fullmatch('[A-Za-z]{1,10}( |-|)[A-Za-z]{1,10}', last_name))
            
            # Exit and cancel if user decides
            if first_name.upper() == 'X':
                return False
            
            # Check if the last_name is valid based on boolean check before
            elif valid_name == False:
                print("Invalid first name, employee must have a valid first name including")
                print("including atleast 2 letters to a maximum of 20, upper or lower case and can")
                print("only include a singlular space ( ) or hyphen (-)")
            
            print("\nPlease enter the new employee's last name")
            last_name = input("\nor [X] to cancel: ")
            
            # Boolean check to make sure the last_name is valid
            valid_name = bool(re.fullmatch('[A-Za-z]{1,10}( |-|)[A-Za-z]{1,10}', last_name))
            
            # Exit and cancel if user decides
            if last_name.upper() == 'X':
                return False
            
            # Check if the last_name is valid based on boolean check before
            elif valid_name == False:
                print("Invalid last name, employee must have a valid last name including")
                print("atleast 2 letters to a maximum of 20, upper or lower case and can")
                print("only include a singlular space ( ) or hyphen (-)")
            
            # Set employee to doesn't exist, then flag if 
            # it does
            employee_exists = False
            
            # Go through database of current employees and check
            # if they exist in the system
            for e in all_employees:
                
                # Check if employee already exists, ensure there is no double ups
                # as this can easily break the system
                if (e.first_name.upper() == first_name.upper() and
                    e.last_name.upper() == last_name.upper()):
                    
                    # If the employee already exists in the system, flag
                    # it, so the loop can't break and print a message to
                    # inform the user
                    employee_exists = True
                    print("Employee is already present in the system,")
                    print("please try again with a different employee!")
                    break
        
        # Obtain the role of the employee, role is not that important
        # and can vary quite alot so, no while loop checks required
        print("\nPlease enter the new employee's role")
        first_name = input("\nor [X] to cancel: ")
        
        

# Function for editing
def edit(e_or_t):
    
    print("\nEditing " + e_or_t)

# Function for finding
def find(e_or_t):
    
    print("\nFinding " + e_or_t)

# Check if date is valid and in particular
# format
def date_valid(date):
    
    try:
        valid_date = datetime.strptime(date, "%d/%m/%y")
        return True
    
    except ValueError:
        return False

# Function to determine if data is a float
def is_float(num):
    
    # Check if it can be converted to a float
    try:
        
        # If it can, then return true
        float(num)
        return True
    
    # If it can't then return false
    except ValueError:
        return False

"""
# Uncomment below to load in data
"""

# Establish the path to the Excel file
path = "~/work/data_storage/UnitedData_Tests_Copy.xlsx"

# Opening workbook
df = pd.read_excel(path)

# Establish max rows and max cols
max_row = len(df)
max_col = len(df.columns)
print("max row: " + str(max_row) + "| max col: " + str(max_col) + "\n")

# Use iterrows to iterate over the rows
for index, row in df.iterrows():
    
    # If cell is empty, break
    if type(row['First Name']) is float:
        break
    
    # If employee has a start date
    elif row['Start Date AU'] != "-":
    
        # Create a new employee object
        # Taking from the information stored in the Excel spreadsheet
        e = Employee(row['First Name'], row['Last Name'], row['Role'], 
                     row['Phone'], row['Email'], row['Start Date AU'])
        
        # Add the department(s) that the employee works for
        departments = row['Departments'].split(", ")
        
        # Add any departments that havent been added already
        for d in departments:
            
            if d not in all_departments:
                
                all_departments.append(d)
            
        
        e.add_departments(departments)
        
        # Append the new employee to the employee list
        all_employees.append(e)
    
    # If employee does not have a start date
    else:
        
        # Create a new employee object
        # Taking from the information stored in the Excel spreadsheet
        e = Employee(row['First Name'], row['Last Name'], row['Role'], 
                     row['Phone'], row['Email'], row['Start Date AU'])
        
        # Add the department(s) that the employee works for
        departments = row['Departments'].split(", ")
        
        e.add_departments(departments)
        
        # Append the new employee to the employee list
        all_employees.append(e)

# Establish a place to store all the data
big_data = []

# Retrieve the list of headers to get a list of dates
header_list = list(df.columns)
date_list = header_list[10:]
big_data.append(date_list)

# Set up while loops to go through test data
i = 0    
while i < max_row:

    # For every new row, add a new empty list
    big_data.append([])
    
    j = 10
    while j < max_col:
        
        # Get the data per square in the big schedule
        data = df.iloc[i, j]
        
        # Check if data is NaN, if so continue on
        if not is_float(data):
            
            # Print put what is in the cell
            # print(data, end=":")
            
            # Append the data from that cell into the 
            # respective list 
            big_data[i + 1].append(data)
        
        else:
            
            # If NaN, enter "-"
            big_data[i + 1].append("-")
            
        # Iterate column
        j += 1
    
    # Print a new line and iterate
    # print()
    i += 1


# print(big_data)

# Go through the big_data table and note every test
i = 1
while i < len(big_data):
    
    j = 0
    while j < len(big_data[i]):
        
        # If test is of category PCR
        if big_data[i][j].upper().startswith("PCR"):
            
            # If the result of the test is positive
            if "POS" in big_data[i][j].upper():
                
                # Create a new test object to store the information
                t = Test("PCR", big_data[0][j], "Pos", all_employees[i - 1])
                
                # Add the test to the respective employee's tests
                all_employees[i-1].add_test(t)
                tests.append(t)
            
            # If the result of the test is negative
            if "NEG" in big_data[i][j].upper():
                
                # Create a new test object to store the information
                t = Test("PCR", big_data[0][j], "Neg", all_employees[i - 1])

                # Add the test to the respective employee's tests
                # and the test database
                all_employees[i-1].add_test(t)
                tests.append(t)
        
        # If the test is of category RAT
        elif big_data[i][j].upper().startswith("RAT"):
            
            # If the result of the test is positive
            if "POS" in big_data[i][j].upper():
                
                # Create a new test object to store the information
                t = Test("RAT", big_data[0][j], "Pos", all_employees[i - 1])
                
                # Add the test to the respective employee's tests
                # and the test database
                all_employees[i-1].add_test(t)
                tests.append(t)
            
            # If the result of the test is negative
            if "NEG" in big_data[i][j].upper():
                
                # Create a new test object to store the information
                t = Test("RAT", big_data[0][j], "Neg", all_employees[i - 1])

                # Add the test to the respective employee's tests
                # and the test database
                all_employees[i-1].add_test(t)
                tests.append(t)
        
        # Increment and continue 
        j += 1
    
    i += 1

# Obtaining positive cases and writing them to a file

# Establish list to store the 
pos_tests = []

count = 0
for t in tests:
    
    if t.result_pos():
        count += 1
        pos_tests.append(t)
        
pos_tests.sort(key=lambda x: x.date)


f = open("/home/seb/work/data_storage/Positive_Cases.txt", "w")

f.write("List of positive test results:\n")
f.write("|Type: |Date:     |Result: |First:       |Last:             |\n")

for t in pos_tests:
    
    f.write(str(t) + "\n")

f.write("Total count: " + str(count) + "\n")

f.close()

"""

for e in all_employees:
    
    print(e)
    
print(len(all_employees))
   
"""
    
"""

bad_input = False

while True:
    
    if not bad_input:
    
        print("\nWelcome to Seb's THE FALL GUY Employee Covid Database! :^)")
        print("How may I help you today?\n")
        
    print("[F] - Find\n")
    print("[A] - Add\n")
    print("[E] - Edit\n")
    print("[H] - Help\n")
    print("[X] - Quit")
    
    bad_input = False
    
    data = input("\n> ")
    
    if data.upper() == 'X':
        print("\nHave a great day!\n")
        sys.exit()
        
    elif data.upper() == 'H':
        
        print(HELP_STRING, end = "")
        data = input("\n> ")
        
    elif data.upper() == 'F':
            
        bad_input = sub_menu(False, "Find")
        
    elif data.upper() == 'A':
        
        bad_input = sub_menu(False, "Add")
        
    elif data.upper() == 'E':
        
        bad_input = sub_menu(False, "Edit")
        
    else: 
        bad_input = True
        print("\nPlease enter one of the options listed,")
        print("or [H] (for help) if you do not understand:\n")
        
"""