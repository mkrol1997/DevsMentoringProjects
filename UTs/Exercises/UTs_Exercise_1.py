def is_prime_number(number: int) -> bool:
    if isinstance(number, int) and number > 1:
        for num in range(2, int(number / 2)):
            if number % num == 0:
                return False
    else:
        return False

    return True
