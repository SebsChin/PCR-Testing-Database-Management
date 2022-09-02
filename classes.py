

# A file to contain all the classes created for the program

from datetime import date, datetime
import enum


# Initiate enum for zones
class Zone(enum.Enum):
    A = 1
    B = 2
    C = 3

# Initiate the Employee class to hold employee specific data
class Employee:
    
    # To initialise the employee instance
    def __init__(self, first_name, last_name, role, phone, email, start_date):
        
        # Set up employee variables
        
        # Definately included:
        self.first_name = first_name
        self.last_name = last_name
        self.departments = []
        self.role = role
        self.phone = phone
        self.email = email
        self.start_date = start_date
        self.tests = []
        
        # Might be useful:
        self.zone = "B"
        self.location = "-"
        self.has_covid = False
    
    # Change how the object is represented
    # when printed
    def __repr__(self):
        
        # Start with empty string
        s = ""
        
        # If the employee's start date is not of type datetime
        if self.start_date == "-": 
            
            s = (self.first_name + ":" + self.last_name + ":-:" +
                self.zone)
        
        # Otherwise
        else:
            
            s = (self.first_name + ":" + self.last_name + ":" +
                self.start_date.strftime("%d/%m/%Y") + ":" + self.zone)
        
        # Return the sring that has been crafted
        return s
    
    def __eq__(self, other):
        
        if (self.first_name == other.first_name and
            self.last_name == other.last_name):
            
            return True
        
        return False
    
    # Allow method to add departments
    def add_departments(self, departments):
        
        for d in departments:
            self.departments.append(d)
    
    # Allow method to add tests
    def add_test(self, test):
        self.tests.append(test)

# Initialise a test class to represent test instances        
class Test:
    
    # Initialise the test instance
    def __init__(self, category, date, result, employee):
        
        # Set up test variables
        
        # Definitely included:
        self.category = category
        self.date = date
        self.result = result
        self.employee = employee
        
        # Might be useful:
        self.add_notes = ""
    
    # Add function to manipulate how to represent cases
    def __repr__(self):
        
        s = ("|" + self.category + "   |" + self.date.strftime("%d/%m/%Y") + "|" + self.result + 
            "     |{:13}|{:18}|".format(self.employee.first_name, self.employee.last_name))
        
        return s
    
    # Function to check if tests are equal
    def __eq__(self, other):
        
        if (self.employee == other.employee
            and self.date == other.date):
            
            return True
        
        return False
    
    # Function to check for positive results
    def result_pos(self):
        
        if self.result.upper() == "POS":
            return True
        
        return False