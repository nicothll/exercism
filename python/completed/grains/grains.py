"""Functions to get numbers of grains on the chessboard or a given square."""


def square(number: int) -> int:
    """Function returns how many grains were on a given square.

    :param number: int - number of a given square
    :return: int - grains on a given square
    """

    if 0 < number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total() -> int:
    """Function returns the total number of grains on the chessboard.

    :return: int - total number of grains on the chessboard
    """
    return sum(square(i) for i in range(1, 65))
