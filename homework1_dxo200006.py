# Dmitrii Obideiko
# DXO200006

import pickle
import re
import sys
import os
import pathlib

class Person:
    def __init__(self, last, first, mi, idNum, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.idNum = idNum
        self.phone = phone
    
    # displays person's data 
    def display(self):
        print("Employee id:", self.idNum)
        print('\t', self.first, self.mi, self.last)
        print('\t', self.phone)
        print('\n')

# parses data from lines, creates objects, puts them into a dictionary, and then return it
def processLines(lines):
    employees = {} # where key: id and value: Person object
    for line in lines:
        data = line.split(',') # separates data
        first = data[0].capitalize()
        last = data[1].capitalize()
        # takes only the first letter of the middle name
        # if no middle name then it becomes "X"
        mi = data[2][:1].capitalize() if data[2] else 'X'
        idNum = data[3]
        phone = data[4]
        # checks if id is in a correct format
        # if it's not then will ask the user to put it until it's correct  
        while len(idNum) != 6 or not re.search('[a-zA-Z]{2}[0-9]{4}', idNum):
            print('ID invalid:', idNum)
            idNum = input('Please enter a valid id: ')  
        # checks if phone number is in a correct format
        # if it's not then will ask the user to put it until it's correct
        while len(phone) != 12 or not re.search('[1-9]{3}-[1-9]{3}-[0-9]{4}', phone):
            print('Phone', phone, 'is invalid')
            print('Enter phone number in form 123-456-7890')
            phone = input('Enter phone number: ')
         
        employees[idNum] = Person(last, first, mi, idNum, phone)
    return employees

if __name__ == '__main__':
    # checks if the user put a system argument
    if len(sys.argv) < 2:
        print('Error: Please enter a filename as a system arg')
        quit()
    
    # opens the file and saves all lines that are present in it
    filePath = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(filePath), 'r') as f:
        text_in = f.read().splitlines()
    
    # skips the first line and sends all lines for processing
    # employees is a dictionary where key is an id and value is a Person object
    employees = processLines(text_in[1:])
    
    # saves the pickle file  
    pickle.dump(employees, open('employees.pickle', 'wb'))
    
    # reads the pickle file 
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # print all employee's data
    print('\n\nEmployee list:')
    for emp_id in employees_in.keys():
        employees_in[emp_id].display()