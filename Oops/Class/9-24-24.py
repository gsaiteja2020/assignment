
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    
    def display(self):
        print("product name is ",self.name)
        print("product price is ",self.price)


i=Product("iphone",49000)
i.display()

shirt=Product("netplay",1500)
shirt.display()
