def sum_matrix(m):
    total_sum = 0

    for element in m:
        total_sum += sum(element)

    return total_sum

# if __name__ == '__main__':
#     m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     print(sum_matrix(m))
#     m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     print(sum_matrix(m))
#     m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
#     print(sum_matrix(m))
