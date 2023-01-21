"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit() : Decrement Alien health by one point.
    is_alive() : Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate) : Move Alien object to new coordinates.
    collision_detection(other) : Check if two Alien objects collide.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        """
        Constructs all the necessary attributes for the alien object.

        :param x_coordinate : int - axis X coordinate
        :param y_coordinate : int - axis Y coordinate
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrement Alien health by one point."""

        self.health -= 1

    def is_alive(self) -> bool:
        """Return a boolean for if Alien is alive (if health is > 0)

        :return: bool - Is it alive?
        """

        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move Alien object to new coordinates.

        :param new_x_coordinate: int - New axis X coordinate
        :param new_y_coordinate: int - New axis Y coordinate
        """

        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other: "Alien") -> None:
        """Check if two Alien objects collide.

        :param other: Alien class - Other Alien object
        :return: None
        """

        pass


def new_aliens_collection(start_positions: list[tuple[int, int]]) -> list[Alien]:
    """Create a list of Alien object with coordinates.

    :param start_positions: list[tuple[int, int]] - list of coordinates
    :return: list[Alien] - list of Alien objects initialize to the start positions
    """

    return [Alien(x_pos, y_pos) for x_pos, y_pos in start_positions]
