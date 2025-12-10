#!/usr/bin/python3
'''
My module document
'''

def is_kind_of_class(obj, a_class):
    '''
    My method document
    '''
    return type(obj) is a_class or isinstance(obj, a_class)
