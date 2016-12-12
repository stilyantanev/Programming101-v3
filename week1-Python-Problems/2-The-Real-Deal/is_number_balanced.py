def is_number_balanced(n):
    digits = [int(x) for x in str(n)]

    if len(digits) == 1:
        return True
    else:
        sum_left = sum([digit for digit in digits[0:len(digits) // 2]])
        sum_right = sum([digit for digit in digits[(len(digits) + 1) // 2:]])

        if sum_left == sum_right:
            return True
        else:
            return False


def main():
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))


if __name__ == '__main__':
    main()
