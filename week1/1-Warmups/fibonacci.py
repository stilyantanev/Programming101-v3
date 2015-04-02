def fibonacci(n):
    a = 1
    b = 1
    fibonacci_nums = []

    if n == 1:
        fibonacci_nums += [a]
        return fibonacci_nums
    elif n == 2:
        fibonacci_nums += [a, b]
        return fibonacci_nums
    else:
        fibonacci_nums += [a, b]
        while n - 2 > 0:
            a, b = b, a + b
            fibonacci_nums += [b]
            n -= 1

        return fibonacci_nums

# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(10))
