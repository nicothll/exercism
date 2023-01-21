def flatten(
    iterable: list[int, str, list[int, str]], memo: list[int, str] | None = None
) -> list[int, str]:
    """Flatten a nested list of integers into a single list without any None values.

    :param iterable: list[int, str, list[int, str]] - The nested list to be flattened.
    :param memo: list[int, str], optional - The list to store the flattened values. Default is None
    :return: list[int, str] - The flattened list
    """

    if memo is None:
        memo = []
    for value in iterable:
        if value is not None:
            if type(value) == list:
                memo = flatten(value, memo)
            else:
                memo.append(value)
    return memo
