my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el+1]for el in range(0, len(my_list)-1) if my_list[el+1] > my_list[el]]

print(new_list)
