def is_prime(a):
    if a < 2:
        return False

    i = 2
    while i < a:
        if a % i == 0:
            return False

        i += 1

    return True


def is_twin_prime(n):
    if not is_prime(n):
        return False

    return is_prime(n-2) or is_prime(n+2)


if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(10))
    print(is_prime(-7))
    print(is_prime(104593))

    print(is_twin_prime(10))
    print(is_twin_prime(37))
    print(is_twin_prime(421))
    print(is_twin_prime(1091))
    print(is_twin_prime(-13))
