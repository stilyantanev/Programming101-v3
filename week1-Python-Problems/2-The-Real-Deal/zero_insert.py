def zero_insert(n):
    digits = [int(digit) for digit in str(n)]

    i = 0
    zero_indexes = []
    while i < (len(digits) - 1):
        if digits[i] == digits[i + 1] or (digits[i] + digits[i + 1]) % 10 == 0:
            zero_indexes.append(i + 1)
        i += 1

    while zero_indexes != []:
        digits.insert(zero_indexes[0], 0)
        del zero_indexes[0]
        for i in range(len(zero_indexes)):
            zero_indexes[i] += 1

    return int("".join(map(str, digits)))


def main():
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(1))
    print(zero_insert(6446))


if __name__ == '__main__':
    main()
