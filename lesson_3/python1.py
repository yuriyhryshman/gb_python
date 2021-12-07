def my_div(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        print('На ноль делить тебе не разрешали)))')
    else:
        return a / b


print(my_div(input('Введите делимое: '), input('Введите делитель: ')))
