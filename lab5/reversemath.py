#!/usr/bin/python3

class ReverseFloat:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value:.2f}"

    def __add__(self, other):
        return ReverseFloat(self.value - other.value)

    def __sub__(self, other):
        return ReverseFloat(self.value + other.value)

    def __mul__(self, other):
        return ReverseFloat(self.value / other.value)

    def __truediv__(self, other):
        return ReverseFloat(self.value * other.value)

