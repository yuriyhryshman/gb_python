import time


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_direction(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        for i in range(self.speed + 1):
            print(f'\r{i} км/ч', end='')
            time.sleep(0.5)


class TownCar(Car):

    def show_speed(self):
        for i in range(self.speed + 1):
            print(f'\r{i} км/ч', end='')
            time.sleep(0.6)
            if i > 60:
                print('Превышение скорости!!!')


class WorkCar(Car):

    def show_speed(self):
        for i in range(self.speed + 1):
            print(f'\r{i} км/ч', end='')
            time.sleep(1.2)
            if i > 40:
                print('Превышение скорости!!!')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def turn_lights(self):
        light = [31, 34]
        print('Включили мигалки. Ведем погоню!')
        print(f'\r\033[6m\033[31m OOO \033[6m\033[34m OOO\033[0m')


class SportCar(Car):

    def show_speed(self):
        for i in range(self.speed + 1):
            print(f'\r{i} км/ч', end='')
            time.sleep(0.02)
            if i > 160:
                print('Превышение скорости!!!')


police_car = PoliceCar(100, 'White', 'Prius')
ferrari = SportCar(170, 'Red', 'Ferrari')
ferrari.go()
ferrari.show_speed()
print(f'{ferrari.name} пронеслась мимо патрульных')
police_car.go()
# police_car.show_speed()
police_car.turn_lights()
ferrari.turn_direction('направо')
police_car.turn_direction('прямо')


