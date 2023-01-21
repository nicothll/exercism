def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Function returns the sum of all the unique multiples of particular numbers until number limit (not including).

    :param limit: int - Number limit, not including
    :param multiples: list[int] - List of multiples
    :return: int - sum of multiples
    """
    if multiples:
        return sum(
            nb
            for nb in range(limit)
            if any(nb % mul == 0 for mul in multiples if mul != 0)
        )
    return 0
