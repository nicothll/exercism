def steps(number: int, step: int = 0) -> int:
    """The Collatz Conjecture or 3x+1:

    If number is even, divide number by 2 to get number / 2.
    If number is odd, multiply number by 3 and add 1 to get 3n + 1.

    :param number: int - given POSITIVE integer.
    :return: int - number of steps when it reached 1
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return step

    if number % 2 == 0:
        return steps(number // 2, step=step + 1)
    else:
        return steps(3 * number + 1, step=step + 1)
