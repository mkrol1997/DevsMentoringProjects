from functools import wraps


def stars_wrapper(func):
    """ Wraps decorated function with stars
    printed above and under function logic """
    @wraps(func)
    def inner(text: str):
        sentences = text.split('\n')
        stars_len = len(max(sentences, key=len)) + 1
        try:
            print('*' * stars_len)
            return func(text)
        finally:
            print('*' * stars_len)
    return inner
