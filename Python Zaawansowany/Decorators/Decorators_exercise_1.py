from functools import wraps


def logged(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'You called {func.__name__}(args={args}, kwargs={kwargs}),'
              f' it returned {str(func(*args, **kwargs))}')
        func()
    return inner
