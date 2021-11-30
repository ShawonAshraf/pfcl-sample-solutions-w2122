from fragments import get_random_text


def easy_password(length):
    passw = ""
    while len(passw) < length:
        passw += get_random_text()

        # if generated password length > length,
        # start over again
        if len(passw) > length:
            passw = ""

    return passw


# testing code
if __name__ == "__main__":
    print(easy_password(10))
    print(easy_password(10))
    print(easy_password(15))
    print(easy_password(2))
