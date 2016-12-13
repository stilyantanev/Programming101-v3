def is_credit_card_valid(number):
    counter_for_digits = len(str(number))
    return is_odd(counter_for_digits) and is_sum_divisible(number)


def is_sum_divisible(number):
    digits = to_digits(number)
    index = 0

    while index < len(digits):
        if is_odd(index):
            digits[index] = sum(to_digits(digits[index] * 2))
        index += 1

    return sum(digits) % 10 == 0


def is_odd(number):
    return number % 2 == 1


def to_digits(number):
    return [int(digit) for digit in str(number)]


def main():
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))


if __name__ == '__main__':
    main()
