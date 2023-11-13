import random
import time
from typing import List, Union
from functools import wraps


def execution_time(func):
    """
    Measures the execution time of a decorated function
    """
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start_time} s")
        return result
    return inner


def generate_random_numbers(arr_length: int) -> List[int]:
    return [random.randint(0, 100) for _ in range(arr_length)]


@execution_time
def bubble_sort(num_arr: List[Union[int, float]]) -> None:
    """
    Sorts an array of numbers in non-decreasing order using the Bubble Sort algorithm.
    """
    arr_length = len(num_arr)

    for i in range(arr_length):
        for j in range(arr_length - i - 1):

            if num_arr[j] > num_arr[j + 1]:
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]


@execution_time
def insertion_sort(num_arr: List[Union[int, float]]) -> None:
    """
    Sorts an array of numbers in non-decreasing order using the Insertion Sort algorithm.
    """
    arr_length = len(num_arr)

    for i in range(1, arr_length):
        key = num_arr[i]
        j = i - 1
        while j >= 0 and key < num_arr[j]:
            num_arr[j + 1] = num_arr[j]
            j -= 1
        num_arr[j + 1] = key


@execution_time
def quick_sort(num_arr: List[Union[int, float]], start: int, end: int) -> None:
    """
    Sorts an array of numbers in non-decreasing order using the Quick Sort algorithm.
    """
    def _quick_sort(_num_arr: List[int], _start: int, _end: int) -> None:
        edge = partition(_num_arr, _start, _end)

        if _start < edge - 1:
            _quick_sort(_num_arr, _start, _end - 1)
        if _end > edge:
            _quick_sort(_num_arr, edge, _end)

    _quick_sort(num_arr, start, end)


def partition(num_list: List[Union[int, float]], start: int, end: int) -> int:
    """
    Partitions a list into for Quick Sort algorithm.
    """
    mid = (start + end) // 2
    pivot = num_list[mid]

    while start <= end:
        while pivot > num_list[start]:
            start += 1

        while pivot < num_list[end]:
            end -= 1

        if start <= end:
            num_list[start], num_list[end] = num_list[end], num_list[start]
            start += 1
            end -= 1

    return start


numbers1 = generate_random_numbers(100)
numbers2 = generate_random_numbers(100)
numbers3 = generate_random_numbers(100)

bubble_sort(numbers1)
insertion_sort(numbers2)
quick_sort(numbers3, 0, len(numbers3) - 1)
