def fact_digits(n):
    n = abs(n)
    sum_of_fact_digits = 0
    digits = []
    remainder = 0

    while n > 0:
        remainder = n % 10
        digits += [remainder]
        n = n // 10

    for digit in digits:
        fact = 1

        while digit > 0:
            fact = fact * digit
            digit = digit - 1

        sum_of_fact_digits += fact

    return sum_of_fact_digits

print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))
