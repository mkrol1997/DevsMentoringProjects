def test_generator(num: int) -> int:
    for i in range(num):
        if i < 5:
            yield i
        else:
            raise StopIteration("Iteration exceeds maximum limi. (limit: 5)")


generator = test_generator(10)

print(next(generator))
print(generator.__next__())
print(next(generator))
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
