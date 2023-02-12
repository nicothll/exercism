def proverb(*args, qualifier: str = None) -> list[str]:
    """Returns a proverb with given arguments

    :param qualifier: str - Modify the final verse of your Proverb.
    :return:list[str] - The proverb.
    """

    if len(args) < 1:
        return []

    qualifier = "" if qualifier is None else qualifier + " "

    _proverb = []
    first_word = args[0]
    for idx in range(len(args) - 1):
        _proverb.append(f"For want of a {args[idx]} the {args[idx + 1]} was lost.")

    return [*_proverb, *[f"And all for the want of a {qualifier}{first_word}."]]
