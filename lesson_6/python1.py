import time
import itertools


class TrafficLight:
    __color = [['Зеленый', 10, 32], ['Желтый', 3, 33], ['Красный', 7, 31]]

    def run(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[2]}m {light[0]}', end='')
            time.sleep(light[1])


trf = TrafficLight()
trf.run()

