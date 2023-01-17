# Conversion
ROMANS_NUMBERS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def roman(number: int) -> str:
    """Function that convert a number into roman number.

    :param number: int - given number.
    :return: str - Roman number
    """
    roman_nb = ""
    i = 0

    while number > 0:
        value = ROMANS_NUMBERS[i][0]
        if number >= value:
            roman_nb += ROMANS_NUMBERS[i][1]
            number -= value
        else:
            i += 1

    return roman_nb
