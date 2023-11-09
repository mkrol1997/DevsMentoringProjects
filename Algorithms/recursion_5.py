def find_gcd(num_a: int, num_b: int) -> int:
    """
    Finds GCD of two given numbers
    """
    lower, higher = sorted([num_a, num_b])

    while lower != 0:
        lower, higher = higher % lower, lower

    return higher


def find_lcm(num_a: int, num_b: int) -> int:
    """
    Finds LCM of two given numbers
    """
    gcd = find_gcd(num_a, num_b)
    return (num_a * num_b) // gcd
