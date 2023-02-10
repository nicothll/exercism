import enum
import collections


class Scrabble(enum.IntEnum):
    A = E = I = O = U = L = N = R = S = T = 1
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10


def score(word: str) -> int:
    """Calculate the Scrabble score for `word`.

    :param word: str - given word.
    :return: int - score.
    """
    word_counter = list(collections.Counter(word).items())

    return sum(Scrabble[letter.upper()] * count for letter, count in word_counter)
