new_list = [15, 12, 9, 8, 7, 7, 4, 3, 1, 0]
num = input('Введите любое натуральное число: ')

if num.isdigit() and num != '0':
    num = int(num)
    if new_list.count(num) == 0:
        for count in list(new_list):
            if count < num:
                new_list.insert(new_list.index(count), num)
                break
    else:
        new_list.reverse()
        for count in list(new_list):
            if count == num:
                new_list.insert(new_list.index(count), num)
                new_list.reverse()
                break

    print(new_list)

else:
    print('Попросили же ввести натуральное число. Ты инициативный что ли?')
