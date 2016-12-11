def to_number(digits):
    return int("".join(map(str, digits)))


def main():
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))


if __name__ == '__main__':
    main()
