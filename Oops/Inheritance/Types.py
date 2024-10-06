# ======================================= INHERITANCE ================================================

# Single level inheritance
class Parent:
    def p(self):
        print("i am parent")

class Child(Parent):
    def c(self):
        print("i am child")

child=Child()
child.p()
child.c()

# multilevel inheritance
class Grandfather:
    def __init__(self):
        self.land=15
        print(self.land)

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.fland= self.land-5
        print(self.fland)

class Child2(Father):
    def __init__(self):
        super().__init__()
        self.sland= self.fland+10
        print(self.sland)
        

obj=Child2()


# multiple inheritance

'''
class A:
    print ("A")

class B:
    print("B")

class C(A,B):
    pass

ob=C()

'''


class Father:
    def __init__(self):
        self.name =  "behaviar"
       
    def m1(self):
        print("this is father classs")
        return "this is m1 "
       
 
class Mother:
    def __init__(self):
        self.color  = "white"
        self.name = "ram"
   
    def m2(self):
        print("this is mother  classs")
 
class child(Mother,Father):
    def dispaly(self):
        Father.__init__(self)
        Mother.__init__(self)
        print(self.color)
        print(self.name)
 
    def m3(self):
        print(self.name)
        print(self.m1())
 
 
obj = child()
obj.m1()
obj.m2()
obj.dispaly()
obj.m3()

# hieracical inheritance
class Z:
    pass

class Y(Z):
    pass

class X(Z):
    pass



