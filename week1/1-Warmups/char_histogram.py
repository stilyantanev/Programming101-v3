def char_histogram(string):
    histogram = {}

    for char in string:
        if char not in histogram:
            histogram[char] = 1
        elif char in histogram:
            histogram[char] += 1

    return histogram

# print(char_histogram("Python!"))
# print(char_histogram("AAAAaaa!!!"))
