def zero_insert(n):
    digits = []
    positions = []
    new_digits = []
    num = 0

    while n > 0:
        digits += [n % 10]
        n = n // 10
    digits.reverse()

    for i in range(len(digits) - 1):
        x = digits[i]
        y = digits[i + 1]
        if x == y or (x + y) % 10 == 0:
            positions.append(i + 1)

    for i in range(len(digits)):
        if i in positions:
            new_digits += [0]
        new_digits = new_digits + [digits[i]]
    index = len(new_digits)

    while index > 0:
        num = num + new_digits[len(new_digits) - index] * 10 ** (index - 1)
        index -= 1

    return num

# print(zero_insert(116457))
# print(zero_insert(55555555))
# print(zero_insert(1))
# print(zero_insert(6446))
