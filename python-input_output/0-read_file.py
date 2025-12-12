#!/usr/bin/python3
'''
My module document
'''


def read_file(filename=""):
    '''
    My function document
    '''
    with open(file=filename, mode="r", encoding="utf-8") as f:
        txt = f.read()
        if f.read() == txt:
            f.close()
            return
        print(txt.strip())
