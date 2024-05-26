#!/usr/bin/python3

class MyMath:
    def absolute(self, number):
        # Returns the absolute value of a number.
        return abs(number)
    
    def average(self, numbers):
        # Returns the average value from a list of numbers.
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
