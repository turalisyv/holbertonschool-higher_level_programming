#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for i in str:
        if i == " ":
            new_str = new_str + " "
            continue
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            new_str = new_str + i
            continue
        new_str = new_str + chr(ord(i)-32)
    print("{}".format(new_str))
