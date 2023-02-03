from typing import Callable


def append(list1: list, list2: list) -> list:
    """Adds all items in the second list to the end of the first list

    :param list1: list - First list of items
    :param list2: list - Second list of items
    :return: list - First list with second list at its end
    """
    return list1 + list2


def concat(lists: list[list]) -> list:
    """Concatenate all lists

    :param lists: list[list] - list with nested lists
    :return: list - All lists concatenate
    """
    result = []
    for _list in lists:
        result += _list
    return result


def filter(function: Callable, list: list):
    """Filtering a given list according to the function

    :param list: function - given function
    :param list: list - given list
    :return: int - number of items in the list
    """
    if list:
        return [item for item in list if function(item)]
    return []


def length(list: list) -> int:
    """Return length of the list

    :param list: list - given list
    :return: int - number of items in the list
    """
    count = 0
    for _ in list:
        count += 1
    return count


def map(function: Callable, list: list) -> list:
    """Mapping a given list according to the function

    :param function: Callable - given function
    :param list: list - given list
    :return: int - number of items in the list
    """
    if list:
        return [function(item) for item in list]
    return []


def foldl(function: Callable, list: list, initial: int | str) -> int | str:
    """Fold (reduce) each item of the list into the accumulator from the left.

    :param function: Callable - Given function
    :param list: list - Given list of numbers
    :param initial: int - Initial number
    :return: list - The list reversed
    """
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function: Callable, list: list, initial: int | str) -> int | str:
    """Fold (reduce) each item of the list into the accumulator from the right.

    :param function: Callable - Given function
    :param list: list - Given list of numbers
    :param initial: int - Initial number
    :return: list - The list reversed
    """
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list: list) -> list:
    """Return a reversed list

    :param list: list - Given list
    :return: list - The list reversed
    """
    return list[::-1]
