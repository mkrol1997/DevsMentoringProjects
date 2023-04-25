three_d = [
            [1, 2, 3, 4],
            [0, -1, -2, -3, -4, -5, -6],
            [1, 10, 15, 12, 20, 20, 20],
            [-15, -13, 14, 20, -1]
          ]

filtered_list = [list_obj for list_obj in three_d if len(list_obj) > 4]
