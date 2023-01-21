import collections
from typing import Callable

# Init counter object
counter = collections.Counter

# Score categories.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: ones_to_sixes(dice, 1)
TWOS = lambda dice: ones_to_sixes(dice, 2)
THREES = lambda dice: ones_to_sixes(dice, 3)
FOURS = lambda dice: ones_to_sixes(dice, 4)
FIVES = lambda dice: ones_to_sixes(dice, 5)
SIXES = lambda dice: ones_to_sixes(dice, 6)
FULL_HOUSE = lambda dice: sum(dice) if set(counter(dice).values()) == {2, 3} else 0
FOUR_OF_A_KIND = lambda dice: four_of_a_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if set(dice) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == {2, 3, 4, 5, 6} else 0
CHOICE = lambda dice: sum(dice)


def ones_to_sixes(dice: list[int], digit: int) -> int:
    """
    Calculate the score for ONES to SIXES category of the game.

    :param dice: List[int] - A list of integers representing the roll of 5 dice.
    :return: int - The score according to the digit category.
    """
    return digit * dice.count(digit)


def four_of_a_kind(dice: list[int]) -> int:
    """
    Calculate the score for the four of a kind category of the game.

    :param dice: list[int] - A list of integers representing the roll of 5 dice.
    :return: int - The score for the four of a kind category.
                    Returns 0 if the roll does not contain 4 of the same number.
    """
    most_common_nb, count = counter(dice).most_common(1)[0]
    if count >= 4:
        return 4 * most_common_nb
    else:
        return 0


def score(dice: list[int], category: Callable) -> int:
    """
    Calculate the score of a given set of dice rolls based on the selected category.

    :param dice: List[int] - A list of integers representing the roll of 5 dice.
    :param category: Callable - A function that determines the scoring category to use.
                       Available categories are YACHT, ONES, TWOS, THREES, FOURS,
                       FIVES, SIXES, FULL_HOUSE, FOUR_OF_A_KIND, LITTLE_STRAIGHT,
                       BIG_STRAIGHT, CHOICE.
    :return: int - The score for the given set of dice rolls and category.
    """
    return category(dice)
