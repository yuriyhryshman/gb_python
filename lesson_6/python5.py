class Stationary:

    def __init__(self, title):
        self.name = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):

    def draw(self):
        print('Запуск отрисовки.')
        print(f'\033[3m\033[31m Вот так пишет {self.name}\033[0m')


class Pencil(Stationary):

    def draw(self):
        print('Запуск отрисовки.')
        print(f'\033[2m\033[36m Вот так пишет {self.name}\033[0m')


class Handle(Stationary):

    def draw(self):
        print('Запуск отрисовки.')
        print(f'\033[1m\033[35m Вот так пишет {self.name}\033[0m')


pen = Pen('красная ручка')
pencil = Pencil('бирюзовый карандаш')
marker = Handle('фиолетовый маркер')
pen.draw()
pencil.draw()
marker.draw()
