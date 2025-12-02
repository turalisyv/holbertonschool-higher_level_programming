#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    m = len(matrix[0])
    n = len(matrix)

    for i in range(0, n):
        for j in range(0, m):
            if j == m - 1:
                print("{:d}".format(matrix[i][j]), end="")
                break
            print("{:d} ".format(matrix[i][j]), end="")
        print()
