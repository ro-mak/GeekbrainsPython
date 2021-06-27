from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_cost(self):
        pass


class Coat(Clothes):
    def __init__(self, V, name):
        super().__init__(name)
        self.V = V

    @property
    def material_cost(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H, name):
        super().__init__(name)
        self.H = H

    @property
    def material_cost(self):
        return self.H * 2 + 0.3


clothes_list = [Suit(200, "Gucci"), Suit(185, "Armani"), Coat(160, "M&S"), Coat(174, "H&M")]

total_cost = 0
for i in clothes_list:
    print(vars(i))
    print(f"Cost: {i.material_cost}")
    total_cost += i.material_cost
print(f"Total cost = {total_cost}")
