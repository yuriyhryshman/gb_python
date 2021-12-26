my_file = open('data3.txt', 'r')
data = []
for line in my_file:
    content = line.split()
    data.append(content[2])
    if int(content[2]) < 20_000:
        content.pop(2)
        print(' '.join(content))

mid = 0

for el in data:
    mid += int(el)

print(f'Средняя з/п состовляет: {int(mid / len(data))}')




