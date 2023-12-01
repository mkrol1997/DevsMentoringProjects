from typing import List, Union
import random


class HeapSort:
    def run(self, arr_values: List[Union[int, float]]) -> None:
        last_internal_parent_idx = len(arr_values) // 2 - 1
        length = len(arr_values)

        for parent_idx in range(last_internal_parent_idx, -1, -1):
            self.__heapify_max_array(arr_values, parent_idx, length)

        for arr_length in range(length - 1, 0, -1):
            arr_values[0], arr_values[arr_length] = arr_values[arr_length], arr_values[0]
            self.__heapify_max_array(arr_values, 0, arr_length)

    def __heapify_max_array(self, arr_values: List[Union[int, float]], parent_index: int, arr_length: int) -> None:
        largest = parent_index

        left_child_idx = 2 * parent_index + 1
        right_child_idx = 2 * parent_index + 2

        if left_child_idx < arr_length and arr_values[left_child_idx] > arr_values[largest]:
            largest = left_child_idx

        if right_child_idx < arr_length and arr_values[right_child_idx] > arr_values[largest]:
            largest = right_child_idx

        if largest != parent_index:
            arr_values[parent_index], arr_values[largest] = arr_values[largest], arr_values[parent_index]
            self.__heapify_max_array(arr_values, largest, arr_length)


def main():
    arr_list = [random.randint(0, 101) for _ in range(1, 16)]

    heap = HeapSort()
    heap.run(arr_list)


if __name__ == "__main__":
    main()
