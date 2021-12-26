data = input('Введите элементы списка: ')
data = data.split()
count = 0

while count < len(data) - 1:
    data[count], data[count + 1] = data[count + 1], data[count]
    count += 2

print(data)
