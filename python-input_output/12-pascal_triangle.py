#!/usr/bin/python3
"""
My module document
"""


def pascal_triangle(n):
    '''
    My function document
    '''
    if n <= 0:
        return []

    res = [[1]]

    for i in range(1, n):
        a = res[-1]
        b = [1]

        for j in range(1, len(a)):
            b.append(a[j - 1] + a[j])

        b.append(1)
        res.append(b)

    return res
