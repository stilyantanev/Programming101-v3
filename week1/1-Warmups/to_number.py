def to_number(digits):
    number = 0
    index = len(digits)

    while index > 0:
        number = number + digits[len(digits) - index] * 10 ** (index - 1)
        index -= 1

    return number

print(to_number([1, 2, 3]))
print(to_number([9, 9, 9, 9, 9]))
print(to_number([1, 2, 3, 0, 2, 3]))
