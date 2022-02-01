
def word2dict(word):
    result = { }
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def can_be_composed(word1, word2):
    dict1 = word2dict(word1)
    dict2 = word2dict(word2)

    for c in dict1:
        if c not in dict2:
            return False

        if dict2[c] < dict1[c]:
            return False

    return True

if __name__ == "__main__":
    examples = [ ("python", "pantyhose"), ("python", "immunotherapy"), ("python", "hypnotists"), ("python", "ponytail"), 
                 ("lesson", "professional"), ("lesson", "responsible"), ("lesson", "longest"),
                 ("code", "docent"), ("messy", "reassembly"), ("computational", "alphanumeric"), ("linguistics", "criminologists")]

    for w1, w2 in examples:
        print(w1, w2, can_be_composed(w1, w2))
