class Matrix:
    def __init__(self, two_dimen_list):
        self.data = two_dimen_list

    def __str__(self):
        result = ""
        for i in self.data:
            for j in i:
                result += f"{j} "
            result += "\n"
        return result

    def get_len(self):
        length = len(self.data)
        for i in self.data:
            length += len(i)
        return length

    def __add__(self, other):
        if type(other) != Matrix:
            raise TypeError("Matrices can only add other matrices")
        if self.get_len() != other.get_len():
            raise Exception("Matrices should have the same size")
        result = []
        for i, el in enumerate(self.data):
            new_list = []
            for j, el2 in enumerate(el):
                other_el = int(other.data[i][j])
                new_list.append(int(el2) + other_el)
            result.append(new_list)
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(m1)
print(m2)
print(m1 + m2)
