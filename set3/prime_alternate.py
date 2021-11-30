import math

"""
there are a lot of ways to check if a number is prime or not.

this file contains 2 solutions for the problem.
1. A simple loop that checks if a number is prime or not.
2. Loop but based on square root of the number.
"""


def prime_simple(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime_sqrt(n):
    if n < 2:
        return False

    # cuts down on the number of iterations
    # a bit faster
    # the idea is that instead of running until n, you run until square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
