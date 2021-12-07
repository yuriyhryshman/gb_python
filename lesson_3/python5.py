def my_list_sum():
    summa = 0
    while True:
        list_sum = input('Вводите числа: ').split()
        for num in list_sum:
            if num == 'E':
                return summa
            else:
                try:
                    summa += int(num)
                except ValueError:
                    print('Если хотите выйти жмите "E".')

        print(f'Вот собственно сумма введенных чисел: {summa}')


print(my_list_sum())
