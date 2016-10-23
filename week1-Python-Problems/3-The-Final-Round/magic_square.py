def magic_square(matrix):
    all_sums = []
    all_sums += [sum(row) for row in matrix]
    all_sums += [sum([row[i] for row in matrix]) for i in range(len(matrix))]

    primary_diagonal_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                primary_diagonal_sum += matrix[i][j]
    all_sums.append(primary_diagonal_sum)

    secondary_diagonal_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + j == len(matrix) - 1:
                secondary_diagonal_sum += matrix[i][j]
    all_sums.append(secondary_diagonal_sum)

    return all(sums == all_sums[0] for sums in all_sums)


def main():
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
    main()
