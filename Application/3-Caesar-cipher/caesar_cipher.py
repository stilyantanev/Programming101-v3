def caesar_encrypt(str, n):
    n %= 26
    char_list = list(str)
    for char in char_list:
        if(ord(char) + n) <= 122 or (ord(char) + n) <= 90:
            char = chr(ord(char) + n)
        elif(ord(char) + n) > 122 or (ord(char) + n) > 90:
            char = chr(ord(char) + n - 26)
        print(char, end="")
    print()

# Examples
caesar_encrypt("abc", 1)
caesar_encrypt("ABC", 1)
caesar_encrypt("abc", 2)
caesar_encrypt("aaa", 7)
caesar_encrypt("xyz", 1)
