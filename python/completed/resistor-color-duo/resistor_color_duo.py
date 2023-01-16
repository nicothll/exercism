COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Function that return the value of the resistor according to the given colors.

    :param colors: list[str] - given colors, here only two
    :return: int: value of the resistor
    """
    return int("".join(str(COLORS.index(color)) for color in colors[:2]))
