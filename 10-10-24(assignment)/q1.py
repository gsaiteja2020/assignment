'''
1.Create a class Vehicle with attributes brand and year. 
The class should have a method get_info() that returns the brand and year of the vehicle. 
Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include 
their respective additional attributes in the returned string.
'''

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    
    def get_info(self):
        return (f"vehicle brand is {self.brand} and year of manufacturing is {self.year}")

class car(Vehicle):
    def __init__(self, brand, year,number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors=number_of_doors
    
    def get_info(self):
        return (f"vehicle brand is {self.brand}, year of manufacturing is {self.year} and number of door are {self.number_of_doors}")

class MotorCycle(Vehicle):
    def __init__(self, brand, year,has_sidedoors):
        super().__init__(brand, year)
        self.has_sidedoors=has_sidedoors
    
    def get_info(self):
        return (f"vehicle brand is {self.brand} and year of manufacturing is {self.year} and has sidedoors {self.has_sidedoors}")
        

brand =input("enter car brand ")
year = input("year of purchase ")
number_of_door =input("number of doors ")
car = car(brand,year,number_of_door)
print(car.get_info())

moto=MotorCycle(input("Brand of the motorcycle "),input("year of purchase"), input("has side doors or not"))
print(moto.get_info())