"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.

SUPERLIST = 3
SUBLIST = 2
EQUAL = 1
UNEQUAL = 0


def sublist(list_one: list, list_two: list) -> str:
    if list_one == list_two:
        return EQUAL

    if len(list_one) > len(list_two):
        list_one, list_two = list_two, list_one
        swap = True
    else:
        swap = False

    len1, len2 = len(list_one), len(list_two)

    for i in range(len2 - len1 + 1):
        if list_two[i : i + len1] == list_one:
            return SUPERLIST if swap else SUBLIST

    return UNEQUAL
