def count_consonants(str):
    CONSONANTS = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count_of_consonants = 0
    index = 0

    while index < len(str):
        if str[index] in CONSONANTS:
            count_of_consonants += 1
        index += 1

    return count_of_consonants


def main():
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))

if __name__ == '__main__':
    main()
