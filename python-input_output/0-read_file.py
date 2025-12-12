#!/usr/bin/python3
'''
My module document
'''


def read_file(filename=""):
    with open(file=filename, mode="r") as f:
        print(f.read())
