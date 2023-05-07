from functools import wraps


def count(func):
    """ Stores counter of function calls in a dictionary """
    registry = Registry()

    @wraps(func)
    def inner():
        try:
            registry[str(func.__name__)] += 1
        except KeyError:
            registry[str(func.__name__)] = 1
        print(registry)
        return func()
    return inner


class Registry:
    _registry = dict()

    def __str__(self) -> str:
        return f'{self.registry}'

    def __getitem__(self, item: str) -> None:
        return self.registry[item]

    def __setitem__(self, key: str, value: int) -> None:
        self.registry[key] = value

    @property
    def registry(self) -> dict:
        return self._registry
