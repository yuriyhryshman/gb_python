a = [[3, 4, 7], [5, 6, 9], [1, 2, 8]]
b = [[9, 3, 1], [0, 4, 7], [5, 8, 6]]

# c = [[12, 7, 8], [5, 10, 16], [6, 10, 14]]


class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.lists)):
            new_matrix.append([])
            for j in range(len(self.lists[i])):
                new_matrix[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, new_matrix))


matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1 + matrix2)
