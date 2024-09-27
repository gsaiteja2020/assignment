'''
1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information.

'''
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def display(self):
        print("NAME - ",self.name," AGE - ",self.age," GENDER - ",self.gender)
        

    def UpdateAge(self):
        self.age=input("enter the new age")

p1=Person("hari",24,"male")
p2=Person("giri",22,"male")
p3=Person("harish",25,"male")
p4=Person("sai",21,"male")
p1.display()
p2.display()
p3.display()
p4.display()
p1.UpdateAge()
p1.display()