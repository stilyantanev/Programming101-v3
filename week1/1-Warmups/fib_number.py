def fib_number(n):
    a = 1
    b = 1
    number = ""

    if n == 1:
        number = str(a)
        return int(number)
    elif n == 2:
        number = str(a) + str(b)
        return int(number)
    else:
        number = str(a) + str(b)

        while n - 2 > 0:
            a, b = b, a + b
            number += str(b)
            n -= 1

        return int(number)

print(fib_number(3))
print(fib_number(10))
