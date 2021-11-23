proceeds = int(input('Введите объем прибыли: '))
expenses = int(input('Введите объем издержек: '))

if proceeds > expenses:
    pure_income = proceeds - expenses
    print(f'Прибыль фирмы составила: {pure_income}$\n'
          'Рентабельность выручки составляет: ', (pure_income / proceeds))
    staff = int(input('Сколько сотрудников работает в компании: '))
    print('Чистая прибыль на сотрудника составляет: ', (pure_income / staff), '$.')

elif proceeds < expenses:
    print('Фирма отработала в убыток \n'
          'Убыток составил: ', (proceeds - expenses), '$')

else:
    print('Фирма отработала в ноль')

