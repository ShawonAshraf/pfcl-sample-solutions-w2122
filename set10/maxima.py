import datetime


def find_maxima(lst):
    if lst == []:
        return []

    result = [lst[0]]
    current_max = lst[0]

    for num in lst:
        if num > current_max:
            current_max = num
            result.append(num)

    return result


if __name__ == "__main__":
    print("[] ->", find_maxima([]))
    print("[1] ->", find_maxima([1]))
    print("[4,1,3] ->", find_maxima([4, 1, 3]))
    print("[2,5,3,1,6,6,7] ->", find_maxima([2, 5, 3, 1, 6, 6, 7]))

    start = datetime.datetime.now()
    print(len(find_maxima(range(100000))))
    print("Time: ", (datetime.datetime.now() - start).total_seconds())
