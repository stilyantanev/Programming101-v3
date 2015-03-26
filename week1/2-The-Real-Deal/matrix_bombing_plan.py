from sum_matrix import sum_matrix
from copy import deepcopy
from pprint import pprint


def calc_bombed_matrix(m, i, j):
    indexes = [-1, 0, 1]
    bomb_m = deepcopy(m)

    for row in indexes:
        for col in indexes:
            if i + row >= 0 and i + row <= len(bomb_m) - 1:
                if j + col >= 0 and j + col <= len(bomb_m[0]) - 1:
                    if not(i + row == i and j + col == j):
                        if bomb_m[i][j] <= bomb_m[i + row][j + col]:
                            bomb_m[i + row][j + col] -= bomb_m[i][j]
                        else:
                            bomb_m[i + row][j + col] = 0

    return bomb_m


def matrix_bombing_plan(m):
    elements = {}

    for i in range(len(m)):
        for j in range(len(m[0])):
            total_sum = sum_matrix(calc_bombed_matrix(m, i, j))
            elements[(i, j)] = total_sum

    return elements

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(matrix_bombing_plan(m))
