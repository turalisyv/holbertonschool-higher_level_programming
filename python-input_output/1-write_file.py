#!/usr/bin/python3
'''
My module document
'''


def write_file(filename="", text=""):
    '''
    My function document
    '''
    with open(file=filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
