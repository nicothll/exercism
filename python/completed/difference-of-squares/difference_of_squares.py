def square_of_sum(number: int) -> int:
    """Function calculate the square of the sum of `number`
    (e.g. number=10 -> (1 + 2 + ... + 10)² = 55² = 3025)
    """
    return sum(i for i in range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Function calculate the sum of squares of `number`
    (e.g. number=10 -> 1² + 2² + ... + 10² = 385)
    """
    return sum(i**2 for i in range(1, number + 1))


def difference_of_squares(number: int) -> int:
    """Function calculate the difference between
    the square of the sum of `number` and the sum of the squares of `number`
    """
    return square_of_sum(number) - sum_of_squares(number)
