#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    res = ""

    try:
        for i in range(x):
            res = res + str(my_list[i])
            length += 1

    except IndexError:
        pass
