def to_number(digits):
    index = len(digits)
    number = 0

    while index > 0:
        number = number + digits[len(digits) - index] * 10 ** (index - 1)
        index -= 1

    return number


def main():
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))

if __name__ == '__main__':
    main()
