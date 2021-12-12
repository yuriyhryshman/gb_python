new_dict = {}

with open('data6.txt', 'r') as f:
    content = []
    for line in f:
        name, num = line.split(':')
        numbers = [i for i in num if i == ' ' or ('0' <= i <= '9')]
        print(numbers)
        num_sum = (sum(map(int, ''.join(numbers).split())))
        new_dict[name] = num_sum

print(new_dict)
