rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('data4n.txt', 'w+', encoding='utf-8') as new_f:
    with open('data4.txt', 'r', encoding='utf-8') as old_f:
        new_f.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in old_f]))
