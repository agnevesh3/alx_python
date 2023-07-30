#!/usr/bin/python3
def print_matrix_integer(matrix):
    for row in matrix:
        row_str = " ".join(
            map(str, row)
        )  # Convert each element in the row to a string and join them with spaces
        print(row_str + "$")
