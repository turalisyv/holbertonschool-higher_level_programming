#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    total = list(tuple_a)
    for i in range(len(tuple_b)):
        if i < len(total):
            total[i] += tuple_b[i]

        else:
            total.append(tuple_b[i])

    return tuple(total)
