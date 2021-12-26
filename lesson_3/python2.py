def user_data(**kwargs):
    # print(f'Инициализируем вывод данных о пользователе')
    # print('...')
    # print(f' имя фамилия: {name} {second_name}\n,'
    #       f' год рождения: {year}\n,'
    #       f' город проживания: {city}\n,'
    #       f' почта: {mail}\n,'
    #       f' телефон: {phone}')
    return ' '.join(kwargs.values())


print(user_data(name='Вася', second_name='Пупкин', year='1982', city='Харьков', mail='vasya1251@gmail.com', phone='0973972634'))

