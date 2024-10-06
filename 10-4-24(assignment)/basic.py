'''
Problem Statement: Create a class Person with attributes: name and age. Create another class Student that inherits from Person and has an additional attribute grade. Define methods in both classes to display the attributes.

Tasks:
Define a Person class with an __init__ method to initialize name and age.
Define a Student class that inherits from Person, with an additional attribute grade.
Define a display_info method in both Person and Student classes to print all attributes.
Create objects for both Person and Student and display their information.

'''
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def display_info(self):
        print(f"name - {self.name} age - {self.age}")


class Student(Person):
    def __init__(self, name, age,grade) -> None:
        Person.__init__(self,name, age)
        self.grade=grade
    def display_info(self): 
        super().display_info()
        print("grade - ",self.grade)

person=Person("shayam",38)
student=Student("wayam",21,"12th")
person.display_info()
student.display_info()