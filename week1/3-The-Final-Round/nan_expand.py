def nan_expand(times):
    if times == 0:
        return ""
    else:
        return times * "Not a " + "NaN"

# print(nan_expand(0))
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))
