def is_decreasing(seq):
    is_monotonously_decreasing = True
    index = len(seq) - 1

    if len(seq) == 1:
        return is_monotonously_decreasing

    while index >= 1:
        if seq[index] < seq[index - 1]:
            is_monotonously_decreasing = True
        elif seq[index] >= seq[index - 1]:
            is_monotonously_decreasing = False
            return is_monotonously_decreasing
        index -= 1

    return is_monotonously_decreasing


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))

if __name__ == '__main__':
    main()
