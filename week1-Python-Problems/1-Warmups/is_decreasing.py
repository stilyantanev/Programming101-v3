def is_decreasing(seq):
    if len(seq) == 1:
        return True
    elif len(seq) == 2:
        return seq[0] > seq[1]
    else:
        if seq[0] > seq[1]:
            return is_decreasing(list(seq[1:]))
        else:
            return False


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()
