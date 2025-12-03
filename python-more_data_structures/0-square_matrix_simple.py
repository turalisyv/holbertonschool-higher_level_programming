#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []

    new_matrix = matrix.copy()
    m = len(new_matrix)
    n = len(new_matrix[0])


    for i in range(m):
        for j in range(n):
            new_matrix[i][j] = new_matrix[i][j] ** 2

    return new_matrix
