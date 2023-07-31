#!/usr/bin/python3
def print_matrix_integer(matrix):
    result_matrix = []
    for row in matrix:
        row_squares = [num**2 for num in row]
        result_matrix.append(row_squares)
    print(result_matrix)
    print(matrix)
