import collections

LETTERS_VALUES = (
    ("AEIOULNRST", 1),
    ("DG", 2),
    ("BCMP", 3),
    ("FHVWY", 4),
    ("K", 5),
    ("JX", 8),
    ("QZ", 10),
)


def score(word: str) -> int:
    """Calculate the Scrabble score for `word`.

    :param word: str - given word.
    :return: int - score.
    """
    word_counter = list(collections.Counter(word).items())

    score = []
    for letter, count in word_counter:
        for letters, point in LETTERS_VALUES:
            if letter.upper() in letters:
                score.append(point * count)
                continue

    return sum(score)
