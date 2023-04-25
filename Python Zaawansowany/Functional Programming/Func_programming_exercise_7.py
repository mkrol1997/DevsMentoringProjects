nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = list(map(lambda number: number**2,
                    list(filter(lambda number: number % 2 == 0, nums))))
