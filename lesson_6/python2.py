class Road:

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calc(self):
        # условной массой квадратного метра толщиной в один слой пусть будет 25 кг
        weight = self._length * self._width * 5 * 25 / 1000
        return f'Итоговая масса асфальт на участвке составит {round(weight)} тонн.'


rd = Road(3000, 20)
print(rd.calc())

