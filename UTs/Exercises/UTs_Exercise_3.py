def partition(array: list, start_index: int, end_index: int) -> int:

    pivot = array[end_index]
    left_indicator_index = start_index
    right_indicator_index = end_index - 1

    while True:
        while left_indicator_index <= right_indicator_index and array[left_indicator_index] <= pivot:
            left_indicator_index += 1

        while left_indicator_index <= right_indicator_index and array[right_indicator_index] >= pivot:
            right_indicator_index -= 1

        if left_indicator_index <= right_indicator_index:
            array[left_indicator_index], array[right_indicator_index] = array[right_indicator_index], array[left_indicator_index]
        else:
            break

    array[end_index], array[left_indicator_index] = array[left_indicator_index], array[end_index]

    return left_indicator_index


def quickSort(array: list, start_index: int, end_index: int) -> None:
    if start_index < end_index:
        pivot = partition(array, start_index, end_index)

        quickSort(array, start_index, pivot - 1)

        quickSort(array, pivot + 1, end_index)
