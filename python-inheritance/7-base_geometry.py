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
