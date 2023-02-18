def slices(series: str, length: int) -> list[str]:
    """
    Return  all the contiguous substrings of length n in that string in the order that they appear.

    :param series: str - String of digits.
    :param length: int - length of the digit series.
    :return: list[str] - All the contiguous substrings.
    """
    # Checking
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")

    substr = []
    for i, d in enumerate(series):
        nb = series[i : i + length] if length > 1 else d
        if len(nb) == length:
            substr.append(nb)
    return substr
