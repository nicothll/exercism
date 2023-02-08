COLORS = (
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
)


def label(colors: list[str]) -> str:
    """Function that return the value of the resistor according to the given colors.

    :param colors: list[str] - given colors, here only three
    :return: str: value of the resistor
    """

    value = int(
        "".join(str(COLORS.index(color)) for color in colors[:2])
    ) * 10 ** COLORS.index(colors[2])

    if value == 0:
        return "0 ohms"
    if value % 10**9 == 0:
        return f"{value // 10**9} gigaohms"
    if value % 10**6 == 0:
        return f"{value // 10**6} megaohms"
    if value % 10**3 == 0:
        return f"{value // 10**3} kiloohms"

    return f"{value} ohms"


print(label(["orange", "orange", "black"]), "33 ohms")
