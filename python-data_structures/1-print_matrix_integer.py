#!/usr/bin/python3
def print_matrix_integer(matrix):
    for i in matrix:
        for j in i:
            print("{}".format(j), end="")


matrix = [[1, 2, 3], [2, 4, 5], [9, 8, 7]]
print_matrix_integer(matrix)
