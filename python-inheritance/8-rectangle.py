#!/usr/bin/python3
'''
My module document
'''


class BaseGeometry():
    '''
    My class document
    '''


    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.width = width
        self.height = height
