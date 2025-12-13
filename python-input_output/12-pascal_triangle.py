#!/usr/bin/python3
"""
My module document
"""


def pascal_triangle(n):
    '''
    My function document
    '''
    def fact(a):
        res = 1
        for i in range(1, a + 1):
            res = res * i
        return res

    def C(n, r):
        return int(fact(n) / (fact(r) * fact(n - r)))

    res = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            temp.append(C(i, j))
        res.append(temp)

    return res
