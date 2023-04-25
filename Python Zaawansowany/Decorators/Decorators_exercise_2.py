from functools import wraps


def make_stars(func):
    @wraps(func)
    def inner(txt):
        sentences = txt.split('\n')
        stars_len = len(max(sentences, key=len)) + 1

        print('*' * stars_len)
        func(txt)
        print('*' * stars_len)

    return inner
