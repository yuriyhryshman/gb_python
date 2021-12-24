from abc import ABC, abstractmethod


class Store:

    def __init__(self, name, capability, location):
        self.name = name
        self.capability = capability
        self.location = location
        self.dict = {}

    def storing(self, technique):
        self.dict.setdefault(technique.name, []).append(technique)

    def transfer(self, name, location):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)
            print(f'{self.dict[name]} перевезли в {location}')


class Technique(ABC):

    @abstractmethod
    def __init__(self, name, number, cost):
        self.name = name
        self.number = number
        self.cost = cost

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def __repr__(self):
        return f'{self.name}-{self.number}-{self.cost}'


class Printer(Technique):

    def __init__(self, name, number, cost, printing_technology, printing_speed, cartridge_life):
        super().__init__(name, number, cost)
        self.technology = printing_technology
        self.speed = printing_speed
        self.cl = cartridge_life

    def action(self):
        return 'Печатает...'

    def __repr__(self):
        return f'{self.name}-{self.number}-{self.cost}-{self.technology}-{self.speed}-{self.cl}'


class Scanner(Technique):

    def __init__(self, name, number, cost, scanner_type, scanning_speed, resolution):
        super().__init__(name, number, cost)
        self.type = scanner_type
        self.speed = scanning_speed
        self.resolution = resolution

    def action(self):
        return 'Сканирует...'

    def __repr__(self):
        return f'{self.name}-{self.number}-{self.cost}-{self.type}-{self.speed}-{self.resolution}'


class Copier(Technique):

    def __init__(self, name, number, cost, copier_speed, resolution, num_of_cop):
        super().__init__(name, number, cost)
        self.speed = copier_speed
        self.resolution = resolution
        self.kpd = num_of_cop

    def action(self):
        return 'Копирует...'

    def __repr__(self):
        return f'{self.name}-{self.number}-{self.cost}-{self.speed}-{self.resolution}-{self.kpd}'


store = Store(28, 1500, 'Киев')
# создаем объект и добавляем
scanner = Scanner('hp', '321', 90, 'Лазерный', 20, '1920x1080')
store.storing(scanner)
printer = Printer('lg', '311', 97, 'Лазерный', 20, '1920x1080')
store.storing(printer)
scanner3 = Scanner('hp', '330', 99, 'Лазерный', 20, '1920x1080')
store.storing(scanner3)
# выводим склад
print(store.dict)
# забираем с склада и выводим склад
store.transfer('hp', 'Киев')
print(store.dict)
# оно почти работает, но у меня уже сдают нервы :)

