#!/usr/bin/python3
"""
My module document
"""

class Student:
    """
    My class document
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if attr == None:
            return self.__dict__

        dict = {}
        for i in attr:
            try:
                dict.update({i: self.__dict__[i]})

            except KeyError:
                continue

        return dict
