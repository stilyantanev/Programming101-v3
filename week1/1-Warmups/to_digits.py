def to_digits(n):
    digit_list = []
    remainder = 0

    while n > 0:
        remainder = n % 10
        digit_list = [remainder] + digit_list
        n = n // 10

    return digit_list

print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))