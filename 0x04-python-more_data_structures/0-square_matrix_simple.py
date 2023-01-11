#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    squared = []
    for row in matrix:
        new = []
        for col in row:
            new.append(col ** 2)
        squared.append(new)
    return squared
