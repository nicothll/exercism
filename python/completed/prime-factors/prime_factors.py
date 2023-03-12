def factors(value: int) -> list[int]:
    """Returns the prime factors of a given natural number.

    Args:
        value (int): A given natural number.

    Returns:
        list[int]: The list of prime factors.
    """
    p_factors = list()
    factor = 2
    while value > 1:
        quotient, remainder = divmod(value, factor)
        if remainder == 0:
            value = quotient
            p_factors.append(factor)
        else:
            factor += 1
    return p_factors
