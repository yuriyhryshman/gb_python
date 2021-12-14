incomes = {'wage': 30_000, 'bonus': 5_000}


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_salary(self):
        salary = 0
        return sum(self._income.values())


employee = Position('Peter', 'Parker', 'Journalist', 300_000, 50_000)
print(employee.get_full_name())
print(employee.get_full_salary())
