def is_armstrong_number(number: int) -> bool:
    """Function that determine is the given number is an Armstrong number or not.
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    :param number: int - given number.
    :return: bool - is it an armstrong number?
    """

    return number == sum(int(nb) ** len(str(number)) for nb in str(number))
