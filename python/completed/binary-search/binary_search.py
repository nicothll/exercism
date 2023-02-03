def find(search_list: list[int], value: int, lower: int = 0, upper: int = None):
    """Searches for a value in a sorted list of integers using binary search algorithm.

    :param search_list: list[int] -  A sorted list of integers.
    :param value: int - The value to be searched for.
    :param lower: int - The lower bound index of the search range.
    :param upper: int - The upper bound index of the search range. Length of list if not specified.
    :return: int - The index of the value in the list, or Exception if the value is not found.
    """
    if upper is None:
        upper = len(search_list) - 1

    if upper >= lower:
        mid_idx = (lower + upper) // 2

        if search_list[mid_idx] == value:
            return mid_idx

        if search_list[mid_idx] < value:
            return find(search_list, value, mid_idx + 1, upper)

        if search_list[mid_idx] > value:
            return find(search_list, value, lower, mid_idx - 1)

    raise ValueError("value not in array")
