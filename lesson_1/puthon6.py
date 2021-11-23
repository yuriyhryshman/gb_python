distance = float(input('Ведите расстояние пробежки за первый день: '))
desire = float(input('Ведите желаемое расстояние пробежки: '))
count = 1
while distance <= desire:
    distance *= 1.1
    count += 1
    if (distance % desire) == 1:
        break

print(f'Желаемый результат будет достигнут не ранее, чем на {count} день')
