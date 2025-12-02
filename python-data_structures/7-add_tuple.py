#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    total = [0, 0]
    for i in range(0, 2):
        if i >= len(tuple_a):
            total[i] = 0 + tuple_b[i]
        if i >= len(tuple_b):
            total[i] = tuple_a[i] + 0
        else:
            total[i] = tuple_a[i] + tuple_b[i]

    return tuple(total)
