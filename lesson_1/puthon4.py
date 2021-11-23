number = int(input('Введите целое натуральное число: '))
remnant = number % 10
number = number // 10
while number > 0:
    if number % 10 > remnant:
        remnant = number % 10
    number = number // 10
print(f'Самая большая цифра в числе равна: {remnant}')
