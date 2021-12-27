class ComplexNumber:

    def __init__(self, int_a, int_b):
        self.number_a = int(int_a)
        self.number_b = int(int_b)

    def __add__(self, other):
        return complex(self.number_a, self.number_b) + complex(other.number_a, other.number_b)

    def __sub__(self, other):
        return complex(self.number_a, self.number_b) - complex(other.number_a, other.number_b)

    def __mul__(self, other):
        return complex(self.number_a, self.number_b) * complex(other.number_a, other.number_b)

    def __truediv__(self, other):
        return complex(self.number_a, self.number_b) / complex(other.number_a, other.number_b)


a = ComplexNumber(1, 3)
b = ComplexNumber(2, 1)

print(a + b)
print(a - b)
print(a * b)
print(a / b)


