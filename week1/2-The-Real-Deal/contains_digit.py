def contains_digit(number, digit):
    digits = []
    while number > 0:
        digits += [number % 10]
        number = number // 10

    return digit in digits

# print(contains_digit(123, 4))
# print(contains_digit(42, 2))
# print(contains_digit(1000, 0))
# print(contains_digit(12346789, 5))
