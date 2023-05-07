from random import choice, shuffle
from threading import Thread
from time import time
from multiprocessing import Pool


NUMBER_OF_ARRAYS = 10
ARRAY_SIZE = 100
NUMBERS_RANGE = 1000


def bubble_sort(list_of_arrays_to_sort: list) -> list:
    sorted_arrays = []
    for arr_to_sort in list_of_arrays_to_sort:
        while True:
            swapped = False
            for index in range(0, len(arr_to_sort) - 1):
                if arr_to_sort[index] > arr_to_sort[index + 1]:
                    arr_to_sort[index], arr_to_sort[index + 1] = \
                        arr_to_sort[index + 1], arr_to_sort[index]
                    swapped = True
            if not swapped:
                sorted_arrays.append(arr_to_sort)
                break
    return sorted_arrays


if __name__ == "__main__":

    # MULTITHREADING SORT
    list_of_arrays = [[choice(range(1, NUMBERS_RANGE))
                       for i in range(0, ARRAY_SIZE)] for j in range(NUMBER_OF_ARRAYS)]

    threads_start = time()

    threads = [
        Thread(target=bubble_sort, args=[list_of_arrays[:2]]),
        Thread(target=bubble_sort, args=[list_of_arrays[2:4]]),
        Thread(target=bubble_sort, args=[list_of_arrays[4:6]]),
        Thread(target=bubble_sort, args=[list_of_arrays[6:8]]),
        Thread(target=bubble_sort, args=[list_of_arrays[8:]]),

    ]

    run_threads = [thread.start() for thread in threads]
    stop_threads = [thread.join() for thread in threads]

    threads_end = time()

    print('Multithreading: {}'.format(threads_end - threads_start))

    for arr in list_of_arrays:
        shuffle(arr)

    # MULTIPROCESSING SORT
    process_start = time()

    pool = Pool(processes=2)
    p1 = pool.apply_async(bubble_sort, [list_of_arrays[:5]])
    p2 = pool.apply_async(bubble_sort, [list_of_arrays[5:]])

    pool.close()
    pool.join()

    process_end = time()

    print('Multiprocessing: {}'.format(process_end - process_start))

    """
    Conclusion:
        - Multithreading
            * Average execution time with 1 thread: 0.00896866666 [s]
              Average execution time with 5 threads: 0.01263125737 [s]
            
            * The fastest, and the most optimal execution time, 
                can be achieved with the use of one thread. 
                According to Amdahl's law, to improve execution time, 
                it is required to parallelize some parts of the code.
            
            * Because cPython is limited with GIL (Global Interpreter Lock), 
                multiple process threads can only run concurrently, 
                which gives no additional performance. 
                
            * It is highly likely that adding more threads and dividing 
                the problem among them will increase the execution time. 
        
        - Multiprocessing
            * Average execution time using 2 processes: 0.21649710337 [s]
              Average execution time using 4 processes: 0.30309255917 [s]

            * It is recommended to use multiprocessing with more complex 
                problems or/and with big data calculations. Referring to Amdahl's law,
                code parallelization will lead to performance improvement,
                as in cPython, processes unlike threads, can be run in parallel.
            
            * Processes in comparison to threads, do not share memory. 
                Process spawn is associated with the time needed to allocate 
                and free the memory, which affects execution time.
                That is why in this exercise, parallelized code execution time is longer
                than concurrent program execution.            
    """
