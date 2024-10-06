'''
3. Multilevel Inheritance
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, and Manager is derived from Employee. Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information.

'''
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def display(self):
        print("name - ",self.name,"  ","age - ",self.age)

class Employee(Person):
    def __init__(self,salary,name,age) -> None:
        Person.__init__(self,name,age)
        self.salary=salary
    def display(self):
        print("salary - ",self.salary)
        return super().display()


class Manager(Employee):
    def __init__(self,department, salary, name, age) -> None:
        super().__init__(salary, name, age)
        self.department=department
    
    def display(self):
        print("department - ",self.department)
        return super().display()

m=Manager("it","25000","hari","26")
m.display()
