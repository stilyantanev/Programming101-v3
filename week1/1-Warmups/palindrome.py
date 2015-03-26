def palindrome(obj):
    obj = str(obj)
    is_palindrome = False

    if len(obj) == 1:
        is_palindrome = True
        return is_palindrome

    first_index = 0
    second_index = len(obj) // 2

    while first_index < second_index:
        if obj[first_index] == obj[len(obj) - first_index - 1]:
            is_palindrome = True
        else:
            is_palindrome = False
            return is_palindrome

        first_index += 1

    return is_palindrome

print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))
