class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt


try:
    list_d = []
    while True:
        elem = input('Введите новый элемент списка: ')

        if elem == 'stop':
            print(list_d)
            break

        elif elem.isdigit():
            list_d.append(int(elem))


except ValueError:
    print('Ты инициативный что-ли?')
except MyError as mr:
    pass
