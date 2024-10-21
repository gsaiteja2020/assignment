'''
Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). 
Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective 
additional attributes in the returned string.
'''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_details(self):
        print(self.name)

    def get_salary(self):
        print(self.salary)

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    
    def get_details(self):
        