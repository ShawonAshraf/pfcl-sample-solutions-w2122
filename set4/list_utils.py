def last(l):
    return l[-1]


def middle(l):
    return l[len(l)//2]


def product(l):
    p = 1
    for li in l:
        p *= li
    return p


def even_sum(l):
    s = 0
    for i in range(0, len(l), 2):
        s += l[i]
    return s


def mean(l):
    return sum(l)/len(l)
