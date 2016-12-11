def is_increasing(seq):
    if len(seq) == 1:
        return True
    elif len(seq) == 2:
        return seq[0] < seq[1]
    else:
        if seq[0] < seq[1]:
            return is_increasing(list(seq[1:]))
        else:
            return False


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()
