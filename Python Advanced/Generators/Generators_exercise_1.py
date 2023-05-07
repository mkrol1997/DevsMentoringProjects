def test_generator(num: int) -> int:
    for i in range(num):
        if i < 5:
            yield i
        else:
            raise StopIteration("Iteration exceeds maximum limit. (limit: 5)")
