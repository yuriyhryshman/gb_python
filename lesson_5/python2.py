f_obj = open('data2.txt', 'r')

i = 0
for line in f_obj:
    i += 1
    print(f'В строке {i} мы имеем {len(line)} символов.')

print(f'Всего в файле {i} строк.')
f_obj.close()
