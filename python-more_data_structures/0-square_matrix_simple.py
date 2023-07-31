#!/usr/bin/python3
def print_matrix_integer(matrix):
    new_matrix = []
    for row in matrix:
        row_squares = [num**2 for num in row]
        new_matrix.append(row_squares)
    return new_matrix, matrix
