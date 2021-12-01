data = input('Введите строку: ')

data = data.split()

for count in data:
    print(data.index(count), count[:10])


