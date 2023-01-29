#!/usr/bin/python3
""" the matrix_divided module """


def matrix_divided(matrix, div):
    """
    divides all element of a matrix

    Args:
        matrix(list): a list of list of integers
        div(int): divisor
    """
    if type(matrix) is not list or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is list:
            if row:
                len_row = len(matrix[0])
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf'):
        raise TypeError("div must be a number")
    div_matrix = []
    for row in matrix:
        new = []
        for value in row:
            res = round((value / div), 2)
            new.append(res)
        div_matrix.append(new)
    return div_matrix
