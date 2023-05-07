def triplets_with_sum(number) -> list[list[int]]:
    """
    Finds all Pythagorean triplets whose sum equals the given number.

    Args:
        number (int): The sum of the Pythagorean triplets.

    Returns:
        list[list[int]]: A list of all Pythagorean triplets whose sum equals the given number.

    Examples:
        >>> triplets_with_sum(12)
        [[3, 4, 5]]

        >>> triplets_with_sum(30)
        [[5, 12, 13], [9, 12, 15]]
    """
    triplets = []
    for a in range(1, number // 3):
        b = (number**2 - 2 * number * a) // (2 * number - 2 * a)
        c = number - b - a
        if a**2 + b**2 == c**2 and a < b < c:
            triplets.append([a, b, c])
    return triplets
