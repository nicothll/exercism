import collections

CARDS = "..23456789TJQKA"

SCORES = {
    (5, 1): 9,
    "SF": 8,
    (4, 1): 7,
    (3, 2): 6,
    "F": 5,
    "S": 4,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
}


def best_hands(hands: list[str]) -> list[str]:
    """
    Returns the best hands from a list of hands based on their scores.

    Args:
        hands (list[str]): A list of hands where each hand is represented by a string.

    Returns:
        list[str]: A list of hands with the best score.
    """
    if len(hands) < 2:
        return hands
    evaluated = [evaluate(h) for h in hands]
    return [hand for hand, rank in zip(hands, evaluated) if rank == max(evaluated)]


def evaluate(hand: str) -> tuple[int, ...]:
    """
    Evaluates a hand of cards and returns its score.

    Args:
        hand (str): A string representing a hand of cards.

    Returns:
        tuple[int, ...]: A tuple containing the score and the ranks of the cards.
    """
    kinds = [CARDS.index(rank) for rank, _ in hand.replace("10", "T").split()]
    counter = collections.Counter(kinds)

    ranks, counts = zip(
        *sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
    )

    # If Ace in hand
    ranks = (5, 4, 3, 2, 1) if ranks == (14, 5, 4, 3, 2) else ranks

    # Evaluate if straight or/and flush
    straight = len(counts) == 5 and (max(ranks) - min(ranks) == 4)
    flush = len(set(h[-1] for h in hand.split())) == 1

    counts = (
        "SF" if straight and flush else "F" if flush else "S" if straight else counts
    )

    return SCORES.get(counts, 0), *ranks
