def count_consonants(str):
    index = 0
    counter = 0
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    while index < len(str):
        if str[index] in consonants:
            counter += 1

        index += 1

    return counter

print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))
