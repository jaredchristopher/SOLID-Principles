# Created by: Jared Christopher
# File: o.py

from abc import ABC, abstractmethod
import math

class Shape:
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

# Triangle is the new shape that I am implementing
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return (self.base * self.height) / 2

def main():
    radius = 1
    side = 2
    length = 3
    width = 4
    base = 5
    height = 6

    c = Circle(radius)
    print(c.get_area())

    sq = Square(side)
    print(sq.get_area())

    rec = Rectangle(length, width)
    print(rec.get_area())

    tri = Triangle(base, height)
    print(tri.get_area())

if __name__ == "__main__":
    main()