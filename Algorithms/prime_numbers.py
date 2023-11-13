import math
from typing import List


def is_prime(number: int) -> bool:
    """
    Check number "n" dividers in range [2, √n]
    """
    for divider in range(2, int(math.sqrt(number)) + 1):
        if not number % divider:
            return False
    return True


def generate_prime_numbers(length: int) -> List[int]:
    """
    Generate list of prime numbers of a given length
    """
    number = 3
    prime_numbers = [2]
    while len(prime_numbers) != length:
        if is_prime(number):
            prime_numbers.append(number)
        number += 2
    return prime_numbers
