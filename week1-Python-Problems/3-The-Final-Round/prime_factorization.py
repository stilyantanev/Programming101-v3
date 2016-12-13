def prime_factorization(n):
    primes = [number for number in range(2, n + 1) if is_prime(number)]

    factorized = []
    for prime in primes:
        if n % prime == 0:
            counter = 0
            while n % prime == 0:
                counter += 1
                n = n // prime
            factorized.append((prime, counter))
            counter = 0

    return factorized


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
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))


if __name__ == '__main__':
    main()
