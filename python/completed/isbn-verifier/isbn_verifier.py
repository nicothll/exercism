def is_valid(isbn: str) -> bool:
    """Check if the given string is a valid ISBN-10.

    :param isbn: str - given ISBN string.
    :return: bool - Is it a valid ISBN-10?
    """
    digits = list(isbn.replace("-", ""))
    if not digits or len(digits) != 10:
        return False

    digits[-1] = "10" if digits[-1] == "X" else digits[-1]

    for (idx, ch), d in zip(enumerate(digits), range(10, 0, -1)):
        if ch.isdigit():
            digits[idx] = int(ch) * d
        else:
            return False

    return sum(digits) % 11 == 0
