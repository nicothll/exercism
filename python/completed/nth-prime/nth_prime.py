import math


def is_prime(number: int) -> bool:
    """Checks if the given number is prime

    :param number: int - A given integer number.
    :return: bool - Is it prime?
    """

    if number == 2 or number == 3:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    for f in range(2, int(math.sqrt(number)) + 1):
        if number % f == 0:
            return False
    return True


def prime(n: int) -> int:
    """
    Returns the prime number according to the given position.

    :param n: int - Position of the prime number.
    :return: int - The nth prime number.
    """
    if n < 1:
        raise ValueError("there is no zeroth prime")
    if n == 1:
        return 2

    primes = [2]
    _number = 3

    while len(primes) < n:
        if is_prime(_number):
            primes.append(_number)
        _number += 1
    return primes[-1]
