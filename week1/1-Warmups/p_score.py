def p_score(n):
    n = str(n)
    is_palindrome = True

    if len(n) == 1:
        return 1
    else:
        first_index = 0
        second_index = len(n) // 2
        while first_index < second_index:
            if n[first_index] != n[len(n) - first_index - 1]:
                is_palindrome = False
                reverse_n = int(n[::-1])
                score = 1 + p_score(int(n) + reverse_n)
                return score
            first_index += 1

    if is_palindrome:
        return 1

# print(p_score(1))
# print(p_score(48))
# print(p_score(198))
