from collections import Counter

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
    """Given a list of values for 5 dice and a category code
    Return the score of the dice for that category.
    If the dice do not satisfy the requirements of the category return 0.
    Categories Codes:
    YACHT -> 0, ONES to SIXES -> 1 to 6, FULL_HOUSE -> 7, FOUR_OF_A_KIND -> 10,
    STRAIGHT: LITTLE -> 11, BIG -> 12, CHOICE -> 13

    :param dice: list[int] - given values of 5 dices (1 to 6).
    :param category: int - given category code. See Score categories section,
    :return: int - score
    """

    # Evaluate dice with Counter class from collections package
    counter = Counter(dice)
    counter_values = set(counter.values())
    value, count = counter.most_common(1)[0]

    # ONES to SIXES categories
    if ONES <= category <= SIXES:
        return category * dice.count(category)

    # YACHT category
    if category == YACHT and len(set(dice)) == 1:
        return 50

    # FULL_HOUSE category (e.g. dice=[1, 1, 3, 3, 3])
    if category == FULL_HOUSE and counter_values == {2, 3}:
        return sum(dice)

    # FOUR_OF_A_KIND category (e.g. dice=[5, 2, 2, 2, 2] or dice=[5, 5, 5, 5, 5])
    if category == FOUR_OF_A_KIND and count >= 4:
        return 4 * value

    # CHOICE category
    if category == CHOICE:
        return sum(dice)

    # LITTLE STRAIGHT categories  (e.g. dice=[1, 2, 3, 4, 5])
    if category == LITTLE_STRAIGHT and set(dice) == {1, 2, 3, 4, 5}:
        return 30

    # BIG STRAIGHT categories  (e.g. dice=[2, 3, 4, 5, 6])
    if category == BIG_STRAIGHT and set(dice) == {2, 3, 4, 5, 6}:
        return 30

    return 0
