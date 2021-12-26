with open('data1.txt', 'w+', encoding='utf-8') as my_f:
    while True:
        line = input('Введите строку: ')
        if not line:
            break
        my_f.write(f'{line}\n')



