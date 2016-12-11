def p_score(n):
    if str(n) == str(n)[::-1]:
        return 1
    else:
        return 1 + p_score(n + int(str(n)[::-1]))


def main():
    print(p_score(121))
    print(p_score(48))
    print(p_score(198))


if __name__ == '__main__':
    main()
