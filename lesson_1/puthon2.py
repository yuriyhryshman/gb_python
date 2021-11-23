time = int(input('Введите кол-во времени в секундах: '))
minutes = time / 60

if time == 60:
    print('Вы ввели времени: 00 часов 01 минут 00 секунд')
if time <= 59:
    print(f'Вы ввели времени: 00 часов 00 минут {time} секунд')

if 1 <= minutes < 60:
    print(f'Вы ввели времени: 00 часов {int(minutes)} минут {time % 60} секунд')

if minutes == 60:
    print('Вы ввели времени: 01 часов 00 минут 00 секунд')

if minutes > 60:
    print(f'Вы ввели времени: {int(minutes / 60)} часов {int(minutes % 60)} минут {time % 60} секунд')






