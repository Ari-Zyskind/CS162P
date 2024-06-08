#!/usr/bin/python3

#lab6.py

import sys

class Point:
    def __init__(self, symbol="."):
        self._symbol = symbol # Initialize the symbol for the point

    def setSymbol(self, symbol):
        self._symbol = symbol # Set a new symbol for the point
    
    def draw(self):
        print(self._symbol) # Draw/print the point

class Triangle(Point):
    def __init__(self, symbol="*", height=3):
        super().__init__(symbol) # Initialize the symbol in the superclass (Point)
        self._height = height # Set the height for the triangle

    def draw(self):
        for i in range(1, self._height + 1): # Draw the triangle row by row
            print(self._symbol * i) 

class Diamond(Point):
    def __init__(self, symbol="*", size=3):
        super().__init__(symbol)  # Initialize the symbol in the superclass (Point)
        self._size = size # Set the size for the diamond

    def draw(self):
        # Top half of diamond
        for i in range(self._size):
            print(" " * (self._size - i - 1) + self._symbol * (2 * i + 1))
        # Bottom half of diamond
        for i in range(self._size - 2, -1, -1):
            print(" " * (self._size - i - 1) + self._symbol * (2 * i + 1))

class Rectangle(Point):
    def __init__(self, symbol="#", width=4, height=2): 
        super().__init__(symbol) # Initialize the symbol in the superclass (Point)
        self._width = width # Set the width for the rectangle
        self._height = height  # Set the height for the rectangle

    def draw(self):
        # Draw the rectnagle
        for h in range(self._height):
            for w in range(self._width):
                print(self._symbol, end="")
            print("")

class Square(Rectangle):
    def __init__(self, symbol="#", size=3):
        super().__init__(symbol, size, size) # Initialize square with equal height and width

def parse_file(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split() 
            shape_type = parts[0]
            symbol = parts[1]

            # Determine dimensions for that shape
            if shape_type == 'P':
                shape = Point(symbol)
            elif shape_type == 'S':
                size = int(parts[2])
                shape = Square(symbol, size)
            elif shape_type == 'T':
                height = int(parts[2])
                shape = Triangle(symbol, height)
            elif shape_type == 'D':
                size = int(parts[2])
                shape = Diamond(symbol, size)
            elif shape_type == 'R':
                width = int(parts[2])
                height = int(parts[3])
                shape = Rectangle(symbol, width, height)
            shapes.append(shape)
    return shapes

def main():
    if len(sys.argv) != 2:
        print("Error: Try again!")
        return
    
    # store as filename what is put into command line argument
    filename = sys.argv[1]
    shapes = parse_file(filename)
    
    # Draw each shape in the list
    for shape in shapes:
        shape.draw()
        # print a new line after each shape for visual/aesthetic reasons
        print()

if __name__ == "__main__":
    main()


