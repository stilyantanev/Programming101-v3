def goldbach(n):
    primes = primes_to_number(n)
    combinations = []

    for x in primes:
        for y in primes:
            if (x + y) == n and x <= (n / 2) and y >= (n / 2):
                combinations.append((x, y))

    return combinations


def primes_to_number(number):
    return [x for x in range(2, number) if is_prime(x)]


def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False

    return True


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))

if __name__ == '__main__':
    main()
