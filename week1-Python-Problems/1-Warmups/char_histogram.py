def char_histogram(string):
    histogram = {}

    for char in string:
        if char not in histogram:
            histogram[char] = 1
        elif char in histogram:
            histogram[char] += 1

    return histogram


def main():
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))

if __name__ == '__main__':
    main()
