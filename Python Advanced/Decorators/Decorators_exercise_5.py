from functools import wraps
from time import time


def timethis(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time()
        try:
            return func(*args, **kwargs)
        finally:
            end_time = time()
            total_time = str(round(end_time - start_time, 3)).split('.')
            print(f'\nExecution time: {total_time[0]}s {total_time[1].zfill(3)}ms')
    return inner
