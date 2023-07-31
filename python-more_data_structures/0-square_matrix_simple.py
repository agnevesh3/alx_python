#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for row in matrix:
        row_squares = [num**2 for num in row]
        new_matrix.append(row_squares)
    return new_matrix
