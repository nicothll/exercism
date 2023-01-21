import collections

# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 10
LITTLE_STRAIGHT = 11
BIG_STRAIGHT = 12
CHOICE = 13


def score(dice: list[int], category: int) -> int:
    """Function that return the score of a given a list of values for 5 dice.

    :param dice: list[int] - given values of 5 dices (1 to 6).
    :param category: int - given category code. See Score categories section,
    :return: int - score
    """

    counter = collections.Counter(dice)

    # FULL_HOUSE category (e.g. dice=[1, 1, 3, 3, 3])
    if category == FULL_HOUSE and set(counter.values()) == {2, 3}:
        return sum(dice)

    # FOUR_OF_A_KIND category (e.g. dice=[5, 2, 2, 2, 2] or dice=[5, 5, 5, 5, 5])
    most_common_nb, most_common_count = counter.most_common(1)[0]
    if category == FOUR_OF_A_KIND and most_common_count >= 4:
        return 4 * most_common_nb

    # LITTLE STRAIGHT category  (e.g. dice=[1, 2, 3, 4, 5])
    if category == LITTLE_STRAIGHT and set(dice) == {1, 2, 3, 4, 5}:
        return 30

    # BIG STRAIGHT category (e.g. dice=[2, 3, 4, 5, 6])
    if category == BIG_STRAIGHT and set(dice) == {2, 3, 4, 5, 6}:
        return 30

    if ONES <= category <= SIXES:
        return category * dice.count(category)

    if category == YACHT and len(set(dice)) == 1:
        return 50

    if category == CHOICE:
        return sum(dice)

    return 0
