
def most_common(tags):
    result = None
    best_freq = 0
    for (k, v) in tags.items():
        if v > best_freq:
            best_freq = v
            result = k

    return result


def read_conllu(filename):
    result = []
    for line in open(filename, "r"):
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        result.append((parts[1], parts[3]))

    return result


def train_and_tag(gold_file, test_words):
    tags = read_conllu(gold_file)
    model = {}
    for word, tag in tags:
        word = word.lower()
        if word not in model:
            model[word] = {}

        if tag not in model[word]:
            model[word][tag] = 1
        else:
            model[word][tag] += 1

    result = []
    for word in test_words:
        word = word.lower()
        if word in model:
            result.append(most_common(model[word]))
        else:
            result.append("UNK")

    return result


# if __name__ == "__main__":
#     import sys
#     print(train_and_tag(sys.argv[1], sys.argv[2].split(",")))
