# меню
# ввод
# расчет
# вывод

def menu():
    # выводим меню програмки
    print('- - - - МЕНЮ - - - -\n',
          '1. Расчитать з/п сотрудника\n'
          ' 2. Выход из программы\n'
          '- - - - ---- - - - -')
    return input('Выберите действие: ')


def entry():
    # собираем данные о сотруднике/сотрудниках
    data = {
        'Выработка в часах': int(input('Введите объем выработки в часах: ')),
        'Ставка в час': int(input('Введите ставку в час ($): ')),
        'Премия в %': int(input('Введите объем премии в процентах: ')),
        'Кол-во сотрудников': int(input('Введите количество сотрудников: '))
    }
    return data


def my_counter(data):
    # проводим нехитрые калькуляции з/п
    data_list = []
    res = 1
    for el in data.values():
        data_list.append(el)
    if data_list[0] < 140:
        print('Премия не начилена')
        data_list.pop(2)
    else:
        data_list[2] = (data_list[2] / 100) + 1
    for el in data_list:
        res *= el
    res = float('{:.3f}'.format(res))
    return res


def results(data, res, num):
    # выводим результаты
    print('Ваши данные: \n'
          f'{data}')
    print('Результат рассчета: \n'
          f'${res} на {num} сотрудника/сотрудников')


def main():
    # заставляем все работать в команде
    choice = 0
    while True:
        choice = int(menu())
        if choice == 1:
            data = entry()
            result = my_counter(data)
            num = data.setdefault('Кол-во сотрудников')
            results(data, result, num)
        elif choice == 2:
            print('Программа завершена')
            break
        else:
            print('Выберите действие: ')


main()
