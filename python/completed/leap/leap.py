def leap_year(year: int) -> bool:
    """Function to report if it's a leap year

    The leap year in the Gregorian calendar occurs:

    - on every year that is evenly divisible by 4
    - except every year that is evenly divisible by 100
    - unless the year is also evenly divisible by 400

    :param year: int - given year.
    :return: bool - is it leap year?

    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
