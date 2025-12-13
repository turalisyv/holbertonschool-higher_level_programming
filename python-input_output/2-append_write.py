#!/usr/bin/python3
'''
My module document
'''


def append_write(filename="", text=""):
    '''
    My function document
    '''
    with open(file=filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
