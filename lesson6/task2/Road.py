class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self):
        return self._length * self._width * 25 * 5
