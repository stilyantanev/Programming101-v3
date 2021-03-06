def fib_number(n):
    a = 1
    b = 1
    number = ""

    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return int(str(a) + str(b))
    else:
        number = str(a) + str(b)
        while n - 2 > 0:
            a, b = b, a + b
            number += str(b)
            n -= 1
        return int(number)


def main():
    print(fib_number(3))
    print(fib_number(10))


if __name__ == '__main__':
    main()
