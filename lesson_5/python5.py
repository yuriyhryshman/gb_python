from random import randint

with open('data5.txt', 'w+', encoding='utf-8') as data_f:
    line = [str(randint(1, 10_000)) for _ in range(1000)]
    data_f.write(f'{" ".join(line)}')
    data_f.seek(0)
    print(sum(map(int, data_f.readline().split())))


