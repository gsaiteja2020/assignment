'''Problem Statement: Create a class structure to represent hybrid inheritance:

Device: Base class with name attribute.
Phone: Derived from Device with an additional phone_number attribute.
Tablet: Derived from Device with an additional screen_size attribute.
Smartphone: Derived from both Phone and Tablet with an additional attribute os.

Tasks:
Define a base class Device with an attribute name.
Define a class Phone that inherits from Device and adds an attribute phone_number.
Define a class Tablet that inherits from Device and adds an attribute screen_size.
Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
Implement methods to display all attributes of the Smartphone.
Create an instance of Smartphone and display its information.
nce:'''

class Device:
    def __init__(self,name) -> None:
        self.name=name
    def display(self):
        print(f"name - {self.name}")
    
class Phone(Device):
    def __init__(self, name,phone_number) -> None:
        Device.__init__(self,name)
        self.phone_number=phone_number
    def display(self):
        print(f"phone number - {self.phone_number}")
        super().display()


class Tablet(Device):
    def __init__(self, name,screen_size) -> None:
        Device.__init__(self,name)
        self.screen_size=screen_size
    def display(self):
        print(f" screen size - {self.screen_size}")
        super().display()

class Smartphone(Phone,Tablet):
    def __init__(self, name, phone_number,screen_size,os) -> None:
        Phone.__init__(self,name, phone_number)
        Tablet.__init__(self,name,screen_size)
        self.os=os
    def display(self):
        print(f" os - {self.os}")
        super().display()
    

sp=Smartphone("s24",945367281,"6 inches","android")
sp.display()