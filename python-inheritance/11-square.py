#!/usr/bin/python3
'''
My module document
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    My class document
    '''
    def __init__(self, size):
        Rectangle.integer_validator(self, "width", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
