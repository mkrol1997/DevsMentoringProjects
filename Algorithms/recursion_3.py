from typing import List


def print_recursively(numbers: List[int]) -> None:
    """
    Recursively print each element of the list in reversed order.
    """
    print(numbers[-1])
    if len(numbers) == 1:
        return

    return print_recursively(numbers[:-1])

