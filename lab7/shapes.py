#!/usr/bin/python3

from abc import ABC, abstractmethod

class Point(ABC):
    def __init__(self, symbol="."):
        self._symbol = symbol

    def setSymbol(self, symbol):
        self._symbol = symbol

    @abstractmethod
    def draw(self):
        pass

class Triangle(Point):
    def __init__(self, symbol="*", height=3):
        super().__init__(symbol)
        self._height = height

    def draw(self):
        for i in range(1, self._height + 1):
            print(self._symbol * i)

class Diamond(Point):
    def __init__(self, symbol="*", size=3):
        super().__init__(symbol)
        self._size = size

    def draw(self):
        for i in range(self._size):
            print(" " * (self._size - i - 1) + self._symbol * (2 * i + 1))
        for i in range(self._size - 2, -1, -1):
            print(" " * (self._size - i - 1) + self._symbol * (2 * i + 1))

class Rectangle(Point):
    def __init__(self, symbol="#", width=4, height=2):
        super().__init__(symbol)
        self._width = width
        self._height = height

    def draw(self):
        for h in range(self._height):
            for w in range(self._width):
                print(self._symbol, end="")
            print("")

class Square(Rectangle):
    def __init__(self, symbol="#", size=3):
        super().__init__(symbol, size, size)

if __name__ == "__main__":
    print("Triangle:")
    triangle = Triangle(symbol="*", height=5)
    triangle.draw()

    print("\nDiamond:")
    diamond = Diamond(symbol="*", size=4)
    diamond.draw()

    print("\nRectangle:")
    rectangle = Rectangle(symbol="#", width=5, height=3)
    rectangle.draw()

    print("\nSquare:")
    square = Square(symbol="@", size=4)
    square.draw()
