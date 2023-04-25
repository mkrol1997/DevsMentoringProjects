from functools import wraps

REGISTRY = dict()


def count(func):
    @wraps(func)
    def inner():
        try:
            REGISTRY[str(func.__name__)] += 1
        except KeyError:
            REGISTRY[str(func.__name__)] = 1
        print(REGISTRY)
        return func()
    return inner
