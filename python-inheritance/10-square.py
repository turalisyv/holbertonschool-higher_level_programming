#!/usr/bin/python3
'''
My module document
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    My class document
    '''
    def __init__(self, width, ):
        Rectangle.integer_validator(self, "width", width)
        self.__width = width


    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__width)

    def area(self):
        return self.__width * self.__width
