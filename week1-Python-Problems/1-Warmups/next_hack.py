def next_hack(n):
    is_number_hack = False

    while not is_number_hack:
        n = n + 1

        bin_number = str(bin(n)[2:])
        reversed_bin_number = str(bin(n)[2:])[::-1]

        sum_of_digits = {}
        for digit in bin_number:
            if digit not in sum_of_digits:
                sum_of_digits[digit] = 1
            else:
                sum_of_digits[digit] += 1

        if bin_number == reversed_bin_number and sum_of_digits["1"] % 2 == 1:
            is_number_hack = True

    return n


def main():
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))


if __name__ == '__main__':
    main()
