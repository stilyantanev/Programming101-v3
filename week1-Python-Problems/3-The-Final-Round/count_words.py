def count_words(arr):
    return {word: arr.count(word) for word in arr}


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()
