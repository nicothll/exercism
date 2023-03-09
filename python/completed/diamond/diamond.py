import string

ALPHABET = string.ascii_uppercase


def rows(letter: str) -> list[str]:
    """
    Create a diamond shape of uppercase letters around the given letter.

    The function takes a single uppercase letter as input and generates a diamond shape
    of uppercase letters with the given letter at the center. For example, if the input
    letter is 'C', the function will return a list of strings representing the following
    diamond shape:

        A
       B B
      C   C
       B B
        A

    Args:
        letter (str): The uppercase letter to use as the center of the diamond.

    Returns:
        list[str]: A list of strings representing the diamond shape.
    """

    if letter == "A":
        return ["A"]

    diamond = list()

    idx_letter = ALPHABET.index(letter)
    length = range(1, len(ALPHABET) * 2, 2)[idx_letter]

    for step in range(idx_letter + 1):
        diamond.append(
            str().join(
                ALPHABET[step]
                if length // 2 + step == i or length // 2 - step == i
                else " "
                for i in range(length)
            )
        )
    return diamond + diamond[-2::-1]
