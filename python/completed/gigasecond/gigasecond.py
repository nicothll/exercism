import datetime


def add(moment: datetime.datetime) -> datetime.datetime:
    """Determine the moment that would be after a gigasecond has passed.

    :param moment: datetime.datetime - given moment
    :return: datetime.datetime - After one gigasecond (10^9)
    """

    return moment + datetime.timedelta(seconds=10**9)
