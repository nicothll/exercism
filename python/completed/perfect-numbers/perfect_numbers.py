import math


def classify(number: int) -> str:
    """Determine if a number is perfect, abundant, or deficient
    based on Nicomachus classification scheme for positive integers.

    :param number: int - A positive integer. Must to be positive.
    :return: str - The classification of the input integer.
    """

    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"

    factors = set()
    for nb in range(1, int(math.sqrt(number)) + 1):
        quotient, remaining = divmod(number, nb)
        if remaining == 0:
            factors.add(nb)
            factors.add(quotient)
    factors.remove(number)
    aliquot = sum(factors)

    if aliquot > number:
        return "abundant"
    if aliquot == number:
        return "perfect"
    return "deficient"
