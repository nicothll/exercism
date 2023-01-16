def is_isogram(string: str) -> bool:
    """Function that determine if a word or phrase is an isogram.

    An isogram is a word or phrase without a repeating letter.

    :param string: str - given word or sentence.
    :return: bool - Is it isogram?
    """
    l = [ch for ch in string.lower() if ch.isalpha()]
    return len(set(l)) == len(l)
