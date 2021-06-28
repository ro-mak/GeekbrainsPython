class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return ComplexNumber(a, b)

    def __str__(self):
        sign = ""
        if self.b > 0:
            sign = "+"
        return f"ComplexNumber: {self.a} {sign} {self.b}j"


complex1 = ComplexNumber(25, 3)
complex2 = ComplexNumber(34, -2)
print(complex1 + complex2)
print(complex1 * complex2)
print(25 + 3j + 34 - 2j)
print((25 + 3j) * (34 - 2j))
