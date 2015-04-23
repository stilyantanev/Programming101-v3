def is_an_bn(word):
    if len(word) % 2 != 0:
        return False
    else:
        is_word = True

        for i in range(len(word) // 2):
            if word[i] == "a" and word[len(word) - i - 1] == "b":
                is_word = True
            else:
                is_word = False
                return is_word

        return is_word


def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    main()
