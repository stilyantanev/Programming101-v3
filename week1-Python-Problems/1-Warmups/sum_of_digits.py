def sum_of_digits(n):
    digits = list(str(abs(n)))

    return sum(int(digit) for digit in digits)


def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))


if __name__ == '__main__':
    main()
