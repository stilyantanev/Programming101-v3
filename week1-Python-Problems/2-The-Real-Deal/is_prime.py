def is_prime(n):
    n = abs(n)
    is_prime = True

    if n == 1:
        is_prime = False
        return is_prime
    else:
        for x in range(2, n):
            if n % x == 0:
                is_prime = False
                return is_prime
            else:
                is_prime = True

        return is_prime


def main():
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))


if __name__ == '__main__':
    main()
