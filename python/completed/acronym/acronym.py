import re


def abbreviate(words: str) -> str:
    """Returns the acronym of the given words.

    :param words: str - A string of words to be abbreviated.
    :return: str - The acronym of the given words.
    """

    return "".join(word[0].upper() for word in re.sub(r"[-_]", " ", words).split())
