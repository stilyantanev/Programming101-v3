def iterations_of_nan_expand(expanded):
    times = expanded.strip().count("Not a")

    if expanded == "":
        return 0
    elif times > 0:
        return times
    else:
        return False

# print(iterations_of_nan_expand(""))
# print(iterations_of_nan_expand("Not a NaN"))
# print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
# print(iterations_of_nan_expand("Show these people!"))
