def max_int(a, b, c):
    data = [a, b, c]
    largest = max(data)
    data.remove(largest)
    largest_2 = max(data)
    return largest + largest_2


print(max_int(4, 9, 17))

