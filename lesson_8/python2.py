class MyError(Exception):

    def __init__(self, txt, num):
        self.txt = txt
        self.num = num


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if b == 0:
        raise MyError('Делить на ноль нельзя!', b)
    else:
        result = a / b
        print(result)

except ValueError:
    print('Ты инициативный что-ли?')
except MyError as mr:
    print(mr.args[0])
    print(mr.args[1])

