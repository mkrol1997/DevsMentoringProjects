from typing import Union


def binary_search(p: int, q: int) -> Union[int, str]:
    """
    Perform a binary search to find a natural number solution to the defined equation.
    """
    left_boundary, right_boundary = 1, q

    while left_boundary <= right_boundary:
        mid = (left_boundary + right_boundary) // 2
        fx = mid ** 3 + p * mid

        if fx == q:
            return mid
        if fx > q:
            right_boundary = mid - 1
        else:
            left_boundary = mid + 1

    return "NIE"


def main():
    number_of_riddles = int(input())
    values = [input().split(" ") for _ in range(number_of_riddles)]

    for variables in values:
        result = binary_search(
            p=int(variables[0]),
            q=int(variables[1])
        )
        print(result)


if __name__ == "__main__":
    main()
