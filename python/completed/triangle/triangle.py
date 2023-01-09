def is_triangle(sides: list[int | float]) -> bool:
    """Function to verify if it is a triangle or not.

    :param sides: list[int | float] - sides of a shape,
    :return: bool - is a triangle?
    """
    if len(sides) > 3:
        return 3
    a, b, c = sides
    return not 0 in sides and a + b >= c and b + c >= a and a + c >= b


def equilateral(sides: list[int | float]) -> bool:
    """Function determine if a triangle is equilateral, all three sides the same length

    :param sides: list[int | float] - sides of a triangle
    :return: bool - is triangle is equilateral?
    """
    if is_triangle(sides):
        a, b, c = sides
        if a == b and b == c and a == c:
            return True
    return False


def isosceles(sides: list[int | float]) -> bool:
    """Function determine if a triangle is isosceles, all two sides the same length

    :param sides: list[int | float] - sides of a triangle
    :return: bool - is triangle is isosceles?
    """
    if is_triangle(sides):
        a, b, c = sides
        if a == b or b == c or a == c:
            return True
    return False


def scalene(sides: list[int | float]) -> bool:
    """Function determine if a triangle is scalene, all sides of different lengths

    :param sides: list[int | float] - sides of a triangle,
    :return: bool - is triangle is scalene?
    """
    if is_triangle(sides):
        a, b, c = sides
        if a != b and b != c and a != c:
            return True
    return False
