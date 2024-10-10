from abc import ABC , abstractmethod
 
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
 
class Car(vehicle):
    def start_engine(self):
        print("car engine started")
   
    def stop_engine(self):
        print("car engine stopped")
class bike(vehicle):
    def start_engine(self):
        print("bike engine started")
   
    def stop_engine(self):
        print("bike engine stopped")
 
car = Car()
car.start_engine()
car.stop_engine()
 
b= bike()
b.start_engine()
b.stop_engine()