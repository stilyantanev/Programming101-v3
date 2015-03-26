def is_increasing(seq):
    is_monotonously_increasing = True
    index = 0

    if len(seq) == 1:
        return is_monotonously_increasing

    while index < len(seq) - 1:
        if seq[index] < seq[index + 1]:
            is_monotonously_increasing = True
        elif seq[index] >= seq[index + 1]:
            is_monotonously_increasing = False
            return is_monotonously_increasing

        index += 1

    return is_monotonously_increasing

print(is_increasing([1, 2, 3, 4, 5]))
print(is_increasing([1]))
print(is_increasing([5, 6, -10]))
print(is_increasing([1, 1, 1, 1]))
