'''
1.Problem Statement: Create a class Teacher with an attribute subject. 
                    Then, create a class Researcher with an attribute field. 
                    Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher, 
                    and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher,
 and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes.
'''
class Teacher:
    def __init__(self,subject):
        self.subject=subject
    
class Researcher():
    def __init__(self,field):
        self.field=field

class TeachingResearcher(Teacher,Researcher):
    def __init__(self,subject,field):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,field)
        

    def dispaly(self):
        print(self.subject,self.field)

tr=TeachingResearcher("maths","statistics")
tr.dispaly()

'''
2.Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly(). Then, create a derived class Eagle that inherits from both Bird and Flyable.

Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods.
'''

class Bird:
    def __init__(self,species):
        self.species=species

class Flyable:
    def fly():
        print("flying")

class Eagle(Bird,Flyable):
    def __init__(self, species):
        Bird.__init__(self,species)
        
    
    def dispaly(self):
        print(self.species)
        Flyable.fly()

eagle=Eagle("Birds")
eagle.dispaly()