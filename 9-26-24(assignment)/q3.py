'''
3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle.
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    
    def calculate_area(self):
        
        area = self.length * self.width
        print("AREA OF",self," - ",area)

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"   

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(7, 4)
rectangle3 = Rectangle(10, 2)


rectangle1.calculate_area()  # Output: 15
rectangle2.calculate_area()  # Output: 28
rectangle3.calculate_area()  # Output: 20
