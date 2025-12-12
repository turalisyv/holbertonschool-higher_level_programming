#!/usr/bin/python3
'''
My module document
'''


def def write_file(filename="", text=""):
    '''
    My function document
    '''
    with open(file=filename, mode="r", encoding="utf-8") as f:
        txt = f.read()
        print(txt.find(text))
