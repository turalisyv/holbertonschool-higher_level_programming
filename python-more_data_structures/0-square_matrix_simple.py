#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix[i][j] ** 2)

        new_matrix.append(row)

    return new_matrix
