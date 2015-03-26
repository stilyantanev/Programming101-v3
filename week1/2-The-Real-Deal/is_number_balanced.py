def is_number_balanced(n):
    digits = []

    while n > 0:
        digits = [n % 10] + digits
        n = n // 10

    if len(digits) == 1:
        return True
    else:
        sum_left = 0
        sum_right = 0

        for digit in digits[0:len(digits) // 2]:
            sum_left += digit

        for digit in digits[(len(digits) + 1) // 2:]:
            sum_right += digit

        if sum_left == sum_right:
            return True
        else:
            return False

print(is_number_balanced(9))
print(is_number_balanced(11))
print(is_number_balanced(13))
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
