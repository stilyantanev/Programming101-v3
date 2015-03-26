def unique_words_count(arr):
    return(len(set(arr)))

print(unique_words_count(["apple", "banana", "apple", "pie"]))
print(unique_words_count(["python", "python", "python", "ruby"]))
print(unique_words_count(["HELLO!"] * 10))
