#!/usr/bin/python3
'''
My module document
'''


class BaseGeometry():
    '''
    My class document
    '''
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise ValueError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        raise Exception("area() is not implemented")
