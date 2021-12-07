def diagonal(matrix):
    result = []
    for i, l in enumerate(matrix):
        result.append(l[i])
    return result


def transpose(matrix):
    result = [[] for _ in range(len(matrix[0]))]
    for l in matrix:
        for i, el in enumerate(l):
            result[i].append(el)

    return result


# matrix1 = [[0, 1, 2, 3, 4],
#            [0, 1, 2, 3, 4]]

# print("Transposed:", transpose(matrix1))

# matrix2 = [['a', 'b'],
#            ['c', 'd']]

# print("Transposed:", transpose(matrix2))
