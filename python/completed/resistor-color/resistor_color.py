def color_code(color: str) -> int:
    """Function returns the color code according to the given color.

    :param color: str - given color.
    :return: list - color code
    """
    return colors().index(color)


def colors() -> list[str]:
    """Function returns color in string format.

    :return: list - resistors colors.
    """
    return [
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
