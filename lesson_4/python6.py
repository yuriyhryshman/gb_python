from itertools import count, cycle


def my_count(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


def my_cycle(data, stop):
    i = 0
    for el in cycle(data):
        if i > stop:
            break
        else:
            print(el)
            i += 1


print(my_cycle('ABC', 10))
print(my_count(7, 15))
