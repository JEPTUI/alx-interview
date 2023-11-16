#!/usr/binpython3
"""Defines a rotate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """Return: Nothing
    Matrix has two dimensions
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
