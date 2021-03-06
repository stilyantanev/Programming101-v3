def count_substrings(haystack, needle):
    return haystack.count(needle)


def main():
    print(count_substrings("This is a test string", "is"))
    print(count_substrings("babababa", "baba"))
    print(count_substrings("Python is an awesome language to program in!", "o"))
    print(count_substrings("We have nothing in common!", "really?"))
    print(count_substrings("This is this and that is this", "this"))  # "This" != "this"


if __name__ == '__main__':
    main()
