from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc


class Coat(Clothes):

    @property
    def calc(self):
        return round(self.size / 6.5) + 0.5


class Costume(Clothes):

    @property
    def calc(self):
        return (2 * self.size) + 0.3


coat = Coat(58)
costume = Costume(60)
print(coat + costume)
