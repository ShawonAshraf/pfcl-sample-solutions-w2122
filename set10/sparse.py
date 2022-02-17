class SparseVector(object):
    def __init__(self, length):
        self.__length = length
        self.__nonZeros = {}

    def __len__(self):
        return self.__length

    def set_pos(self, pos, elem):
        self.__nonZeros[pos] = elem

    def get_pos(self, pos):
        if pos in self.__nonZeros:
            return self.__nonZeros[pos]
        else:
            return 0

    def get_non_zeros(self):
        return list(self.__nonZeros.keys())

    def concatenate(self, vec):
        result = SparseVector(self.__length + len(vec))
        for pos, val in self.__nonZeros.items():
            result.set_pos(pos, val)

        for pos in vec.get_non_zeros():
            result.set_pos(self.__length + pos, vec.get_pos(pos))

        return result

    def __str__(self):
        result = "SparseVector["
        for i in range(self.__length - 1):
            result += str(self.get_pos(i)) + ","

        if self.__length > 0:
            result += str(self.get_pos(self.__length - 1))

        result += "]"
        return result
