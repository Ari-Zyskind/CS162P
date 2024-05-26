#!/usr/bin/python3

import random

class FootballPlayer:
    def __init__(self, first_name, last_name, position):
        self._first_name = first_name
        self._last_name = last_name
        self._position = position
        self._jersey_number = None

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_jersey_number(self):
        return self._jersey_number

    def set_jersey_number(self, jersey_number):
        self._jersey_number = jersey_number

    def determine_jersey_number(self):
        if self._position.lower() in ['qb', 'p', 'k']:
            self._jersey_number = random.randint(1, 19)
        elif self._position.lower() in ['wr', 'te']:
            self._jersey_number = random.randint(10, 19)
        elif self._position.lower() in ['rb', 'db']:
            self._jersey_number = random.randint(20, 49)
        elif self._position.lower() in ['lb']:
            self._jersey_number = random.randint(50, 59)
        elif self._position.lower() in ['ol']:
            self._jersey_number = random.randint(60, 69)
        elif self._position.lower() in ['dl']:
            self._jersey_number = random.randint(70, 79)
        else:
            self._jersey_number = None
