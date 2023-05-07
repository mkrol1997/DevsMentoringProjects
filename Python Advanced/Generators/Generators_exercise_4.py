def fibonacci_generator(fibonacci_numbers_quantity: int) -> int:
    first_num, second_num = 0, 1
    for fibonacci_number in range(fibonacci_numbers_quantity):
        yield first_num
        first_num, second_num = second_num, first_num + second_num
