my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = lambda x: [y**2 for y in x]
cubed = lambda x: [y**3 for y in x]

squared_list = squared(my_list)
cubed_list = cubed(my_list)
