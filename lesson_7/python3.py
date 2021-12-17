class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - self.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

    def make_order(self, row_n):
        return '\n'.join(['*' * row_n for i in range(self.number // row_n)]) + '\n' + '*' * (self.number % row_n)


cell_1 = Cell(17)
cell_2 = Cell(5)

print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
