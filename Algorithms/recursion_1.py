from typing import List


def recursion_print(list_of_numbers: List[int]) -> None:
    """
    Recursively print each element of the list.
    """
    print(list_of_numbers[0])
    if len(list_of_numbers) == 1:
        return
    return recursion_print(list_of_numbers[1:])
