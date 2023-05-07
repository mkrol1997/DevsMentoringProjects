my_args = [1, 5, 10, 25, 100, 130]

add_15_to_arg = lambda x: x+15
multiply_values = lambda x, y: x * y

y = [add_15_to_arg(x) for x in my_args]
j = [multiply_values(x, 2) for x in my_args]
