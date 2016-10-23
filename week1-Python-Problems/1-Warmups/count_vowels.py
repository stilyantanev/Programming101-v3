def count_vowels(str):
    VOWELS = "aeiouyAEIOUY"
    count_of_vowels = 0
    index = 0

    while index < len(str):
        if str[index] in VOWELS:
            count_of_vowels += 1
        index += 1

    return count_of_vowels


def main():
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))

if __name__ == '__main__':
    main()
