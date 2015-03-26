def contains_digits(number, digits):
    number_digits = []
    is_contains = True

    while number > 0:
        number_digits += [number % 10]
        number = number // 10

    for digit in digits:
        if digit in number_digits:
            is_contains = True
        else:
            is_contains = False
            return is_contains

    return is_contains

print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6, 4]))
print(contains_digits(123456789, [1, 2, 3, 0]))
print(contains_digits(456, []))
