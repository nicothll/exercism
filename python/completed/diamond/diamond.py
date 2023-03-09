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

    letters = [chr(k) for k in range(ord("A"), ord(letter) + 1)]

    diamond_line = letters[::-1] + letters[1:]

    diamond = list()
    for _letter in letters:
        diamond.append(
            "".join(_letter if _letter == ch else " " for ch in diamond_line)
        )
    return diamond + diamond[-2::-1]
