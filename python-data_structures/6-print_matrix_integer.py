#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    n = len(matrix[0])

    for i in range(0, n):
        for j in range(0, n):
            print("{}".format(matrix[i][j]), end=" ")
        print()
