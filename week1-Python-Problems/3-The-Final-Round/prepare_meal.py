def prepare_meal(number):
    entire_string = (spam_times(number) * "spam ").strip()

    if spam_times(number) > 0 and eggs(number) != "":
        entire_string += " and "

    return "\"" + entire_string + eggs(number) + "\""


def spam_times(number):
    n = 0
    times = 0

    while 3 ** n <= number:
        if number % (3 ** n) == 0:
            times = n
        n += 1

    return times


def eggs(number):
    if number % 5 == 0:
        return "eggs"

    return ""


def main():
    print(prepare_meal(5))
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(15))
    print(prepare_meal(45))
    print(prepare_meal(7))


if __name__ == '__main__':
    main()
