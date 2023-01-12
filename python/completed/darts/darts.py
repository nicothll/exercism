def score(x: int | float, y: int | float) -> int:
    """Function that returns the earned points in a single toss of a Darts game according to Cartesian coordinates x and y.

    inner circle: return 10 points
    middle circle: return 5 points
    outer circle: return 1 points
    outside the target: return 0 point

    The equation of a circle is (x - a)**2 + (y - b)**2 = r**2
    where a and b are the coordinates of the center (a, b) and r is the radius.

    :param x: int or float - given a point x in the target.
    :param y: int or float- given a point y in the target.
    :return: int - score of a single toss
    """
    eq = x**2 + y**2
    if eq <= 1**2:
        return 10
    if eq <= 5**2:
        return 5
    if eq <= 10**2:
        return 1
    return 0
