from random import choice
from typing import Union, List


def generate_random_sorted_numbers(length=31) -> List[int]:
    """
    Generate and return a sorted list of random numbers between 0 and `length`.
    """
    return sorted([choice(range(length)) for _ in range(length)])


def binary_search(number: int, list_of_numbers: List[int]) -> Union[int, bool]:
    """
    Perform a binary search to find the index of given number in a sorted list.
    """
    left_boundary, right_boundary = 0, len(list_of_numbers) - 1

    while left_boundary <= right_boundary:
        mid = (left_boundary + right_boundary) // 2

        if list_of_numbers[mid] < number:
            left_boundary = mid + 1
        elif list_of_numbers[mid] > number:
            right_boundary = mid - 1
        else:
            return mid
    return False


def find_lowest_accepted_number(list_of_numbers: List[int], lowest: int = 21) -> Union[int, bool]:
    """
    Find the index of the lowest number from range (21, 31) in the sorted list.
    """
    for number in range(lowest, 31):
        index_found = binary_search(number, list_of_numbers)
        if index_found:
            return index_found
    return False


def main():
    numbers = generate_random_sorted_numbers()
    len_start_index = find_lowest_accepted_number(numbers)

    if not len_start_index:
        return False

    "Finds index of the first number appearance if duplicates"
    try:
        while numbers[len_start_index] == numbers[len_start_index - 1]:
            len_start_index -= 1
    except IndexError:
        len_start_index = 0

    print(len(numbers[len_start_index:]) >= 10)


if __name__ == "__main__":
    main()


