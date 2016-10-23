def factorial(n):
    fact = 1

    while n >= 1:
        fact = fact * n
        n = n - 1

    return fact


def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))

if __name__ == '__main__':
    main()
