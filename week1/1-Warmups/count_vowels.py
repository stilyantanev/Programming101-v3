def count_vowels(str):
    index = 0
    counter = 0
    vowels = "aeiouyAEIOUY"

    while index < len(str):
        if str[index] in vowels:
            counter += 1

        index += 1

    return counter

print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))
