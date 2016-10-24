def sum_of_digits(n):
    n = abs(n)
    sum_nums = 0

    while n > 0:
        sum_nums += n % 10
        n = n // 10

    return sum_nums


def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))


if __name__ == '__main__':
    main()
