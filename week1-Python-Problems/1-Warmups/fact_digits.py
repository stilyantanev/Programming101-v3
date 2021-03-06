def fact_digits(n):
    sum_facts = 0

    digits = [int(digit) for digit in str(abs(n))]
    for digit in digits:
        fact = 1
        while digit > 1:
            fact = fact * digit
            digit = digit - 1
        sum_facts += fact

    return sum_facts


def main():
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))


if __name__ == '__main__':
    main()
