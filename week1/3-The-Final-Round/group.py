def group(things):
    index = 0
    big_group = []
    small_group = []

    while index < len(things):
        if things[index] in small_group or small_group == []:
            small_group.append(things[index])
        else:
            big_group.append(small_group)
            small_group = []
            small_group.append(things[index])

        index += 1

    big_group.append(small_group)

    return big_group

if __name__ == '__main__':
    print(group([1, 1, 1, 2, 3, 1, 1]))
    print(group([1, 2, 1, 2, 3, 3]))
