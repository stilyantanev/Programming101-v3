def next_hack(n):
    is_number_hack = False
    counter_for_one_bits = 0
    remainder = 0
    digits = []

    while not is_number_hack:
        n = n + 1
        current_num = n

        while current_num > 0:
            remainder = current_num % 2
            digits = [remainder] + digits
            current_num = current_num // 2

        for digit in digits:
            if digit == 1:
                counter_for_one_bits += 1

        if counter_for_one_bits % 2 == 1:
            if len(digits) == 1:
                is_number_hack = True

            start = 0
            end = len(digits) // 2

            while start < end:
                if digits[start] == digits[len(digits) - start - 1]:
                    is_number_hack = True
                else:
                    is_number_hack = False
                    break

                start += 1

        counter_for_one_bits = 0
        digits = []

    return n

print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
