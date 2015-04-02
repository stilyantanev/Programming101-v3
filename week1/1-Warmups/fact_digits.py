def fact_digits(n):
    sum_of_fact_digits = 0
    remainder = 0
    digits = []
    n = abs(n)

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

# print(fact_digits(111))
# print(fact_digits(145))
# print(fact_digits(999))
