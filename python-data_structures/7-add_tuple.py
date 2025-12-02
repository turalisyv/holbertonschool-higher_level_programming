#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]

    for i in range(0, len(tuple_a)):
        if i < 2:
            list_a[i] = tuple_a[i]

    for i in range(0, len(tuple_b)):
        if i < 2:
            list_b[i] = tuple_b[i]

    return tuple((list_a[0] + list_b[0], list_a[1] + list_b[1]))
