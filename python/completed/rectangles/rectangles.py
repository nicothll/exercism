from dataclasses import dataclass
from typing import Iterator


@dataclass
class Point:
    """A Point in 2D space.

    Attributes:
        row (int): The row of the Point.
        col (int): The column of the Point.
    """

    row: int
    col: int


class Diagram:
    """A Diagram class that represents a rectangle diagram.

    Attributes:
        height (int): The height of the diagram.
        width (int): The width of the diagram.
    """

    def __init__(self, schema: list[str]) -> None:
        """Initializes a new Diagram object.

        Args:
            schema (list[str]): The list of strings that represents the diagram.

        Raises:
            IndexError: If the height of the diagram is less than or equal to zero.
        """
        self._schema = schema
        self.height = len(schema)
        self.width = len(schema[0]) if self.height > 0 else 0

    def is_rectangle(self, p1: Point, p2: Point) -> bool:
        """Checks if the given points form a rectangle in the diagram.

        Args:
            p1 (Point): The first point of the rectangle.
            p2 (Point): The second point of the rectangle.

        Returns:
            bool: True if the given points form a rectangle, False otherwise.
        """
        if not all(
            self._schema[r][c] == "+" for r, c in [(p1.row, p2.col), (p2.row, p1.col)]
        ):
            return False
        for r in range(p1.row + 1, p2.row):
            if not all(self._schema[r][c] in "|+" for c in [p1.col, p2.col]):
                return False
        for c in range(p1.col + 1, p2.col):
            if not all(self._schema[r][c] in "-+" for r in [p1.row, p2.row]):
                return False
        return True

    def vertices(self, corner: Point = Point(-1, -1)) -> Iterator[Point]:
        """Yields the vertices of the rectangles in the diagram.

        Args:
            corner (Point): The starting corner point. Defaults to Point(-1, -1).

        Yields:
            Point: The vertices of the rectangles in the diagram.
        """
        for r in range(corner.row + 1, self.height):
            for c in range(corner.col + 1, self.width):
                if self._schema[r][c] == "+":
                    yield Point(r, c)


def rectangles(strings: list[str]) -> int:
    """Counts the number of rectangles in the given list of strings.

    Args:
        strings (list[str]): The list of strings that represents the diagram.

    Returns:
        int: The number of rectangles in the given list of strings.
    """
    counter = 0
    diagram = Diagram(strings)
    for p1 in diagram.vertices():
        for p2 in diagram.vertices(p1):
            if diagram.is_rectangle(p1, p2):
                counter += 1
    return counter
