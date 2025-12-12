#!/usr/bin/python3

def read_file(filename=""):
    with open(file=filename, mode="r") as f:
        print(f.read())
