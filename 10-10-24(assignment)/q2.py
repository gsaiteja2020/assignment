'''
Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.

'''
from abc import ABC , abstractmethod

class Animal:
    @abstractmethod
    def make_sounds(self):
        pass

class Dog(Animal):
    def make_sounds(self):
        print( "woof")

class Cat(Animal):
    def make_sounds(self):
        print("meow")

class Cow(Animal):
    def make_sounds(self):
        print("moo")

dog= Dog()
cat=Cat()
cow = Cow()
dog.make_sounds()
cat.make_sounds()
cow.make_sounds()