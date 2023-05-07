def prime_numbers_generator() -> int:
    number = 2
    while True:
        number_dividers = [num for num in range(1, int(number/2)+1)
                           if number % num == 0]
        if len(number_dividers) == 1:
            yield number
        number += 1


prime_numbers = prime_numbers_generator()

for i in range(20):
    print(prime_numbers.__next__())
