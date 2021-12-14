def rotated(lst, n):
    length = len(lst)

    new_list = []
    for i, item in enumerate(lst):
        rotated_i = i + n
        new_list.append(lst[rotated_i % length])

    return new_list
