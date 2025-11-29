#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for i in str:
        if i == " ":
            new_str = new_str + " "
            continue
        new_str = new_str + chr(ord(i)-32)
    print(new_str)
