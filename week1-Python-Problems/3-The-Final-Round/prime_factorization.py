def prime_factorization(n):
    factorized = []
    primes = []
    index = 2
    counter = 0

    while index <= n:
        if is_prime(index):
            primes.append(index)

        index += 1

    for prime in primes:
        if n % prime == 0:
            while n % prime == 0:
                counter += 1
                n = n // prime

            factorized.append((prime, counter))
            counter = 0

    return factorized


def is_prime(n):
    index = 2
    is_prime = True

    while index < n:
        if n % index == 0:
            return False

        index += 1

    return is_prime


def main():
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))

if __name__ == '__main__':
    main()
