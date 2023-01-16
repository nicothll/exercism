def response(hey_bob: str) -> str:
    """Function that answer according to the given `hey_bob` parameter

    :param hey_bob: str - given sentence
    :return: str - answer of Bob
    """

    hey_bob = hey_bob.strip()  # Remove whitespaces and special characters like \n
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."
