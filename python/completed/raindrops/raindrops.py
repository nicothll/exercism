def convert(number: int) -> str:
    """Function that convert a number into a string that contains raindrop sounds.

    :param number: int - given number
    :return: str - raindrop sound
    """
    sound = ""
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    return sound if sound else str(number)
