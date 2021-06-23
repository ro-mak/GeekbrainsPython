class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        if other is not Cell:
            raise TypeError("Cell can be added only to another Cell")
        self.quantity += other.quantity

    def __sub__(self, other):
        if other is not Cell:
            raise TypeError("Cell can be substracted only from another Cell")
        if self.quantity - other.quantity > 0:
            self.quantity -= other.quantity
        else:
            print("Cells cannot be substracted because this cell is smaller")

    def __mul__(self, other):
        if other is not Cell:
            raise TypeError("Cell can be multiplied by another Cell")
        self.quantity *= other.quantity

    def __truediv__(self, other):
        if other is not Cell:
            raise TypeError("Cell can be divide only by another Cell")
        self.quantity //= other.quantity

    def make_order(self, number_of_cells_on_line):
        previous = 0
        for i in range(0, self.quantity + 1):
            for j in range(previous, i):
                print("*", end="")
            if i % number_of_cells_on_line == 0 and i != 0:
                print("\n")
            previous = i


cell1 = Cell(12)
cell1.make_order(5)
