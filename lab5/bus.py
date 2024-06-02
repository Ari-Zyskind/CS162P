#!/usr/bin/python3

import math

class Bus:
    def __init__(self, students, age):
        self._students = students
        self._age = age
        self._calculate_seats()

    # Getter for students
    def get_students(self):
        return self._students

    # Setter for students
    def set_students(self, value):
        self._students = value
        self._calculate_seats()

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, value):
        self._age = value
        self._calculate_seats()

    def _calculate_seats(self):
        if self._age < 10:
            seats = math.ceil(self._students / 3)
        else:
            seats = math.ceil(self._students / 2)
        print(f"Number of bus seats needed: {seats}")

