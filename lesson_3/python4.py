def my_pow(x, y):
    if x <= 0 or y >= 0:
        print('Принимаю действительное положительное число x и целое отрицательное число y')
    else:
        y = y * -1
        print(y)
        result = 1
        for i in range(y):
            result *= x
            i += 1
        return 1 / result

# def my_pow(x, y):
#     if x <= 0 or y >= 0:
#         print('Принимаю действительное положительное число x и целое отрицательное число y')
#     else:
#         y = y * -1
#         result = x ** y
#         return 1 / result


print(my_pow(3, -2))
