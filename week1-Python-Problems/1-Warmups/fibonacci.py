def fibonacci(n):
    nums = [1]

    if n == 1:
        return nums
    else:
        nums.append(1)
        
        while n - 2 > 0:
            nums.append(nums[-1] + nums[-2])
            n -= 1

        return nums


def main():
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(10))


if __name__ == '__main__':
    main()
