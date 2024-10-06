'''
1.Problem Statement: Design a class hierarchy for an employee management system with the following structure:

Employee: Base class with name and salary.
Developer: Inherits from Employee with an additional attribute programming_language.
Manager: Inherits from Employee with an additional attribute team_size.
Intern: Inherits from Developer and has an additional attribute internship_duration.
Implement a method to display the details of each employee.
'''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("name - ",self.name)
        print("salary - ",self.salary)

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language=programming_language
    
    def display(self):
        print("programming language - ",self.programming_language)   
        return super().display()
         

class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    
    def display(self):
        print("team size - ",self.team_size)
        return super().display()

class Intern(Developer):
    def __init__(self, name, salary, programming_language,internship_duration):
        super().__init__(name, salary, programming_language)
        self.id=internship_duration
    
    def display(self):
        print("internship duration - ",self.id)
        return super().display()
       

emp=Employee("hari",25000)
dev=Developer("siri",50000,"java")
mgr=Manager("ganesh",80000,30)
i=Intern("balu",20000,"python",5)

emp.display()
dev.display()
mgr.display()
i.display()

'''
2.Problem Statement: Create a base class Vehicle with attributes brand and model. Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information.
'''

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
class Car(Vehicle):
    def __init__(self, brand, model,num_doors):
        super().__init__(brand, model)
        self.num_doors=num_doors
    
    def display(self):
        print(f"brand - {self.brand} model - {self.model} number of doors - {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, model,type):
        super().__init__(brand, model)
        self.type=type
    
    def display(self):
        print(f"brand - {self.brand} model - {self.model} type - {self.type }")

car=Car("BMW","A6",5)
bike=Bike("yamaha","gt500","sports")

car.display()
bike.display()