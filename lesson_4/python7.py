def fact(num):
    fact_n = 1

    if num == 0:
        yield f'{num}! = 1'

    elif num < 0:
        yield 'Факториал бывает у натуральных чисел и нуля'

    else:
        for i in range(1, num+1):
            fact_n *= i
            yield f'{num}! = {fact_n}'


for el in fact(int(input('Введите число: '))):
    print(el)
