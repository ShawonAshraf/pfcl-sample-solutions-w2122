from random import shuffle, choice


def decipher(msg, perm):
    alphabet = {l: i for (i, l) in enumerate(perm)}
    codes = {i: l for (i, l) in enumerate("abcdefghijklmnopqrstuvwxyz")}

    result = ""
    for letter in msg:
        if letter == ' ':
            result += letter
            continue

        lId = alphabet[letter]
        newLetter = codes[lId]
        result += newLetter

    return result


if __name__ == "__main__":
    perm = "wnoegbjpkyxlfiuastqhvmcrzd"
    assert decipher("wnoeg", perm) == "abcde"
    assert decipher("rzd", perm) == "xyz"

    answer = "the brown fox jumps over the dog"
    assert decipher("hpg ntuci bur yvfaq umgt hpg euj", perm) == answer
    assert decipher("k lumg azhpui", perm) == "i love python"
