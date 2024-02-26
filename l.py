# Created by: Jared Christopher
# File: l.py
import math

# To maintain consistency, I have each shape class implements a get_area() method with their respective calculations 
# while still offering a unified interface through the Shape superclass. This approach supports code readability, maintainability, 
# and ensures LSP is not violated. This enabled me to implement a polygon subclass without affecting the program or violating LSP.

class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area()")

    # In order to not violate LSP, I am implementing a get_dimensions function
    # that will work as my replacement for the set_width and set_height funcitons
    # that were previously in the Circle and Rectangle subclasses as stated in assignment.
    def set_dimensions(self, *args):
        raise NotImplementedError("Subclasses must implement set_dimensions()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def set_dimensions(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return (self.base * self.height) / 2
    
    def set_dimensions(self, base, height):
        self.base = base
        self.height = height
    
# I implement the Polygon subclass and maintain LSP
class Polygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length
    
    def get_area(self):
        return (self.sides * self.side_length ** 2) / (4 * math.tan(math.pi/self.sides))

    def set_dimensions(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length

def main():
    c = Circle(2)
    rec = Rectangle(3, 4)
    tri = Triangle(5, 6)
    poly = Polygon(5, 12)

    print("Circle area:", c.get_area())
    print("Rectangle area:", rec.get_area())
    print("Triangle:", tri.get_area())
    print("Polygon:", poly.get_area())

    # Setting new dimensions
    c.set_dimensions(4)
    rec.set_dimensions(6, 8)
    tri.set_dimensions(10, 12)
    poly.set_dimensions(6, 12)

    print("Updated circle area:", c.get_area())
    print("Updated rectangle area:", rec.get_area())
    print("Updated triangle area:", tri.get_area())
    print("Updated polygon area:", poly.get_area())

if __name__ == "__main__":
    main()