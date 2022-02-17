def find_opposites(lst):
    result = []

    word_set = set()  # searching inside a set is faster than searching inside a list
    for word in lst:
        word_set.add(word)

    for word in lst:
        rev = word[::-1]

        if rev != word:
            continue

        if rev in word_set:
            result.append((word, rev))

    return result
